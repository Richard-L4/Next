from django.contrib import admin
from .models import Contact, CardText, \
    CardTextTranslation, Comment, CommentReaction


# Register your models here.
admin.site.register(Contact)


class CommentReactionLine(admin.TabularInline):
    model = CommentReaction
    extra = 0
    readonly_fields = ('user', 'reaction')


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


@admin.register(CommentReaction)
class CommentReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'reaction')
    list_filter = ('reaction', 'user')
    search_fields = ('user_username', 'comment_text')
