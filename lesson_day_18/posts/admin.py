from django.contrib import admin
from .models import Post, Actor, Category, Country, Language # new

# Register your models here.
admin.site.register(Post) # new
admin.site.register(Actor) # new
admin.site.register(Category) # new
admin.site.register(Country) # new
admin.site.register(Language) # new


