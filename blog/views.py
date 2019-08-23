from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


'''
this is all the dummy data that we had before working with database
now that we have our database, we'll need to import those models(Post and User)
posts = [
        {
                'author': 'Sushrut Tabakade',
                'title': 'Animal Farm',
                'date_posted': 'Feb 29, 2019',
                'content': 'Blah Blah'
        },
        {
                'author': 'Suyash Tabakade',
                'title': 'Animal Farm 2',
                'date_posted': 'Feb 30, 2019',
                'content': 'Some generic Shit'
        }
]'''


#function to handle traffic from our home page
#it will take request as argument and will return http response saying that we have landed on the home page
def home(request):
        '''context ={'posts': posts} #key is string, value is posts list we created
        #return HttpResponse('<h1>Blog Home</h1>')  #response of home, message will display
        '''
        context = {'posts': Post.objects.all()}
        return render(request, 'blog/home.html', context)  #this is to load template home.html, it looks for the template name, we'll locate our template by sub directory in our template

class PostListView(ListView):
        model = Post
        template_name = 'blog/home.html' #<app>\<model>_<viewtype>.html
        context_object_name = 'posts' #it should know what variable should we be looping over, or else it will take a listobject for looping
        ordering = ['-date_posted']

class PostDetailView(DetailView):   #detailview for an individual post
        model = Post        #template name looking for is blog\post_detail.html

class PostCreateView(LoginRequiredMixin , CreateView):
        model = Post
        fields = ['title', 'content']  #because using CreateView without fields attribute is prohibited
        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)  #we are overriding the form_valid method after setting the author

class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin ,UpdateView):
        model = Post
        fields = '__all__'  #because using fields attribute is prohibited
        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)
        def test_func(self):  #applied a check on the user
                post = self.get_object()
                if post.author == self.request.user:
                    return True
                return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'   #go to path after deletion
    fields = '__all__'  # because using fields attribute is prohibited

    def test_func(self):  # applied a check on the user
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def about(request):
        return render(request, 'blog/about.html', {'title': "About Page"})

