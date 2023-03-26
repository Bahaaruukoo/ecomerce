from django.urls import path
from . import views
from store.controller import authview, cart, checkout

urlpatterns = [
    path('', views.home, name='home'),
    path('collcetions', views.collections, name="collections"),
    path('collcetions/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collcetions/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),

    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart',cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),

    #path('wishlist', wishlist.index, name='wishlist'),
    #path('add-to-wishlist', wishlist.addtowishlist, name='addtowishlist'),
    #path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
    
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),
    
]