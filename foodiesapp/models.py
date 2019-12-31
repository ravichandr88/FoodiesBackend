from django.db import models



from django.db import models


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass






class Meal(models.Model):
    name = models.CharField(max_length=200)
    price = models.TextField(blank=True)
    
    pic = models.ImageField(upload_to='pics', blank=True)
    field = models.CharField(max_length=50,default='meal', editable=False)



class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.TextField(blank=True)

    pic = models.ImageField(upload_to='pics', blank=True)
    field = models.CharField(max_length=50,default='food', editable=False)
  



class BEVERAGES(models.Model):
    name = models.CharField(max_length=200)
    price = models.TextField(blank=True)

    pic = models.ImageField(upload_to='pics', blank=True)
    field = models.CharField(max_length=50,default='bevrage', editable=False)
 


class COMBOS(models.Model):
    name = models.CharField(max_length=200)
    price = models.TextField(blank=True)

    pic = models.ImageField(upload_to='pics', blank=True)
    field = models.CharField(max_length=50,default='combo', editable=False)
   


class Slider(models.Model):
    title = models.CharField(max_length=200)
    alt = models.CharField(max_length=200)

    image = models.ImageField(upload_to='pics', blank=True)

    thumbImage = models.ImageField(upload_to='pics', blank=True)



class Gallery(models.Model):
  
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics', blank=True)

  

# class Gallery(models.Model):
  
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='pics', blank=True)










class Consult(models.Model):

    Feedback = 'Feedback'
    Report = 'Report a bug'
    Feature = 'Feature request'
  
    SUBJECT_CHOICES = [
        (Feedback, 'Feedback'),
        (Report, 'Report a bug'),
        (Feature, 'Feature request'),
        
    ]




    name = models.CharField(max_length=30,blank=True)
    subject = models.CharField(max_length=30,choices=SUBJECT_CHOICES,blank=True)
    message = models.TextField(max_length=500,blank=True)
    from_email = models.CharField(max_length=30,blank=True)



    # name = models.CharField(max_length=16)
    # position = models.CharField(max_length=16, null=True)
    # group = models.CharField(max_length=50)
    # email = models.CharField(max_length=50, null=True)
    # phone = models.CharField(max_length=14)
    # describe = models.TextField(blank=True, null=True)
    # file = models.FileField(blank=True, null=True)
    # create_date = models.DateTimeField(auto_now_add=True)
    # update_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name


    # class Meta:
    #     db_table = 'Consult'







