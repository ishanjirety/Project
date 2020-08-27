from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from . import models 
import datetime

validated=0
flag=0
def index(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          context={ 
               "username":request.session.get('user_id'),
               }
          return render(request, 'index.html', context)
                    
def store(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          context={ 
             "username":request.session.get('user_id'),
             "menu":models.items.objects.all()
               }
          return render(request, 'store.html', context)
     
def about(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          context={ 
               "username":request.session.get('user_id'),
               }
          return render(request, 'about.html', context)

def checkout(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          return render(request, 'checkout.html', {})

def register(request):
     return render(request, 'register.html', {})

def log(request):
     if request.session.get('loggedin') != "loggedin":
          context ={
               "status" : 1,
          }
          return render(request,'login.html',context)
     else:
          return render(request,'index.html')

def reg(request):
     if request.method=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          mobile=request.POST.get('mobile')
          secQue=request.POST.get('secQue')
          u=models.login(username=username,password=password,mobile=mobile,secQue=secQue)
          u.save()
          return render(request, 'login.html', {})     #passing flag to login to show success full reg msg
     else:
          raise PermissionDenied

def loginValidation(request):
     username=request.POST.get('username')
     password=request.POST.get('password')
     try:
          log=models.login.objects.get(username=username,password=password)
          validated=True
          context = {
             "username": username,
                 }
          request.session['user_id']=username
          request.session['pass']=password
          request.session['loggedin']="loggedin"
          return render(request, 'index.html', context)
     except models.login.DoesNotExist:
          context ={
               "status" : 0,
          }
          return render(request,'login.html',context)

def membership(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          context = {
             "username": request.session.get('user_id'),
                 }
          return render(request,'membership.html',context)

def membership_reg(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          if request.method=="POST":
               username=request.session.get('user_id')
               password=request.session.get('pass')
               print(username)
               membership_type=request.POST.get('membership')
               membership_reg=models.membership(username=username,typ=membership_type,date=datetime.date.today())
               membership_ins_inLogin=models.login.objects.filter(username=username,password=password).update(membership_type=membership_type)
               membership_reg.save()
               return render(request,'membership.html')
          else: 
               print('GET Method Called')
               return render(request,'membership.html')
     
def donations(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          if request.method=="GET":
               return render(request,'Donations.html')
          else:
               email=request.POST.get('inputEmail4')
               name=request.POST.get('Name')
               address=request.POST.get('inputAddress')
               city=request.POST.get('inputCity')
               postalcode=request.POST.get('inputZip')
               wt=request.POST.get('wt')
               donate=models.donations(username=name,date=datetime.date.today(),weight=wt,email=email,city=city,address=address,postalcode=postalcode)
               donate.save()
               flag=1
               context={
                    "flag":flag,
               }
               return render(request,'donations.html',context)
def logout(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          del request.session['user_id']
          del request.session['pass']
          del request.session['loggedin']
          return render(request,'login.html')

         
def placeorder(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          amount=request.POST.get('total')
          request.session['total']=amount
          return render(request,'address.html',{'amt':amount})

def checkout(request):
          if request.session.get('loggedin') != "loggedin":
               return render(request, 'login.html')
          else:
               if request.method=="POST":
                    email=request.POST.get('email')
                    print(email)
                    name=request.POST.get('name')
                    address=request.POST.get('address')
                    address2=request.POST.get('address2')
                    city=request.POST.get('City')
                    state=request.POST.get('state')
                    postal_code=request.POST.get('zip')
                    mobile=request.POST.get('mobile')
                    o=models.order(email=email,username=name,address=address,address2=address2,city=city,state=state,postalcode=postal_code,date=datetime.date.today(),mobile=mobile)
                    o.save()
                    return render(request,'checkout.html')