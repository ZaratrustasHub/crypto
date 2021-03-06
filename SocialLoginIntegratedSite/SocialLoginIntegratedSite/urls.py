from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SocialLoginIntegratedSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bank/', include('bank.urls')), #
   # url(r'^accounts/', include('registration.backends.simple.urls')),
   # url(r'^accounts/login/', include('registration.backends.simple.urls')),  
   # url(r'^accounts/logout/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^captcha/', include('captcha.urls')),
)
