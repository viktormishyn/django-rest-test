from django.urls import path
from .views import article_list

urlpatterns = [
    path('api/articles', article_list),
]
