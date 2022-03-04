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

        dots = Iot_dots_ampers.objects.filter(device_id=1,measure_date__range=("2022-02-17 00:00:00.0","2022-02-17 23:59:0.0"))[:1000]
        dots_2 = Iot_dots_ampers.objects.filter(device_id=2,measure_date__range=("2022-02-17 00:00:00.0","2022-02-17 23:59:0.0"))[:1000]
        dots_3 = Iot_dots_ampers.objects.filter(device_id=3,measure_date__range=("2022-02-17 00:00:00.0","2022-02-17 23:59:0.0"))[:1000]

        print(len(dots))
        print(len(dots_2))
        print(len(dots_3))
        # return Response(content, status=status.HTTP_200_OK)
        

        

        print(request.query_params.get('dots'))

        dot_query=request.query_params.get('dots')
        
      
        min=(int(dot_query)-1)*1000
        max=min+1000
      
          
        
        for cont_point in range(0, len(dots_3), 1):
            dict3 = {}
            print("fecha",dots[cont_point].measure_date)
            dict3["name"] = cont_point
            dict3["Fase_1"] = (dots[cont_point].value_amper)/1000
            dict3["Fase_2"] = (dots_2[cont_point].value_amper)/1000
            dict3["Fase_3"] = (dots_3[cont_point].value_amper)/1000

            dict3["fecha"] = dots_2[cont_point].measure_date

            # dict3["Fase_1"] = (tuple.value_volt)
            # dict3["Fase_2"] = (dots_2[cont_point].value_volt)
            points.append(dict3)
            
            # print(cont_point)
            
        content["points"]=points
        content["max"]=max
        content["min"]=min

        
 
        return Response(content, status=status.HTTP_200_OK)

class Tag_Graph (APIView):

    def get(self, request):
      content={}  
      

      tag_number=Iot_tag_dot.objects.latest('id')
      
      content["tag"]=tag_number.tag_number



      return Response(content, status=status.HTTP_200_OK)
    
    def post(self, request):
      content={}
      device_id=request.data["device_id"]
      tag_number=request.data["tag_number"]
      
      Iot_tag_dot.objects.create(tag_number=int(tag_number),device_id=device_id)

        
 
      return Response(content, status=status.HTTP_200_OK)