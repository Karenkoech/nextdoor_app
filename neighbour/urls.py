from django.urls import path
from . import views

urlpatterns = [
      
     path('', views.Home_view, name='home_view'),
     path('all-hoods/', views.hoods, name='hood'),
     path('new-hood/', views.create_hood, name='new-hood'),
     path('join_hood/<id>', views.join_hood, name='join-hood'),
     path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
     path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
     path('<hood_id>/new-post', views.create_post, name='post'),
     path('<hood_id>/members', views.hood_members, name='members'),
     path('search/', views.search_business, name='search'),
     
]