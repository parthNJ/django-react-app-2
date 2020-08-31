from .models import Program, UserProgram, PurchasedProgram
from rest_framework import viewsets, permissions
from .serializers import ProgramSerializers, UserProgramSerializers, PurchasedProgramSerializers

class UserProgramViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserProgramSerializers
    def get_queryset(self):
        return UserProgram.objects.filter(user=self.request.user)    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class ProgramViewset(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    queryset = Program.objects.all()
    serializer_class = ProgramSerializers

class PurchasedProgramViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PurchasedProgramSerializers
    def get_queryset(self):
        return PurchasedProgram.objects.filter(user=self.request.user)    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
