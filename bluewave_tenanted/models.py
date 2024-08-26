from django.db import models
from django_tenants.models import TenantMixin

class TenantLog(models.Model):
    tenant_id = models.IntegerField()
    log_file = models.FileField(upload_to='logs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tenant {self.tenant_id} Log {self.id}"