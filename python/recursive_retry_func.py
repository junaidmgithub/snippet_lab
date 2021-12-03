def recursive_retry_func(*args, **kwargs):
    try:
        value = args[0] / args[1]
        print("try Worked", value)
    except Exception as e:
        print("except block worked")
        if kwargs.get('ESCAPE_FLAG', None):
            return None
        kwargs['ESCAPE_FLAG'] = True
        recursive_retry_func(5, 2, **kwargs)

recursive_retry_func(1, 0)
