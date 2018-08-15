from django.conf.urls import url
from . import views
app_name = "iot"
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^accounts/', views.UserFormView.as_view(), name='accounts')
]