"""kohsuke URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from web.views import Index, StuffDetailView, AccountDetailView, StuffMoreListView
from api import urls as api_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Index.as_view(), name='index'),
    path('stuff/<int:pk>', StuffDetailView.as_view(), name='stuff_detail'),
    path('stuff/more/<int:type>', StuffMoreListView.as_view(), name='stuff_more'),
    path('account/<int:pk>', AccountDetailView.as_view(), name='account_detail'),
    path('api/', include(api_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
