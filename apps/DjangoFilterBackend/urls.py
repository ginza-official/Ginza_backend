from django.urls import path
from .views import *

urlpatterns = [
    path("", UserListView.as_view()),  # list all users
    path("user/<int:pk>", UserbyID.as_view()),  # find user by id
    path("user_search/", UsernameListSearch.as_view()),  # find user by username
    path("user_search/<str:username>", UsernameSearch.as_view()),  # user search by username retriveview
    path("custom/", CustomFilter.as_view()),  # user search by custom filterset class
]