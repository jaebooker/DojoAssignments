from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.survey1),
    url(r'^ninjas$', views.survery2),
    url(r'^(?P<color>\w+)$', views.survey3)
]
