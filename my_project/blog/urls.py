from django.urls import path
from blog.views import home, posts, browser


app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('posts', posts, name='posts'),
    path('browser', browser, name='browser'),
]