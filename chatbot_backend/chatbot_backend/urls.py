import os
from django.urls import path
from django.views.generic import TemplateView

# Use deployment views if in deployment environment
if os.environ.get('RENDER') or os.environ.get('USE_SIMPLE_PROCESSOR'):
    from chatapi.views_deployment import ChatView, weather_api, PerformanceView
else:
    from chatapi.views import ChatView, weather_api, PerformanceView

urlpatterns = [
    path('api/chat/', ChatView.as_view(), name='chat'),
    path('api/performance/', PerformanceView.as_view(), name='performance'),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/weather/', weather_api, name='weather-api'),
]
