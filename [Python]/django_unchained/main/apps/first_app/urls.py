from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.survey1),
    url(r'^survey$', views.survey2),
    url(r'^result$', views.survey3)
]
