from rest_framework.views import APIView
from .serializer import ToDoSerializer
from rest_framework.response import Response
from rest_framework import status
from.models import Todo
from django.shortcuts import get_object_or_404
from rest_framework import generics



# class TodoListCreateAPIView(APIView):
#     def get(self,request):
#         todos = Todo.objects.all()
#         serializer = ToDoSerializer(todos,many=True)

#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ToDoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class TodoDetailAPIView(APIView):

#     def get_object(self,pk):
#         return get_object_or_404(Todo,pk=pk)
    
#     def get(self,request,pk):
#         todo = self.get_object(pk)
#         serializer = ToDoSerializer(todo)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         todo = self.get_object(pk)
#         serializer = ToDoSerializer(todo,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#     def patch(self,request,pk):
#         todo = self.get_object(pk)
#         serializer= ToDoSerializer(todo,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#     def delete(self,request,pk):
#         todo = self.get_object(pk)
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()

class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()
    lookup_field = "pk" # default