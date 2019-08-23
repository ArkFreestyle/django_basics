from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice
from .forms import BasicForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return HttpResponseRedirect after successfull POST data. 
        # This prevents data from being posted twice if user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def basic_form(request):
    
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            return render(request, 'polls/basic_form.html', {"form": form, "lat": form.cleaned_data["latitude"], "lng": form.cleaned_data["longitude"]})
    else:
        form = BasicForm()
    
    return render(request, 'polls/basic_form.html', {"form": form})


def basic_form2(request):
    
    print("\n------------------------------------------------------------------")
    print("request:", request)
    print("\nrequest.POST:", request.POST)
    print("\nrequest.body:", request.body)
    print("\nrequest.POST.keys()", request.POST.keys())
    print("\nrequest.POST.items()", request.POST.items())
    print("------------------------------------------------------------------")
    form = 0
    return render(request, 'polls/basic_form2.html', {"form": form})


def basic_form3(request):

    print("\nrequest.POST:", request.POST)

    return render(request, "polls/basic_form3.html")