from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import *
from .models import *

from .scripts.association_rule_mining import recommend

@api_view(['GET'])
def get_user(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    user = Users.objects.filter(username=username, password=password)
    if user:
        serializer = UsersSerializer(user.first())
        return Response(serializer.data)
    else:
        return Response(status=404)

@api_view(['POST'])
def add_user(request):
    user = UsersSerializer(data=request.data)
    if Users.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=404)

@api_view(['GET'])
def list_products(request):
    products = Products.objects.all()
    if products:
        serializers = ProductsSerializer(products, many=True)
        return Response(serializers.data)
    else:
        return Response(status=404)

@api_view(['POST'])
def add_product(request):
    product = ProductsSerializer(data=request.data)
    if Products.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=404)

@api_view(['GET'])
def delete_product(request):
    productId = int(request.GET.get("productId"))
    product = Products.objects.filter(id=productId)
    if product:
        product.first().delete()
        return Response(status=200)
    else:
        return Response(status=404)

@api_view(['GET'])
def purchase_product(request):
    productId = int(request.GET.get("productId"))
    userId = int(request.GET.get("userId"))
    data = {'productid':productId, 'userid':userId}
    serializer = PurchasesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    else:
        return Response(status=500)

@api_view(['GET'])
def delete_purchase_product(request):
    purchaseId = int(request.GET.get("purchaseId"))
    purchases = Purchases.objects.filter(id=purchaseId)
    if purchases:
        purchases.first().delete()
        return Response(status=200)
    else:
        return Response(status=404)

@api_view(['GET'])
def purchase_list(request):
    userId = int(request.GET.get("userId"))
    purchases = Purchases.objects.filter(userid=userId)
    if purchases:
        purchases_serializer = PurchasesSerializer(purchases, many=True)
        return Response(purchases_serializer.data)
    else:
        return Response(status=404)
@api_view(['GET'])
def recommend(request):
    recommendations = recommend(int(request.GET.get("userId")))
    return Response({
        "Recommendations": recommendations
    },status=200)