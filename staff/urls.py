from django.urls import path
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    path('login/', views.login, name='Login'),
    path('admin/', views.admin_panel),
    path('manage/', views.manage_panel),


]


