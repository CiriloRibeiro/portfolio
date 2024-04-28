from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Post

def home_page(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "projects/home_page.html", {'page_obj': page_obj})

def about(request):
     return render(request, "projects/about.html")

def custom_404_error(request, exception):
    return redirect('home-page')  # Redirect to the home page URL (named 'home')
