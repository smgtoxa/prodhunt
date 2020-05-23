from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
def home(requests):
    return render(requests, "products/home.html")

@login_required
def create(requests):
    if requests.method == 'POST':
        if requests.POST['title'] and requests.POST['body'] and requests.POST['url']  and requests.FILES['icon'] and requests.FILES['image']:
                product = Product()
                product.title = requests.POST['title']
                product.body = requests.POST['body']
                if requests.POST['url'].startswith('http://') or requests.POST['url'].startswith('https://'): 
                    product.urs = requests.POST['url']
                else:
                    product.urs = 'http://' + requests.POST['url']
                product.icon = requests.FILES['icon']
                product.image = requests.FILES['image']
                product.pub_date = timezone.datetime.now()
                product.hunter = requests.user
                product.save()
                return redirect('home')
        else:
            return render(requests, 'products/create.html', {'error':'Not all fields are filled out!'})
    else:
        return render(requests, 'products/create.html')