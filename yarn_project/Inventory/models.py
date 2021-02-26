from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

WEIGHT_CHOICES = (
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ("6", "6"), 
    ("7", "7"), 
   
)

PRIORITY_CHOICES = (
    ("low", "low"), 
    ("medium", "medium"), 
    ("high", "high"), 
    
   
)

COLOR_CHOICES = (
    ("red", "red"),
    ("orange", "orange"), 
    ("yellow", "yellow"), 
    ("green", "green"), 
    ("blue", "blue"), 
    ("purple", "purple"), 
    ("pink", "pink"), 
    ("white", "white"), 
    ("gray", "gray"), 
    ("brown", "brown"), 
    ("black", "black"),
)




class Yarn(models.Model):
    image = models.ImageField(upload_to="yarn/images/", blank=True, null=True, default="default.jpg")
    color = models.CharField(max_length=200)
    weight = models.CharField(max_length=20, choices = WEIGHT_CHOICES, default="4")
    brand = models.CharField(max_length=200)
    yards = models.IntegerField(blank=True, null=True)
    hook = models.CharField(max_length=200, blank=True, null=True)
    grams = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    care_instructions = models.CharField(max_length=500, default="", blank=True, null=True)
    color_group = models.CharField(max_length=50, choices=COLOR_CHOICES, default="blue")
    
    class Meta:
        ordering = ['brand', 'color']

    def __str__(self):
        return self.color + " - " + self.brand



class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="project/images/")
    purpose = models.CharField(max_length=200, default="")
    start_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    #Relationship
    yarn = models.ManyToManyField(Yarn, null=True, blank=True)
    hook = models.CharField(max_length=20, default="")
    pattern = RichTextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=50, choices= PRIORITY_CHOICES, default="low")

  

    def __str__(self):
        return self.title


class ProjectIdeas(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title