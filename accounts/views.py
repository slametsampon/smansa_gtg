# accounts/views.py
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView

from .forms import SmansaUserCreate_form
from .models import SmansaUser

class SignUpView(CreateView):
    form_class = SmansaUserCreate_form
    #success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        self.object.set_password(form.cleaned_data['password'])

        self.object.save()

        return super(SignUpView,self).form_valid(form)    

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('accounts:blogger-detail', kwargs={'pk': self.kwargs['pk'],})

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

