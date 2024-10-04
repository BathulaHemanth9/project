from django.urls import path
from.import views

urlpatterns=[
    path('stdlogin/',views.studentlogin,name="loginurl"),
    path('teacherlogin/',views.teacherlogin,name="tloginurl"),
    path('adminlogin/',views.adminlogin,name="aloginurl"),
    path('newstd/',views.poststudent,name="poststdurl"),
    path('newteacher/',views.postteacher,name="postteacher"),
    path('stdupdate/<int:stid>/',views.studentupdate,name="stdupdateurl"),
    path('teacherupdate/<int:tid>/',views.teacherupdate,name="teacherupdateurl"),
    path('getstudent/<int:stid>/',views.getstudent, name="getstudenturl" ),
    path('getteacher/<int:tid>/',views.getteacher, name="getteacherurl" ),
    path('viewattendance/<int:stid>/',views.viewattendance,name="viewattendance"),
    path('viewmarks/<int:stid>/',views.viewmarks,name="viewmarks"),
    path('addattd/', views.addatt, name='pastattendence'),
    path('addmarks/', views.add_marks, name='add_marks'),
    path('logout/',views.logoutteacher,name="tlogouturl"),
    path('slogout/',views.logoutstd,name="slogouturl"),
    
    
]