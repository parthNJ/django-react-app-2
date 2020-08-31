from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User


class Program(models.Model):
    name = models.CharField(max_length=225)
    cost = models.IntegerField(default=0)
    description = models.TextField(default="", max_length=555)

#Serves as a Cart - User programs currently in a cart
class UserProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="program")

#Programs the user has purchased
class PurchasedProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="Purchasedprogram")
    purchase_date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    zipcode = models.IntegerField(default=00000)

    