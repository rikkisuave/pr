from django.conf.urls import include,url
from django.contrib import admin

urlpatterns=[
    url(r'^polls/', include('polls.urls')),
    url(r'^frm/', include('frmtest.urls')),
    url(r'^bo/',include('polls.urls')),
    url(r'^admin/', admin.site.urls),
] 
