from django.contrib import admin
from .models import BirdType, Birds, Feed, Medication, Sales, Employers, DoctorVisit, MedicalReport, Purchase, Casualty, Notification


class BirdTypeAdmin(admin.ModelAdmin):
	 list_display = ('bird_type', 'quantity')

class BirdsAdmin(admin.ModelAdmin):
	list_filter = ('bird_type',)
	list_display = ('bird_type', 'description', 'quantity', 'cost_per_bird', 'date')

class FeedAdmin(admin.ModelAdmin):
	list_display = ('bird', 'description', 'date')

class MedicationAdmin(admin.ModelAdmin):
	list_filter = ('bird',)
	list_display = ('bird', 'description', 'remark', 'prescription', 'date')

class SalesAdmin(admin.ModelAdmin):
	list_filter = ('birds',)
	list_display = ('birds', 'quantity', 'selling_price')

class EmployersAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'salary')

class DoctorVisitAdmin(admin.ModelAdmin):
	list_display = ('doctor_name', 'purpose', 'date', 'description')

class MedicalReportAdmin(admin.ModelAdmin):
	list_display = ('case', 'description', 'birds', 'date', 'remark', 'prescription')

class PurchaseAdmin(admin.ModelAdmin):
	list_filter = ('purchase_type',)
	list_display = ('purchase_type', 'amount', 'description', 'quantity', 'date')


class CasualtyAdmin(admin.ModelAdmin):
	list_filter = ('casualty_type', 'birds')
	list_display = ('casualty_type', 'birds', 'quantity')


class NotificationAdmin(admin.ModelAdmin):
	list_display = ('birds', 'description', 'date')
	list_filter = ('birds',)


admin.site.register(BirdType, BirdTypeAdmin)
admin.site.register(Birds, BirdsAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Employers, EmployersAdmin)
#admin.site.register(DoctorVisit, DoctorVisitAdmin)
admin.site.register(MedicalReport, MedicalReportAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Casualty, CasualtyAdmin)
#admin.site.register(Notification, NotificationAdmin)