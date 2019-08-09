from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.timezone import now

"""

Menu  => Section {pills} => Article

home => news 		  }
	=> week challenge => title - date - author - content - active - sectionID

Name - active
	=> Name - menuID
		=>  title - date - author - content - active - sectionID



"""
# 5 rekords on site
class ArticlesQuerySet(models.QuerySet):
    def getNews(self):
        return self.filter((Q(active=1) & Q(section_id=2)))[:5]

    def getChallenge(self):
        return self.filter((Q(active=1) & Q(section_id=3)))[:5]

    def getIntro(self):
	    return self.filter((Q(active=1) & Q(section_id=4)))[:5]


STATUS_BIT = (
	(1, 'Active'),
	(0, 'In Active'),
)


# Home
class Menu(models.Model):
	name = models.CharField(max_length=300, null=False,unique=True)
	active = models.BooleanField(default=True, choices=STATUS_BIT)
	createDate = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User,related_name="menu_creator",on_delete=models.CASCADE)

	def __str__(self):
		return str(self.name)

class Section(models.Model):
	name = models.CharField(max_length=255)
	active = models.BooleanField(default=True, choices=STATUS_BIT)
	createDate = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User,related_name="section_creator", on_delete=models.CASCADE)
	menu = models.ForeignKey(Menu, related_name="section_to_menu", on_delete=models.CASCADE)
	def __str__(self):
		return str(self.name)

class Article(models.Model):
	title = models.CharField(max_length=1000,default="News")
	content = models.TextField(max_length=10000)
	description = models.CharField(max_length=100)
	active = models.BooleanField(default=True, choices=STATUS_BIT)
	createDate = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User, related_name="article_creator", on_delete=models.CASCADE)
	section = models.ForeignKey(Section, related_name="article_to_section", on_delete=models.CASCADE)

	objects = ArticlesQuerySet.as_manager()

	def __str__(self):
		return str(self.content)

# Family
class FirstWords(models.Model):
	word = models.CharField(max_length=100, default="n/a")
	wojtekWord = models.TextField(max_length=100)
	lenaWord = models.TextField(max_length=100)
	createDate = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User, related_name="word_added", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.word)

class Excursion(models.Model):
	destination= models.CharField(max_length=100, default="na")
	description = models.TextField(max_length=1000, default="na")
	createDate = models.DateTimeField(default=now)
	creator = models.ForeignKey(User, related_name="excurion_added", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.destination)