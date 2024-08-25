
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/', views.about,name='about'),
    path('shop/', views.shop,name='shop'),
    path('contact/', views.contact,name='contact'),
    path('Login_User/', views.Login_user,name='login'),
    path('Logout_User/', views.Logout_User,name='logout'),
    path('register_user/', views.register_user,name='register'),
    path('update_user/', views.update_user,name='update'),
    path('update_password/', views.update_password,name='update_password'),
    path('update_Info/', views.update_Info,name='update_Info'),
    path('product<int:pk>',views.see_product,name='product'),
    path('category<str:foo>',views.category,name='category'),
    path('policies/',views.policies,name='policies'),
    path('search/',views.search,name='search'),
    path('refund_policy/',views.refund_policy,name='refund_policy'),
    path('terms_services/',views.terms_services,name='terms_services'),
    path('category_summary/',views.category_summary,name='category_summary'),
    path('checkout/', views.check_out, name='checkout'),
    path('order_now/', views.order_now, name='order_now'),
    path('order_now/', views.order_now, name='order_now'),
    
]
