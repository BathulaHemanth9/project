from rest_framework import serializers
from alogin.models import student,teacher,Admin
from rest_framework.exceptions import ValidationError

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
    
    # def validate_salary(self,esal):
    #     if esal<0:
    #         raise serializers.ValidationError("Negative salary")
        
    #     return esal

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
