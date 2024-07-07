import secrets
import string

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm, UserRecoveryForm
from users.models import User
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject='Подтверждение аккаунта',
            message=f'Для подтверждения аккаунта перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def generate_password():
    character = string.ascii_letters + string.digits
    password = "".join(secrets.choice(character) for i in range(10))
    return password


class UserPasswordResetView(PasswordResetView):
    form_class = UserRecoveryForm
    template_name = 'users/recovery_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if self.request.method == 'POST':
            user_email = self.request.POST.get('email')
            user = User.objects.filter(email=user_email).first()
            if user:
                new_password = generate_password()
                user.set_password(new_password)
                user.save()
                send_mail(
                        subject="Восстановление пароля",
                        message=f"Здравствуйте! Ваш пароль для доступа на наш сайт изменен:\n"
                                f"Данные для входа:\n"
                                f"Email: {user_email}\n"
                                f"Пароль: {new_password}",
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[user.email]
                    )
                return HttpResponseRedirect(reverse('users:login'))
