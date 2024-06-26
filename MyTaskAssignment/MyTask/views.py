
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .filters import TaskFilter
from .models import Task
from .serializers import TaskSerializer

class TaskPagination(PageNumberPagination):
    # setting the number of items in each page like it will show 10 items only  
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 50  

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['create_time', 'updated_time']
    search_fields = ['name', 'category']
    filterset_class = TaskFilter
    pagination_class = TaskPagination  


#end
# Create your views here.
# def home(request):
#     return HttpResponse("Hello World")
