from django.shortcuts import render,redirect,get_object_or_404
from .models import product,catagory,Profile,order,customer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm,UpdateUserForm,UpdatePasswordForm,UserInfoForm
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponse


import json
from cart.cart import Cart


# myapp/templatetags/replace.py

# Create your views here.


def search(request):
	# Determine if they filled out the form
	if request.method == "POST":
		searched = request.POST['searched']
		# Query The Products DB Model
		searched = product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
		# Test for null
		if not searched:
			messages.success(request, "That Product Does Not Exist...Please try Again.")
			return render(request, "BuyKaro/search.html", {})
		else:
			return render(request, "BuyKaro/search.html", {'searched':searched})
	else:
		return render(request, "BuyKaro/search.html", {})




def update_Info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = Profile.objects.get(user__id=request.user.id)
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
		if form.is_valid():
			# Save original form
			form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('home')
		return render(request, "BuyKaro/update_info.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')


def home(request):
    products=product.objects.all()
    collections=catagory.objects.all()
    return render(request,'BuyKaro/home.html',{'Products':products,'Collections':collections})

def about(request):
    return render(request,'BuyKaro/about.html',{})

def policies(request):
    return render(request,'BuyKaro/policies.html')


def terms_services(request):
    return render(request,'BuyKaro/terms_services.html')


def refund_policy(request):
    return render(request,'BuyKaro/refund_policy.html')



def shop(request):
    return render(request,'BuyKaro/home.html',{})



def contact(request):
    return render(request,'BuyKaro/contact.html',{})




def Login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			# Do some shopping cart stuff
			current_user = Profile.objects.get(user__id=request.user.id)
			# Get their saved cart from database
			saved_cart = current_user.old_cart
			# Convert database string to python dictionary
			if saved_cart:
				# Convert to dictionary using JSON
				converted_cart = json.loads(saved_cart)
				# Add the loaded cart dictionary to our session
				# Get the cart
				cart = Cart(request)
				# Loop thru the cart and add the items from the database
				for key,value in converted_cart.items():
					cart.db_add(product=key, quantity=value)

			messages.success(request, ("You Have Been Logged In!"))
			return redirect('home')
		else:
			messages.success(request, ("There was an error, please try again..."))
			return redirect('login')

	else:
		return render(request, 'BuyKaro/login.html', {})





def Logout_User(request):
    logout(request)
    messages.success(request,'You were Logged Out')
    return redirect('home')




def register_user(request):

    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #login user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Registration Sucessful')
            return redirect('home')
        else:
            messages.success(request,'sorry,try again please')
            return redirect('register')
    else:
        return render(request,'BuyKaro/register.html',{'form':form})
    

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'User has been updated')
            return redirect('home')
        
        return render(request, 'BuyKaro/update_user.html', {'user_form': user_form})
    else:
        messages.error(request, 'You need to login to update')
        return redirect('home')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
       
        if request.method=='POST':
            form=UpdatePasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Updated,Please Login Again...')
               # login(request,current_user)
                return redirect('login')
            else:
                for error in form.errors.values():
                    messages.error(request,error)
                    return redirect('update_password')

        else:
            form=UpdatePasswordForm(current_user)
            return render(request,'BuyKaro/update_password.html',{'form':form})
    else:
        messages.success(request,'Please Login First')
        return redirect('home')
              

def see_product(request,pk):
    product_=product.objects.get(id=pk)
    cat_product=product_.catagory
    products=product.objects.all()
    return render(request,'BuyKaro/product.html',{'product':product_
                                                ,'products':products,'product_cat':cat_product})

def category(request,foo):


    foo=foo.replace('-',' ')
    try:
        category=catagory.objects.get(name=foo)
        products_from_cat=product.objects.filter(catagory=category)
        return render(request,'BuyKaro/categories.html',{'products_from_cat':products_from_cat,'category':category})
    except:
        messages.success(request,'Category not found')
        return redirect('home')
   
def category_summary(request):
    products=product.objects.all()
    return render(request,'BuyKaro/category_summary.html',{'Products':products})


def order_form(request):

    cart=Cart(request)
    cart_items=cart.get_products()
    quantities=cart.get_quants()
    totals=int(cart.cart_total())
    return render(request, 'BuyKaro/checkout.html', {'cart_items': cart_items,'totals':totals})


# views.py
def check_out(request):
     
    cart=Cart(request)
    cart_products=cart.get_products()
    quantities=cart.get_quants()
    totals=int(cart.cart_total())

    return render(request,'BuyKaro/check_out.html',{"cart_products":cart_products,'quantities':quantities,'totals':totals})



def clear(self):
    self.cart = {}
    self.session.modified = True
    if self.request.user.is_authenticated:
        current_user = Profile.objects.filter(user__id=self.request.user.id)
        current_user.update(old_cart=str(self.cart))



def order_now(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        new_order = order()
        new_order.name = request.POST.get('fname')
        new_order.email = request.POST.get('email')
        new_order.phone = request.POST.get('phone')
        new_order.address = request.POST.get('address')
        new_order.ordered_date = timezone.now()
        new_order.total_price = cart.cart_total()
        new_order.save()
    
        ordered_items = cart.get_products()
        quantities = cart.get_quants()

        cart.clear()  # Optionally clear the cart after placing the order
        return redirect('cart')  # Redirect to a confirmation page

    return redirect('cart')  # Redirect to the cart page if not POST method
