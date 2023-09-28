"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tw_portfolio import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as allauth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.display_all, name='all'),
    path('home/', views.display_all, name="home"),
    path('dashboard/', views.display_dashboard, name="dashboard"),
    path('edit-home/', views.display_edit_home, name="edit-home"),
    path('edit-personal-detail', views.display_edit_personal_detail, name="edit-personal-detail"),
    path('add-skill', views.display_add_skill, name="add-skill"),
    path('add-project', views.display_add_project, name="add-project"),
    path('add-work-history', views.display_add_work_history, name="add-work-history"),
    path('add-education', views.display_add_education, name="add-education"),
    path('edit-skill', views.display_edit_skill, name="edit-skill"),
    path('edit-skill/<skill_id>/', views.display_edit_skill, name="edit-skill"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
