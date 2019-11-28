from django.contrib import admin
from .models import Profile, Cart, Order

admin.sites.AdminSite.index_title = 'Sahara Admin'
admin.sites.AdminSite.site_header = "Sahara Admin"
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Order)
