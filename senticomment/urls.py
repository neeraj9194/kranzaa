from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^(?P<slug>[a-z,0-9,-]+)', views.linechart, name='view_line_chart'),
    
]
