from django.contrib import admin

from .models import Answer, Question, Quiz, QuizTakers, Response

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(QuizTakers)
admin.site.register(Response)
