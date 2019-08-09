from django.contrib import admin
from .models import Menu, Section, Article, FirstWords, Excursion
# Register your models here.
@admin.register(Menu)
class SitesEdit(admin.ModelAdmin):
	list_display = ("id","name","active","createDate","creator")
	list_editable = ("name",)

@admin.register(Section)
class SitesEdit(admin.ModelAdmin):
	list_display = ("id","name", "active","menu", "createDate","creator")
	list_editable = ("name","active","menu",)

@admin.register(Article)
class ArticlesEdit(admin.ModelAdmin):
	list_display = ("id","title","content","section", "description","active","createDate","creator")
	list_editable = ("title","content","active",)

@admin.register(FirstWords)
class FirstWordsEdit(admin.ModelAdmin):
	list_display = ("id","word","wojtekWord","lenaWord", "createDate","creator")
	list_editable = ("word","wojtekWord","lenaWord",)


@admin.register(Excursion)
class ExcursionEdit(admin.ModelAdmin):
	list_display = ("id","destination","description","createDate","creator",)
	list_editable = ("destination","description",)
