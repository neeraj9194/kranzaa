from django.db import models
from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import datetime
#from location_field.models.plain import PlainLocationField


class Category(models.Model):
    cat_title=models.CharField(max_length=100,unique=True)
    slug=models.CharField(max_length=120,unique=True)
    parent_category = models.ForeignKey('self', null=True, blank=True)
    
    def __str__(self):
        return self.cat_title


class RegStore(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    desc=models.TextField()
    storeslug=models.CharField(max_length=120,unique=True)
    date_added=models.DateTimeField('Date Added',auto_now_add=True,auto_now=False)
    address=models.CharField(max_length=200)
    owner=models.CharField(max_length=100)
    avail_city = (
        ('delhi', 'Delhi'),
        ('mumbai', 'Mumbai'),
    )
    city=models.CharField(max_length=20,choices=avail_city,default='delhi')
    phone_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[89]\d{9}$', message="Wrong Mobile Number ")
    phone_number = models.CharField(validators=[phone_regex], blank=True,max_length=10)
    category=models.ManyToManyField(Category,default=None)
    main_pic=models.ImageField(upload_to="static/store_img/")

    def __str__(self):
        return self.name

class Location(models.Model):
    store=models.ForeignKey(RegStore,default=None)
    loc_name = models.CharField(max_length=70)
    point = models.PointField(default='POINT(0.0 0.0)')
    objects = models.GeoManager()
    def __str__(self):
        return self.loc_name

class Comments(models.Model):
    user=models.ForeignKey(User)
    created = models.DateTimeField()#auto_now_add=True)
    comment=models.TextField(max_length=300)
    STATUS_CHOICES = [(i,i) for i in range(1,11)]
    ratings=models.IntegerField(choices=STATUS_CHOICES)
    store = models.ForeignKey(RegStore)
    pos_score_comment=models.DecimalField(max_digits=6, decimal_places=4)
    neg_score_comment=models.DecimalField(max_digits=6, decimal_places=4)
    polarity_comment=models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return self.comment
