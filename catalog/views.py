from django.shortcuts import render


def home(requests):
    return render(requests, "home.html")


def contacts(requests):
    return render(requests, "contacts.html")
