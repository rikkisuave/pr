from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^frm', views.contact, name='contact'),
]
