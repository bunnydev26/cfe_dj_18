from django.conf.urls import include, url
from django.contrib import admin
from newsletter.views import contact
urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),

]
