from django.db import models

# Create your models here.

class student(models.Model):
    stid=models.IntegerField(primary_key=True)
    stname=models.CharField(max_length=20)
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mail=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=20)
    address=models.CharField(max_length=30,default="Unknown")
    def __str__ (self):
        return self.stname

class teacher(models.Model):
    tid = models.IntegerField(primary_key=True)
    tname = models.CharField(max_length=20)
    salary = models.IntegerField()
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mobile_no=models.CharField(max_length=20)
    mail=models.CharField(max_length=20)
    address=models.CharField(max_length=30,default="Unknown")
    def __str__ (self):
        return self.tname
    
class Admin(models.Model):
    adminid = models.IntegerField(primary_key=True)
    adminname = models.CharField(max_length=20)
    salary = models.IntegerField()
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mobile_no=models.CharField(max_length=20)
    mail=models.CharField(max_length=20)
    def __str__ (self):
        return self.adminname

class Attendance(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    class Meta:
        unique_together = ('student', 'date') 
    def __str__(self):
        return f"{self.student} - {self.date}: {self.status}"

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)  # E.g., 'CS101'

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)  # Default total marks
    assessment_date = models.DateField()
    teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, related_name='marks_records')

    class Meta: 
        unique_together = ('student', 'subject', 'assessment_date')
    def __str__(self):
        return f"{self.student} - {self.subject.name}: {self.marks_obtained}/{self.total_marks} (Recorded by {self.teacher})"