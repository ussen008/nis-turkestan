
from django.urls import path
from . import views

appname = 'studentapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('students/', views.students, name='student_list'),
    path('students/<int:id>/', views.student, name='student'),
    path('students/new', views.add_student, name='add_student'),
    path('ajax/load-students/', views.load_students, name='ajax_load_student'), # AJAX
    path('infocarta/', views.info, name='infocarta'),
    path('appeal/', views.appeal_upload, name='appeal'),
    path('participant/', views.participant_upload, name='participant'),
    
]
