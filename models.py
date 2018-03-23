from django.db import models



# Create your models here.


class Office(models.Model):
        id_number=models.CharField(max_length=255)
	department=models.CharField(max_length=255)
	status=models.CharField(max_length = 255)
	remarks=models.TextField()
	certificate_type=models.CharField(max_length = 255)
	def __str__(self):
		return self.id_number +","+ self.department

class File(models.Model):
	name = models.CharField(max_length = 255)
	path = models.TextField()
	def __str__(self):
		return self.path

class Office_final(models.Model):
        id_number=models.CharField(max_length=255)
	department=models.CharField(max_length=255)
	final_status=models.CharField(max_length = 255)
	remarks=models.TextField()
	certificate_type=models.CharField(max_length = 255)
	pc=models.ForeignKey(File, related_name = "pc")
	marks_memos=models.ForeignKey(File, related_name = "marks_memo")
	study=models.ForeignKey(File, related_name = "study")
	def __str__(self):
		return self.id_number +","+ self.department

