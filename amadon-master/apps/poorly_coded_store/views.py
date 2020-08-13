from django.shortcuts import render, redirect, HttpResponseRedirect,reverse
from .models import *

def index(request):
    return render(request, 'index.html', {"all_products": Product.objects.all()})

def cart(request):
    if request.method == 'POST':
        request.session['new_quantity'] = int(request.POST['quantity'])
        request.session['new_price'] = float(request.POST['price']) * int(request.session['new_quantity'])
    return redirect('/checkout')

def checkout(request):
    try:
        request.session['total_quantity'] += int(request.session['new_quantity'])
        request.session['total_cost'] += float(request.session['new_price'])
    except:
        request.session['total_quantity'] = int(request.session['new_quantity'])
        request.session['total_cost'] = float(request.session['new_price']) * request.session['new_quantity']
        return HttpResponseRedirect(reverse('apps.poorly_coded_store:index.html'))
    return render(request, 'checkout.html')

    """
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return render(request, 'checkout.html', context)
    """