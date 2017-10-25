from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from artworks import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile', views.profile),
    url(r'^artwork/(?P<id>[\w-]+)$', views.artwork, name='artwork'),
    url(r'^artwork/(?P<id>[\w-]+)/adopt/$', views.adopt, name='adopt'),
    url(r'^artwork/(?P<id>[\w-]+)/unadopt/$', views.unadopt),
    url(r'^artwork/(?P<id>[\w-]+)/check-in/$', views.checkin, name='checkin'),
    url(r'^artworks/$', views.artworks),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
