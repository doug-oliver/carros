from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Car, CarInventory
from django.db.models import Sum

def car_Inventory_update():
    car_count = Car.objects.all().count()
    car_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    
    CarInventory.objects.create(
        cars_count=car_count, 
        cars_value=car_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'No description available.'  
    

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_Inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_Inventory_update()

