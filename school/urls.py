from django.conf.urls import include,url

from . import views
from school.api.api_views import (
    SchoolListAPIView,
)

urlpatterns = [
    url(r'^api_list/$', SchoolListAPIView.as_view(), name='school_list'),
]
