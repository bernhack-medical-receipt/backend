from rest_framework import serializers
from .models import Receipt, Drug, DrugPrescription
from ..users.serializers import UserSerializer


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class DrugPrescriptionSerializer(serializers.ModelSerializer):
    drug = DrugSerializer()

    class Meta:
        model = DrugPrescription
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    drugs = DrugSerializer(many=True)
    user = UserSerializer()
    prescribed_drugs = serializers.SerializerMethodField()

    class Meta:
        model = Receipt
        fields = '__all__'

    def get_prescribed_drugs(self, obj):
        return DrugPrescriptionSerializer(DrugPrescription.objects.filter(receipt=obj), many=True).data
