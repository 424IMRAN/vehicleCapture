"""TransAnalyst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard', views.dashboard, name='home'),
    path('camera', views.cameras, name='cameralist'),
    path('camera/new', views.cameraNew, name='camera'),    
    path('video', views.video, name='video'),
    path('video/new', views.videoNew, name='videolist'),
    path('delete_cam/<list_id>/', views.delete_cam,name='delete_cam' ),
    path('edit_cam/<list_id>/', views.edit_cam,name='edit_cam' ),
    path('delete_vid/<list_id>/', views.delete_vid,name='delete_vid' ),
    path('edit_vid/<list_id>/', views.edit_vid,name='edit_vid' ),
]
