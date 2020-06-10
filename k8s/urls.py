from django.conf.urls import  url
from k8s import  views
urlpatterns = [
    url(r'^log$',views.getLog),
    url(r'^loginfo$',views.getLogInfo),

]