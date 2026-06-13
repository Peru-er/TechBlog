from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.models import User, Product
from polls.forms.form_example import FormProduct
from .views import (
    say_hello,
    home_view,
    check_experience,
    popular_posts,
    get_product,
    products,
    about_view,
    contact_view
)

# app.get("polls/")

def products(request):
    products = Product.objects.all()

    if request.method == "POST":
        form = FormProduct(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            stock = form.cleaned_data['stock']
            price = form.cleaned_data['price']

            product = Product.objects.create(
                name=name,
                description=description,
                stock=stock,
                price=price
            )

            return render(request, 'products.html', {
                'product': product,
                'products': products,
                'create_product_form': FormProduct()
            })
    else:
        form = FormProduct()

    return render(request, 'products.html', {
        'products': products,
        'create_product_form': form
    })

def get_product(request):
    product = Product.objects.all()
    print(product)
    return HttpResponse("ajkhbdakjsdbkasbdka")


def register(request):
    pre_user_data = {
        "first_name": None,
        "last_name": None,
        "email": None,
        "phone": None
    }
    context = {}
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        #Додатково треба брати ще confirm_password -> confirm_password = request.POST.get("confirm_password")
        user = User.objects.filter(email=email).first()
        if user:
            context = {
                "pre_user_data": pre_user_data,
                "message": "Користувач з таким email уже існує!!!",
            }
            return render(request, "register.html", context=context)

        #Робити перевірку чи password == confirm_password,
        # якщо False значить користувач десь помилився коли підтверджував пароль і треба йому повідомити про це

        new_user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone
        )

        password_hash = new_user.password_hash(password)
        new_user.update(password=password_hash)
        new_user.save()
        context = {
            "user": new_user,
            "message": "Користувач успішно зарейструвався!",
        }
        return render(request, "register.html", context=context)
    if request.method == "GET":
        return render(request, "register.html", context=pre_user_data)



def login(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(email=email).first()
        message = {"message": "Користувача з таким email не існує!!!"}
        context.update(message)
        if user is None:
            return render(request, "login.html", context=context)
        if user:
            if user.check_password(password):
                return redirect("home_view")
            else:
                message = {"message": "Не вірний пароль!!!"}
                context.update(message)
                return render(request, "login.html", context=context)
    if request.method == "GET":
        return render(request, "login.html", context=context)






def say_hello(request):
    return HttpResponse("Hello World")


#Сторінка 1. now_time - Через datetime дістати зарашній час,
# і коли клієнт заходить нас сторінку просто виводити чей час.


#Сторінка 1. now_date - Через datetime дістати зарашній дату,
# і коли клієнт заходить нас сторінку просто виводити чей дату.


# Головна сторінка блогу
def home_view(request):
    context = {
        "blog_name": "TechBlog",
        "description": "Найкращі статті про технології та програмування"
    }
    return render(request, "home.html", context)


# name = models.CharField(max_length=255)
#     description = models.TextField(null=True, blank=True)
#     stock = models.PositiveIntegerField(default=0, null=False)
#     price = models.FloatField(default=0.0, null=False)
#     is_active = models.BooleanField()
#     create_at = models.DateTimeField(auto_now_add=True)

# Перевірка досвіду користувача (через POST форму)
def check_experience(request):
    experience_years = None
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        stock = request.POST.get("stock")
        price = request.POST.get("price")
        print(name, description, stock, price)
        # Отримуємо число років досвіду з форми, якщо не передано — беремо 0
        experience_years = int(request.POST.get('years', 0))
    elif request.method == "GET":
        print("Ще додаткова логіка при методі GET")
    return render(request, "experience.html", {"years": experience_years})


# Відображення списку популярних постів
def popular_posts(request):
    posts_data = [
        {"title": "Вивчаємо Python", "views": 1520},
        {"title": "Django для початківців", "views": 980},
        {"title": "JavaScript ES6", "views": 1340},
        {"title": "React Hooks", "views": 760},
        {"title": "Machine Learning", "views": 2100},
    ]

    about_me = {
        "name": "Діма",
        "age": "27",
    }
    context = {
        "blog_title": "Популярні статті TechBlog",
        "posts": posts_data,
        "info": about_me
    }
    return render(request, "popular.html", context=context)

def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')
