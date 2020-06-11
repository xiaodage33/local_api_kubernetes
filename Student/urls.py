from django.conf.urls import  url
from Student import  views

urlpatterns=[
    url(r'^add$', views.add),
    url(r'^index$', views.index),
    url(r'^getinfo$', views.select),
    url(r'^sms$', views.sms),
    url(r'^del$', views.del_info),
    url(r'^edit$', views.edit_info),

]