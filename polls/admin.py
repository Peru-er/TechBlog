from django.contrib import admin
from polls.models import User, Product

# class UserAdmin(admin.ModelAdmin):
#     list_display = ["first_name", "last_name", "phone", "email"]
#     list_filter = ["first_name"]
#     search_fields = ["email"]
#
# admin.site.register(User, UserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "email"]
    list_filter = ["first_name"]
    search_fields = ["email"]


# name = models.CharField(max_length=255)
#     description = models.TextField(null=True, blank=True)
#     stock = models.PositiveIntegerField(default=0, null=False)
#     price = models.FloatField(default=0.0, null=False)
#     is_active = models.BooleanField()
#     create_at = models.DateTimeField(auto_now_add=True)
#

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "stock", "price", "is_active", "create_at"]
    list_filter = ["name", "price", "is_active"]
    search_fields = ["name", "price"]
