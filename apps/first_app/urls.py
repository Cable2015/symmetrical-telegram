from django.conf.urls import url
from  . import views

print "TEST IN APP URLS.PY"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog$', views.blog)

]
