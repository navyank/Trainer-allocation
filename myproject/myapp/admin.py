from django.contrib import admin
from .models import Course
from .models import Trainer
from .models import Slot
from .models import Student
from .models import Batch

from import_export.admin import ImportExportModelAdmin

class Students(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('FullName','Qualification','CourseName','trainer','Batch','Time')
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['Batch'].queryset = Batch.objects.filter(status='not_filled')
    #     return form
# Register your models here.
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(Slot)
admin.site.register(Student,Students)
admin.site.register(Batch)