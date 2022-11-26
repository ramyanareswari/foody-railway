from django.contrib import admin
from miniquiz.models import *

admin.site.register(ResultModel)
admin.site.register(QuizModel)

class AnswerInLine(admin.TabularInline):
    model = AnswerModel

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]

admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(AnswerModel)
