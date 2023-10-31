import networkx as nx
from course_processor import course_processor
import datetime

def schedule_processor(pending_list, dag, schedule_list):
    # To store the list of courses that need scheduling as per pre-requites and pending courses
    temp_list = []
    final_schedule_list = []
    today = datetime.date.today()
    year = today.year

    semester_list = {year: {"Fall": [], "Spring": [], "Summer": []}, year + 1: {"Fall": [], "Spring": [], "Summer": []},
                  year + 2: {"Fall": [], "Spring": [], "Summer": []},
                  year + 3: {"Fall": [], "Spring": [], "Summer": []}}

    while(len(pending_list) > 0):
        temp_list.insert(0,pending_list.pop(0))
        temp_course = []
        predecessors_list = []
        processed_list = []

        while(len(temp_list) > 0):
            temp_crs = temp_list[0]
            temp_course.append(temp_list.pop(0))

            if(temp_crs in dag.nodes):
                predecessors_list = list(dag.predecessors(temp_crs))

            if(len(predecessors_list) == 0):
                continue

            elif(len(predecessors_list) == 1):
                if(predecessors_list[0] in pending_list):
                    temp_list.insert(0,predecessors_list[0])

            else:
                for i in predecessors_list:
                    if(i in pending_list):
                        temp_list.insert(0,i)
        processed_list += list(set(temp_course))

        pending_list = remove_checked_course(pending_list, processed_list)

        final_schedule_list = course_processor(processed_list, schedule_list, dag, semester_list)

    return final_schedule_list

def remove_checked_course(pending_list, removal_list):
    for i in removal_list:
        j = 0
        while(j < len(pending_list)):
            if(i in pending_list[j]):
                pending_list.pop(j)
                break
            else:
                j += 1
    #print("The latest pending list is ",pending_list)
    return pending_list

