from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse  
from django.template.loader import render_to_string
# Create your views here.
# def january(request):
#     return HttpResponse("this works!")

# def february(request):
#     return HttpResponse("go for a walk everyday")

monthly_challenges={
    "january": "Eat no meat everyday for entire month",
    "february": "Walk for at least 20 minutes everyday",
    "march": "Learn Django atleast for 20 min everyday",
    "april": "learn data science for at least half an hour everyday",
    "may": "go to the gym for at least 30 minutes everyday",
    "june": "eat only vegetables every friday for the whole month",
    "july": "read 1 thousand words everyday ",
    "august": " Sleep for 4 hour max",
    "september": "take the wife out for a date",
    "october": "Apply for new jobs everyday",
    "november": "spend every weekend with the children",
    "december": None
}


def index(request):
    # list_of_months = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     month_path = reverse("month-challenge", args=[month])
    # #     list_of_months += f"<ul><li><a href= \"{month_path}\">{month.capitalize()}</a></li></ul>"
    # return HttpResponse(list_of_months)
    return render(request, "challenges/index.html", {
        "months": months
    }, )
        
def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
    redirect_month = months[month- 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(f"<h1>{redirect_path}</h1>")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # return HttpResponse(f"<h1>{challenge_text.capitalize()}</h1>")
        # response_data = render_to_string("challenges/challenge.html") or we can use this below
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month.title()
        })
    except:
        # return HttpResponseNotFound("<h1>This month is not supported</h1>")
        response_data =  render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404()