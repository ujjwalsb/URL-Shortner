from django.conf.urls import include, url
from url_shortner import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'(?P<short_url_id>\w{6})$', views.original_link_redirect, name='original_link_redirect'),
    url(r'^shortlink/$', views.short_link, name='short_link'),
    url(r'^analytics/$', views.all_link, name='all_link'),
]
