from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from store.models import Product,Cart


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            print(prod_id, product_check)
            if (product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        try:
                            Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        except:
                            return JsonResponse({'status':"Product not added"})
                        else:
                            return JsonResponse({'status':"Product successfully added"})
                    else:
                        return JsonResponse({'status':"Only "+ str(product_check.quantity) + " is available"})
                    
            else:
                return JsonResponse({'status':"No product found"})
        else:
            return JsonResponse({'status':'Login to continue'})
        
    return redirect('home')

def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context= {'cart':cart}
    return render(request, "store/cart.html", context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':'Updated Successfully'})
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):            
            cart = Cart.objects.get(product_id=prod_id, user=request.user)            
            cart.delete()
            return JsonResponse({'status':'deleted Successfully'})
    return redirect('/')