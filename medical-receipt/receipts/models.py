from django.db import models
from ..users.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Drug(BaseModel):
    title = models.CharField(max_length=255)
    license_owner = models.TextField()
    category = models.TextField()
    package_size = models.TextField()
    unit = models.TextField()
    active_ingredients = models.TextField()
    ingredients = models.TextField()
    application = models.TextField()

    def __str__(self):
        return f'Drug {self.title}'


class DrugPrescription(BaseModel):
    drug = models.ForeignKey(Drug, on_delete=models.SET_NULL, null=True)
    receipt = models.ForeignKey("Receipt", on_delete=models.SET_NULL, null=True)
    frequency = models.CharField(max_length=255)  # TODO: make a better frequency


class Receipt(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    disease = models.CharField(max_length=255)

    drugs = models.ManyToManyField(Drug, related_name='prescribed_drugs', through=DrugPrescription)

    def __str__(self):
        return f'Receipt #{self.id} for {self.user}'
