from django.shortcuts import render

from artworks.models import Artwork


def index(request):
    artworks = Artwork.objects.order_by('-title').filter(active=True)[:5]
    context = {'artworks': artworks}

    return render(request, 'index.html', context)

def artwork(request, id):
    artwork = Artwork.objects.get(id=id)

    context = {'artwork': artwork}

    return render(request, 'artwork.html', context)

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
