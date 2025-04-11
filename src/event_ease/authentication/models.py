from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    address = models.TextField()
    profile_image = models.ImageField(upload_to='customers', blank=True, null=True)

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")

    def __str__(self):
        return self.name
