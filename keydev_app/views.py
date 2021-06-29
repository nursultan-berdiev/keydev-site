from django.shortcuts import render
from .models import Messages
from django.core.mail import EmailMessage
from django.contrib import messages
import sweetify
from django.http import HttpResponseRedirect
from .message_text import message_text


# Create your views here.
def index(request):
    model = Messages

    def verbose(str):
        v_name = model._meta.get_field(str).verbose_name.title()
        return v_name

    context = {
        'name': verbose('name'),
        'email': verbose('email'),
        'phone': verbose('phone'),
        'message': verbose('message')
    }

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        message_to_database = model(name=name, email=email, phone=phone, message=message)
        message_to_database.save()

        mail_list = ['info@keydev.org.kg', email]
        msg = EmailMessage(
            name,
            message_text(name, email, phone, message),
            'site@keydev.org.kg',
            mail_list
        )  # Отправка сообщения на почту
        msg.content_subtype = "html"
        msg.send()

        sweetify.success(request, 'Отправлено!', text='Уважаемый, {} Спасибо большое за Ваше обращение'.format(name),
                         persistent='Вернуться', icon='success')
        return HttpResponseRedirect('/')
    else:
        pass

    return render(request, 'keydev_app/index.html', context)
