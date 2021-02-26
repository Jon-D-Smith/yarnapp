from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime, date
from django.contrib.auth.mixins import LoginRequiredMixin

#local imports
from .models import Yarn, Project, ProjectIdeas
from .forms import ProjectForm, YarnForm, ProjectIdeasForm
from .filters import YarnFilter

# Create your views here.

def home(request):
    projects = Project.objects.all().order_by('deadline')

    today = date.today()
    

    context = {'projects' : projects, 'today':today }
    return render(request, 'Inventory/index.html', context)

def completed(request):
    
    projects = Project.objects.all().order_by('deadline')

   
    

    context = {'projects' : projects}
    return render(request, 'Inventory/completed_projects.html', context)

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin,CreateView):
    template_name = "Inventory/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy('home')
    login_url = '/admin'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['yarn_list'] = Yarn.objects.all()
        return context

   
class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = "Inventory/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy('home')
    login_url = '/admin'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['yarn_list'] = Yarn.objects.all()
        return context


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    success_url = reverse_lazy("home")
    login_url = '/admin'

##### YARN ######

def yarn(request):

    ORDER_CHOICES = ['brand', 'color', 'amount', 'weight', 'color_group']

    yarns = Yarn.objects.order_by('color_group', 'color')

    yarnFilter = YarnFilter(request.GET, yarns)
    
    yarns = yarnFilter.qs
    #if not request.GET.get('sort') == "":
     #   yarns = yarnFilter.qs.order_by(request.GET.get('sort', 'color'))
    if request.GET.get('sort') in ORDER_CHOICES:
        yarns = yarnFilter.qs.order_by(request.GET.get('sort', 'color'))
    else:
        yarns = yarnFilter.qs.order_by('color_group', 'color')
   
    context = {'yarns':yarns, 'yarnFilter':yarnFilter}
    return render(request, 'Inventory/yarn.html', context)

class YarnDetailView(DetailView):
    model = Yarn

class YarnCreateView(LoginRequiredMixin,CreateView):
    template_name = "Inventory/yarn_form.html"
    form_class = YarnForm    
    success_url = reverse_lazy('yarn')
    login_url = '/admin'

class YarnUpdateView(LoginRequiredMixin,UpdateView):
    model = Yarn
    template_name = "Inventory/yarn_form.html"
    form_class = YarnForm
    success_url = reverse_lazy('yarn')
    login_url = '/admin'

class YarnDeleteView(LoginRequiredMixin,DeleteView):
    model = Yarn
    success_url = reverse_lazy('yarn')
    login_url = '/admin'


#### Project Ideas ####

def projectIdeas(request):
    ideas = ProjectIdeas.objects.order_by('title')

    context = {'ideas':ideas}
    return render(request, 'Inventory/project_ideas.html', context)

class ProjectIdeasCreateView(LoginRequiredMixin,CreateView):
    template_name = "Inventory/project_ideas_form.html"
    form_class = ProjectIdeasForm   
    success_url = reverse_lazy('project-ideas')
    login_url = '/admin'

class ProjectIdeasUpdateView(LoginRequiredMixin,UpdateView):
    model = ProjectIdeas
    template_name = "Inventory/project_ideas_form.html"
    form_class = ProjectIdeasForm   
    success_url = reverse_lazy('project-ideas')
    login_url = '/admin'

class ProjectIdeasDeleteView(LoginRequiredMixin,DeleteView):
    model = ProjectIdeas
    success_url = reverse_lazy('project-ideas')
    login_url = '/admin'