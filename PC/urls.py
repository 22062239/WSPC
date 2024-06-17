from django.urls import path
from PC import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('success/', views.success, name='success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)