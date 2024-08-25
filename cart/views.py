from django.shortcuts import render,get_object_or_404
from .cart import Cart
from BuyKaro.models import product
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.



def cart_summary(request):

    cart=Cart(request)
    cart_products=cart.get_products()
    quantities=cart.get_quants()
    totals=int(cart.cart_total())
    return render(request,'cart/cart_summary.html',{'cart_products':cart_products,'quantities':quantities,'totals':totals})

def cart_add(request):
    #get the cart
    cart=Cart(request)
    #test for POST
    if request.POST.get('action')=='post':
        #get stuff
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product_=get_object_or_404(product,id=product_id)

        #get cart quantity
        cart_quanitity=cart.__len__()
        #Save to a session
        cart.add(product=product_ ,quantity=product_qty)

        response=JsonResponse({'qty':cart_quanitity})
        messages.success(request,'Product Added to Cart sucessfully !!!')
        return response
    
def cart_delete(request):
    cart=Cart(request)
    #test for POST
    if request.POST.get('action')=='post':
        #get stuff
        product_id=int(request.POST.get('product_id'))
        cart.delete(product_id)
        response=JsonResponse({'product_id':product_id})
        messages.success(request,'Cart item Deleted sucessfully !!!')
        return response
        

def cart_update(request):
    
    cart=Cart(request)
    #test for POST
    if request.POST.get('action')=='post':
        #get stuff
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))

        cart.update(product=product_id,quantity=product_qty)
        response=JsonResponse({'qty':product_qty})
        messages.success(request,'Cart updated sucessfully !!!')
        return response