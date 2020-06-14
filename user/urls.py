from django.contrib import admin
from django.urls import path
from .views import UserCRUD

urlpatterns = [
    path(r'^(?P<pk>\d+)/$', UserCRUD.as_view(),name = 'CRUD'),
]
