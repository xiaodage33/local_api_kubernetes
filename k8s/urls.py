from django.conf.urls import  url
from k8s import  views
urlpatterns = [
    url(r'^log$',views.getLog),
    url(r'^loginfo$',views.getLogInfo),
    url(r'^errorlog$',views.getErrorLog),
    url(r'^eroorlogfile$',views.log_error_file),
]