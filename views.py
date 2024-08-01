from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *
from.serializers import *

@api_view(['GET'])
def Get(request):
    obj = sqldatabase.objects.all()
    info = sqlserializers(obj, many = True)
    return Response({"status" : 200, "payload" : info.data ,"show" : "COMPLETE"})

@api_view(['POST'])
def post(request):
    data = request.data
    info = sqlserializers(data= request.data)
    if not info.is_valid():
        return Response({"Status" : "201", "Show" : "No Mercy"})
    info.save()
    return Response({"Status" : 200, "loading" : data, "Show" : "compleated"})

@api_view(['PUT'])
def put(request,id):
    try:
        obj = sqldatabase.objects.get(id=id)
        info = sqlserializers(obj,data=request.data)
        if not info.is_valid():
            return Response({"status" : 201, "Show" : "Invalid"})
        info.save()
        return Response({"status" : 200, "loading" : serializers.data, "show" : "valid"}) 
    except Exception as M:
        return Response({"Status" : 401, "show" : "Invalid"})
    
@api_view(['PUT'])
def patch(request,id):
    try:
        obj = sqldatabase.objects.get(id=id)
        info = sqlserializers(obj,data=request.data, partial = True)
        if not info.is_valid():
            return Response({"status" : 201, "Show" : "Invalid"})
        info.save()
        return Response({"status" : 200, "loading" : serializers.data, "show" : "valid"}) 
    except Exception as M:
        return Response({"Status" : 401, "show" : "Invalid"})
    
@api_view(['DELETE'])
def delete(request,id):
    try:
        obj = sqldatabase.objects.get(id=id)
        obj.delete()
        return Response({"status" : 200, "show" : "Deleted"})
    except Exception as T:
        return Response({"status" : 400, "show" : "Already deleted"})
    

    