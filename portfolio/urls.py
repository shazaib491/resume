from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('admin_mini',admin_mini,name='admin_mini'),
    path('dashboard/',dashboard,name='dashboard'),
    path('About_admin/',About_admin,name="about_admin"),
    path('about_all/',About_all,name="about_all"),
    path('about_update/<int:about_id>',about_update,name="about_update"),
    path('Logout',Logout,name="Logout")
]
