from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from rest_framework.response import Response
from alogin.models import student,teacher
from.serializers import StudentSerializer,TeacherSerializer
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import authentication_classes,permission_classes

# Create your views here.

@api_view(['GET','POST'])
def getstudentapi(request):
    if request.method == 'GET':
        #internalprocessing()
        std = student.objects.all()
        stddata = StudentSerializer(std,many =True)
        return Response(stddata.data)

    if request.method == 'POST':
        stddata = StudentSerializer(data=request.data)
        if stddata.is_valid() == True:
            stddata.save()
            return Response(status = HTTP_201_CREATED)
        else:
            return Response(stddata.errors,status = HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def modifystudentapi(request,pk):
    print("hooo")
    print(request.method)
    std = student.objects.get(stid = pk)
    if request.method == 'PUT':
        stddata= StudentSerializer(std,data=request.data)

        if stddata.is_valid() == True:
            stddata.save()
            return Response(status = HTTP_200_OK)
        else:
            return Response(stddata.errors,status = HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        stddata = StudentSerializer(std)
        print(stddata.data)
        return Response(stddata.data)
        
    if request.method == 'DELETE':
        print("Hi")
        std = student.objects.get(stid = pk)
        std.delete()
        return Response(status = HTTP_200_OK)
    

@api_view(['GET','POST'])
def getteacherapi(request):
    if request.method == 'GET':
        #internalprocessing()
        emps = teacher.objects.all()
        empdata = TeacherSerializer(emps,many =True)
        return Response(empdata.data)

    if request.method == 'POST':
        empdata = TeacherSerializer(data=request.data)
        if empdata.is_valid() == True:
            empdata.save()
            return Response(status = HTTP_201_CREATED)
        else:
            return Response(empdata.errors,status = HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def modifyteacherapi(request,pk):
    print("hooo")
    print(request.method)
    emps = teacher.objects.get(tid = pk)
    if request.method == 'PUT':
        empdata= TeacherSerializer(emps,data=request.data)

        if empdata.is_valid() == True:
            empdata.save()
            return Response(status = HTTP_200_OK)
        else:
            return Response(empdata.errors,status = HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        empdata = TeacherSerializer(emps)
        print(empdata.data)
        return Response(empdata.data)
        
    if request.method == 'DELETE':
        print("Hi")
        emps = teacher.objects.get(tid = pk)
        emps.delete()
        return Response(status = HTTP_200_OK)


def studentlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']

                student_obj=student.objects.filter(userid=username,password=password)
                if student_obj != None:
                        return redirect('studenturl')
                else:
                        return redirect('loginurl')

def teacherlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']

                teacher_obj=teacher.objects.get(userid=username,password=password)
                if teacher_obj != None:
                        return redirect('teacherurl')
                else:
                        return redirect('loginurl')


# @login_required  # Ensure only logged-in users can access
# def studentdash(request):
#     user = request.user

#     # Ensure the logged-in user is a student
#     if user.role == 'student':
#         # Pass the user's details to the template
#         context = {
#             'stid': user.stid,
#             'stname': user.stname,
#             'mail': user.mail,
#             'mobile_no': user.mobile,
#         }
#         return render(request, 'studentdash.html', context)
#     else:
#         # If not a student, restrict access and redirect or show error
#         messages.error(request, 'Access restricted to students only.')
#         return redirect('loginurl')
