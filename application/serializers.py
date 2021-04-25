from rest_framework import serializers
from .models import Answer, Response, Question, QuizTakers, Quiz


class QuizTakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTakers
        fields = '__all__'
        read_only_fields = ('__all__',)


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text')


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()

    def get_choices(self, obj):
        ordered_queryset = Answer.objects.filter(id=obj.id).order_by('?')
        return ChoiceSerializer(ordered_queryset, many=True, context=self.context).data

    class Meta:
        model = Question
        fields = ('label', 'choices')
