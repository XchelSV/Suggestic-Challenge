from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from .serializers import *
from .helpers import flattener
from .models import Sequence

# Create your views here.
class FlattnesSequenceView(APIView):

    def post(self, request):
        try:
            serializer = FlattnesSequenceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            result = flattener(serializer.validated_data['sequence'])
            sequence_record = Sequence.objects.create(
                value=result,
            )
            return Response({"result": result}, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response({"result": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"result": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FlattnesSequenceListView(ListAPIView):
    serializer_class = FlattnesSequenceListSerializer
    def get_queryset(self):
        return Sequence.objects.all()
