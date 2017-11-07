def strTimeToSecond(time):
    time_list = time.split(':')
    return float(time_list.pop()) + int(time_list.pop()) * 60 + int(time_list.pop()) * 3600


def cell(line_table):
    list_line = line_table.split(',')
    time = strTimeToSecond(list_line[0])
    exchange = list_line[3][0]
    append_trade(time, exchange)


trades = {'V': [], 'D': [], 'X': [], 'Y': [], 'B': [], 'J': [], 'Q': [], 'Z': [], 'K': [], 'P': [], 'All': []}
max = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
times = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}


def append_trade(time, exchange):
    trades[exchange].append(time)
    while time - trades[exchange][0] >= 1:
        trades[exchange].pop(0)
    if len(trades[exchange]) > max[exchange]:
        max[exchange] = len(trades[exchange])
        times[exchange] = trades[exchange][0]
    if exchange != 'All':
        exchange = 'All'
        append_trade(time, exchange)


def secondToStrTime(time):
    zero_minutes = ''
    zero_hours = ''
    zero_seconds = ''
    hour = int(time // 3600)
    time -= hour * 3600
    minutes = int(time // 60)
    seconds = int((time - minutes * 60) * 1000) / 1000
    if hour < 10: zero_hours = '0'
    if minutes < 10: zero_minutes = '0'
    if seconds < 10: zero_seconds = '0'
    return zero_hours + str(hour) + ':' + zero_minutes + str(minutes) + ':' + zero_seconds + str(seconds)


def output():
    print('Алгоритм проходит один раз по таблице, а так же линейно проверяет списки временных промежутков на разницу '
          'времени\n=> сложность алгоритма: O(n)')
    for a in max:
        space = '  '
        if a == 'All': space = ''
        print(a + ':', space + str(max[a]), ' ' * (4 - len(str(max[a]))) + secondToStrTime(times[a]))


with open("TRD2.csv") as f:
    f.readline()
    for line in f.readlines():
        cell(line)
output()
