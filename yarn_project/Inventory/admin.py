from django.contrib import admin

from .models import Yarn, Project, ProjectIdeas
# Register your models here.

#admin.site.register(Yarn)


@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_display = ('color', 'weight', 'brand', 'yards', 'amount')
    list_filter = ('brand', 'color', 'weight')
    search_fields = ('brand', 'color')
    

#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'purpose', 'start_date', 'deadline')
    list_filter = ('title', 'purpose', 'start_date', 'deadline')
    search_fields = ('title', 'purpose', 'yarn')


admin.site.register(ProjectIdeas)