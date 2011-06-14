from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=1024)
    date_added = models.DateTimeField('date added', auto_now_add=True)

    def __unicode__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=1024)
    date_added = models.DateTimeField('date added', auto_now_add=True)

    def __unicode__(self):
        return self.title

class LogEntry(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(Job, blank=True, null=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=1024)
    entry = models.TextField()
    date_created = models.DateTimeField('date created', auto_now_add=True)
    
    def __unicode__(self):
        return '%s, %s: %s' % (self.company.name, self.job.title, self.subject)

