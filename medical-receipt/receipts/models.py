from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Drug(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'Drug {self.title}'


class DrugPrescription(BaseModel):
    drug = models.ForeignKey(Drug, on_delete=models.SET_NULL, null=True)
    receipt = models.ForeignKey("Receipt", on_delete=models.SET_NULL, null=True)
    frequency = models.CharField(max_length=255)  # TODO: make a better frequency


class Receipt(BaseModel):
    disease = models.CharField(max_length=255)

    drugs = models.ManyToManyField(Drug, related_name='prescribed_drugs', through=DrugPrescription)
