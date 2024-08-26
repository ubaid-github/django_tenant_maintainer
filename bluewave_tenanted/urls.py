# bluewave_tenanted/urls.py

from django.urls import path, include
from . import views as tenant_views
# import demoapp.views as demo_views
from .demoapp import views as demo_views
from . import views

app_name = 'bluewave_tenanted'

urlpatterns = [
    path('logs/', views.tenant_log_list, name='tenant_log_list'),
    path('demos/', demo_views.demo_model_list, name='demo_model_list'),
    # Other URLs
]
