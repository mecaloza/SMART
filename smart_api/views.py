from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from smart_api.models import *
# Create your views here.
#agregar arquitectura de guardado de fases


class Create_dot(APIView):
  def post(self, request):
    print(request.data)

    device_id=request.data["device_id"]
    value=request.data["value"]
    measure=request.data["measure"]
    value_volt=request.data["volt"]

    Iot_dots_ampers.objects.create(value_amper=value,device_id=device_id,measure_amper=measure,measure_volt="voltaje",value_volt=value_volt)

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


        dots = Iot_dots_ampers.objects.all().values()
        
        for tuple in dots:
            dict3 = {}
            dict3["x"] = tuple["id"]
            dict3["y"] = tuple["value"]
            points.append(dict3)
            
        content["points"]=points
 
        return Response(content, status=status.HTTP_200_OK)

      