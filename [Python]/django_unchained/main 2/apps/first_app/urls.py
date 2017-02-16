from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.yourMethodFromUrls),
    url(r'^create$', views.create)
]
