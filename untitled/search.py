#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   search.py
@Time    :   2019/05/09 12:57:17
@Author  :   Txh
@Version :   1.0
@Contact :   849366508@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

"""
课   时间
1-2  8:00-9:30
3-4  10:00-11:30
5-6  13:00-14:30
7-8  15:00-16:30
9=10 18:00-19:30
"""
import parse as ps
import pandas as pd
import datetime

firstday = datetime.datetime(2019, 3, 4)
timetable = {1: 8, 2: 9, 3: 10, 4: 11, 5: 13, 6: 14, 7: 15, 8: 16, 9: 18, 10: 19}
rooms = ps.parseSeat()


def check(roomid, date):
    # 教室id、日期时间,return seats
    # 日期格式datetime
    week = (date-firstday).days//7+1
    seats = []
    for seat in rooms[roomid].seatlist:
        if seat.student is None:  # 空闲座位
            seats.append(0)
        else:
            lessons = seat.student.class_.lesson
            min = 0
            for lesson in lessons:
                # print(week,lesson.week,lesson.day,date.weekday()+1)
                weeks = []
                if(len(lesson.week) > 1):
                    for i in range(len(lesson.week)):
                        if(len(lesson.week[i]) > 1):
                            for j in range(lesson.week[i][0], lesson.week[i][1]+1):
                                weeks.append(j)
                        else:
                            weeks.append(lesson.week[i][0])
                else:
                    if(len(lesson.week[0]) > 1):
                        for i in range(len(lesson.week[0])):
                            weeks.append(lesson.week[0][0])
                    else:
                        weeks.append(lesson.week[0][0])
                if((week in weeks) and (lesson.day == date.weekday()+1)):
                    # print(week,lesson.week,lesson.day,date.weekday()+1)
                    if(lesson.single_or_double == 'single' and week % 2 == 0):
                        seats.append(-1)
                        break
                    elif(lesson.single_or_double == 'double' and week % 2 == 1):
                        seats.append(-2)
                        break
                    elif(date.hour >= timetable[lesson.start_hour] and date.hour < timetable[lesson.end_hour]):
                        min += 90-date.minute
                    elif(date.hour == timetable[lesson.end_hour] and date.minute < 30):
                        min += 30-date.minute
                    if(min != 0):
                        seats.append(min)
                        break
                else:
                    seats.append(-4)
                    break
    return seats


if __name__ == '__main__':
    date = datetime.datetime(2019, 3, 18, 8, 10)
    seats = check(1, date)
    print(len(seats))
    print(seats)
