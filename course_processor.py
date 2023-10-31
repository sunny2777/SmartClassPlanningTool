import datetime
from get_semester_details import find_if_scheduled

def course_processor(course_list, schedule_list, graph, semester_list):

    today = datetime.date.today()
    curr_year = today.year
    # print(today.month)
    #  = {year:{"Fall":[],"Spring":[],"Summer":[]},year+1:{"Fall":[],"Spring":[],"Summer":[]},year+2:{"Fall":[],"Spring":[],"Summer":[]},year+3:{"Fall":[],"Spring":[],"Summer":[]}}
    # print(.keys())
    # print([2023]['Fall'])
    course_list.sort()
    fall = schedule_list[0]
    spring = schedule_list[1]
    summer = schedule_list[2]
    i = 0

    # Eliminating the courses for which schedule is not available
    while(i < len(course_list)):
        if(course_list[i] in list(fall.keys())):
            i += 1
        elif(course_list[i] in list(spring.keys())):
            i += 1
        elif(course_list[i] in list(summer.keys())):
            i += 1
        else:
            course_list.pop(i)
    t1_math = []
    t2 = []
    # Considering the MATH courses into a t1_math
    # The other courses into t2
    for i in course_list:
        if(i.startswith("MATH")):
            t1_math.append(i)
        else:
            t2.append((i[-5:]).strip())

    t1_math.sort()
    t2.sort()
    final_course_list = []
    final_course_list += t1_math
    for i in t2:
        for j in course_list:
            if(j.endswith(i)):
                final_course_list.append(j)
    # print("sorted list is :",final_course_list)

    prev_course = []

    while(len(final_course_list) > 0):
        temp = final_course_list[0]
        got_schedule = find_if_scheduled(semester_list, temp, graph)
        #print(got_schedule)
        #if(temp in fall.keys() or temp in spring.keys() or temp in summer.keys()):
            # print("Current processing course: ", temp)
        if(len(got_schedule) == 0):
            keys = list(semester_list.keys())
            keys.sort()
            for key in keys:
                if key == curr_year:
                    # Check if the course is available in the current year
                    if 1 <= today.month <= 5:
                        spring_flag = True
                        summer_flag = True
                        fall_flag = True
                    elif 6 <= today.month <= 7:
                        spring_flag = False
                        summer_flag = True
                        fall_flag = True
                    elif 8 <= today.month <= 12:
                        spring_flag = False
                        summer_flag = False
                        fall_flag = True
                else:
                    #Check for future years
                    spring_flag = True
                    summer_flag = True
                    fall_flag = True
                #if(spring_flag and fall_flag and summer_flag):
                    #print("All semester flags are up")
                # print("current processing year : ",key)
                if(len(semester_list[key]['Spring']) < 4 and spring_flag):
                    if(len(prev_course) == 0):
                        if(temp in (spring.keys())):
                            # print("it is a match",semester_list[key]['Spring'])
                            (semester_list[key]['Spring']).append(temp)
                            # print(semester_list[key]['Spring'])
                            break
                    else:
                        if(prev_course not in semester_list[key]['Spring'] and temp in spring.keys()):
                            (semester_list[key]['Spring']).append(temp)
                            break
                if(len(semester_list[key]['Summer']) < 2 and summer_flag):
                    if(len(prev_course) == 0):
                        if(temp in summer.keys()):
                            (semester_list[key]['Summer']).append(temp)
                            break
                    else:
                        if(prev_course not in semester_list[key]['Summer'] and temp in summer.keys()):
                            (semester_list[key]['Summer']).append(temp)
                            break
                if(len(semester_list[key]['Fall']) < 4 and fall_flag):
                    # print("Entered here in Fall section")
                    if (len(prev_course) == 0):
                        if (temp in fall.keys()):
                            (semester_list[key]['Fall']).append(temp)
                            break
                    else:
                        if (prev_course not in semester_list[key]['Fall'] and temp in fall.keys()):
                            (semester_list[key]['Fall']).append(temp)
                            break
        else:
            start_year = got_schedule[0]
            keys = list(semester_list.keys())
            keys.sort()
            ind = keys.index(start_year)
            keys = keys[ind:]
            # print("printing keys if we have a got schdedule ",keys)
            for key in keys:
                if key == start_year:
                    # Check if the course is available in the current year
                    if(got_schedule[1] == "Spring"):
                        spring_flag = True
                        fall_flag = True
                        summer_flag = True
                    elif(got_schedule[1] == "Summer"):
                        spring_flag = False
                        summer_flag = True
                        fall_flag = True
                    elif(got_schedule[1] == "Fall"):
                        spring_flag = False
                        summer_flag = False
                        fall_flag = True
                else:
                    #Check for future years
                    spring_flag = True
                    summer_flag = True
                    fall_flag = True
                #if(spring_flag and fall_flag and summer_flag):
                    # print("All semester flags are up")
                    # print("current processing year : ",key)
                if(len(semester_list[key]['Spring']) < 4 and spring_flag):
                    if(len(prev_course) == 0):
                        if(temp in (spring.keys())):
                            # print("it is a match",semester_list[key]['Spring'])
                            (semester_list[key]['Spring']).append(temp)
                            # print(semester_list[key]['Spring'])
                            break
                    else:
                        if(prev_course not in semester_list[key]['Spring'] and temp in spring.keys()):
                            (semester_list[key]['Spring']).append(temp)
                            break
                if(len(semester_list[key]['Summer']) < 2 and summer_flag):
                    if(len(prev_course) == 0):
                        if(temp in summer.keys()):
                            (semester_list[key]['Summer']).append(temp)
                            break
                    else:
                        if(prev_course not in semester_list[key]['Summer'] and temp in summer.keys()):
                            (semester_list[key]['Summer']).append(temp)
                            break
                if(len(semester_list[key]['Fall']) < 4 and fall_flag):
                    # print("Entered here in Fall section")
                    if (len(prev_course) == 0):
                        if (temp in fall.keys()):
                            (semester_list[key]['Fall']).append(temp)
                            break
                    else:
                        if (prev_course not in semester_list[key]['Fall'] and temp in fall.keys()):
                            (semester_list[key]['Fall']).append(temp)
                            break
        #print("---------Course scheduling is completed-------")
        # print()
        prev_course = temp
        final_course_list.pop(0)
    # print()
    return semester_list