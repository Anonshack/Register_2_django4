from django.urls import path
from .views import (HomePageView,
                    BlogDeleteView,
                    BlogDetailView,
                    NewsPostView,
                    )

urlpatterns = [
    path('new/post/', NewsPostView.as_view(), name='new_post'),
    path('clay/', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/delete ', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('sat/', InfoPageView.as_view(), name='info'),
]