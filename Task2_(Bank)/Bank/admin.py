from django.contrib import admin
from Bank.models import Client

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "balance")
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    save_on_top = True
