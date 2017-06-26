from django.shortcuts import get_object_or_404, render

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from artworks.models import Artwork, Adoption


def index(request):
    artworks = Artwork.objects.order_by('-id').filter(active=True)[:5]
    context = {'artworks': artworks}

    return render(request, 'index.html', context)

def artwork(request, id):
    artwork = get_object_or_404(Artwork, pk=id)

    adoptees = Adoption.objects.filter(artwork=artwork)

    if request.user.is_authenticated:
        adopted = Adoption.objects.filter(user=request.user, artwork=artwork)
    else:
        adopted = False

    return render(request, 'artwork.html',
        {'artwork' : artwork, 'adoptees': adoptees, 'adopted': adopted})

@login_required
def adopt(request, id):
    artwork = get_object_or_404(Artwork, pk=id)
    adoptees = Adoption.objects.filter(artwork=artwork)

    check_adopted = Adoption.objects.filter(user=request.user, artwork=artwork)

    if not check_adopted:
        adopt = Adoption(user=request.user, artwork=artwork)
        adopt.save()

    adopted = True

    return render(request, 'artwork.html', {'artwork' : artwork, 'adoptees': adoptees, 'adopted': adopted})

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
