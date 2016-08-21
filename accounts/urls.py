from django.conf.urls import include,url

from accounts.views import index, login_view

urlpatterns = [
    url(r'^index/$', index, name='index_view'),
    url(r'^login/$', login_view, name='login_view'),

]
