from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from school.models import School
from .serializers import SchoolSerializer, SchoolCreateSerializers

class SchoolListAPIView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolCreateAPIView(CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolCreateSerializers
    permission_classes = [IsAuthenticated]

    #to authorise a user for creating content, Only User can Create Content but that does not belong To the User

    def perform_create(self,serializer):
        serializer.save()
