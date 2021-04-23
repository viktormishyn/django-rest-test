from django.urls import path
from .views import article_list, article_detail 

urlpatterns = [
    path('api/articles', article_list),
    path('api/articles/<int:pk>', article_detail),
]
