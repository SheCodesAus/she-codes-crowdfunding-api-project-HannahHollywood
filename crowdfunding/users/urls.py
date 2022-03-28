from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view()),
    path('<int:pk>/', views.CustomUserDetail.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('badge/', views.BadgeView.as_view(), name="badge-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
