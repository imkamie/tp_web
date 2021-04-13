from django.shortcuts import render

from django.shortcuts import render

questions = [
    {
        'id': idx,
        'title': f'Title number {idx}',
        'text': f'Some text for question #{idx}'
    } for idx in range(10)
]

def index(request):
    return render(request, 'index.html', {'questions': questions})

def hot_questions(request):
  return render(request, 'hot_questions.html', {'questions': questions})

def question(request, pk):
  question = questions[pk]
  return render(request, 'question.html', {"question": question})

def ask(request):
  return render(request, 'ask.html', {})

# def question(request):
#   return render(request, 'question.html', {})

def tag(request):
  return render(request, 'tag.html', {})

def settings(request):
  return render(request, 'settings.html', {})

def login(request):
  return render(request, 'login.html', {})

def signup(request):
  return render(request, 'signup.html', {})
