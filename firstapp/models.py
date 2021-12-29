from django.db import models

# Create your models here.
class studentdetails(models.Model):
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	gender=models.CharField(max_length=50)
	did=models.CharField(primary_key=True,max_length=50)
	course=models.CharField(max_length=50)

	class Meta:
		verbose_name="studentdetails"
		verbose_name_plural="studentdetails"

	def __str__(self):
		return self.name