from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.Order.as_view(), name='Order'),
]