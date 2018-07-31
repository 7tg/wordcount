from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def homepage(request):
	return render(request, 'home.html')

def eggs(repuest):
	return HttpResponse("<h1>eggs</h1>")

def count(request):
	text = request.GET['full_text']
	length = len(text.split())
	count = Counter(text.split())
	return render(request, 'count.html',{'full_text':text,'length':length,'count':count.most_common(10)})

def about(request):
	return render(request,'about.html')