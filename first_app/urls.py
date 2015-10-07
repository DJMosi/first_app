from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$','home.views.index', name='home'),
     url(r'^feedback/$','home.views.feedback', name='Feedback'),
     url(r'^admin/', include(admin.site.urls)),
)

    # Examples:
    #url(r'^$', 'first_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

