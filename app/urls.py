from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/<int:id>/', views.blog, name='blog'),
    re_path(r'^product/(?P<slug>[\w-]+)/$', views.product, name='product'),
]
