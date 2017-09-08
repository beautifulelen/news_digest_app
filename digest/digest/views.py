from rest_framework import mixins, viewsets
from .models import News, Category, Job, Search
from .serializers import NewsSerializer, CategorySerializer, JobSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class NewsViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows new to be viewed or created.
    """
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer
    parser_classes = (JSONParser,)


class SearchView(APIView):

    def post(self, request):
        search, create = Search.objects.get_or_create(param=request.data)
        qs = search.filter_news()
        ns = NewsSerializer(qs, many=True, context={'request': request})
        return Response(ns.data)


class SearchDetailView(APIView):

    def post(self, request, pk, format=None):
        job_send = Job(type='send_email',
                       status='pending',
                       kwargs={'email': request.data['email'],
                                'pk': pk,})
        job_send.save()
        return Response(status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or created.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class JobViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    API endpoint that allows jobs to be viewed or created.
    """
    queryset = Job.objects.all().order_by('-updated_at')[:10]
    serializer_class = JobSerializer
