from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from student import views

urlpatterns = patterns('',
    url(r'^$', 'student.views.login_view', name='home_login'),
    url(r'^logout/$', 'student.views.logout_view', name='home_login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls')),
    url(r'^office/', include('office.urls')),
    url(r'^hod/', include('hod.urls')),
    url(r'^examination/', include('examination.urls')),
    url(r'^library/', include('library.urls')),
    url(r'^pt/', include('pt.urls')),
    url(r'^director/', include('director.urls')),

)
