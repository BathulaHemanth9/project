from django.urls import path
from.import views

urlpatterns = [
    path('getstudent/',views.getstudentapi,name="studenturl"),
    path('modifystudent/<int:pk>/',views.modifystudentapi),
    path('getteacher/',views.getteacherapi,name="teacherurl"),
    path('modifyteacher/<int:pk>/',views.modifyteacherapi),
    path('studentlogin/',views.studentlogin),
    path('teacherlogin/',views.teacherlogin),
    # path('studentdashboard/',views.studentdash,name="stddashurl")

]