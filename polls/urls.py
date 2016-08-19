from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^te$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^temtest$', views.temtest, name='this is a template test'),
    url(r'^bo/$',views.boottmp,name='boot'),
]
