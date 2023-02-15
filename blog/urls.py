from django.urls import path
from .views import render_posts


urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', views)
]
