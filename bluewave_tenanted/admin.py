from django.contrib import admin
from .models import TenantLog

# Register your models here.
@admin.register(TenantLog)
class TenantLogAdmin(admin.ModelAdmin):
    list_display = ('tenant_id',)