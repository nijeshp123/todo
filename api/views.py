from multiprocessing import managers
from django.shortcuts import render

from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.models import Todos
from api.serializers import TodoSerializer,RegistrationSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User

class TodosView(ViewSet):
    def list(self,request,*args,**Kw):
        qs=Todos.objects.all()
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kw):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kw):
        id=kw.get("pk")
        qs=Todos.objects.get(id=id)
        serializer=TodoSerializer(qs,many=False)
        return Response(data=serializer.data)
    def destroy(self,request,*args,**kw):
        id=kw.get("pk")
        Todos.objects.get(id=id).delete()
        return Response(data="deleted")
    
    def update(self,request,*args,**kw):
        id=kw.get("pk")
        object=Todos.objects.get(id=id)
        serializer=TodoSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    


# localhost:8000/api/v1/todos/pending_todos/
# get

# # localhost:8000/api/v1/todos/completed_todos/
#get


# localhost:8000/api/v1/todos/2/mark_as_done/
#post
 

class TodosModelViews(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()

    @action(methods=["GET"],detail=False)
    def pending_todos(self,request,*args,**kw):
        qs=Todos.objects.filter(status=False)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    @action(methods=["GET"],detail=False)
    def completed_tods(self,request,*args,**kw):
        qs=Todos.objects.filter(status=True)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)

    @action(methods=["post"],detail=True)
    def mark_as_done(self,request,*args,**kw):
        id=kw.get("pk")
        # Todos.objects.filter(id=id).update(status=True)
        object=Todos.objects.get(id=id)
        object.status=True
        object.save()
        serializer=TodoSerializer(object,many=False)
        return Response(data=serializer.data)
        
class UsersView(ModelViewSet):
    
    serializer_class=RegistrationSerializer
    queryset=User.objects.all()

    # def create(self,request,*args,**kw):
    #     serializer=RegistrationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         User.objects.create_user(**serializer.validated_data)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)




