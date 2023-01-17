from django.contrib import admin
from .models import City, Contact, Package, Activity, PackageAccomodation, Testimonial, Transport, Accomodation, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Package)
admin.site.register(Activity)
admin.site.register(Transport)
admin.site.register(Accomodation)
admin.site.register(Contact)
admin.site.register(PackageAccomodation)
admin.site.register(City)
admin.site.register(Testimonial)