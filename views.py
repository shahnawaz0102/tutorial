from multiprocessing import context
from pdb import post_mortem
from urllib import request
from django import views
from django.shortcuts import redirect, render, HttpResponse
from contractor_app.models import User,contractor #ConnectedUsersToContractor
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
# from .forms import AddWorkDetailForm
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from datetime import date


# Remove redundant import
# User = get_user_model()

# Create your views here.
def register(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        umail = request.POST.get('umail')
        upass = request.POST.get('upass')
        ucpass = request.POST.get('ucpass')
        register_as = request.POST.get('register_as')

        context = {}
        if uname == "" or upass == "" or ucpass == "" or umail == "" or register_as == "":
            context['errmsg'] = "All fields are required"
            return render(request, 'register.html', context)
        elif upass != ucpass:
            context['errmsg'] = "Passwords do not match"
            return render(request, 'register.html', context)
        else:
            try:
                if User.objects.filter(email=umail).exists():
                    context['errmsg'] = "User with this email already exists"
                    return render(request, 'register.html', context)
                new_user = User.objects.create_user(name=uname, email=umail, password=upass, register_as=register_as)
                context['success'] = "User created successfully"
            except Exception as e:
                context['errmsg'] = "An error occurred"
                return render(request, 'register.html', context)

        return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        umail = request.POST.get('umail')
        upass = request.POST.get('upass')
        context = {}
        
        if umail == "" or upass == "":
            context['errmsg'] = 'This field should not be empty...'
            return render(request, 'login.html', context)
        else:

            if User.objects.filter(email=umail, register_as='contractor').exists():
                u = authenticate(email=umail, password=upass)
                if u is not None:
                    login(request, u)
                    return redirect("/index2")
                else:
                    context['errmsg'] = "Invalid username or password."
                    return render(request, 'login.html', context)
            else:
                u = authenticate(email=umail, password=upass)
                if u is not None:
                    login(request, u)
                    return redirect("/index")
                else:
                    context['errmsg'] = "Invalid username or password."
                    return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def index(request):
    return render(request, "index.html")

def index2(request):
     return render(request, "index2.html")

def my_view(request):
    if not request.user.has_perm('myapp.can_view_special_page'):
        return HttpResponseForbidden("You don't have permission to access this page.")

def work_detail(request):
        field = request.GET.get('field','')
        context = {}
        context['field'] = field        

        if request.method == "POST":
            company_name  = request.POST.get('companyName')
            contractor_name =  request.POST.get('contractorName')
            gstin =  request.POST.get('gstin')
            location =  request.POST.get('location')
            city =  request.POST.get('city')
            projects_completed =  request.POST.get('projectsCompleted') 
            experience_years =  request.POST.get('experience')
            
            if contractor.objects.filter(company_name=company_name,contractor_occupation=field).exists():
                context['errmsg']="The Company is already registered"
                return render (request,"work_detail.html",context)
                                         
            # Create an instance of the selected model and save it to the database
            else:
                contractor.objects.create(
                    company_name=company_name,
                    contractor_name=contractor_name,
                    gstin=gstin,
                    location=location,
                    city=city,
                    projects_completed=projects_completed,
                    experience_years=experience_years,
                    contractor_occupation=field
                )
                context['success'] = "Details submitted successfully."
                return render(request,"work_detail.html",context)
        else:
            return render(request,"work_detail.html",context)

def contractor_detail(request):
    field = request.GET.get('field', '')
    contractors = contractor.objects.filter(contractor_occupation=field)
    return render(request, "contractor_detail.html", {'contractors': contractors, 'field': field})


def connect_contractor(request):
    todaysDate=date.today()
    contractorId=request.GET.get('contractor_id','')
    contractorData=contractor.objects.filter(id=contractorId)
    userData=User.objects.filter(id=request.user.id)
    #ConnectedUsersToContractor.objects.create(date=todaysDate,contractorId=contractorData[0],userId=userData[0], status='Pending')
    return render(request,'connect_contractor.html')

   




