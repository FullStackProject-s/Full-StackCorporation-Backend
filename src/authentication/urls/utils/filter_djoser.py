def filtered_djoser_urls(urls: list) -> list:
    resulted_djoser_list_name = (
        'customuser-list',

        'customuser-activation',

        'customuser-reset-password',
        'customuser-reset-password-confirm'
    )
    return list(filter(
        lambda pattern: pattern.name in resulted_djoser_list_name, urls
    ))
