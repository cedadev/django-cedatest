
from django.urls import path
from cedatest_control import views

urlpatterns = (
    path('list_users', views.list_users, name='listusers'),
)
