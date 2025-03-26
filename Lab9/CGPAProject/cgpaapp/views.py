from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def calculate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        total_marks = request.POST.get('total_marks')

        if name and total_marks.isdigit():
            cgpa = int(total_marks) / 50

            # Store in session
            request.session['name'] = name
            request.session['cgpa'] = cgpa

            return redirect('result')

    return redirect('index')

def result(request):
    name = request.session.get('name', 'Student')
    cgpa = request.session.get('cgpa', 0)

    return render(request, 'cgpaapp/result.html', {'name': name, 'cgpa': cgpa})
