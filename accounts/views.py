# accounts/views.py
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SmansaUserCreate_form, SmansaUserVerifyForm, smansauser_admin_form
from .models import SmansaUser
from blog.models import Blog, BlogComment

class SmansaUserCreateView(CreateView):
    form_class = SmansaUserCreate_form
    model = SmansaUser
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(SmansaUserCreateView, self).get_context_data(**kwargs)

        return context

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        self.object.set_password(form.cleaned_data['password'])

        self.object.save()

        return super(SmansaUserCreateView,self).form_valid(form)    

class BloggerListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    model = SmansaUser
    paginate_by = 5

    def get_queryset(self):

        if self.request.user.is_superuser:
            return SmansaUser.objects.filter(verified_by=0)
        else:
            displayUser = list()
            displayUser.append(self.request.user.id)

            activeUser = SmansaUser.objects.filter(verified_by__gt=0)

            for usr in activeUser:
                displayUser.append(usr.id)

            return SmansaUser.objects.filter(pk__in=displayUser)

class BloggerNewListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    template_name = 'accounts/newBlogger_list.html'  # Specify your own template name/location
    model = SmansaUser
    paginate_by = 5

    def get_queryset(self):

        return SmansaUser.objects.filter(verified_by=0)

class BloggerActiveListView(generic.ListView):
    """
    Generic class-based view for a list of bloggers.
    """
    template_name = 'accounts/activeBlogger_list.html'  # Specify your own template name/location
    model = SmansaUser
    paginate_by = 5

    def get_queryset(self):

        return SmansaUser.objects.filter(verified_by__gt=0)

class BloggerDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = SmansaUser

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class SmansaUserVerifyView(LoginRequiredMixin, UpdateView):
    form_class = SmansaUserVerifyForm
    model = SmansaUser
    template_name = 'accounts/smansauser_verify.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(SmansaUserVerifyView, self).get_context_data(**kwargs)

        return context

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        if form.cleaned_data.get('verify', None):
            #Add logged-in user as author of comment
            self.object.verified_by = self.request.user.id

            content_type = ContentType.objects.get_for_model(Blog)
            permission = Permission.objects.get(
                codename='add_blog',
                content_type=content_type,
            )
            self.object.user_permissions.add(permission)
            content_type = ContentType.objects.get_for_model(BlogComment)
            permission = Permission.objects.get(
                codename='add_blogcomment',
                content_type=content_type,
            )
            self.object.user_permissions.add(permission)
        self.object.save()

        return super(SmansaUserVerifyView,self).form_valid(form)    

class AdminSmansaView(LoginRequiredMixin, FormView):
    template_name = 'accounts/smansauser_admin.html'  # Specify your own template name/location
    form_class = smansauser_admin_form

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)

        context['caption'] = 'Blog Alumni SMANSA Genteng'

        bloggers = SmansaUser.objects.all()
        newComers = bloggers.filter(verified_by=0).count()
        activeBloggers = bloggers.filter(verified_by__gt=0).count()
        context['bloggers'] = bloggers.count()
        context['newComers'] = newComers
        context['activeBloggers'] = activeBloggers

        blogs = Blog.objects.all().count()
        context['blogs'] = blogs

        return context

class SmansaUserDeleteView(generic.DeleteView): 
    # specify the model you want to use 
    model = SmansaUser 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url = '/accounts/bloggers/'

