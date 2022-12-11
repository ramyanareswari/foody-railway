from django.forms import ModelForm
from miniquiz.models import *

# (DONE) Create form.
class MiniQuizForm(ModelForm):
    class Meta :
        model = QuizModel
        fields = "__all__"