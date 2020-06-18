from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from .models import CartItem
from django.contrib.auth import get_user


# Create your views here.

from Raul.models import product

from .models import Cart

def view(request):
    User = get_user(request)
    template = "Raul/cart.html"
    if User.is_authenticated:
        # Check is user assoicated with an ACTIVE CartID #
        try:
            cart = Cart.objects.get(id=request.session['cart_id'],active=True)
            print("Try with ID")
        except :
            pass
        else:
            print("cart.user and request.user.is_authenticated:")
            if not cart.user and request.user.is_authenticated:
                userCartNum = Cart.objects.filter(user=User,active=True).count()
                if userCartNum > 0:
                    userCart = Cart.objects.get(user=User,active=True)
                    userCart.delete()

                cart.user = User
                cart.save()
                context = {'cart': cart}
                return render(request, template, context)

            # Check if an ACTIVE cart is asspcated with User #
        try:
            cart = Cart.objects.get(user=User,active=True)
        except:
            pass
        else:
            request.session['cart_id'] = cart.id
            context= {'cart':cart}
            return render(request, template, context)


    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id,active=True)
    except:
        the_id= None

    if the_id:
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {"cart":cart}
        return render(request, template, context)

    else:
        empty_message = "Your cart is empty, go shop"
        context = {"empty" : True, "empty_message" : empty_message}
        return render(request, template, context)

    context = {"cart":cart}
    return render(request, template, context)




def update_cart(request,slug):
    request.session.set_expiry(3000000)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = ''
        update_qty = False

    try:
        the_id = request.session['cart_id']
    except:
        new_cart= Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)


    try:
        producter= product.objects.get(slug=slug)
    except product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart= cart, product=producter)
    if(request.user.is_authenticated):
        cart.user = request.user
        cart_item.user = request.user


    if created:
        print("Yes")
    #print(qty)
    if int(qty) == 0 and update_qty:
        cart_item.delete()
    elif update_qty:
        cart_item.quantity = qty
        cart_item.save()
    else:
        pass
    #if cart_item not in cart.items.all():
    #    cart.items.add(cart_item)
    #else:
    #    cart.items.remove(cart_item)

    new_total = 0.00
    line_total = 0.00
    #item.line_total = float(item.product.price) * (item.quantity)
    for item in cart.cartitem_set.all():
        if(item.quantity != None):
            print(item.product)
            new_total += float(item.product.price) * (item.quantity)
            line_total = float(item.product.price) * (item.quantity)
            item.line_total = line_total
            print(item.line_total)

        item.save()

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.pennies_total = cart.total * 100

    cart.save()
    return redirect(reverse("cart"))










