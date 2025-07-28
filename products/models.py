from django.db import models
import uuid

#  DRY -> Don't Repeat Yourself

class BaseModel(models.Model):
    uid = models.UUIDField(default= uuid.uuid4,editable=False,primary_key=True)
    created_at = models.DateField(auto_created=True) 
    updated_at = models.DateField(auto_created=True)

    class Meta:       # it will be treated as an abstract class and it will not create a model and table
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=100)
    Product_slug = models.SlugField(null=False,unique=True)
    marked_price = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    is_available = models.BooleanField(default=True)

    

class Product_Meta_Info(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_info')
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    quantity_unit = models.CharField(null=False, choices= (('kg','kg'),('g','g'),('ltr','ltr'),('ml','ml'),('pcs','pcs')), max_length=4, default='pcs')
    is_quantity_limited = models.BooleanField(default=False)
    limited_quantity = models.IntegerField(default=0)



class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    product_image = models.ImageField(upload_to='product_images/',null=False,blank=False)





