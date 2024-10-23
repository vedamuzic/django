# from django.db import models

# # Create your models here.

# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     discription = models.TextField()  # Note the spelling here


# # class vedamusic(models.Model):
# #     song_name=models.CharField(max_length=100)
# #     song_artist=models.CharField(max_length=100)
# #     discription=models.TextField()



# class userlogin(models.Model):
#     user_name = models.CharField(max_length=100)
#     user_id = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=20) 



from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    discription = models.TextField() 



class Login(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100)



class Profile(models.Model):
    name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pics/' , null=True , blank=True)
    bio = models.EmailField(max_length=300, blank=True)
