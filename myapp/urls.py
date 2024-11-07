from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my_home'),
    path('about/', views.about, name='about_us'),
    path('services/', views.services, name='our_services'),
    path('blog/', views.blog, name='blog_posts'),
]
