from django.urls import path
from .import views
from .views import PagesDetailView, PagesListView

urlpatterns = [
path('', PagesListView.as_view(), name = 'index')

]
