from django.shortcuts import render

def index_view (request):
    return render(request, 'index.html')

def calculate_view(request):

    if request.method == 'GET':
        return render(request, 'calculate.html')
    elif request.method == 'POST':
        context = {
            'number1': request.POST.get('number1'),
            'number2': request.POST.get('number2'),
            'author': request.POST.get('author'),
            'operation': request.POST.get('operation'),
            'result': 0
        }
        if context['operation'] == 'add':
            context['result'] = int(context['number1']) + int(context['number2'])
            context['operation'] = '+'
        elif context['operation'] == 'subtraction':
            context['result'] = int(context['number1']) - int(context['number2'])
            context['operation'] = '-'
        elif context['operation'] == 'multiply':
            context['result'] = int(context['number1']) * int(context['number2'])
            context['operation'] = '*'
        else:
            if context['number1'] == '0':
                context['result'] = 'Invalid division.'
            else:
                context['result'] = round(int(context['number1']) / int(context['number2']), 3)
                context['operation'] = '/'

        return render(request, 'result.html', context)
