from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.survey1),
    url(r'^blogs$', views.survey2),
    url(r'^comments/(?P<id>\d+)$', views.survey3)
]
