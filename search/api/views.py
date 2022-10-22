from rest_framework import generics
from ..models import Training
from ..query import query_elastic
from .serializers import TrainSerializer

class TrainList(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        if q is not None:
            return query_elastic(q)
        return super().get_queryset()