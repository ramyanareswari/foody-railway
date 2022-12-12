from miniquiz.models import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# View main page to start quiz
def show_quiz_homepage(request):
    quiz = QuizModel.objects.all()
    return render(request, 'main.html', {'quizs' : quiz})

def get_quiz_model(request):
    quiz = QuizModel.objects.all()
   
    data = serializers.serialize('json', quiz)

    return HttpResponse(data, content_type='application/json')

def get_quiz_beneran(request, pk:int):
    quiz = QuizModel.objects.get(pk = pk)

    ls = []
    dc = {}

    dc["name"] = quiz.name
    dc["number_of_question"] = quiz.number_of_questions
    dc["required_score_to_pass"] = quiz.required_score_to_pass

    ls.append(dc)

    jsonStr = json.dumps(ls)

    # Return JsonResponse
    return HttpResponse(jsonStr, content_type='application/json')

def get_question(request, pk:int):

    # Getting all quiz object
    quiz = QuizModel.objects.get(pk=pk)

    # Variable for accomodate question text
    questions = []

    # Looping questions
    for q in quiz.get_questions():
   
        # Append question to the list
        questions.append({"question" : str(q), "pk" : q.pk})

    jsonStr = json.dumps(questions)

    # Return JsonResponse
    return HttpResponse(jsonStr, content_type='application/json')

def get_option(request, pk: int, pk2: int) :

    questions = QuestionModel.objects.get(pk=pk2)
 
    # Variable for accomodate question text
    answers = []

    # Looping questions
    for q in questions.get_answers():
        answers.append({"answer" : q.text, "point" : q.point, "correct" : q.correct, "pk" : q.pk, "question" : q.question.pk})
    
    jsonStr = json.dumps(answers)

    # Return JsonResponse
    return HttpResponse(jsonStr, content_type='application/json')

def save_assessment(request, pk: int):

    if request.method == "POST" :
        user_answers = json.loads(request.body)["answers"]

        ls = json.loads(request.body)["user"]
        user_username = ""
        if len(ls) > 0:
            user_username = ls[0]

        quiz = QuizModel.objects.get(pk = pk)
        questions = quiz.get_questions()

        score = 0
        full_score = 0
        result = []
        inc = 0
        lulus = False

        for q in questions:
            option = q.get_answers()
            result.append({})
            max_score = 0
            truth = False

            for o in option:
                if o.text == user_answers[inc]:
                    score += o.poin

                    if o.correct :
                        truth = True
                
                if o.poin > max_score :
                    max_score = o.poin
            
            full_score += max_score

            result[inc]['question'] = q.text
            result[inc]['answer'] = user_answers[inc]
            result[inc]['truth'] = truth 
            result[inc]['correct'] = truth 

            inc = inc+1

        presentase = 0
        
        if (full_score == 0) :
            presentase = 0
        else :
            presentase = round(score/full_score *100, 2)
        

        if presentase >= quiz.required_score_to_pass :
            lulus = True

        final_result = [{"quiz" : quiz.name, "score_to_pass" : quiz.required_score_to_pass , "score" : presentase, "lulus" : lulus, "result" : result}]
        
        jsonStr = json.dumps(final_result)

        user = User.objects.get(username = user_username)
        ResultModel.objects.create(quiz=quiz, user=user, score=presentase)

        # Return JsonResponse
        return HttpResponse(jsonStr, content_type='application/json')
    
    return HttpResponse("")

@login_required(login_url='/login/')
# View quiz page to start the quiz
def show_quiz_mainpage(request, pk:int):
    quiz = QuizModel.objects.get(pk = pk)
    return render(request, 'quiz.html', {'obj': quiz})

@login_required(login_url='/login/')
# View quiz questions and answers in json format
def quiz_data_view(request, pk: int):
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