"""GoFriends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from gofriends_site.views import HomeView, CustomerCreate, WDView

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^customer_create/$', CustomerCreate.as_view(), name='customer_create'),

    url(r'^web_development/$', WDView.as_view(), name='web_development'),

    url(r'^admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

