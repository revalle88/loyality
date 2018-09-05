from django.db import models

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	bdate = models.DateField('Date')
	card = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	#check = models.CharField(max_length=50, unique=True)
	summ = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
	city = models.CharField(max_length=50,blank=True)
	street = models.CharField(max_length=250,blank=True)
	email = models.EmailField(max_length=70,blank=True)

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	card = models.CharField(max_length=50)
	check = models.CharField(max_length=50, unique=True)
	summ = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
	date = models.DateField('Date')



	class Meta:
		verbose_name = "Order"
		verbose_name_plural = "Orders"

	def __unicode__(self):
		return '%s %s' % (self.card, self.summ)


