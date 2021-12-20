

from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path("create_dot/", views.Create_dot.as_view(), name="Create_dot"),
 
]

