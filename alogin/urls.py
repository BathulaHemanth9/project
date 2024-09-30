from django.urls import path
from.import views

urlpatterns=[
    path('stdlogin/',views.studentlogin,name="loginurl"),
    # path('signup/',views.adminsignup,name="signupurl"),
    path('teacherlogin/',views.teacherlogin,name="loginurl"),
    path('adminlogin/',views.adminlogin,name="loginurl"),
    path('newstd/',views.poststudent,name="poststdurl"),
    path('newteacher/',views.postteacher,name="postteacher"),
    path('stdupdate/<int:stid>/',views.studentupdate,name="stdupdateurl"),
    path('teacherupdate/<int:tid>/',views.teacherupdate,name="teacherupdateurl"),
    path('getstudent/',views.getstudent, name="getstudenturl" ),
    path('getteacher/',views.getteacher, name="getteacherurl" ),
    
]