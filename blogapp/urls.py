from django.urls import path
from . import views as blogappview

urlpatterns = [
    path("", blogappview.blogindex, name="blogindex"),
    path("<category>/", blogappview.blogcategory, name="blogcategory"),
    path("post/<int:pk>/", blogappview.blogdetail, name="blogdetails"),
]
