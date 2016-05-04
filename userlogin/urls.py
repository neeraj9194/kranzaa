from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.login_view, name='login'),
    url(r'^base$', views.base, name='base'),
]
