from django.urls import path
from .views import CustomerRegView, HomeView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CustomerRegView.as_view(), name="login"),
    path('accounts/login/', CustomerRegView.as_view()),
    path('profile/', HomeView.as_view(), name="home"),
    path('profile/<str:pt>', HomeView.as_view(), name="projectdetail"),
    path('upload/', views.upload_data, name="project"),
    path('patient/', views.patient_data, name="patient"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
