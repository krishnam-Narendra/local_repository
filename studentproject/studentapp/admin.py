from django.contrib import admin
from .models import StudentRegister, ProxyStudentRegister,MarksDetails
from .models import Post
# Register your models here.

class StudentRegisterAdmin(admin.ModelAdmin):
    list_display = ['roolno','fname','lname','father_name','course','school_name','email']

class ProxyStudentRegisterAdmin(admin.ModelAdmin):
    list_display = ['roolno','fname','lname','father_name','course','school_name','email']

class MarksDetailsAdmin(admin.ModelAdmin):
    list_display = ['Telugu','Hindi','English','Mathametics','NS','PS','Social']

admin.site.register(Post)
admin.site.register(MarksDetails,MarksDetailsAdmin)
admin.site.register(StudentRegister,StudentRegisterAdmin)
admin.site.register(ProxyStudentRegister,ProxyStudentRegisterAdmin)

