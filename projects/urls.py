from django.urls import path
from . import views as projectview

urlpatterns = [
    path("project/<int:pk>/", projectview.projectdetail, name="projectdetails"),
]