from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.survey1),
    url(r'^process_money$', views.survery2)
]
