from django.shortcuts import render
from .models import Post
def index(request):
	if request.method == 'POST':
		post=Post(name="name", dishname="dishname", review="review")
		post.name = request.POST.get('name')
		post.email = request.POST.get('email')
		post.dishname = request.POST.get('dishname')
		post.review= request.POST.get('review')
		post.save()
	p=Post()
	p=Post.objects.all().values('dishname','review')
	return render(request,'index.html',{'p' : p})


