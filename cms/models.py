from django.db import models


class Paper(models.Model):
    title = models.CharField('Title', max_length=1023)
    authors = models.CharField('Authors', max_length=1023, blank=True)
    references = models.CharField('References', max_length=1023, blank=True)
    pages = models.CharField('Pages', blank=True, max_length=255)
    year = models.IntegerField('Year',blank=True, default = 0)
    URL = models.CharField('URL', max_length=1023, blank=True)
    abstract = models.TextField('Abstract', blank=True)
    reading = models.CharField('Reading',blank=True, max_length=255)
    note = models.CharField('Note',blank=True, max_length=255)
    def __str__(self):
        return self.title

class Report(models.Model):
    paper = models.ForeignKey(Paper,verbose_name='Paper',related_name='reports')
    reporter = models.CharField('Reporter', max_length=255)
    grade = models.CharField('Grade', max_length=32, blank=True)
    date = models.CharField('Date', max_length=255)
    motivations = models.TextField('Motivations', blank=True)
    contributions = models.TextField('Contributions', blank=True)
    questions = models.TextField('Questions and Future works', blank=True)
    def __str__(self):
        return self.motivations
