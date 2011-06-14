from django.contrib import admin
from reversion.admin import VersionAdmin

from joblog.models import LogEntry, Job, Company

class LogEntryAdmin(VersionAdmin):
    """"""

class JobAdmin(VersionAdmin):
    """"""

class CompanyAdmin(VersionAdmin):
    """"""

admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
