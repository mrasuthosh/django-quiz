from django.http import HttpResponse, JsonResponse
from django.shortcuts import render , redirect
from . models import * 
import random
# Create your views here.

def home(request):
    context = {
        'categoery':Categoery.objects.all()
    }
    if request.GET.get('categoery'):
        return redirect(f"/quiz/?categoery={request.GET.get('categoery')}")
    return render(request,"home.html",context)

def quiz(request,nums):
    context = {
        'categoery' : request.GET.get('categoery')
    }
    return render(request,'quiz.html')

def get_uizz(request):
    try:
        question_objs = Qusetion.objects.all()
        
        if request.GET.get('categoery'):
            question_objs = question_objs.filter(ctrgy__categoery_name__icontains=request.GET.get('categoery'))
        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append(
                {
                "category":question_obj.ctrgy.categoery_name,
                "question" : question_obj.categoery_qstn,
                "marks":question_obj.makrs,
                "answers":question_obj.get_answers()
            }
            )
        paylod = {'status':200,'data':data}
        
        return JsonResponse(paylod)

    except Exception as e:
        print(e)
    return HttpResponse("Some thing went wrong !")