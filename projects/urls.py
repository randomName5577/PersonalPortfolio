from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>', views.project_detail, name='project_detail'),
    path('<str:technology>', views.projects_sorted, name='projects_sorted')
]
