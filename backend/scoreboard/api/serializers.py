from rest_framework import serializers

from ..models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'author',
            'points',
            'edited_at',
        )
        model = Score
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        
        if user.pk != instance.author.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        
        instance.author = validated_data['author']
        instance.points = validated_data['points']
        instance.save()
        return instance