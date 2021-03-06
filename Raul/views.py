from django import http
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, CreateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import product, Category, FeatuedProducts
from users import forms
from django.contrib.auth import login,logout,authenticate
from users.forms import CreateUserForm, UserAddressForm


def search(request):
    try:
        q= request.GET.get('q')
    except:
        q= None
    if q:
        products1= product.objects.filter(title__icontains=q)
        pro= product.price
        context = {'query': q , 'products1': products1, "price" : pro}
        template = 'Raul/results.html'
    else:
        context = {}
        template = 'Raul/product.html'
    return render(request, template, context)


def home(request):
    return render(request, 'Raul_Inc/index.html')


def secondHome(request):
    featProd = FeatuedProducts.objects.all()
    form = forms.LoginForms(request.POST or None)
    Register_form = forms.CreateUserForm(request.POST or None)
    context = {'form': form,"Register_form": Register_form,"Feat":featProd}
    if 'register' in request.POST:
        request.session.set_expiry(60)
        if Register_form.is_valid():
            Reg = Register_form.save(commit=False)
            Reg.email = Reg.username
            Reg.save()

            new_user = authenticate(username=Register_form.cleaned_data['username'],
                                    password=Register_form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            Register_form = forms.CreateUserForm()
            context = {'form': form,"Register_form" : Register_form,"Feat":featProd}
            messages.success(request, 'You are now logged in!')
            return render(request, 'Raul/home.html',context)
        else:
            messages.error(request, "Oops something went wrong please try again.")
            form = forms.LoginForms()
            context = {'form': form,"Register_form": Register_form,"Feat":featProd}
            return render(request, 'Raul/home.html',context)

    if 'login' in request.POST:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            context = {'form': form,"Register_form": Register_form,"Feat":featProd}
            login(request,user)
            return render(request, 'Raul/home.html',context)
        else:
            messages.error(request, 'Oops please try again')
            return render(request, 'Raul/home.html',context)

    return render(request, 'Raul/home.html',context)



def landingpage(request):
    return render(request, 'Raul/landing.html')


def products(request):
    featProd = FeatuedProducts.objects.all()
    products = product.objects.all()
    template = 'Raul/product.html'
    form = forms.LoginForms(request.POST or None)
    Register_form = forms.CreateUserForm(request.POST or None)
    context = {'form': form,"Register_form" : Register_form,"Feat":featProd}
    if 'register' in request.POST:
        request.session.set_expiry(60)
        if Register_form.is_valid():
            Reg = Register_form.save(commit=False)
            Reg.email = Reg.username
            Reg.save()
            context = {'products': products, 'form': form,"Register_form": Register_form}
            new_user = authenticate(username=Register_form.cleaned_data['username'],
                                    password=Register_form.cleaned_data['password1'],
                                    )

            login(request, new_user)
            Register_form = forms.CreateUserForm()
            messages.success(request, 'You are now logged in!')
            return render(request, template,context)
        else:
            messages.error(request, "Oops something went wrong please try again.")
            form = forms.LoginForms()
            context = {'products': products, 'form': form,"Register_form": Register_form}
            return render(request, template,context)

    if 'login' in request.POST:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            context = {'products': products, 'form': form,"Register_form": Register_form}
            login(request,user)
            return render(request, template,context)
        else:
            messages.error(request, 'Oops please try again')
            return render(request, template,context)



    products = product.objects.all()
    context = {'products': products, 'form': form,"Register_form": Register_form}
    template = 'Raul/product.html'
    return render(request, template, context)


def CategoryView(request, cats):
    template = 'Raul/categories.html'
    form = forms.LoginForms(request.POST or None)
    Register_form = forms.CreateUserForm(request.POST or None)
    cat_products = product.objects.filter(category__iexact=cats)
    context = {'cats': cats, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
    if 'register' in request.POST:
        request.session.set_expiry(60)
        if Register_form.is_valid():
            Reg = Register_form.save(commit=False)
            Reg.email = Reg.username
            Reg.save()

            new_user = authenticate(username=Register_form.cleaned_data['username'],
                                    password=Register_form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            context = {'cats': cats, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
            messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request, template,context)
        else:
            messages.error(request,"Oops please try again.")
            form = forms.LoginForms()
            context = {'cats': cats, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
            return render(request, template,context)

    if 'login' in request.POST:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            context = {'cats': cats, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
            login(request,user)
            return render(request, template,context)
        else:
            messages.error(request, 'Oops please try again')
            return render(request, template,context)
    return render(request, template,context)



def SectionView(request, sec):
    a=3
    template = 'Raul/categories.html'
    form = forms.LoginForms(request.POST or None)
    Register_form = forms.CreateUserForm(request.POST or None)
    cat_products = product.objects.filter(section__iexact=sec)
    context = {'sec': sec, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
    if 'register' in request.POST:
        request.session.set_expiry(60)
        if Register_form.is_valid():
            Reg = Register_form.save(commit=False)
            Reg.email = Reg.username
            Reg.save()
            #hiiii
            new_user = authenticate(username=Register_form.cleaned_data['username'],
                                password=Register_form.cleaned_data['password1'],
                                )
            login(request, new_user)
            Register_form = forms.CreateUserForm()
            form = forms.LoginForms()
            context = {'cats': sec, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
            messages.success(request, f'Your account has been created! You are now able to log in')
            return render(request, template,context)
        else:
            messages.error(request, Register_form.error_messages)
            form = forms.LoginForms()
            context = {'sec': sec, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
            return render(request, template,context)

    if 'login' in request.POST:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            context = {'sec': sec, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
            login(request,user)
            a = 4
        else:
            messages.error(request, Register_form.error_messages)
            form = forms.LoginForms()
            context = {'sec': sec, 'cat_products': cat_products,'form': form,"Register_form": Register_form}
            return render(request, template,context)

    return render(request, template,context)


def singleView(request, slug):
    try:
        single_product = product.objects.get(slug=slug)
        context = {'single_product': single_product}
        return render(request, 'Raul/single_product.html', context)
    except:
        raise


# Create your views here.
