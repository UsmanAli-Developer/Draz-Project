from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from  Models.models import Products
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password1')
        fullname = request.POST.get('fullname')

        
        if User.objects.filter(username=phone,).exists():
            return render(request, 'signup.html', {
                'error': 'Your phone number aleardy exist'
            })
        
        for user in User.objects.all():
         if check_password(password, user.password):
           return render(request, 'signup.html', {
            'error': 'This password is already used by another user.'})

       
        user = User.objects.create_user(username=phone, password=password,first_name=fullname)

       
        user = authenticate(username=phone, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {
                'error': 'Authentication failed, please try again.'
            })

    return render(request, 'signup.html')




def home(request):

    Model_show=Products.objects.all()[:30]


    return render(request,'index.html', {'products': Model_show} )


def login_page(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password1')

        user = authenticate(username=phone, password=password)  

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'logins.html', {
                'error': 'Invalid phone or password.'
            })

    return render(request, 'logins.html')


def product_page(request,id):
      Model_show=Products.objects.get(pk=id)
      return render(request,'product-page.html',{'products': Model_show})


def Add_to_card(request, id):
    cart = request.session.get('cart', {})
    product_id = str(id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Products.objects.get(product_id=product_id)
        item_total = product.product_price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    return render(request, 'Add-to-card.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def update_quantity(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        str_id = str(id)

        if quantity > 0:
            cart[str_id] = quantity
        else:
            cart.pop(str_id, None)

        request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    str_id = str(id)

    if str_id in cart:
        del cart[str_id]

    request.session['cart'] = cart
    return redirect('view_cart')

def header(request): 
    st=request.GET.get("search")
    if st != None:
        if st:
          products = Products.objects.filter(product_name__icontains=st)
        else:
           products = Products.objects.all()
        return render(request, 'product_list.html', {'products': products})
    
def search_page(request):  
    st=request.GET.get("search")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    products = Products.objects.all()

    if st != None:
        if st:
          products = Products.objects.filter(product_name__icontains=st)
        else:
          products = Products.objects.all()[:30]
    
    if min_price and max_price:
        products = products.filter(product_price__gte=min_price, product_price__lte=max_price)
    


    return render(request,'search_page.html', {'products': products})

def logout_user(request):
    logout(request)
    return redirect('login-page')

   
def close_popup(request):
     if request.user.is_authenticated:
        return render(request, 'close_popup.html') 
     else:
        return render(request, 'popup_cancelled.html') 
     

     # views.py


@login_required(login_url='/login/')
def payment_page(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Test Product',
                },
                'unit_amount': 5000,  # 50 USD
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )
    return render(request, 'payment.html', {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })


def payment_success(request):
    return render(request, 'success.html')

def payment_cancel(request):
    return render(request, 'cancel.html')