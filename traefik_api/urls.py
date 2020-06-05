from django.conf.urls import  url
from traefik_api  import  views
urlpatterns=[
    url(r'^trae$',views.trae),
]