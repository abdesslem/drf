from rest_framework import serializers
from .models import University, Student

# Serializers define the API representation.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name','university')



# Serializers define the API representation.
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)
