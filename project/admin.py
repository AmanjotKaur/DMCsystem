from project.models import Student_info
from django.contrib import admin
from project.models import Certificate

class Student_infoAdmin(admin.ModelAdmin):
	list_display = ('Roll_Number', 'Name','Branch','Father_name','Date_of_birth') 
	#list_filter = ['Roll_Number']
	search_fields = ['Roll_Number']
class CertificateAdmin(admin.ModelAdmin):
	list_display=('dmc_number','Semester','Year_of_passing','Obtained_marks','Maximum_marks','Received')
#class CertificateInline(admin.StackedInline):
	#model = Certificate
	
admin.site.register(Student_info, Student_infoAdmin)
admin.site.register(Certificate,CertificateAdmin)

