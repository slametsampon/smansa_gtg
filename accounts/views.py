# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SmansaUserCreate_form

class SignUpView(CreateView):
    form_class = SmansaUserCreate_form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        self.object.set_password(form.cleaned_data['password'])

        self.object.save()

        return super(SignUpView,self).form_valid(form)    
