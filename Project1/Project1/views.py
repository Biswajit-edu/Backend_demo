from django.http import HttpResponse
from django.shortcuts import render
from Project1.utils.logic import get_first_name, printing

emailid=""

def home(request):
    # return HttpResponse("Hello World! You are at Switzerland.")
    name = ["Ravi","Hari"]
    return render(request, 'website/index.html',{'nm':emailid})


def contactUs(request):
    # return HttpResponse("Hello World! You are at Switzerland.")
    name = ["Ravi","Hari"]
    if request.method == "POST":
        emailid = request.POST['email']
        First = request.POST['f_name']
        Last = request.POST['s_name']
        print(emailid,First,Last)
    print("here "+ emailid)
    names = ["Madhav","Arun","Harry","Jhon"]
    gname = get_first_name(names)
    printing()
    return render(request, 'website/contact.html',{'nm':emailid, 'gname':gname})

def villa(request):
    return HttpResponse("Hello World! You are at lauterbrunen.")

def hot(request):
    return HttpResponse("Hello World! You are at swissbank.")