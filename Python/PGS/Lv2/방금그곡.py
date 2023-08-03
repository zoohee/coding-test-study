# 시간복잡도: 
# 최악시간: 
# 난이도: Lv2
# Url: https://school.programmers.co.kr/learn/courses/30/lessons/17683#
# Reference: Me, time -> GPT
from datetime import datetime, timedelta
def calculate_time(time1, time2):
    time_format = "%H:%M"
    datetime1 = datetime.strptime(time1, time_format)
    datetime2 = datetime.strptime(time2, time_format)
    time_difference = datetime2 - datetime1
    minutes = time_difference.total_seconds() / 60
    return int(minutes)

def substitute(msg):
    new_alpha = {'A#':'H', 'C#':'I', 'D#':'J', 'F#':'K', 'G#':'L'}
    if '#' in msg:
        for key in new_alpha.keys():
            if key in msg:
                msg = msg.replace(key, new_alpha[key])
    return msg

def solution(m, musicinfos):
    answer = ""
    arr = []
    new_infos = [ [""] * 5 for _ in range(len(musicinfos))]
    m = substitute(m)
    
    for i in range(len(musicinfos)):
        new_infos[i] = musicinfos[i].split(',')
        new_infos[i][3] = substitute(new_infos[i][3])
        new_infos[i].append(calculate_time(new_infos[i][0], new_infos[i][1]))
        new_infos[i].append(new_infos[i][3] * (new_infos[i][4] // len(new_infos[i][3])) + new_infos[i][3][:new_infos[i][4] % len(new_infos[i][3])])
        if m in new_infos[i][5]:
            arr.append(i)

    if len(arr) == 0:
        return "(None)"
    elif len(arr) == 1:
        return new_infos[arr[0]][2]
    else:
        index = arr[0]
        max = new_infos[arr[0]][4]
        for i in range(1, len(arr)):
            if max < new_infos[arr[i]][4]:
                max = new_infos[arr[i]][4]
                index = arr[i]
        return new_infos[index][2]
    
# 다른 사람 풀이
def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
    found = {'time': 0, 'name': '(None)'}

    for data in musicinfos:
        start, end, name, song = data.split(',')

        start_hour, start_min = map(int, start.split(':'))
        end_hour, end_min = map(int, end.split(':'))
        length = (end_hour-start_hour)*60 + (end_min-start_min)

        song = song.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
        song = (song*max(1, int(length/len(song))+1))[:length]

        if m in song and found['time'] < length:
            found = {'time': length, 'name': name}

    return found['name']
