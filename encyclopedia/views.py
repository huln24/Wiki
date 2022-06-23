from turtle import title
from django.shortcuts import render, redirect
import markdown
from django import forms
from django.http import HttpRequest, HttpResponseRedirect
from re import search
import random
from . import util

# class fore represting a form
class NewTaskForm(forms.Form):
    # create fields of the form
    search = forms.CharField()


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def newpage(request):
    return render(request, "encyclopedia/newpage.html")


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
        entries = util.list_entries()
        results = list()
        if query.lower() in (string.lower() for string in entries):
            return render(
                request,
                "encyclopedia/entry.html",
                {
                    "entry": markdown.markdown(util.get_entry(query)),
                    "title": query.capitalize(),
                },
            )
        for entry in entries:
            if search(query.lower(), entry.lower()):
                results.append(entry)
        return render(
            request, "encyclopedia/results.html", {"query": query, "results": results}
        )
    return HttpResponseRedirect(request.path_info)


def randompage(request):
    randomp = random.choice(util.list_entries())
    return redirect(entry, title=randomp)
