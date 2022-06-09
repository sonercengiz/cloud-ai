from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import UserIdSerializer

from .scripts.association_rule_mining import recommend

@api_view(['GET',])
def AssociationRuleMining(request):
    recommendations = recommend(int(request.GET.get("userId")))
    return Response({
        "Recommendations": recommendations
    },status=200)