from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostView.as_view(), name= 'posts_list'),
    path('pred/', views.Predict.as_view(), name= 'pred_list'),
]