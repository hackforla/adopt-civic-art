
from django.conf.urls import url
from django.contrib import admin

from artworks import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^artwork/(?P<id>[\w-]+)$', views.artwork),
    url(r'^admin/', admin.site.urls),
]
