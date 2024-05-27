from django.contrib import admin
from . models import register,subject,mark

# Register your models here.
class regadmin(admin.ModelAdmin):
    list_display = ['name','age','img']
    list_editable = ['age','img']

admin.site.register(register,regadmin)

admin.site.register(subject)


class markad(admin.ModelAdmin):
    list_display = ['stu_id', 'mark', 'sub_id']
    list_editable = ['mark']
admin.site.register(mark,markad)

