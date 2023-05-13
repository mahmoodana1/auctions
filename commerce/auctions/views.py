from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError 



def index(request):
    elements = Listing.objects.all()
    context = {"elements":elements}
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "GET":
        return render(request, "auctions/create_listing.html")
        
    if request.method == "POST":
        Pcategory = request.POST["category"]
        Ptitle = request.POST["title"]
        Pdescription = request.POST["description"]
        Pbid = request.POST["bid"]
        try:
            Pimage = request.FILES["image"]
        except MultiValueDictKeyError:
            Pimage = "Error"
        Pauther_id = int(request.POST["auther_id"])
        
        if Listing.objects.filter(title = Ptitle).exists():
            return render(request, "auctions/create_listing.html", {
                "messege":"Choose another title"
            }) 

        try :
            categories.objects.get(category_name = Pcategory) 
        except categories.DoesNotExist:
            categories.objects.create(category_name = Pcategory)

        obj = get_object_or_404(categories, category_name= Pcategory)
        Pcategory_id = obj.pk
        Listing(title = Ptitle, description = Pdescription, bid = Pbid, image = Pimage, category_id = Pcategory_id, auther_num = Pauther_id).save()
        return HttpResponseRedirect(reverse("index")) 


def listing_view(request, listing_id):
    if request.method == "GET":
        auther_id = Listing.objects.filter(id = listing_id).values_list('auther_num', flat=True)[0]
        Listing_id = Listing.objects.filter(id = listing_id).values_list('id', flat=True)[0]
        listing = Listing.objects.filter(id = listing_id).values()
        users_ids_linked_to_this_listing = users_watchlist.objects.filter(listing_id = Listing_id).values_list('user_num', flat=True)
        return render(request, "auctions/listing_view.html", {
            "listing":listing,
            "auther_id":auther_id,
            "listing_id":Listing_id,
            "users_ids_linked_to_this_listing":users_ids_linked_to_this_listing,
            "comments":comment.objects.filter(listing_id = listing_id)
        })
    elif request.method == "POST":
        Listing_id = request.POST["listing_id's"]
        listing_id = Listing.objects.get(id = Listing_id)
        current_user_id = request.POST["user_id"]
        user = User.objects.get(id=current_user_id)
        users_watchlist.objects.create(user_num = user, listing_id = listing_id).save()
        return HttpResponseRedirect(reverse("index"))
        
            
def remove_from_wishlist(request, user_id, listing_id):
    if request.method == "POST":
        deleted_obj = users_watchlist.objects.filter(user_num = user_id, listing_id = listing_id)
        deleted_obj.delete()
        return HttpResponseRedirect(reverse("index"))


def watch_list(request, user_id):
    elements = users_watchlist.objects.filter(user_num = user_id).values_list('listing_id', flat=True)
    return render(request, "auctions/watch_list.html", {
        "elements":elements,
        "listings":Listing.objects.all()
    })


def bid_on_listing(request, listing_id, bidder_id):
    
    if request.method == "POST":
        my_bid = int(request.POST["bid"])
        current_listing_bid = Listing.objects.filter(id = listing_id).values_list('bid', flat=True)[0]
        if current_listing_bid >= my_bid:
            return HttpResponseRedirect(reverse('index'))
        elif current_listing_bid < my_bid:
            Listing.objects.filter(id = listing_id).update(bid = my_bid, highest_bidder = bidder_id)
            return HttpResponseRedirect(reverse('index'))



def close_bid(request, listing_id):
    Listing.objects.filter(id = listing_id).update(is_closed = True)
    return HttpResponseRedirect(reverse('index'))

def comment_action(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        user_name = request.POST["user_name"]
        Plisting = Listing.objects.get(id = listing_id)
        comment_content = request.POST["comment_content"]
        comment.objects.create(auther_name = user_name, listing_id = Plisting, content = comment_content)
        return HttpResponseRedirect(reverse("index"))