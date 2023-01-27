from django.contrib.auth import get_user_model

from general.email import (
    PasswordResetOverrideEmail,
    ActivationOverrideEmail,
    ActivationConfirmationOverrideEmail,
    PasswordChangedConfirmationOverrideEmail
)

from core.celery import app

User = get_user_model()


@app.task(bind=True, default_retry_delay=5 * 60, max_retries=5)
def send_activation_user_email(
        self,
        context: dict,
        email: list[str]
):
    """
    Task for sending activation email when user created.
    """
    try:
        context['user'] = User.objects.get(id=context.get('user_id'))
        ActivationOverrideEmail(context=context).send(email)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, default_retry_delay=5 * 60, max_retries=5)
def send_activation_confirmation_user_email(
        self,
        context: dict,
        email: list[str]
):
    """
    Task for sending confirmation email, when user confirm her active status.
    """
    try:
        context['user'] = User.objects.get(id=context.get('user_id'))
        ActivationConfirmationOverrideEmail(context=context).send(email)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, default_retry_delay=5 * 60, max_retries=5)
def send_reset_password_email(
        self,
        context: dict,
        email: list[str]
):
    """
    Task for sending reset password email, when user forget her password and
    want reset him.
    """
    try:
        context['user'] = User.objects.get(id=context.get('user_id'))
        PasswordResetOverrideEmail(context=context).send(email)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task(bind=True, default_retry_delay=5 * 60, max_retries=5)
def send_reset_password_confirmation_email(
        self,
        context: dict,
        email: list[str]
):
    """
    Task for sending confirmation email, after reset user password.
    """
    try:
        context['user'] = User.objects.get(id=context.get('user_id'))
        PasswordChangedConfirmationOverrideEmail(context=context).send(email)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
