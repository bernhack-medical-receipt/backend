from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from .models import Receipt
from ..users.models import UserTypeChoices
from .serializers import ReceiptSerializer

from rest_framework import views


class ReceiptViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class UserReceiptByUserView(views.APIView):

    def get(self, request, user_id: str):
        # block users from watching others' receipts
        if request.user.role in (UserTypeChoices.PHARMACIST, UserTypeChoices.DOCTOR) or request.user.id == user_id:
            qs = Receipt.objects.filter(user=user_id)
            serializer = ReceiptSerializer(qs, many=True)
            return Response(serializer.data)
        else:
            return Response(status=HTTP_401_UNAUTHORIZED)
