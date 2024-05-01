from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),  # Added comma here
    path("login/", views.handlelogin, name='login'),  # Added comma here
    path("registration/", views.handleregistration, name='registration'),  # Comma added here
    path("translator/", views.translator_home, name='translator_home'),
    path("project-manager/", views.project_manager, name='project_manager_home'),
    path("chief-editor/", views.chief_editor_home, name='chief_editor_home'),
    path("success/", views.successful_register, name='successful_register'),
    path('project/update/<int:project_id>/', views.update_project, name='update_project'),
    path('project-manager/<int:project_id>/', views.project_manager, name='project_manager'),
    path('project-manager/', views.project_manager, name='project_manager'),
    path('project-detail/<int:project_id>/', views.project_manager_detail, name='project_manager_detail'),
    path('translator/<int:project_id>/', views.project_detail, name='project_detail'),
# path('translator/<int:project_id>/', views.project2_detail, name='project2_detail'),
    path('some-view/', views.some_view, name='some_view'),
]