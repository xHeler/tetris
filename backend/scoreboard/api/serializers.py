from rest_framework import serializers

from ..models import Score


class ScoreSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        fields = (
            'id',
            'author',
            'points',
            'edited_at',
        )
        model = Score
        
    def create(self, validated_data):
        user = self.context['request'].user
        
        if Score.objects.filter(author__username=user).exists():
            score = Score.objects.filter(author=user).first()
            if validated_data['points'] <= score.points:
                return score
            score.author = user
            score.points = validated_data['points']
            score.save()
            return score
        return Score.objects.create(author=user, points=validated_data['points'])
        