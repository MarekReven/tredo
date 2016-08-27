# -*- coding: utf-8 -*-
from django.shortcuts import render
from tredo.forms import EmailForm
from django.utils.encoding import smart_str
from django.core.mail import EmailMessage

def index(request):

    print('start')
    if request.method == 'POST':
        print('1')
        email_form = EmailForm(data=request.POST)
        print(request.POST)
        print('2')
        print(email_form.data)
        if email_form.is_valid():
            print('3')
            email = email_form.save()
            print('4')
            email_to_send = EmailMessage('{0}'.format("Masz nowy email z Tredo.net"),
                                         'Imie i nazwisko: {0}\n\nEmail: {1}\n\nWiadomosc: {2}'.format(smart_str(email.name), smart_str(email.email), smart_str(email.message)),
                                         to=['some_email'])
            print('5')
            email_to_send.send()
            print('Udalo sie')
        else:
            print email_form.errors, email_form.errors

    else:
        print('else')
        email_form = EmailForm()

    return render(request,
                  'tredo/index.html',
                  {'email_form': email_form})

