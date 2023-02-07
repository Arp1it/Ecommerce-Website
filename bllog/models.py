from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=100)
    head0content = models.CharField(max_length=5000)
    head1 = models.CharField(max_length=100)
    head1content = models.CharField(max_length=5000)
    head2 = models.CharField(max_length=100)
    head2content = models.CharField(max_length=5000)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title