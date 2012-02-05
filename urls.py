from django.conf.urls.defaults import include, patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Example:
    # (r'^bullshit_bingo/', include('bullshit_bingo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'generator.views.generate'),
    (r'^(?P<x>\d+)x(?P<y>\d+)$', 'generator.views.generate'),
    
    (r'^add/author/$', 'author.views.add'),
    (r'^view/author/(?P<ID>\d+)/$', 'author.views.view'),
    (r'^view/author/list/', 'author.views.listAll'),
    
    (r'^add/phrase/$', 'phrase.views.add'),
    (r'^view/phrase/(?P<ID>\d+)/$', 'phrase.views.view'),
    (r'^view/phrase/list/', 'phrase.views.listAll'),
)
