from django.contrib import admin
from .models import Collection, CollectionUser

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin): pass

@admin.register(CollectionUser)
class CollectionUserAdmin(admin.ModelAdmin): pass
