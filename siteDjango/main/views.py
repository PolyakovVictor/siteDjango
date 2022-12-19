from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .forms import LoginForm
from .forms import ProductForm
from django.contrib.auth import authenticate, login
from .models import Category, Product


def index(request):
    return render(request, "main/index.html")


def addForm(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Form error'

    form = ProductForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, "main/addForm.html", data)


def scumCard(request):
    return render(request, "main/scumCard.html")


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/')
#                 else:
#                     return "<h1>Invalid password</h1>"
#             #         return redirect('main/login.html', {'htmltext': htmltext})
#             # else:
#                 # return HttpResponse('main/login.html', {% block  %}{ % endblock % })
#                 #     return redirect('main/login.html', {'htmltext': htmltext})
#                 #     # return'Invalid login'
#     else:
#         form = LoginForm()
#     return render(request, 'main/login.html', {'form': form})

def user_login(request):
    # login_error = "Incorrect password or username"
    # data_error = {"login_error": login_error}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                # return redirect("main/login.html", context=data_error)
                return redirect('/login/')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('/login/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'main/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'main/product/detail.html',
                  {'product': product})
