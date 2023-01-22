from djoser import email


class ActivationOverrideEmail(email.ActivationEmail):
    template_name = 'email/activation.html'


class ActivationConfirmationOverrideEmail(email.ConfirmationEmail):
    template_name = 'email/confirmation.html'


class PasswordResetOverrideEmail(email.PasswordResetEmail):
    template_name = 'email/password_reset.html'


class PasswordChangedConfirmationOverrideEmail(
    email.PasswordChangedConfirmationEmail
):
    template_name = 'email/password_changed_confirmation.html'
