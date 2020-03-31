from django.urls import path

from . import views

app_name = 'files'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:student_name>/', views.student, name='student'),
    path('<str:student_name>/files/<file_type>', views.file, name='file'),
]
