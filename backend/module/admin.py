from django.contrib import admin
# Register your models here.
from .models import Program, UserProgram, PurchasedProgram

admin.site.register(Program)
admin.site.register(UserProgram)
admin.site.register(PurchasedProgram)