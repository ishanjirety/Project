from django.db import models

class login(models.Model):
    login_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    secQue=models.CharField(max_length=30)
    mobile=models.CharField(max_length=30,default="")
    membership_type=models.CharField(max_length=10,default="None")

class items(models.Model):
    items_id=models.IntegerField(primary_key=True)
    itemName=models.CharField(max_length=100)
    itemDescription=models.CharField(max_length=200)
    itemPrice=models.IntegerField()
    itemDiscounnt=models.IntegerField()
    itemImage=models.CharField(max_length=100,default="")

class donations(models.Model):
    donations_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=30,default="")
    date=models.CharField(max_length=30,default="")
    weight=models.IntegerField()
    email=models.CharField(max_length=30,default="")
    city=models.CharField(max_length=10,default="")
    address=models.CharField(max_length=50,default="")
    postalcode=models.IntegerField()

class membership(models.Model):
     membership_id=models.IntegerField(primary_key=True)
     username=models.CharField(max_length=30)
     date=models.CharField(max_length=10)
     typ=models.CharField(max_length=20)

class order(models.Model):
    order_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    date=models.CharField(max_length=10)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=40)
    total=models.CharField(max_length=10)
    