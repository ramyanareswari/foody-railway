from miniquiz.models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from homepage.views import login_user

# View main page to start quiz
def show_quiz_homepage(request):
    quiz = QuizModel.objects.all()
    return render(request, 'main.html', {'quizs' : quiz})

@login_required(login_url='/login/')
# View quiz page to start the quiz
def show_quiz_mainpage(request, pk):
    quiz = QuizModel.objects.get(pk = pk)
    return render(request, 'quiz.html', {'obj': quiz})

@login_required(login_url='/login/')
# View quiz questions and answers in json format
def show_quiz_json(request, pk):
    quiz = QuizModel.objects.get(pk = pk)
    questions = []

    for q in quiz.get_questions():
        answers = []

        for a in q.get_answers():
            answers.append(a.text)

        questions.append({str(q): answers})
    
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

# To check request is ajax
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required(login_url='/login/')
# Save the quiz and view the result
def save_quiz(request, pk):
    questions = []
    if is_ajax(request):
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = QuestionModel.objects.get(text=k)
            questions.append(question)
    print(questions)

    user = request.user
    quiz = QuizModel.objects.get(pk=pk)

    score = 0
    multiplier = 100 / 5
    results = []
    correct_answer = None

    for q in questions:
        a_selected = request.POST.get(q.text)

        if a_selected != "":
            question_answers = AnswerModel.objects.filter(question=q)
            for a in question_answers:
                if a_selected == a.text:
                    if a.correct:
                        score += 1
                        correct_answer = a.text
                else:
                    if a.correct:
                        correct_answer = a.text

            results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
        else:
            results.append({str(q): 'not answered'})
        
    score_ = float(score * multiplier)
    ResultModel.objects.create(quiz=quiz, user=user, score=score_)

    if score_ >= quiz.required_score_to_pass:
        return JsonResponse({'passed': True, 'score': score_, 'results': results})
    else:
        return JsonResponse({'passed': False, 'score': score_, 'results': results})