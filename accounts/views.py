# accounts/views.py
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView

from .forms import SmansaUserCreate_form
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

