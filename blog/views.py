from inspect import ismethoddescriptor
from django.shortcuts import render
from blog.models import Yazi

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def yazilar(request):
	context = {
		"blogs": Yazi.objects.all()
	}
	return render(request, 'yazilar.html',context)

def yazidetay(request, slug):
	blog = Yazi.objects.get(slug=slug)
	return render(request, 'yazidetay.html',{
		"blog": blog
	})