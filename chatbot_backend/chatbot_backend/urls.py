from django.urls import path
from chatapi.views import ChatView, weather_api, PerformanceView
from django.views.generic import TemplateView

urlpatterns = [
    path('api/chat/', ChatView.as_view(), name='chat'),
    path('api/performance/', PerformanceView.as_view(), name='performance'),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/weather/', weather_api, name='weather-api'),
]
