from api import views
from django.urls import path

urlpatterns = [
    path('api/AssociationRuleMining', views.AssociationRuleMining, name='api'),
]