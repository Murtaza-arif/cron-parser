from cron_parser import parse_string
from sys import argv


def handle_exp(_exp):
    try:
        minute, hour, day, month, week, cmd = _exp.split(" ")
    except:
        raise Exception('arguments error')

    return '\n'.join([
        "minute: {}".format(parse_string(minute, 'minute')),
        "hour: {}".format(parse_string(hour, 'hour')),
        "day of month: {}".format(parse_string(day, 'day')),
        "month: {}".format(parse_string(month, 'month')),
        "day of week: {}".format(parse_string(week, 'week')),
        "command: {}".format(cmd)
    ])


if __name__ == '__main__':
    print(handle_exp(argv[1]))
