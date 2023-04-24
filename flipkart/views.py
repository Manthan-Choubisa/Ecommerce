from django.shortcuts import render,HttpResponse,redirect
from .serializers import Regserializer
from rest_framework import viewsets

# Create your views here.
from .models import *
from django.contrib.auth.hashers import check_password,make_password


# def index(request):
    # if request.method == "POST":
    #     f_name = request.POST.get('fname')
    #     l_name = request.POST.get('lname')
    #     c_obj = Registration(
    #         first_name = f_name,
    #         last_name = l_name
    #     )
    #     c_obj.save()
    
    # fetch_obj= Registration.objects.all()
    # fetch_obj=Registration.objects.filter(first_name = "pooja")
    # fetch_obj=Registration.objects.get(first_name = "pooja")
    # return render(request, 'home.html', {'key':fetch_obj})

def index(request):
    if request.method == "POST":
        product_id = request.POST.get('cartid')
        remove= request.POST.get('minus')
        cart_id = request.session.get('cart')
       


        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                cart_id[product_id]=quantity + 1
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id]= quantity + 1
            else:
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1
        request.session['cart'] = cart_id
        print(request.session['cart'])

    catid = request.GET.get('cat_id')
    pr_name = request.GET.get('name')
    
    category_info = Category.objects.all()
    if catid:
        product_info = Product.objects.filter(category=catid)
    else:
        product_info = Product.objects.all()
    
    if pr_name:
        product_info = Product.objects.filter(pro_name=pr_name)
    


   
    context = {
        'category':category_info,
        'product' : product_info
    }
    return render(request, 'home.html',context=context)


def contact(request):
   
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == "POST":
        f_name=request.POST.get('fname')
        l_name=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        mobile=request.POST.get('mobile')
        gender=request.POST.get('gender')

        c_obj = Registration(
          first_name=f_name,
          last_name=l_name,
          email=email,
          password=make_password(password),
          mobile=mobile,
          gender=gender,

       )
        c_obj.save()
    return redirect('home')


def login(request):
    if request.method == "POST":
        email_id=request.POST.get('emailid')
        password=request.POST.get('password')

        try:
            fetch_email = Registration.objects.get(email=email_id)
            if check_password(password,fetch_email.password):
                # return HttpResponse("Login Successfull")
                request.session['name']=fetch_email.first_name
                request.session['customer_id']=fetch_email.id


                return redirect('home')
            else:
                return HttpResponse("Wrong password")
        except:
            return HttpResponse("Email Id Doesn't Exists")
        

def logout(request):
    request.session.clear()
    return redirect('home')

def cart_details(request):
    prod_dtls = "no product in cart"
    if request.session.get('cart'):

          cart_info =list(request.session.get('cart').keys())
          prod_dtls = Product.objects.filter(id__in = cart_info)

    return render(request,'cart.html',{'pro_dtls':prod_dtls})

def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')

        customer_id = request.session.get('customer_id')
        if not customer_id:
            return HttpResponse("please login")
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in = list(cart))
        for p in product:
            order_info = order(
                address = address,
                mobile = mobile,
                price = p.price,
                product = p,
                quantity = cart.get(str(p.id)),
                customer = Registration(id= customer_id),
            )
            order_info.save()
        request.session['cart']={}

        return redirect('order')
    
def order_dtls(request):
    ord_dtls= Order.objects.all()
    tp=0
    for t in ord_dtls:
        tp = tp + (t.price* t.quantity)
    return render(request, 'order.html', {'ord_dtls': ord_dtls,'tp':tp})



class UserViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = Regserializer