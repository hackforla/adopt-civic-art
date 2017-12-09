from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.forms import modelformset_factory

from artworks.models import AboutPage, Artwork, Adoption, Tip, Checkin, CheckinImage
from artworks.forms import CheckinForm, CheckinImageForm, TipForm


def index(request):
    artworks = Artwork.objects.order_by('-id').filter(active=True)

    return render(request, 'index.html', {
        'artworks': artworks,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    })


def about(request):
    about = AboutPage.objects.last()

    return render(request, 'about.html', {
        'about': about
    })


def artwork(request, id):
    artwork = get_object_or_404(Artwork, pk=id)

    adoptees = Adoption.objects.filter(artwork=artwork)

    last_checkin = Checkin.objects.filter(artwork=artwork) \
        .order_by('-timestamp')[:1]

    if request.user.is_authenticated:
        adopted = Adoption.objects.filter(user=request.user, artwork=artwork)
    else:
        adopted = False

    return render(request, 'artwork.html', {
        'artwork': artwork,
        'adoptees': adoptees,
        'last_checkin': last_checkin,
        'adopted': adopted
    })


def artworks(request):
    artworks = Artwork.objects.order_by('-id').filter(active=True)

    return render(request, 'artworks.html', {
        'artworks': artworks,
    })


@login_required
def profile(request):
    adoptions = Adoption.objects.filter(user=request.user)

    return render(request, 'registration/profile.html', {
        'adoptions': adoptions
    })


@login_required
def adopt(request, id):
    artwork = get_object_or_404(Artwork, pk=id)
    adoptees = Adoption.objects.filter(artwork=artwork)

    check_adopted = Adoption.objects.filter(user=request.user, artwork=artwork)

    if not check_adopted:
        adopt = Adoption(user=request.user, artwork=artwork)
        adopt.save()

    adopted = True

    return render(request, 'artwork.html', {
        'artwork': artwork,
        'adoptees': adoptees,
        'adopted': adopted
    })


@login_required
def unadopt(request, id):
    artwork = Artwork.objects.filter(id=id)

    Adoption.objects.filter(user=request.user, artwork=artwork).delete()

    adoptions = Adoption.objects.filter(user=request.user)

    return render(request, 'registration/profile.html', {
        'adoptions': adoptions
    })


@login_required
def checkin(request, id):
    artwork = Artwork.objects.get(id=id)

    # https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django

    CheckinImageFormSet = modelformset_factory(
        CheckinImage,
        form=CheckinImageForm,
        min_num=1,
        max_num=3,
        extra=3
    )

    if request.method == 'POST':
        checkinForm = CheckinForm(request.POST)
        formset = CheckinImageFormSet(
            request.POST,
            request.FILES,
            queryset=CheckinImage.objects.none())

        if checkinForm.is_valid() and formset.is_valid():
            checkin = checkinForm.save(commit=False)
            checkin.user = request.user
            checkin.artwork = artwork

            checkin.save()
            # Save check in damage many to many checkboxes
            checkinForm.save_m2m()

            photos = formset.save(commit=False)

            for photo in photos:
                photo.checkin = checkin
                photo.save()

            return redirect('artwork', id=artwork.id)
        else:
            formErrors = formset.errors

            return render(request, 'check-in.html', {
                'artwork': artwork,
                'checkinForm': checkinForm,
                'formset': formset,
                'formErrors': formErrors
            })

    else:
        checkinForm = CheckinForm()
        formset = CheckinImageFormSet(queryset=CheckinImage.objects.none())

    return render(request, 'check-in.html', {
        'artwork': artwork,
        'checkinForm': checkinForm,
        'formset': formset
    })


def tip(request, id):
    artwork = Artwork.objects.get(id=id)

    if request.user.is_authenticated():
        return render(request, 'artwork.html', {
            'artwork': artwork,
        })

    if request.method == 'POST':
        form = TipForm(request.POST)

        if form.is_valid():
            tip = Tip(artwork=artwork, condition=form.cleaned_data['condition'])
            tip.save()

            return render(request, 'artwork.html', {
                'artwork': artwork,
                'tipSubmitted': True
            })
    else:
        form = TipForm

    return render(request, 'submit-a-tip.html', {
        'artwork': artwork,
        'form': form
    })


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
