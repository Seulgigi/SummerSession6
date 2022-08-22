from django.urls import path
from .views import *
from . import views

app_name = "projectapp"
urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>', views.movie_detail_update_delete),
    path('review/', views.review_list_create),
    path('<int:movie_pk>/create_review', views.review_detail_update_delete),
]