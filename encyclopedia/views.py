from django.shortcuts import render
import markdown


from . import util


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
