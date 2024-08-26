# bluewave_tenanted/demoapp/models.py

from django.db import models

class DemoModel(models.Model):
    tenant_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    # class Meta:
    #     permissions = [
    #         ("view_demomodel", "Can view demo model"),
    #     ]

    def __str__(self):
        return f"{self.name} (Tenant {self.tenant_id})"
