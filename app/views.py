from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.contrib import messages

def testSite(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return HttpResponse("test passed _ string form my site")