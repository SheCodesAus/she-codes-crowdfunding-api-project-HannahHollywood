from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>', views.PledgeDetail.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category'),
    path('comments/', views.CommentList.as_view()), 
    path('projects/comments/<int:pk>/', views.CommentDetail.as_view(), name="project-comments"),
]

urlpatterns = format_suffix_patterns(urlpatterns)