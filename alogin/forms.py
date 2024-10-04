from django import forms
from .models import student,teacher,Attendance,Marks

# class StudentAuthenticationForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')

#         if username and password:
#             try:
#                 student = student.objects.get(username=username)
#                 if not student.password == password: 
#                     raise forms.ValidationError("Incorrect password.")
#             except student.DoesNotExist:
#                 raise forms.ValidationError("Student with this username does not exist.")

#         return cleaned_data
    

# class FacultyAuthenticationForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')

#         if username and password:
#             try:
#                 faculty = teacher.objects.get(username=username)
#                 if not teacher.password == password :
#                     raise forms.ValidationError("Incorrect password.")
#             except teacher.DoesNotExist:
#                 raise forms.ValidationError("Faculty with this username does not exist.")

#         return cleaned_data

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