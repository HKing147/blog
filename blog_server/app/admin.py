from django.contrib import admin
from app.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Label)
admin.site.register(Comment)
