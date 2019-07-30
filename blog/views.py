from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import blog

def allblog(request):
	allposts =  blog.objects
	return render(request, 'blog/bloghome.html', {'allposts': allposts.all})

def details(request, blog_id):
	fullpost = get_object_or_404(blog, pk=blog_id)
	return render(request, 'blog/details.html', {'post':fullpost})