from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate as auth_authenticate,login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from.models import student,teacher,Admin
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def studentlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']

                student_obj=student.objects.filter(userid=username)
                return render(request,'alogin/getstudent.html',{'student':student_obj})
                # print(student_obj)
                # if student_obj != None:
                #         return redirect('getstudenturl')
                # else:
                #         return redirect('loginurl')

def teacherlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']

                teacher_obj=teacher.objects.filter(userid=username)
                return render(request,'alogin/getteacher.html',{'teacher':teacher_obj})
                # if teacher_obj != None:
                #         return redirect('getteacherurl')
                # else:
                #         return redirect('loginurl')

def adminlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']

                admin_obj=Admin.objects.get(userid=username,password=password)
                if admin_obj != None:
                        return HttpResponse("hello admin")
                else:
                        return redirect('loginurl')
                

def poststudent(request):
      if request.method == 'GET':
            return render(request,'alogin/poststudent.html')
      
      if request.method == 'POST':
            stid = request.POST['stdid']
            stname = request.POST['stdname']
            userid = request.POST['stuname']
            password = request.POST['stpassword']
            email = request.POST['stemail']
            mobile = request.POST['stnum']

            std = student(stid=stid,stname=stname,userid=userid,password=password,mail=email,mobile_no=mobile)
            std.save()
            return HttpResponse('welcome')

def postteacher(request):
      if request.method == 'GET':
            return render(request,'alogin/postteacher.html')
      
      if request.method == 'POST':
            tid = request.POST['teid']
            tname = request.POST['tename']
            userid = request.POST['teuname']
            password = request.POST['tepassword']
            email = request.POST['teemail']
            mobile = request.POST['tenum']
            salary = request.POST['tesal']

            tea = teacher(tid=tid,tname=tname,salary=salary,userid=userid,password=password,mobile_no=mobile,mail=email)
            tea.save()
            return HttpResponse('Teacher details successfully register')
      

def studentupdate(request,stid):
       if request.method == "GET":
              stdata=student.objects.get(stid=stid)
              return render(request,'alogin/updatestd.html',{'stupdate':stdata})
       
       if request.method == 'POST':
              sid=int(request.POST['sid'])
              sname=(request.POST['sname'])
              suser=(request.POST['suser'])
              spass=(request.POST['spass'])
              smail=(request.POST['smail'])
              smobile=(request.POST['smobile'])
              print(request.FILES)
              obj=student(stid=sid,stname=sname,userid=suser,password=spass,mail=smail,mobile_no=smobile)
              obj.save()
              return HttpResponse("update successfully")
       
def teacherupdate(request,tid):
       if request.method == 'GET':
              teacherdata=teacher.objects.get(tid=tid)
              return render(request,'alogin/updateteacher.html',{'teupdate':teacherdata})
       
       if request.method == 'POST':
              tid=int(request.POST['tid'])
              tname=(request.POST['tname'])
              salary=int(request.POST['tsal'])
              tuser=(request.POST['tuser'])
              tpass=(request.POST['tpass'])
              tmobile=(request.POST['tmobile'])
              tmail=(request.POST['tmail'])
              print(request.FILES)
              obj=teacher(tid=tid,tname=tname,salary=salary,userid=tuser,password=tpass,mobile_no=tmobile,mail=tmail)
              obj.save()
              return HttpResponse("update successfully")

def getstudent(request):
       if request.method =='GET':
        stdobjects=student.objects.all()
        print(stdobjects)
        return render(request,'alogin/getstudent.html',{'student':stdobjects})

def getteacher(request):
       if request.method =='GET':
        tobjects=teacher.objects.all()
        print(tobjects)
        return render(request,'alogin/getteacher.html',{'teacher':tobjects})

# def studentlogin(request):
#         if request.method == "GET":
#                 return render(request,'alogin/login.html')
#         if request.method == "POST":
#                 username = request.POST['uname']
#                 password = request.POST['pwd']

#                 student_obj=student.objects.filter(userid=username,password=password)
#                 if student_obj != None:
#                         return redirect('studenturl')
#                 else:
#                         return redirect('loginurl')