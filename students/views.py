# Create your views here.
from django.http import HttpResponse
from students.models import Student


def detail(request, student_id):
    stud = Student.objects.get(pk=student_id)
    return HttpResponse("you requested the student id=%s,name=%s " % (student_id,stud.name))
