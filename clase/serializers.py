from django.forms import widgets
from rest_framework import serializers
from clase.models import Clase, ClaseAlumno


class ClaseSerializer(serializers.ModelSerializer):
	profesor = serializers.SerializerMethodField()
	empieza = serializers.SerializerMethodField()
	termina = serializers.SerializerMethodField()
	calificacion = serializers.SerializerMethodField()
	comentario = serializers.SerializerMethodField()
	
	class Meta:
		fields = ('id','profesor', 'termina', 'empieza', 'calificacion', 'comentario')
		model = Clase

	def get_profesor(self, obj):
		return obj.profesor.get_full_name()

	def get_empieza(self, obj):
		return obj.empieza.strftime('%d/%m/%Y %H:%M')

	def get_termina(self, obj):
		return obj.termina.strftime('%d/%m/%Y %H:%M')

	def get_calificacion(self, obj):
		return self.context['calificacion']

	def get_comentario(self, obj):
		return self.context['comentario']
