from django.contrib import admin
from .models import User, Product, Tag, Article


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


def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)


make_featured.short_description = 'Позначити як Featured'


def reset_views(modeladmin, request, queryset):
    queryset.update(views=0)


reset_views.short_description = 'Скинути перегляди'


def export_articles(modeladmin, request, queryset):
    for article in queryset:
        print(
            article.title,
            article.author,
            article.views
        )


export_articles.short_description = 'Експорт статей'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'author',
        'views',
        'likes',
        'is_featured',
        'published_at'
    ]

    list_filter = [
        'is_featured',
        'published_at',
        'author',
        'tags'
    ]

    search_fields = [
        'title',
        'content'
    ]

    list_editable = [
        'is_featured'
    ]

    filter_horizontal = [
        'tags'
    ]

    readonly_fields = [
        'views',
        'likes'
    ]

    actions = [
        make_featured,
        reset_views,
        export_articles
    ]


admin.site.register(Tag)
