from django.conf.urls import url
from django.contrib import admin
from .views import Ruc_service,Dni,Numpersonas
urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^ruc/', Ruc_service.as_view(), name='ruc'),
    url(r'^dni/$', Dni.as_view(), name='dni'),
    url(r'^numdni/$', Numpersonas.as_view(), name='personas'),
]
