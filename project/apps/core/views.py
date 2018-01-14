from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer

# ViewSets define the view behavior.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# ViewSets define the view behavior.
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
