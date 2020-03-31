
def args_to_kwargs(params: list, separator: str) -> dict:
    kwargs = {}
    for param in params:
        assert param.count('=') == 1
        key, value = param.split('=')
        value = eval(value) if is_evaluable(value) else value
        kwargs.update({key: value})
    return kwargs


def is_evaluable(value):
    try:
        eval(value)
        return True
    except Exception:
        return False
