from djoser.urls import urlpatterns as urls


def filtered_djoser_urls() -> list:
    resulted_djoser_list = (
        'customuser-activation',
        'customuser-resend-activation',

        'customuser-reset-password',
        'customuser-reset-password-confirm'
    )
    return list(filter(
        lambda pattern: pattern.name in resulted_djoser_list, urls
    ))
