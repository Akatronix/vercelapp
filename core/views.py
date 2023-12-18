from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData
from .serializer import DataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getData(request):
    valueupdate = SensorData.objects.all()
    return JsonResponse({"sensorvalues":list(valueupdate.values())})



@api_view(['GET','POST'])
def value(request):
    if request.method == 'GET':
        sensorval = SensorData.objects.all()
        serializer = DataSerializer(sensorval, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT', 'DELETE'])
def insert(request, id):
    try:
        sensorvalid = SensorData.objects.get(pk=id)

    except SensorData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = DataSerializer(sensorvalid)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        serializer = DataSerializer(sensorvalid, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        sensorvalid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



   