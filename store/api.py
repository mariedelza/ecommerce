from rest_framework import viewsets
from .serializers import productSerializer
from rest_framework.permissions import IsAuthenticated
from .models import product


class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
    permission_classes = [IsAuthenticated]
    
    
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(created_by=user)
    