from django.forms import ModelForm
from miniquiz.models import *

# (DONE) Create form.
# jadi redundant forms-nya cokkkk
class MiniQuizForm(ModelForm):
    class Meta :
        model = QuizModel
        fields = "__all__"