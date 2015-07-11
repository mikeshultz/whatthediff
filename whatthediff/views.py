from django.shortcuts import render_to_response

def home(rquest):
    "Homepage"
    return render_to_response("home.html", {})