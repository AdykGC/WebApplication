from django.urls import path
from app import views
from . import views

urlpatterns = [
    path("", views.handleregistration, name='registration'),
# Login-Registration
    path("success/", views.successful_register, name='successful_register'),
    path("login/", views.handlelogin, name='login'),  
    path("registration/", views.handleregistration, name='registration'),  

# Workers main pages
    path("translator/", views.translator_home, name='translator_home'),
    path("chief-editor/", views.chief_editor_home, name='chief_editor_home'),



    path('update_activity/<int:activity_id>/', views.update_activity, name='update_activity'),
    path('update_activity_2/<int:activity_id>/', views.update_activity_2, name='update_activity_2'),
]