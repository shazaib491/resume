from django.db import models

# Create your models here.

class intro(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    img=models.ImageField(blank=True, null=True)
    twitter=models.URLField(max_length=200,blank=True, null=True)
    facebook=models.URLField(max_length=200,blank=True, null=True)
    instagram=models.URLField(max_length=200,blank=True, null=True)
    telegram=models.URLField(max_length=200,blank=True, null=True)
    git=models.URLField(max_length=200,blank=True, null=True)
    linkedin=models.URLField(max_length=200,blank=True, null=True)

class basic(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name


class education(models.Model):
    edutitle = models.CharField(max_length=100, blank=True, null=True)
    eduDateTo = models.DateField(blank=True, null=True)
    eduDateFrom = models.DateField(blank=True, null=True)
    eduFrom = models.CharField(max_length=100, blank=True, null=True)
    eduDis = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.edutitle


class experiance(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    dis1 = models.CharField(max_length=200, blank=True, null=True)
    dis2 = models.CharField(max_length=200, blank=True, null=True)
    dis3 = models.CharField(max_length=200, blank=True, null=True)
    dis4 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name

class product(models.Model):
    cat=models.ForeignKey(category, on_delete=models.CASCADE)
    img=models.ImageField(blank=True, null=True)
    title=models.CharField(max_length=50,blank=True, null=True)
    subtitle=models.CharField(max_length=50,blank=True, null=True)
    link=models.URLField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.title + '---' + str(self.cat.name)
    
class about(models.Model):
    head=models.CharField(max_length=50,blank=True, null=True)
    img=models.ImageField(blank=True, null=True)
    s_Intro=models.CharField(max_length=150,blank=True, null=True)
    dob=models.DateField(blank=True, null=True)
    website=models.URLField(max_length=200,blank=True, null=True)
    mobile=models.IntegerField(blank=True, null=True)
    city=models.CharField(max_length=50,blank=True, null=True)
    age=models.IntegerField(blank=True, null=True)
    degree=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=254,blank=True, null=True)
    country=models.CharField(max_length=50,blank=True, null=True)
    introduction=models.CharField(max_length=500,blank=True, null=True)
    freelance=models.BooleanField(blank=True, null=True)
    avail=models.BooleanField(blank=True, null=True)
    def __str__(self):
        return self.head
    
class testimonial(models.Model):
    img=models.ImageField(blank=True, null=True)
    name=models.CharField(max_length=50,blank=True, null=True)
    designation=models.CharField( max_length=50,blank=True, null=True)
    comments=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class services(models.Model):
    icon=models.CharField(max_length=50,blank=True, null=True)
    title=models.CharField(max_length=50,blank=True, null=True)
    caption=models.TextField(blank=True, null=True)
    color=models.CharField(max_length=50,blank=True, null=True)
    def __str__(self):
        return self.title
    
class contact(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=254,blank=True, null=True)
    subject=models.CharField(max_length=100,blank=True, null=True)
    message=models.CharField(max_length=150,blank=True, null=True)
    def __str__(self):
        return self.name + '-----' + self.email
    
