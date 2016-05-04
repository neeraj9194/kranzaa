from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.store_view, name='view_all_stores'),
    url(r'^category/(?P<slug>[a-z,0-9,-]+)', views.store_category, name='store_cat'),
    url(r'^(?P<slug>[a-z,0-9,-]+)', views.store_home, name='store'),
]
