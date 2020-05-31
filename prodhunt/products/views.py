from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(requests):
    products = Product.objects
    return render(requests, "products/home.html", {"products": products})

@login_required(login_url='/users/signup')
def create(requests):
    if requests.method == 'POST':
        if requests.POST['title'] and requests.POST['body'] and requests.POST['url']  and requests.FILES['icon'] and requests.FILES['image']:
                product = Product()
                product.title = requests.POST['title']
                product.body = requests.POST['body']
                if str(requests.POST['url'].lower()).startswith('http://') or str(requests.POST['url'].lower()).startswith('https://'): 
                    product.urs = requests.POST['url']
                else:
                    product.urs = 'http://' + requests.POST['url']
                product.icon = requests.FILES['icon']
                product.image = requests.FILES['image']
                product.pub_date = timezone.datetime.now()
                product.hunter = requests.user
                product.save()
                return redirect('/products/' + str(product.id))
        else:
            return render(requests, 'products/create.html', {'error':'Not all fields are filled out!'})
    else:
        return render(requests, 'products/create.html')
    
    
def detail(requests, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(requests, 'products/detail.html', {'product':product})

@login_required(login_url='/users/signup')    
def upvote(requests, product_id):
    if requests.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))     

