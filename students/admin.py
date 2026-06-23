from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'phone', )
    search_fields = ('name','phone',)
    list_filter = ('age',)

# admin.site.register(Student, StudentAdmin)
