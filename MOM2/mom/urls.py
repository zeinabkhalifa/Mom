from django.conf.urls import patterns, include, url
from mom import views

urlpatterns = patterns('',
        #login urls:
        url(r'^$', views.index, name='index'),
        url(r'^login/$',views.login,name='login'),
        url(r'^logout/$',views.logout,name='logout'),
        url(r'^auth_view/$',views.auth_view,name='auth_view'),

	#submit:
        url(r'^submit/$',views.logout,name='submit'),

)
