from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Tarif(models.Model):
    daya = models.IntegerField()
    tarif = models.IntegerField()

    class Meta:
        verbose_name = "Tarif"
        verbose_name_plural = "Tarifs"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tarif_detail", kwargs={"pk": self.pk})


class User(AbstractUser):
    address = models.CharField(max_length=100)
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE, null=True)


class Months(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = "Months"
        verbose_name_plural = "Monthss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Months_detail", kwargs={"pk": self.pk})



class Uses(models.Model):
    custommer = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.ForeignKey(Months, on_delete=models.CASCADE)
    year = models.IntegerField()
    meter_start = models.IntegerField()
    meter_end = models.IntegerField()

    class Meta:
        verbose_name = "Uses"
        verbose_name_plural = "Usess"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Uses_detail", kwargs={"pk": self.pk})


class Tagihan(models.Model):
    custommer = models.ForeignKey(User, on_delete=models.CASCADE)
    uses = models.ForeignKey(Uses, on_delete=models.CASCADE)
    month = models.ForeignKey(Months, on_delete=models.CASCADE)
    year = models.IntegerField()
    sum_meter = models.IntegerField()
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Tagihan"
        verbose_name_plural = "Tagihans"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tagihan_detail", kwargs={"pk": self.pk})


class PayMent(models.Model):
    tagihan = models.ForeignKey(Tagihan, on_delete=models.CASCADE)
    custommer = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.ForeignKey(Months, on_delete=models.CASCADE)
    date_pay = models.DateTimeField(auto_now_add=True)
    biaya_admin = models.IntegerField(default=5000)
    sumPayment = models.IntegerField()
    

    class Meta:
        verbose_name = "PayMent"
        verbose_name_plural = "PayMents"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PayMent_detail", kwargs={"pk": self.pk})
