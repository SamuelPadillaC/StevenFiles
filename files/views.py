from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404

from .models import Student

# Create your views here.
def index(request):
    load_students = Student.objects.order_by('name')
    template = loader.get_template('files/index.html')
    context = {
        'load_students': load_students,
    }
    return HttpResponse(template.render(context, request))

def student(request, student_name):
    student = get_object_or_404(Student, pk=2)
    return render(request, 'files/student.html', {'student': student})

def file (request, student_id, file_type):
    return HttpResponse("You are looking at a file %s of student %s" % (file_type, student_id))