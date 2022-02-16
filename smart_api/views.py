from this import d
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
    if value ==None:
      value=0
  
    value_volt=request.data["volt"]
    if value_volt ==None:
      value_volt=0



    Iot_dots_ampers.objects.create(value_amper=value,device_id=device_id,measure_amper=measure,measure_volt="voltaje",value_volt=value_volt)

    return Response( status=status.HTTP_200_OK)

  def get(self, request):

    content="si llego"
      #debo empezar el codigo de  recuperacion del correo
  

    return Response(content, status=status.HTTP_200_OK)

class Dot_Graph (APIView):

    def get(self, request,codigo):

        content = {}
        points = []

        
        cont_point=1

        dots = Iot_dots_ampers.objects.filter(device_id=1)
        dots_2 = Iot_dots_ampers.objects.filter(device_id=2)
        print(len(dots))
        print(len(dots_2))
        print(request.query_params.get('dots'))

        dot_query=request.query_params.get('dots')
        min=0
        max=1000
        if(dot_query=="1"):
          min=0
          max=1000
        elif(dot_query=="2"):
          print("aqui")
          min=1000
          max=2000
          
        
        for cont_point in range(min, max, 1):
            dict3 = {}
            dict3["name"] = cont_point
            dict3["Fase_1"] = (dots[cont_point].value_amper)/1000
            dict3["Fase_2"] = (dots_2[cont_point].value_amper)/1000
            # dict3["Fase_1"] = (tuple.value_volt)
            # dict3["Fase_2"] = (dots_2[cont_point].value_volt)
            points.append(dict3)
            
            # print(cont_point)
            
        content["points"]=points
 
        return Response(content, status=status.HTTP_200_OK)

      