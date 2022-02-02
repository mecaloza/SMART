from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from smart_api.models import *
# Create your views here.


class Create_dot(APIView):
  def post(self, request):
    print(request.data)

    device_id=request.data["device_id"]
    value=request.data["value"]
    measure=request.data["measure"]
    Iot_dots.objects.create(value=value,device_id=device_id,measure=measure)

    return Response( status=status.HTTP_200_OK)

  def get(self, request):

    content="si llego"
      #se agrega consideracion de codigo
      #debo empezar el codigo de  recuperacion del correo
      #debo empezar el codigo de  recuperacion del correo

 


    return Response(content, status=status.HTTP_200_OK)

class Dot_Graph (APIView):

    def get(self, request):

        content = {}
        points = []


        dots = Iot_dots.objects.all().values()
        
        for tuple in dots:
            dict3 = {}
            dict3["x"] = tuple["id"]
            dict3["y"] = tuple["value"]
            points.append(dict3)
            
        content["points"]=points
 
        return Response(content, status=status.HTTP_200_OK)

      