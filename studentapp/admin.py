from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class Studentresource(resources.ModelResource):
    class Meta:
        model = Student


class StudentAdmin(ImportExportModelAdmin):
    resources_class = Studentresource


admin.site.register(Category_class)
admin.site.register(Participant)
admin.site.register(Tutor)
admin.site.register(Kurator)
admin.site.register(Vospitatel)
admin.site.register(AppealCurators)
admin.site.register(Student, StudentAdmin)
