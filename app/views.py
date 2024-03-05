from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.models import *
from app.serializers import *
# Create your views here.
class prodcrud(APIView):
    def get(self,request,product_id):
        PDO=Product.objects.all()
        PJO=ProductModelSerializer(PDO,many=True)
        return Response(PJO.data)
    
    def post(self,request,product_id):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted'})
        else:
            return Response({'error':'Data is not inserted'})
        
    def put(self,request,product_id):
        PO=Product.objects.get(product_id=product_id)
        UPDO=ProductModelSerializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated'})
        else:
            return Response({'error':'data is not updataed'})
    
    def patch(self,request,product_id):
        PO=Product.objects.get(product_id=product_id)
        UPDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'data is updated'})
        else:
            return Response({'error':'data is not updataed'})
    
    def delete(self,request,product_id):
        Product.objects.get(product_id=product_id).delete()
        return Response({'delete':'data is deleted'})