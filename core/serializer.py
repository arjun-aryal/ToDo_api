from rest_framework import serializers
from .models import Todo

class ToDoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    desciption = serializers.CharField()
    due_date = serializers.DateTimeField()
    status = serializers.ChoiceField(choices=Todo.STATUS_CHOICES,default='PENDING')
    priority = serializers.ChoiceField(choices=Todo.PRIORITY_CHOICES,default=1)


    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desciption = validated_data.get('desciption', instance.desciption)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)

        instance.save()

        return instance