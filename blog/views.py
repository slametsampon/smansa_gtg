from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Blog, BlogComment
from .forms import BlogCreate_form
from accounts.models import SmansaUser

from django.views.generic import TemplateView

# Create your views here.
'''
class BlogHomeView(TemplateView):
    template_name = 'blog/index.html'
'''

class BlogHomeView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = Blog
    paginate_by = 5

    
class BlogListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = Blog
    paginate_by = 5

    
from django.shortcuts import get_object_or_404

class BlogListbyAuthorView(generic.ListView):
    """
    Generic class-based view for a list of blogs posted by a particular SmansaUser.
    """
    model = Blog
    paginate_by = 5
    template_name ='blog/blog_list_by_author.html'
    
    def get_queryset(self):
        """
        Return list of Blog objects created by SmansaUser (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author=get_object_or_404(SmansaUser, pk = id)
        return Blog.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        """
        Add SmansaUser to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(SmansaUser, pk = self.kwargs['pk'])
        return context
    
class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Blog

    
class BloggerListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    model = SmansaUser
    paginate_by = 5


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('blog:blog-detail', kwargs={'pk': self.kwargs['pk'],})

class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = Blog
    form_class = BlogCreate_form
    template_name = 'blog/blog_form.html'

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCreateView, self).get_context_data(**kwargs)

        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user

        # Call super-class form validation behaviour
        return super(BlogCreateView, self).form_valid(form)

