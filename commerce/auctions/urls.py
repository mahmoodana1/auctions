from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create, name="create"),
    path("watch_list/<str:user_id>", views.watch_list, name="watch_list"),
    path("<int:listing_id>", views.listing_view, name="listing"),
    path("bid_on_listing/<str:listing_id>/<int:bidder_id>", views.bid_on_listing, name="bid_on_listing"),
    path("remove_from_wishlist/<str:user_id>/<str:listing_id>", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("close_bid/<str:listing_id>", views.close_bid, name="close_bid"),
    path("comment", views.comment_action, name="comment_action")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)