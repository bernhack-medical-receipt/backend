from django.contrib import admin
from .models import Drug, Receipt


class DrugsInline(admin.TabularInline):
    model = Receipt.drugs.through


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    pass


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    inlines = [
        DrugsInline
    ]

    exclude = ('drugs',)
