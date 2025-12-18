from django.contrib import admin
from .models import Contact, Register, CardText, CardTextTranslation, Comment


# Register your models here.
admin.site.register(Contact)


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Inline translations
class CardTextTranslationInline(admin.TabularInline):
    model = CardTextTranslation
    extra = 1


@admin.register(CardText)
class CardTextAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CardTextTranslationInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('CardText', 'user', 'text', 'created_at')
    list_filter = ('CardText', 'user')
    search_fields = ('text',)
