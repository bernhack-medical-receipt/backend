from django.contrib import admin
from .models import Drug, Receipt


class DrugsInline(admin.TabularInline):
    model = Receipt.drugs.through
    autocomplete_fields = ('drug',)


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ('title', 'category', 'package_size')
    list_filter = ('category', )


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    inlines = [
        DrugsInline
    ]

    exclude = ('drugs',)
    autocomplete_fields = ('user',)

    list_display = ('created_at', 'user', 'disease', )
