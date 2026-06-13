from django.urls import path
from .views import say_hello, home_view, check_experience, popular_posts, get_product, products
# import views

urlpatterns = [
    path('polls/hello', say_hello, name="say_hello"),
    path('polls/home', home_view, name="home_view"),
    path('polls/check_experience', check_experience, name="check_experience"),
    path('polls/popular_posts', popular_posts, name="popular_posts"),
    path('polls/get_product', get_product, name="get_product"),
    path('polls/products', products, name="products"),
]

# urlpatterns = [
#     path('polls/hello', views.say_hello, name="say_hello")
# ]