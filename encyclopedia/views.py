from turtle import title
from django.shortcuts import render, redirect
import markdown
from django import forms
from django.http import HttpRequest, HttpResponseRedirect
from re import search
import random
from . import util

# class for represting a form
class NewEntryForm(forms.Form):
    # create fields of the form
    title = forms.CharField(label="Page Title:")
    content = forms.CharField(label="Content of the page:", widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def newpage(request):
    # If user sumbmitted some data, put data inside form variable
    if request.method == "POST":
        newEntry = NewEntryForm(request.POST)
        if newEntry.is_valid():
            title = request.POST["title"]
            content = request.POST["content"]
            if title.lower() in (string.lower() for string in util.list_entries()):
                return render(
                    request,
                    "encyclopedia/newpage.html",
                    {
                        "errormsg": 'Error! \nAn entry with title "'
                        + title
                        + '" already exists.',
                        "form": newEntry,
                    },
                )
            else:
                util.save_entry(title, content)
                return redirect(entry, title=title)
        # if form is not valid, pass bback the form that they sumbitted
    return render(request, "encyclopedia/newpage.html", {"form": NewEntryForm})


def entry(request, title):
    if request.method == "POST":
        new_content = request.POST["content"]
        util.save_entry(title, new_content)
        return redirect(entry, title=title)
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    return render(
        request,
        "encyclopedia/entry.html",
        {
            "entry": markdown.markdown(util.get_entry(title)),
            "title": title,
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
                    "title": query,
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


def edit(request, title):
    # if request.method == "POST":
    #   new_content = request.POST["content"]
    #  util.save_entry(title, new_content)
    # return redirect(entry, title=title)
    return render(
        request,
        "encyclopedia/edit.html",
        {"title": title, "content": util.get_entry(title)},
    )
