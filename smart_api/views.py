from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from smart_api.models import *
# Create your views here.


class Create_dot(APIView):
  def post(self, request):

    device_id=request.data["device_id"]
    value=request.data["value"]
    measure=request.data["measure"]

    
    Iot_dots.objects.create(value=value,device_id=device_id,measure=measure)

    return Response( status=status.HTTP_200_OK)