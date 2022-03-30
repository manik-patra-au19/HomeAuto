from ast import Return
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from . models import Device,UserDevice

# Create your views here.
def index(request):
    return HttpResponse("this is home")


def getdevicestatus(request,pk):   
    try:
        device=Device.objects.get(deviceID=pk)

        dict_ ={"deviceId":device.deviceID,
                "light":device.lightStatus,
                "fan":device.fanstatus}
        return JsonResponse(dict_)
    except Device.DoesNotExist:
        return JsonResponse({"message":"no device found"})

def togglelight(request,pk):
    try:

        device=Device.objects.get(deviceID=pk)
        
        if device.lightStatus==0:
            device.lightStatus = 1
        else:
            device.lightStatus = 0
        device.save()

        dict_ ={"deviceId":device.deviceID,
                "light":device.lightStatus,
                "fan":device.fanstatus}

        
        return JsonResponse(dict_)
    except Device.DoesNotExist:

        return JsonResponse({"message":"no device found"})

def togglefan(request,pk):
    try:

        device=Device.objects.get(deviceID=pk)
        
        if device.fanstatus==0:
            device.fanstatus = 1
        else:
            device.fanstatus = 0
        device.save()
        dict_ ={"deviceId":device.deviceID,
                "light":device.lightStatus,
                "fan":device.fanstatus}       
        return JsonResponse(dict_)

    except Device.DoesNotExist:

        return JsonResponse({"message":"no device found"})