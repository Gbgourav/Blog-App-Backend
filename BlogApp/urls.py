"""BlogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Backend import views
from Backend.views import BlogCreateView, ObtainAuthToken, GetBlogDataAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', admin.site.urls),
    path('blog/', BlogCreateView.as_view(), name='blog-create'),
    path('token/', ObtainAuthToken.as_view(), name='token'),
    path('get_data/', GetBlogDataAPI.as_view(), name='get_data'),
    path('csrf_token/', views.csrf_token_view, name='csrf_token'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
