from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Receipt
from .serializers import ReceiptSerializer

from rest_framework import views


class ReceiptViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class UserReceiptView(views.APIView):

    def get(self, request, user_id: str):
        qs = Receipt.objects.filter(user=user_id)
        serializer = ReceiptSerializer(qs, many=True)
        return Response(serializer.data)
