from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate as auth_authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from.models import student,teacher,Admin,Attendance,Marks
from django.contrib.auth.forms import UserCreationForm
from .forms import AttendanceForm,MarksForm


# Create your views here.

def studentlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']

                student_obj=student.objects.get(userid=username,password=password)
                student_id = student_obj.stid 
                student_name = student_obj.stname
                return redirect('getstudenturl',stid=student_id)

def teacherlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']
                teacher_obj = teacher.objects.get(userid=username, password=password)
                teacher_id = teacher_obj.tid  
                teacher_name = teacher_obj.tname
                return redirect('getteacherurl',tid=teacher_id,)

def adminlogin(request):
        if request.method == "GET":
                return render(request,'alogin/login.html')
        if request.method == "POST":
                username = request.POST['uname']
                password = request.POST['pwd']

                admin_obj=Admin.objects.get(userid=username,password=password)
                if admin_obj != None:
                        students = student.objects.all()
                        teachers = teacher.objects.all()
                        return render(request,'alogin/admindash.html', {'students': students, 'teachers': teachers})
                else:
                        return redirect('aloginurl')
                

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
            address = request.POST['saddress']

            std = student(stid=stid,stname=stname,userid=userid,password=password,mail=email,mobile_no=mobile,address=address)
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
            address = request.POST['taddress']


            tea = teacher(tid=tid,tname=tname,salary=salary,userid=userid,password=password,mobile_no=mobile,mail=email,address=address)
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
              saddress=(request.POST['saddress'])
              print(request.FILES)
              obj=student(stid=sid,stname=sname,userid=suser,password=spass,mail=smail,mobile_no=smobile,address=saddress)
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
              taddress=(request.POST['taddress'])
              print(request.FILES)
              obj=teacher(tid=tid,tname=tname,salary=salary,userid=tuser,password=tpass,mobile_no=tmobile,mail=tmail,address=taddress)
              obj.save()
              return HttpResponse("update successfully")

def getstudent(request,stid):
       if request.method =='GET':
        stdobjects=student.objects.get(stid=stid)
        print(stdobjects)
        return render(request,'alogin/getstudents.html',{'obj':stdobjects})

def getteacher(request,tid):
       if request.method =='GET':
        tobjects=teacher.objects.get(tid=tid)
        students = student.objects.all()
        return render(request,'alogin/getteacher.html',{'faculty':tobjects,'students': students})



def viewattendance(request,stid):
       if request.method == 'GET':
        attendance_records = Attendance.objects.filter(student__stid=stid)
        return render(request,'alogin/viewattendance.html',{'attendance_records': attendance_records})

def viewmarks(request,stid):
       if request.method == 'GET':
        marks = Marks.objects.filter(student__stid=stid)
        return render(request,'alogin/viewmarks.html',{'marks_records': marks})
       

def addatt(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            date = form.cleaned_data['date']
            if Attendance.objects.filter(student=student, date=date).exists():
                messages.error(request, 'Attendance for this student on this date already exists.')
            else:
                form.save()
                messages.success(request, 'Attendance recorded successfully.')
                return redirect('pastattendence')  
    else:
        form = AttendanceForm()

    return render(request, 'alogin/add_attendance.html', {'form': form})


def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            subject = form.cleaned_data['subject']
            assessment_date = form.cleaned_data['assessment_date']
            if Marks.objects.filter(student=student, subject=subject, assessment_date=assessment_date).exists():
                messages.error(request, 'Marks for this student in this subject on this date already exist.')
            else:
                form.save()
                messages.success(request, 'Marks added successfully.')
                return redirect('add_marks')  
    else:
        form = MarksForm()

    return render(request, 'alogin/add_marks.html', {'form': form})

def logoutteacher(request):
    logout(request)
    return redirect('tloginurl')
def logoutstd(request):
    logout(request)
    return redirect('loginurl')
