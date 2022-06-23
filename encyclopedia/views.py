from django.shortcuts import render
import markdown
from django import forms
from django.http import HttpResponse, HttpRequest

from . import util

# class fore represting a form
class NewTaskForm(forms.Form):
    # create fields of the form
    search = forms.CharField()


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    return render(
        request,
        "encyclopedia/entry.html",
        {
            "entry": markdown.markdown(util.get_entry(title)),
            "title": title.capitalize(),
        },
    )


def result(request: HttpRequest):
    if request.method == "POST":
        query = request.POST["q"]
