from django.contrib.auth import get_user_model

from djoser.email import (
    PasswordResetEmail,
    ActivationEmail,
    PasswordChangedConfirmationEmail
)
from core.celery import app

User = get_user_model()


@app.task(bind=True, default_retry_delay=5 * 60)
def send_reset_password_email(
        self,
        context: dict,
        email: list[str]
):
    try:
        context['user'] = User.objects.get(id=context.get('user_id'))
        PasswordResetEmail(context=context).send(email)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, default_retry_delay=5 * 60)
def send_reset_password_confirmation_email(
        self,
        context: dict,
        email: list[str]
):
    try:
        context['user'] = User.objects.get(id=context.get('user_id'))
        PasswordChangedConfirmationEmail(context=context).send(email)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, default_retry_delay=5 * 60)
def send_activation_user_email(
        self,
        context: dict,
        email: list[str]
):
    try:
        context['user'] = User.objects.get(id=context.get('user_id'))
        ActivationEmail(context=context).send(email)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
