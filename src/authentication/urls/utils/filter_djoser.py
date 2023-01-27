def filtered_djoser_urls(urls: list) -> list:
    """
    Function for filter djoser urls, return new list with only need urls.
    """
    resulted_djoser_list_name = (
        'customuser-list',

        'customuser-activation',

        'customuser-reset-password',
        'customuser-reset-password-confirm'
    )
    return list(filter(
        lambda pattern: pattern.name in resulted_djoser_list_name, urls
    ))
