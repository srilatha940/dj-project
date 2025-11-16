from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import StudentNew
# from basic.models import InstaPost
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

# TO TEST DATABASE CONNECTION THROUGH API
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":'ok','db':'connected'})
    except Exception as e:
        return JsonResponse({'status':'error','db':str(e)})

@csrf_exempt
def addStudent(request):
    print(request.method)
    if request.method=='POST':
        data=json.loads(request.body)
        student=StudentNew.objects.create(
            name=data.get('name'),
            age= data.get('age'),
            email=data.get('email')
            )
        return JsonResponse({"status":"success","id":student.id},status=200)
    elif request.method=="GET":
        result=list(StudentNew.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)

    elif request.method=="PUT":
        data=json.loads(request.body)
        ref_id=data.get("id")       #getting_id
        new_email=data.get('email')     #getting_email
        existing_student=StudentNew.objects.get(id=ref_id)      #fetched the object as per the id
        # print(existing_student)
        existing_student.email=new_email    #updating with new email
        existing_student.save()
        updated_data=StudentNew.objects.filter(id=ref_id).values().first()

        return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)
        
    elif request.method=="DELETE":
        data=json.loads(request.body)
        ref_id=data.get("id")   #getting id
        get_deleting_data=StudentNew.objects.filter(id=ref_id).values().first()
        to_be_delete=StudentNew.objects.get(id=ref_id)
        to_be_delete.delete()

        return JsonResponse({"status":"success","message":"student record deleted successfully","deleted data": get_deleting_data},status=200)
    return JsonResponse({'error':'Use post method'},status=400)
    
# @csrf_exempt
# def addPost(request):
#     print(request.method)
#     if request.method=='POST':
#         data=json.loads(request.body)
#         post=InstaPost.objects.create(
#             post_name=data.get('post_name'),
#             post_type=data.get('post_type'),
#             post_date=data.get('post_date'),
#             post_description=data.get('post_description')
#         )
#         return JsonResponse({"status":"success","id":post.id,"message":"Post created Successfully!"},status=200)
#     elif request.method=="GET":
#         return JsonResponse({"req":"get method requested"},status=200)
#     elif request.method=="PUT":
#         return JsonResponse({"req":"put method requested"},status=200)
#     elif request.method=="DELETE":
#         return JsonResponse({"req":"delete method requested"},status=200)
#     return JsonResponse({'error':"use post method"},status=200)
