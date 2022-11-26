from django.db import models
from django.contrib.auth.models import User

# Model for Mini Quiz object.
class QuizModel(models.Model):

    # Attributes.
    name = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="durations of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="minimum score to pass")

    # String function.
    def __str__(self):
        return f"{self.name}"

    # Function to get all questions.
    def get_questions(self):
        return self.questions.all()[:self.number_of_questions]


# Model for questions.
class QuestionModel(models.Model):

    # Attributes.
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name="questions")
    created = models.DateTimeField(auto_now_add=True)

    # String function.
    def __str__(self):
        return str(self.text)

    # Function to get all answers.
    def get_answers(self):
        return self.answers.all()


# Model for answers.
class AnswerModel(models.Model):

    # Attributes.
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name="answers")
    created = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField()

    # String function.
    def __str__(self):
        return f"question : {self.question.text} | answer : {self.text} | correct : {self.correct}"


# Model for result.
class ResultModel(models.Model):

    # Attributes.
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    # String function.
    def __str__(self):
        return str(self.pk)