from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.models import *
from app.serializers import *
# Create your views here.
class prodcrud(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        PJO=ProductModelSerializer(PDO,many=True)
        return Response(PJO.data)
    
    def post(self,request):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted'})
        else:
            return Response({'error':'Data is not inserted'})