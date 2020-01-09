from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=500)
    urls = models.TextField()
    body = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # this chages the name what is seen from the admin panel
        return self.title

    # return a short body
    def summery(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
