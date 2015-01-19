#encoding: utf-8
from clase.models import Clase, ClaseAlumno
from clase.serializers import ClaseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.http import HttpResponse, JsonResponse
from rest_framework import status

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

class ClaseCalificar(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, id_clase, matricula, format=None):
        try:
        	clase = Clase.objects.get(id=id_clase)
        	alumno_clase = ClaseAlumno.objects.get(clase=clase, alumno__enrollment=matricula)
        	serializer = ClaseSerializer(clase, context={'calificacion': alumno_clase.calificacion,
        	 'comentario': alumno_clase.comentario})
        	info = serializer.data
        	status_code = status.HTTP_200_OK
        except (Clase.DoesNotExist, ClaseAlumno.DoesNotExist) as e: 
        	info = u"Matrícula o número de clase incorrecto."
        	status_code = status.HTTP_404_NOT_FOUND
        data = {"data":info, "status_code":  status_code}
        response = JsonResponse(data=data)
        response.status_code = status_code
        return response

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)