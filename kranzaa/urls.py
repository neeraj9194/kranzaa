"""kranzaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from userlogin import views as user_view
from store import views as store_view

urlpatterns = [
    url(r'^$', user_view.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('userlogin.urls')),
    url(r'^logout/', user_view.logout_view),
    url(r'^store/', include('store.urls')),
    url(r'^search/$', store_view.searchResults, name='searchResults'),
    url(r'^chart/', include('senticomment.urls')),
]
