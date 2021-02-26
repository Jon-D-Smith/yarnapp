from django import forms

from .models import Project, Yarn, ProjectIdeas

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "deadline" : forms.TextInput(attrs={'class':'form-control',  'type':'date'}),
            "start_date" : forms.TextInput(attrs={'class':'form-control',  'type':'date'}),
            "yarn" : forms.CheckboxSelectMultiple(attrs={'class':'scrollbar'}),
            
            
        }
        labels = {
            'is_complete': ('Complete'),
            'yarn' : (''),
        }
        

class YarnForm(forms.ModelForm):
    class Meta:
        model = Yarn
        fields = "__all__"


class ProjectIdeasForm(forms.ModelForm):
    class Meta:
        model = ProjectIdeas
        fields = "__all__"    