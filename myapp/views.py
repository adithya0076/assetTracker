from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import get_droplets 
import json, requests
# Create your views here.

# def index(request):
#     return render(request, 'index.html')


# class GetDroplets(TemplateView):
#     template_name = 'index.html'
#     def get_context_data(self, *args, **kwargs):
#         context = {
#             'droplets' : get_droplets(),
#         }
#         return context

def index(request):
    platformUrl = 'https://flespi.io/gw/devices/2438257/messages?data=%7B%22count%22%3A10%2C%22fields%22%3A%22battery.level%2Cdevice.id%2Cposition.latitude%2Cposition.longitude%2Ctimestamp%22%2C%22filter%22%3A%22%22%2C%22reverse%22%3Atrue%7D'
    platformReq = requests.get(platformUrl, headers={'Authorization': 'FlespiToken ILAqNLKluS2NCLNmvb1DgZSDm3G7ye64Puls3TCozsZ14AcnA3QGTz75qD1OHXHk'}).json()

    s1 = json.dumps(platformReq)

    b = platformReq['result']

    
    return render(request,'index.html', {'b': b})

def geofence(request):
    return render(request, 'geofence.html')

def findKey(name,dic):
    if name in dic:
        return dic[name]
    else:
        return ""


def devices(request):
    platformUrl = 'https://flespi.io/gw/devices/2435913%2C2438085%2C2438257?fields=name'
    platformReq = requests.get(platformUrl, headers={'Authorization': 'FlespiToken ILAqNLKluS2NCLNmvb1DgZSDm3G7ye64Puls3TCozsZ14AcnA3QGTz75qD1OHXHk'}).json()

    s1 = json.dumps(platformReq)
    
    b = platformReq['result']
    return render(request, 'devices.html', {'b': b} )