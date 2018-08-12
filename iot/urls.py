from django.conf.urls import url
from . import views
app_name = "iot"
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^signup', views.UserFormView.as_view(), name='signup')
]