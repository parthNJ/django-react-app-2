from lead.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.lead.all()
        #get all leads by a specific user

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
