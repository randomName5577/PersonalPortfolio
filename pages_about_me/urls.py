from django.urls import path

from . import views

app_name = 'pages_about_me'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('aboutme/', views.AboutMePage.as_view(), name='aboutme'),
    path('contactme/', views.contactmepage, name='contactme'),
]
