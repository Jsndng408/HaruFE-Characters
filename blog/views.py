from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] # Sorts post from newest to oldest
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

	# Be mindful of the name
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# Validates that the logged in user is the one who created the post
	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

# Mixin has to be the leftmost arguments
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

# 'title': 'Vio\'s HaruFE Characters'

def about(request):
	return render(request, 'blog/about.html', {'title': 'About Vio' })