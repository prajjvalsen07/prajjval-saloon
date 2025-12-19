from django.contrib import admin

# Register your models here.
from .models import Service, AboutUs,review,Contactform

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_desc', 'service_img')
admin.site.register(Service, ServiceAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'about_description','about_img','about_feature1','about_feature2')
admin.site.register(AboutUs, AboutUsAdmin)



class reviewAdmin(admin.ModelAdmin):
    list_display = ('review_description','review_img','review_name','review_proffession')
admin.site.register(review,reviewAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display=('fullname','email','phone','message')
admin.site.register(Contactform,ContactAdmin)

