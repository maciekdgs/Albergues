# from django.db import models
#
#
# class Countries(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#
#
# class Cities(models.Model):
#     name = models.CharField(max_length=64)
#     zipcode = models.CharField(max_length=10)
#     country = models.ForeignKey(Countries, null=False, on_delete=models.CASCADE)
#
#
# class Addresses(models.Model):
#     street_name = models.CharField(max_length=128)
#     street_number = models.CharField(8)
#     apartment_number = models.CharField(8)
#     #  TODO powiązać z Cities
#     city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
#
#
# class Pilgrims(models.Model):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.CharField(max_length=64)
#     phone_number = models.CharField(max_length=64)
#     #  TODO połączyć z Cities, Countries, Streets, Albergues, Routes
#     city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
#     address = models.ForeignKey(Addresses, null=True, on_delete=models.SET_NULL)
#
#
# class Albergues(models.Model):
#     name = models.CharField(max_length=64)
#     total_beds = models.IntegerField()
#     beds_available = models.IntegerField()  # TODO powiązać jakoś z BedsAvailability
#     bed_price = models.DecimalField()
#     #  TODO powiązać z Cities, Countries, Streets, Routes, Amenities
#
#
# class Amenities(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#     #  TODO powiązać z Albergues
#
#
# class Routes(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#     #  TODO powiązać z Cities, Countries, Albergues
#
#
# class Stops(models.Model):
#     city = models.ForeignKey(Cities, on_delete=models.CASCADE)
#     route = models.ForeignKey(Routes, on_delete=models.CASCADE)
#     stop_number = models.IntegerField()
#
#
# #  TODO przemyśleć jak obsługiwać dostępne miejsca; jak zarządzać informacją, że danego dnia jest tyle i tyle miejsc dostępnych
# class BedsAvailability(models.Model):
#     date = models.DateField(auto_now=True)
#     albergue = models.ForeignKey(Albergues, on_delete=models.CASCADE)
#     available_beds_left = models.IntegerField()
#
#
# class AmenitiesAvailability(models.Model):
#     amenity = models.ForeignKey(Amenities, on_delete=models.CASCADE)
#     albergue = models.ForeignKey(Albergues, on_delete=models.CASCADE)
