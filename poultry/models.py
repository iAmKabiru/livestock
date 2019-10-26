from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.db.models import F, Sum

class BirdType(models.Model):
	bird_type = models.CharField(max_length=255, verbose_name="Livetocks")

	def __str__(self):
		return self.bird_type

	def quantity(self):
		return self.birds_set.count()

	class Meta:
		verbose_name = 'Animal Type'
		verbose_name_plural = 'Animal Types'


class Birds(models.Model):
	bird_type = models.ForeignKey(BirdType, on_delete=models.CASCADE, verbose_name="Animals")
	description = models.CharField(max_length = 255)
	quantity = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
	cost_per_bird = models.IntegerField(default=0, verbose_name = 'cost per Animal (N)')

	class Meta:
		verbose_name = 'Animals'
		verbose_name_plural = 'Animals'

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = 'Animal'
		verbose_name_plural = 'Animals'


class Feed(models.Model):
	bird = models.ForeignKey(Birds, on_delete=models.CASCADE, verbose_name="Animal")
	description = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.description



class Medication(models.Model):
	bird  = models.ForeignKey(Birds, on_delete=models.CASCADE, verbose_name="Animals")
	description = models.CharField(max_length=255)
	remark = models.TextField(blank=True, null=True)
	prescription = models.TextField(null=True, blank=True)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.description



class Sales(models.Model):
	birds = models.ForeignKey(Birds, on_delete=models.CASCADE, verbose_name="Animals")
	quantity = models.IntegerField()
	selling_price = models.IntegerField(verbose_name = 'selling price (N)')

	class Meta:
		verbose_name_plural = 'Sales'

	def __str__(self):
		return self.birds.description


class Employers(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	salary = models.CharField(max_length=255, verbose_name = 'salary (N)')

	class Meta:
		verbose_name_plural = 'Employers'

	def __str__(self):
		return self.name


class DoctorVisit(models.Model):
	doctor_name = models.CharField(max_length=255)
	purpose = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	description = models.TextField()

	def __str__(self):
		return self.doctor_name


class MedicalReport(models.Model):
	case = models.CharField(max_length=255)
	description = models.TextField()
	birds = models.ForeignKey(Birds, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Animals")
	date = models.DateTimeField(auto_now_add = True)
	remark = models.TextField( null=True, blank=True)
	prescription = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.case

class Purchase(models.Model):
	purchase_type_choices = (
		('feed', 'feed'),
		('animals', 'animals'),
		('medicine', 'medicine'),
		('equipement', 'equipement')
		)
	purchase_type = models.CharField(max_length=255, choices=purchase_type_choices)
	amount = models.IntegerField(default=0, verbose_name='Amount (N)')
	description = models.CharField(max_length=255, blank=True, null=True)
	quantity = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True)


class Casualty(models.Model):
	casualty_type_choices = (
		('death','death'),
		('injury', 'injury'),
		)
	birds = models.ForeignKey(Birds, on_delete=models.CASCADE, verbose_name = "Animals")
	casualty_type = models.CharField(max_length=255, choices = casualty_type_choices)
	quantity = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural = 'Casualties'




class Notification(models.Model):
	birds = models.ForeignKey(Birds, on_delete=models.CASCADE)
	description = models.TextField()
	date = models.DateField()


# signal for updating birds on casualties 
@receiver(post_save, sender=Casualty, dispatch_uid="update_when_add_casualty")
def update_when_add_casualty(sender, **kwargs):
    casualty = kwargs['instance']
    if casualty.pk:
        MedicalReport.objects.create(case=casualty.casualty_type, birds=casualty.birds, description="found" + " " + str(casualty.quantity) + " " + "affected")
        Birds.objects.filter(pk=casualty.birds_id).update(quantity=F('quantity') - casualty.quantity)


"""
# signal for creating medical report on casualty  
@receiver(post_save, sender=Casualty)
def casualty_is_created(sender, instance, created, **kwargs):
    casualty = kwargs['instance']
    print(created)
    if created:
        MedicalReport.objects.create(case=casualty.type, birds=casualty.birds)
    else:
        instance.medicalreport.save()
"""


# signal for updating birds on sale
@receiver(post_save, sender=Sales, dispatch_uid="update_when_add")
def update_when_add(sender, **kwargs):
    sales = kwargs['instance']
    if sales.pk:
        Birds.objects.filter(pk=sales.birds_id).update(quantity=F('quantity') - sales.quantity)


# signal for creating medication record on medical report
@receiver(post_save, sender=MedicalReport, dispatch_uid="update_when_add_report")
def update_when_add_report(sender, **kwargs):
    report = kwargs['instance']
    if report.pk:
        Medication.objects.create(bird=report.birds, remark=report.remark, prescription=report.prescription)
