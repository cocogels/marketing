from django.urls import path
from . import views

app_name = 'crm_blog'

urlpatterns = [
    path('home/', views.blog_home_view, name='home'),
]
