from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import TenantLog

@permission_required('bluewave_tenanted.view_tenantlog', raise_exception=True)
def tenant_log_list(request):
    logs = TenantLog.objects.filter(tenant_id=request.user.tenant_id)
    return render(request, 'tenant_log_list.html', {'logs': logs})