from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(form)
        #If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()


            #Redirect to Home
            return HttpResponseRedirect('/')
        
        else:
            #No, Show Error
            return HttpResponseRedirect(form.erros.as_json())


    
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('created_at')[:20]
    # Show
    return render(request, 'posts.html',{'posts': posts})

def delete(request, post_id):
   # Find Post
   post = Post.objects.get(id = post_id)

   post.delete()
   return HttpResponseRedirect('/')

def edit(request,post_id):
    # If the method is POST
    post = Post.objects.get(id=post_id)
    print('Hello World')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance = post)
        #If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            return HttpResponseRedirect('/')   
    else: 
        form=PostForm
        return render(request,'edit.html',{'post':post,'form':form})

def like(request, post_id):
   # Find Post
   post = Post.objects.get(id = post_id)
   newlikecount=post.like_count+1
   post.like_count=newlikecount
   post.save()
   return HttpResponseRedirect('/')

