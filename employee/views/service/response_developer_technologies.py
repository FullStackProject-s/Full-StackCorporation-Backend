from general import PostResponse


def developer_technologies_response(tech_list, message):
    if tech_list:
        return PostResponse.response_ok(
            message
        )
    return PostResponse.not_found_response('Tech\'s not found')
