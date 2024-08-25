from .cart import Cart



#create a context processor so that cart works on all pages of the site

def cart(request):
    return {'cart': Cart(request)}
