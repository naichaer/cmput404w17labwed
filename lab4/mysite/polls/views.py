from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request,'polls/detail.html',context)

def results(request,question_id):
	#response= "You're looking at the results of question %s."
	#return HttpResponse(response % question_id)
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request,'polls/results.html',context)

def vote(request,question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
		    'question': p,
		    'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
