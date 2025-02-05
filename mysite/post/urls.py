from django.urls import path
from .views import PostList, PostWrite

urlpatterns = [
    # path('write/', PostWrite.as_view()),
    path('list/', PostList.as_view()),
    path('write/',PostWrite.as_view()),
]