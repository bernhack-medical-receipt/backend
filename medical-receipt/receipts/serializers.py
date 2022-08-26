from rest_framework import serializers
from .models import Receipt, Drug


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    drugs = DrugSerializer(many=True)

    class Meta:
        model = Receipt
        fields = '__all__'
