from django.urls import path
from . import views  # An alternative to "import blog.views"

urlpatterns = [
    path('new', views.new_blog, name = 'new'),
    path('create', views.create, name = 'create'),
    path('<int:blog_id>', views.detail, name = 'detail'),
]
