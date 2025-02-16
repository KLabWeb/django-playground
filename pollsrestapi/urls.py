from django.urls import path

from . import views

app_name = "pollsrestapi"
urlpatterns = [
    path("", views.questions_list, name="questions_list"),
    path("<int:question_id>/", views.detail, name="detail"),
]