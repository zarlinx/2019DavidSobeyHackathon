"""mysite URL Configuration

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
from django.urls import include, path
from pages.views import index_view, input_view, storewise_view, store_view, class_view, csvStore_view, csvProduct_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path('index/', index_view, name='index'),
    path('input/', input_view, name='input'),
    path('storewise/', storewise_view, name='storewise'),
    #path('payzant/', include('payzant.urls')),
    path('class/',class_view, name='class'),
    path('store/', store_view, name='store'),
    #path('dashboard/', dashboard_view, name='dashboard'),
    path('csvStore/', csvStore_view, name='csvStore'),
    path('csvProduct/', csvProduct_view, name='csvProduct'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
