from django.http import HttpResponse

def index(request):
    return HttpResponse('Helllo Django by HttpResponse')
# 建立3個view
# detail => 你在哪一個問題頁面
# results => 查看問題的結果
# vote => 投票頁免

def detail(request, question_id):
    return HttpResponse(" you are looking at question %s" %question_id)

def results(request, question_id):
    return HttpResponse("you are looking at the result of question %s" %question_id)

def vote(request, question_id):
    return HttpResponse("you are vote  for question %s" %question_id)