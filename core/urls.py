from django.urls import path
from .import views
from .views import HomePageView, AboutView, LoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('login', LoginView.as_view(), name='login'),
]
