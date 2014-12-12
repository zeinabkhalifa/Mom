from django.conf.urls import patterns, include, url
from ashghali import views

urlpatterns = patterns('',
        #login urls:
	url(r'^$', views.index, name='index'),
        url(r'^login',views.login,name='login'),
        url(r'^invalid_login',views.invalid_login,name='invalid_login'),
        url(r'^logout',views.logout,name='logout'),

        #submit:
        url(r'^submit',views.logout,name='submit'),

)
