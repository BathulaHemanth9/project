from django import forms
from alogin.models import student,teacher,Attendance,Marks


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('present', 'Present'), ('absent', 'Absent')]),
        }

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks_obtained', 'total_marks', 'assessment_date', 'teacher']
        widgets = {
            'assessment_date': forms.DateInput(attrs={'type': 'date'}),
        }