from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse     #To dynamic redirect way

# Create your views here.
#def home(request):
#    return render(request, 'app_main/pages/home.html')     #Função para chamada de um arquivo html, note o caminho
                                                           #que tem como base a pasta template.

monthly_dic = {
    "january": "This works",
    "february": "Walk at least 20 min every day",
    "march": "Go to gyn every day",
    "april": "Don't forget of learning Django"
}

def index(request):
    months = list(monthly_dic.keys())  #Return a list of dict keys
    list_items = ""

    for i in months:
        captalized_month = i.capitalize()
        month_path = reverse("month-challenge-path", args=[i])
        list_items += f"<li><a href=\"{month_path}\">{captalized_month}</li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        monthly_text = monthly_dic[month]
        return render(request, "app_main/pages/challenge.html", {
            "text": monthly_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("Nothing to say")


def monthly_challenges_by_number(request, month):
    months = list(monthly_dic.keys())  #Return a list of dict keys
    if (month > len(months) or (month < 1)):
        return HttpResponseNotFound("Invalid number of month.")
    else:
        redirect_month = months[month - 1]  #Return a month name
#        return HttpResponseRedirect("/challenges/" + redirect_month)  #Redirect to real URL
        redirect_path = reverse("month-challenge-path", args=[redirect_month])  #Same that "/challenges/" + redirect_month, using the name of path
        return HttpResponseRedirect(redirect_path)
