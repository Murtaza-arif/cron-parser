valid_value_range = {
    'week': [i for i in range(0, 7)],
    'month': [i for i in range(1, 13)],
    'hour': [i for i in range(0, 24)],
    'day': [i for i in range(1, 32)],
    'minute': [i for i in range(0, 60)]
}


def handle_range(_exp, exp_type):
    start, end = _exp.split('-')
    try:
        start, end = int(start), int(end)
    except:
        raise Exception("Invalid values")
    return ' '.join([str(c) for c in valid_value_range[exp_type][start:end + 1]])


def handle_slash(_exp, exp_type):
    start, end = _exp.split('/')
    try:
        end = int(end)
    except:
        raise Exception("Invalid values")

    if start == "*":
        return ' '.join([str(c) for c in valid_value_range[exp_type] if c % end == 0])
    try:
        start = int(start)
    except:
        raise Exception("Invalid values")
    return ' '.join([str(c) for c in range(start, len(valid_value_range[exp_type]), end)])


def handle_list(_exp):
    inputs = _exp.split(",")
    return " ".join(inputs)


def parse_string(_exp, exp_type):
    # handle *
    if _exp == "*":
        return " ".join([str(c) for c in valid_value_range[exp_type]])

    if "-" in _exp:
        return handle_range(_exp, exp_type)

    if "/" in _exp:
        return handle_slash(_exp, exp_type)

    if "," in _exp:
        return handle_list(_exp)
    return _exp
