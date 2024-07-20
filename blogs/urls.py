from django.urls import path
from . import views


# http://127.0.0.1/category/2
urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category')
]