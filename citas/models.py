from django.db import models
# Create your models here.

class Lugares(models.Model):
	Sujeto = models.CharField(max_length=50)
	

	def __str__(self):
		return self.Sujeto
    

class Critica_sitios(models.Model):
	opinion =models.CharField(max_length=400)
	calificacion = models.IntegerField(default=0)

	MASCULINO='Axel E González'
	FEMENINO= 'Bianca E Monroy'
	Type_CHOICES =(
		(MASCULINO, 'Axel E González'),
		(FEMENINO, 'Bianca E Monroy')
		)

	evaluador= models.CharField(choices=Type_CHOICES, default= FEMENINO, max_length=20)

	ya_visitado=models.BooleanField(default=False)
	
	lugar = models.ForeignKey(Lugares, on_delete=models.CASCADE)


	def __str__(self):

		return self.opinion


class Sitios_visitados(models.Model):
	a='Bianca todavia no realiza un comentario'
	b='Axel todavia no realiza un comentario'

	Lugar_que_visite=models.CharField(max_length=50)

	Comentario_Bianca=models.CharField(max_length=400, default=a)

	calificacion_Bianca=models.IntegerField(default=0)

	Comentario_Axel=models.CharField(max_length=400, default=b)

	calificacion_Axel=models.IntegerField(default=0)

	def __str__(self):

		return self.Lugar_que_visite
		
