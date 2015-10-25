from django.contrib import admin
from .models import WhatTheUser, InviteToken

@admin.register(WhatTheUser)
class WhatTheUserAdmin(admin.ModelAdmin): pass

@admin.register(InviteToken)
class InviteTokenAdmin(admin.ModelAdmin): pass