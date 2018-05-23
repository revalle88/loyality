from django.db import models

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	bdate = models.DateField('Date')

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)


