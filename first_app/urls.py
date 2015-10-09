from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# admin.autodiscover()


urlpatterns = patterns[
	url(r'^$', 'home.views.index', name='home'),
	url(r'^feedback/$', 'home.views.feedback', name='feedback'),
	url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Examples:
# url(r'^$', 'first_app.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
