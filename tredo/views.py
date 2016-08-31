# -*- coding: utf-8 -*-
from django.shortcuts import render
from tredo.forms import EmailForm
from django.utils.encoding import smart_str
from django.core.mail import EmailMessage

def index(request):

    if request.method == 'POST':
        email_form = EmailForm(data=request.POST)

        if email_form.is_valid():
            email = email_form.save()
            email_to_send = EmailMessage('{0}'.format("Masz nowy email z Tredo.net"),
                                         'Imie i nazwisko: {0}\n\nEmail: {1}\n\nWiadomosc: {2}'.format(smart_str(email.name), smart_str(email.email), smart_str(email.message)),
                                         to=['receiver_email'])
            email_to_send.send()
            message_sent = 'Twoja wiadomość została wysłana, dziękuję za kontakt.'
            context_dict = {'email_form': email_form, 'message_sent': message_sent}

        else:
            print email_form.errors, email_form.errors
            message_not_sent = 'Niestety wysłanie wiadomości nie powiodło się, proszę o kontakt telefoniczny.'
            context_dict = {'email_form': email_form, 'message_not_sent': message_not_sent}

    else:
        print('else')
        email_form = EmailForm()
        context_dict = {'email_form': email_form}

    return render(request, 'tredo/index.html', context_dict)

