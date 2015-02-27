from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shadrus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^resumes/get/(?P<person_id>\d+)/$', 'person.views.personpage'),
    url(r'^blank/get/(?P<username>\w+)/$', 'person.views.ownblank'),
    url(r'^blank/second/get/(?P<username>\w+)/$', 'person.views.ownblanksecond'),
    url(r'^saveblank/get/(?P<username>\w+)/$', 'person.views.saveownblank'),
    url(r'^saveeducationblank/get/(?P<username>\w+)/$', 'person.views.addeducation'),
    url(r'^savejobblank/get/(?P<username>\w+)/$', 'person.views.addjob'),

    url(r'^cabineteducation/get/(?P<username>\w+)/$', 'person.views.cabineteducation'),
    url(r'^cabinetjob/get/(?P<username>\w+)/$', 'person.views.cabinetjob'),

    url(r'^changeeducation/get/(\d+)/$', 'person.views.changeeducation'),
    url(r'^changejob/get/(\d+)/$', 'person.views.changejob'),

    url(r'^query/get/$', 'person.views.mainpage'),

    url(r'^cabinet/get/(?P<username>\w+)/$', 'person.views.owncabinet'),
    url(r'^savecabinet/get/(?P<username>\w+)/$', 'person.views.saveowncabinet'),
    url(r'^page/(\d+)/$', 'person.views.mainpage'),
    url(r'^$', 'person.views.mainpage'),
)
