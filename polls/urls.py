from django.urls import path
from .views import say_hello, home_view, check_experience, popular_posts, get_product, products
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

urlpatterns = [
    path('polls/hello', say_hello, name="say_hello"),
    path('polls/home', home_view, name="home_view"),
    path('polls/check_experience', check_experience, name="check_experience"),
    path('polls/popular_posts', popular_posts, name="popular_posts"),
    path('polls/get_product', get_product, name="get_product"),
    path('polls/products', products, name="products"),
    path('polls/about_view', about_view, name="about_view"),
    path('polls/contact_view', contact_view, name="contact_view")
]

# urlpatterns = [
#     path('polls/hello', views.say_hello, name="say_hello")
# ]
