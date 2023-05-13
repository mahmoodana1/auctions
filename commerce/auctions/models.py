from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class categories(models.Model):
    category_name = models.CharField(max_length=32)
    def __str__(self):
        return self.category_name


class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    bid = models.IntegerField()
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    category = models.ForeignKey(categories, related_name="listing_category", blank=True, on_delete=models.CASCADE)
    auther_num = models.IntegerField()
    highest_bidder = models.IntegerField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title}, current bid:{self.bid} ({self.category})"

class users_watchlist(models.Model):
    user_num = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user_num} has wishlised listing {self.listing_id}"

class comment(models.Model):
    auther_name = models.CharField(max_length=30)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    def __str__(self):
        return f"{self.auther_name} commented {self.content}"