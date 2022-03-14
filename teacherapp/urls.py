from django.urls import path
from . import views

appname = 'teacherapp'

urlpatterns = [
    path('', views.visit, name='visit'),

]
