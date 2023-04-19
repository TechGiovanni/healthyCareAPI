from django.db import models
# from django.contrib.postgres.fields import ArrayField
# Create your models here.


class User(models.Model):
    first_name = models.CharField(
        max_length=200, verbose_name="the user first name")
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=30)
    mobile_number = models.CharField(
        'Phone number', max_length=300, unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name

    # def __str__(self):
    #     return self.first_name + " " + self.last_name + " " + self.email + " " + self.mobile_number + " " + self.date_of_birth

    # def get_item(self):
    #     return f'{self.first_name} {self.last_name} : {self.mobile_number}'


# class Dentist(models.Model):
#     first_name = models.CharField(
#         max_length=200, verbose_name="the dentist first name")
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200, unique=True)
#     specialty = models.CharField(max_length=50)
#     address = models.CharField(max_length=250)
#     useful_information = models.CharField(max_length=500)
#     means_of_payment = models.CharField(max_length=100)
#     price = models.IntegerField()
    # pictures = ArrayField(models.CharField(max_length=10, blank=True), size=8)


# class Institution(models.Model):
#     name = models.CharField(
#         max_length=100, verbose_name="the institution name")
#     address = models.CharField(max_length=250)
#     mobile_number = models.CharField(max_length=30, unique=True)
#     fax_number = models.CharField(max_length=30, unique=True)
#     price = models.IntegerField()

# When the business is open


# class Hours_of_operation(models.Model):
#     monday = models.CharField(max_length=5)
#     tuesday = models.CharField(max_length=5)
#     wednesday = models.CharField(max_length=5)
#     thursday = models.CharField(max_length=5)
#     friday = models.CharField(max_length=5)
#     saturday = models.CharField(max_length=5)
#     sunday = models.CharField(max_length=5)

# Dates available for appointments


# class appointment_Dates(models.Model):
#     monday = models.CharField(max_length=5)
#     tuesday = models.CharField(max_length=5)
#     wednesday = models.CharField(max_length=5)
#     thursday = models.CharField(max_length=5)
#     friday = models.CharField(max_length=5)
#     saturday = models.CharField(max_length=5)
#     sunday = models.CharField(max_length=5)


# class Appointments(models.Model):
#     user_id = models.ManyToManyField(
#         User, on_delete=models.PROTECT, related_name="client", verbose_name="the user that created the appointment")
#     appointment_with_hospital = models.ManyToManyField(
#         Dentist, on_delete=models.PROTECT, related_name="practitioner_or_facility", blank=True, verbose_name="the appointment with a hospital")
#     appointment_with_dentist = models.ManyToManyField(
#         Dentist, on_delete=models.PROTECT, related_name="practitioner_or_facility", blank=True, verbose_name="the appointment with a dentist")
