from django.urls import path
# from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetailAPIView

urlpatterns = [
    # path('api/articles', article_list),
    # path('api/articles/<int:pk>', article_detail),
    path('api/articles', ArticleAPIView.as_view()),
    path('api/articles/<int:id>', ArticleDetailAPIView.as_view()),
]
