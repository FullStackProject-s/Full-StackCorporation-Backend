def preprocessing_filter_elastic(endpoints):
    return [
        (path, path_regex, method, callback)
        for (path, path_regex, method, callback) in endpoints
        if '/documents/' not in path
     ]
