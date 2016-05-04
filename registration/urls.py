from django.conf.urls import include, url
import views

urlpatterns = [

    # url(r'^$', views.base, name='base'),
    # url(r'^guestregistration/$', views.guestregisration, name='guestregistration'),
    url(r'^$', views.Base, name='Base'),
    url(r'^Guestregistration',views.Guestregistration,name='Guestregistration'),
    url(r'^Passportupload',views.Passportupload,name='Passportupload'),

]
