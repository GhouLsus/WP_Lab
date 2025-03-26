from django.shortcuts import render, redirect
from .models import Vote
from django.db.models import Count

def vote(request):
    if request.method == "POST":
        choice = request.POST.get('choice')
        if choice:
            Vote.objects.create(choice=choice)
        return redirect('results')

    return render(request, 'voteapp/vote.html')

def results(request):
    total_votes = Vote.objects.count()
    if total_votes == 0:
        percentages = {'Good': 0, 'Satisfactory': 0, 'Bad': 0}
    else:
        votes_count = Vote.objects.values('choice').annotate(count=Count('choice'))
        percentages = {v['choice']: round((v['count'] / total_votes) * 100, 2) for v in votes_count}

    return render(request, 'voteapp/results.html', {'percentages': percentages})
