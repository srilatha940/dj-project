from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def sample(request):
    return HttpResponse("hello world")

def sample1(request):
    return HttpResponse("Welcome to django")

def sampleInfo(request):
    # data={
    #     "name":"sri",
    #     "age":21,
    #     "city":"hyd"
    #     }
    # TO PASS NON-DICT OBJECTS USE SAFE
    data={"result":[1,2,3,4]}
    return JsonResponse(data,safe=False)
    
def dynamicResponse(request):
    name=request.GET.get("name","Sri")
    city=request.GET.get("city","hyd")
    return HttpResponse(f"hello {name} from {city}")

def add(request):
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    num1=int(num1)
    num2=int(num2)
    result=num1+num2
    return HttpResponse(f"Addition = {result}")

def sub(request):
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    num1=int(num1)
    num2=int(num2)
    result=num1-num2
    return HttpResponse(f"Subtraction={result}")

def mul(request):
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    num1=int(num1)
    num2=int(num2)
    result=num1*num2
    return HttpResponse(f"Multiplication = {result}")

def div(request):
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    num1=int(num1)
    num2=int(num2)
    result=num1//num2
    return HttpResponse(f"Division = {result}")