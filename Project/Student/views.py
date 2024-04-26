from django.shortcuts import render
from django.views import View
# Create your views here.

class StudentView(View):
    def get(self, request):
        return render(request, "Student/student.html")
class StudentCourse(View):
    def get(self, request):
        return render(request, "Student/my_course.html")
class StudentProfile(View):
    def get(self, request):
        return render(request, "Student/profile.html")
class StudentRegister(View):
    def get(self, request):
        return render(request, "Student/course_registration.html")