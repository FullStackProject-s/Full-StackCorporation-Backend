def preprocessing_filter_spec(endpoints):
    filtered = []
    for (path, path_regex, method, callback) in endpoints:
        if not path.startswith("/auth/"):
            filtered.append((path, path_regex, method, callback))
    return filtered
