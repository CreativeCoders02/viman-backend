from django.contrib import admin

from .models import TestModel,Proof,Request,Room,Student,Slot
# Register your models here.

admin.site.register(TestModel)
admin.site.register(Proof)
admin.site.register(Request)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Slot)
