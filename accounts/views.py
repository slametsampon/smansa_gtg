# accounts/views.py
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SmansaUserCreate_form, SmansaUserVerifyForm
from .models import SmansaUser

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

class BloggerDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = SmansaUser

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

        self.object.save()

        return super(SmansaUserVerifyView,self).form_valid(form)    

