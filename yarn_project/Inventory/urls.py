from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    ##Projects
    path('', views.home, name='home'),
    path('project/create', views.ProjectCreateView.as_view(), name="project-create"),
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(), name="project-update"),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name="project-delete"),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name="project-detail"),
    path('completed_projects/', views.completed, name="completed"),
    ##Yarn
    path('yarn/', views.yarn, name="yarn"),
    path('yarn/create/', views.YarnCreateView.as_view(), name="yarn-create"),
    path('yarn/<int:pk>/update/', views.YarnUpdateView.as_view(), name="yarn-update"),
    path('yarn/<int:pk>/delete/', views.YarnDeleteView.as_view(), name="yarn-delete"),
    path('yarn/<int:pk>/', views.YarnDetailView.as_view(), name="yarn-detail"),
    ##Project Ideas
    path('project/ideas', views.projectIdeas, name="project-ideas"),
    path('project/ideas/create', views.ProjectIdeasCreateView.as_view(), name="project-ideas-create"),
    path('project/ideas/<int:pk>/update', views.ProjectIdeasUpdateView.as_view(), name="project-ideas-update"),
    path('project/ideas/<int:pk>/delete/', views.ProjectIdeasDeleteView.as_view(), name="project-ideas-delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)