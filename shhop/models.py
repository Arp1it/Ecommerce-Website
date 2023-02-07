from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=5000)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    Image = models.ImageField(upload_to="shhop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    email= models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

class Order(models.Model):
    oder_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email_id = models.CharField(max_length=111)
    address = models.CharField(max_length=500)
    city= models.CharField(max_length=111)
    state= models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=50)
    date_of_order = models.DateField()

class OrdersUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    orderid = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."