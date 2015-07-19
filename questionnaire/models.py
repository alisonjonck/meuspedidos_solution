from django.db import models

class Candidate(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()

	html = models.IntegerField(null=True, blank=True)
	css = models.IntegerField(null=True, blank=True)
	javascript = models.IntegerField(null=True, blank=True)
	python = models.IntegerField(null=True, blank=True)
	django = models.IntegerField(null=True, blank=True)
	ios = models.IntegerField(null=True, blank=True)
	android = models.IntegerField(null=True, blank=True)