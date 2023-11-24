from django.urls import path
from .views import IndexViews


urlpatterns = [
    path('menu/', IndexViews.as_view(), name='index'),
]