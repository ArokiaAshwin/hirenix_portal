from django.contrib import admin
from django.urls import path
from portal import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # The Smart Home Page (Redirects based on role)
    path('', views.index, name='index'), 

    path('admin/', admin.site.urls),
    path('list/', views.internship_list, name='list'),
    path('apply/<int:pk>/', views.apply_now, name='apply_now'),
    path('success/<int:application_id>/', views.success_page, name='success_page'),
    
    # Recruiter Paths
    path('dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('post-internship/', views.post_internship, name='post_internship'),
    path('update-status/<int:pk>/<str:status>/', views.update_status, name='update_status'),
    
    # Student Paths
    path('my-applications/', views.student_dashboard, name='my_applications'),
    
    # Auth paths
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)