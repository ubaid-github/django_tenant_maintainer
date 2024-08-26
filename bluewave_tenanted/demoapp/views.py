from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import DemoModel

@permission_required('demoapp.view_demomodel', raise_exception=True)
def demo_model_list(request):
    demos = DemoModel.objects.filter(tenant_id=request.user.tenant_id)
    return render(request, 'demo_model_list.html', {'demos': demos})
