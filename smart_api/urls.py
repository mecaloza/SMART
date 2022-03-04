

from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path("create_dot/", views.Create_dot.as_view(), name="Create_dot"),
    path("dot_graph/<int:codigo>/", views.Dot_Graph.as_view(), name="Dot_Graph"),
    path("tag_graph/", views.Tag_Graph.as_view(), name="tag_graph"), 
]

