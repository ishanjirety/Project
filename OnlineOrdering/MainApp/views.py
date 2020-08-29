from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
import hashlib
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
               "type" : request.session.get('memType'),
               }
          return render(request, 'index.html', context)
                    
def store(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          context={ 
             "username":request.session.get('user_id'),
             "menu":models.items.objects.all(),
             "type" : request.session.get('memType'),
               }
          return render(request, 'store.html', context)
     
def about(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          context={ 
               "username":request.session.get('user_id'),
               "type" : request.session.get('memType'),
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

          ###################################################
          passwordEnc=hashlib.md5(password.encode()).hexdigest()  #one Way Encryption
          print(passwordEnc)  
          ####################################################

          mobile=request.POST.get('mobile')
          secQue=request.POST.get('question')
          ans=request.POST.get('ans')
          u=models.login(username=username,password=passwordEnc,mobile=mobile,secQue=secQue,ans=ans)
          u.save()
          return render(request, 'login.html', {})     #passing flag to login to show success full reg msg
     else:
          raise PermissionDenied

def loginValidation(request):
     username=request.POST.get('username')
     password=request.POST.get('password')
     #####################################################
     passwordEnc=hashlib.md5(password.encode()).hexdigest()      #input Password Conversion To Check
     #####################################################
     try:
          log=models.login.objects.get(username=username,password=passwordEnc)
          fet=models.login.objects.filter(password=passwordEnc,username=username)
          for fet in fet:
               memType=fet.membership_type
          request.session['memType']=memType
          validated=True
          context = {
             "username": username,
             "type":memType,
                 }
          request.session['user_id']=username
          request.session['pass']=passwordEnc
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
             "type" : request.session.get('memType'),
                 }
          return render(request,'membership.html',context)

def membership_reg(request):
     if request.session.get('loggedin') != "loggedin":
          return render(request, 'login.html')
     else:
          if request.method=="POST":
               username=request.session.get('user_id')
               password=request.session.get('pass')
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
                    "type" : request.session.get('memType'),
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
def forgot(request):
      if request.session.get('loggedin') != "loggedin":
               if request.method=="POST":
                         mobile=request.POST.get('mob')
                         print(mobile)
                         try:
                              log=models.login.objects.get(mobile=mobile)
                              log1=models.login.objects.filter(mobile=mobile)
                              request.session['mob1']=mobile
                              for log in log1:
                                   question=log.secQue
                              return render(request,"forgot.html",{"found":"found","question":question})
                         except models.login.DoesNotExist:
                              return render(request,"forgot.html",{"found":"Notfound"})
               else:
                    return render(request,"forgot.html",{"found" : "Notfound"})
def val(request):
     if request.session.get('loggedin') != "loggedin":
          if request.method=="POST":
               ans=request.POST.get('ans')
               try:
                    verify=models.login.objects.filter(mobile=request.session.get('mob1'),ans=ans)
                    return render(request, "forgot.html",{"found":"true"})
               except models.login.DoesNotExist:
                    return render(request,"forgot.html")  

def val2(request):
          if request.session.get('loggedin') != "loggedin":
                if request.method=="POST":
                    newpass=request.POST.get('password')
                    #####################################
                    passwordEnc=hashlib.md5(newpass.encode()).hexdigest()  #one Way Encryption
                    print(passwordEnc)  
                    #####################################
                    change=models.login()
                    change=models.login.objects.filter(mobile=request.session.get('mob1')).update(password=passwordEnc)
                    return render(request,"login.html")