from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.contrib import messages
from datetime import datetime
from .models import Article, FirstWords, Excursion

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    #return HttpResponse("Site is unedr maintanance!")
    return render(
    	request, "home/index.html",
    	{
    		"title" : "Last Char",
    		"year" 	: datetime.now().year,
    		"news"  : Article.objects.getNews(),
    		"weekChallenge" : Article.objects.getChallenge()
    	}
    )

def family(request):
	assert isinstance(request, HttpRequest)
	return render(
		request, "family/family.html",
    	{
    		"firstWord" : FirstWords.objects.all(),
    		"excursion" : Excursion.objects.all()
    	}
	)

def programming(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, "programming/programming.html",
        {
            "intro" : Article.objects.getIntro()
            #"excursion" : Excursion.objects.all()
        }
    )