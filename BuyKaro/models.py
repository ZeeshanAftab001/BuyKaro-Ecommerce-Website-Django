from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

# Customer Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

# Categories of Products
class catagory(models.Model):
    name = models.CharField(max_length=50)
    image_cat = models.ImageField(upload_to='upload/product/', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

# Customers
class customer(models.Model):
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=12,default='')
    email = models.EmailField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.first_name

# Products
class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='upload/product/')
    on_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Customer Orders
class order(models.Model):
    name= models.CharField(max_length=100, default="Unknown")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=15, default="000-000-0000")
    address = models.TextField(default="")
    ordered_date = models.DateTimeField(default=datetime.datetime.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Ensure this is DecimalField

    def __str__(self):
        return f"Ord"