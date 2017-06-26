
from django.conf.urls import include, url
from django.contrib import admin

from artworks import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
  url(r'^accounts/', include('registration.backends.simple.urls')),
  url(r'^accounts/profile', views.index),
	url(r'^artwork/(?P<id>[\w-]+)$', views.artwork),
  url(r'^artwork/(?P<id>[\w-]+)/adopt/$', views.adopt),
  url(r'^admin/', admin.site.urls),
]
