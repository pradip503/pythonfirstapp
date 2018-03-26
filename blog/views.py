from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'list.html', {'post': posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.created = timezone.now()
			post.save()
			return redirect('post_list')
	else:
		form = PostForm()
	return render(request, 'new_post.html', {'form': form})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	return render(request, 'post-detail.html', {'post': post})

def edit_post(request, pk):
		template = 'new_post.html'
		post = get_object_or_404(Post, pk = pk)

		if request.method == 'POST':
			form = PostForm(request.POST, instance = post)
			if form.is_valid():
				form.save()
				return redirect('/')

		else:
			form = PostForm(instance=post)

		context={
		'form': form,
		'post': post,
		}
		return render(request, template, context)

def post_delete(request, pk):
	blog = get_object_or_404(Post, pk = pk)
	blog.delete()
	return HttpResponse("Successfully deleted!!")