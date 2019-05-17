# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:38:44 2019

@author: hxw

Room包含一个Seat类的list
Seat对应一个Student，如果这个作为没有被Student包年，则Student为None
Student含有一个Class_类，这个Class_类包含一个Lesson的list，表示这个班级要上的所有课程
通过扫描这个Lesson list，确定这个seat当前是否被占用
"""

import pandas as pd
import numpy as np
import math

class Class():
    def __init__(self,name):
        self.name = name
        self.lesson = []
    
    def setId(self,Id):
        self.Id = Id
        
    def getId(self):
        return self.Id
    
    def getName(self):
        return self.name
    
    def addLesson(self,lesson):
        for each in lesson:
            self.lesson.append(each)
            
    def getLessons(self):
        return self.lesson
    
    
class Lesson():
    def __init__(self,name=None,teacher=None,code=None):
        self.name = name
        self.teacher = teacher
        self.code = code
        
    def setTime(self,day,week,start_hour,end_hour,single_or_double):
        self.day = day
        self.week = week
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.single_or_double = single_or_double
        

class Student():
    def __init__(self,class_,student_id):
        self.class_ = class_
        self.student_id = student_id
        
    def getClass_(self):
        return self.class_
    

class Seat():
    def __init__(self,seat_id,student=None):
        self.seat_id = seat_id
        self.student = student
        
    def getSeatId(self):
        return self.seat_id

    def getStudent(self):
        return self.student


class Room():
    def __init__(self,room_id):
        self.room_id = room_id
        self.seatlist = []
        
    def addSeat(self,seat):
        self.seatlist.append(seat)
    
    def getSeats(self):
        return self.seatlist


def parseDate(date):
    
    date = date.strip('[]')
    weeks = date.split("]")[0]    
    if weeks.find("单")!= -1:
        single_or_double = 'single'
        weeks = weeks[:weeks.find("单")-1]
    elif weeks.find("双")!= -1:
        single_or_double = 'double'
        weeks = weeks[:weeks.find("双")-1]
    else:
        single_or_double = 'together'
        
    weeks = weeks.strip("周")
    hours = date.split("[")[1].strip("节")  
    weeks = weeks.split(",")
    num_start_week = len(weeks)    
    week = []   
    for i in range(num_start_week):
        if weeks[i].find("-")!=-1:
            start_week = weeks[i].split("-")[0]
            end_week = weeks[i].split("-")[1]
        else:
            start_week = weeks[i]
            end_week = weeks[i]
            
        week.append([int(start_week),int(end_week)])
    
    start_hour = int(hours.split("-")[0])
    end_hour = int(hours.split("-")[1])
#    print(week,start_hour,end_hour)
    return {'week':week,
            'start_hour':start_hour,
            'end_hour':end_hour,
            'single_or_double':single_or_double}

    
def parseLesson(data,day):
    """
    创建一个或数个以data为名字的课程
    """
    lines = data.split("\n")
    num_lines = len(lines) - 1
    num_lessons = num_lines // 5
    
    LessonList = []
    for i in range(num_lessons):
        lesson_name = lines[i * 5 + 0]
        lesson_teacher = lines[i * 5 + 1]
        lesson_code = lines[i * 5 + 2]
        lesson_date = parseDate(lines[i * 5 + 4])
        lesson = Lesson(lesson_name,lesson_teacher,lesson_code)
        
        lesson.setTime(day=day,week=lesson_date['week'],start_hour=lesson_date['start_hour'],
                       end_hour=lesson_date['end_hour'],
                       single_or_double=lesson_date['single_or_double'])
        LessonList.append(lesson)
        
    return LessonList
     

def parseClass(data,i):
    """
    创建一个以data为名字的班级
    """
    class_ = Class(data)
    class_.setId(i)
    return class_


def parseTable():
    df = pd.read_excel("lessons.xls")[3:]
    row = len(df)
    col = len(df.columns)
    
    all_class = {}
    class_id_map = {}
    for i in range(row):
        print(i)
        class_ = parseClass(df.iloc[i,0],i)
        for j in range(1, col):
            data = df.iloc[i,j]
            day = math.ceil(j / 5)
            if not pd.isna(data):
#                print(data)   
                if j > 0:
                    lesson = parseLesson(data,day=day)
                    class_.addLesson(lesson)
        class_name = class_.getName()
        
        class_id_map[i] = class_name
        all_class[class_name] = class_
        
        
    return all_class,class_id_map        

def parseSeat():
    """
    解析座位-学生映射，返回结构化的Room
    """
    df = pd.read_excel("seats.xls")
    rooms = {}
    (class_name_instance_map,class_id_name_map) = parseTable()
    for i in range(len(df)):
        room_id = df['room_id'][i]
        if room_id not in rooms.keys():
            rooms[room_id] = Room(room_id=room_id)
        student_id = df['student_id'][i]
        class_id = df['class_id'][i]
        
        if pd.isna(class_id):
            class_instance = None
        else:
            class_name = class_id_name_map[class_id]
            class_instance = class_name_instance_map[class_name]
        
        if pd.isna(student_id):
            student = None
        else:
            student = Student(class_=class_instance,student_id=int(student_id))
    
        seat_id = df['seat_id'][i]
        seat = Seat(seat_id=seat_id,student=student)
        rooms[room_id].addSeat(seat)
    
    return rooms

    
def main():
    return parseSeat()
    

if __name__ == '__main__':
    rooms = main()

        