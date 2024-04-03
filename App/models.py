from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list')


class Product(models.Model):
    author = models.ForeignKey(User ,on_delete=models.CASCADE )
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, default="uncategorized" )
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + ' | ' + str(self.author)
    
    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image =image
        self.save()

    def short_description(self):
        word = self.description.split()  #spilt the word into list 
        if len(word) > 50:  # if word are greater than 50 then 
            return " ".join(word[:30]) + "..."
        else:
            return self.description


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.subject + ' ' +self.email