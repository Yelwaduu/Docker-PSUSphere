from django.urls import path
from . import views

urlpatterns = [
    path('colleges/', views.CollegeListCreateAPIView.as_view(), name='college-list-create'),
    path('colleges/<int:pk>', views.CollegeRetrieveUpdateDestroyAPIView.as_view(), name='college-detail'),
    
]