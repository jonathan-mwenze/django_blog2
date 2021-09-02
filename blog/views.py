from django.shortcuts import render
from .models import Post
from .import model_helpers

def index(request, category_name=model_helpers.post_category_all()):
	posts = Post.objects.all()
	context = {
	   'category': category,
	   'posts':posts,
	   'title':'Home',
	}
	return render(request, 'blog/index.html', context)
return render()