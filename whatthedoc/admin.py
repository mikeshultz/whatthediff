from django.contrib import admin
from .models import WebDocument, WebDocumentBody

@admin.register(WebDocument)
class WebDocumentAdmin(admin.ModelAdmin): pass

@admin.register(WebDocumentBody)
class WebDocumentBodytAdmin(admin.ModelAdmin): pass