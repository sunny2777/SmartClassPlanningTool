import sys

import networkx as nx
from schedule_processor import schedule_processor
from node_processor import extract_pre_requisite
from pending_course_processor import extract_pending_course
from extract_course_schedule import extract_course_schedule
from extract_course_schedule import schedule_final_processor
from special_course_processor import special_course_processor
from output_excel import generate_output_excel
import os
import sys



def advising_home():
    print("Welcome to the Class advising system tool")
    # total arguments
    n = len(sys.argv)
    #print(n)
    pending_course = sys.argv[1]
    pre_requisites = sys.argv[2]
    schedule = sys.argv[3]
    # Special courses
    special_course1 = "CPSC 4000"
    special_course2 = "CPSC 3165"
    # Pending_list = ["CPSC 5157","CPSC 5155","CPSC 4176","CPSC 5128","CPSC 3131","CPSC 3125","CPSC 3121","CPSC 5115",
    # "CPSC 4175", "CPSC 5135","CPSC 3175","CPSC 2108","MATH 5125","CPSC 1302","CPSC 1301K","CPSC 2105","CYBR 2106","CYBR 2159"]
    Pending_list = []
    if(os.path.exists(pending_course) and os.path.exists(pre_requisites) and os.path.exists(schedule) and os.path.isfile(pending_course) and os.path.isfile(pre_requisites) and os.path.isfile(schedule)):
        ind = os.path.abspath(pending_course).rindex("/")
        location = os.path.abspath(pending_course)[:ind+1]
        #print(location)

        # First processing the input - 1
        pending_list = extract_pending_course(pending_course)
        if(len(pending_list) > 0):
        # Processing the input - 2
            dag_graph = extract_pre_requisite(pre_requisites)
            if(len(dag_graph) > 0):
        # Processing the input - 3

                course_schedule = extract_course_schedule(schedule)
                #if()
                if(len(course_schedule) > 0):
                # Pre-check processing
                    pre_requisite_graph = dag_graph[0]

                    fall = list(set(dag_graph[1] + course_schedule[0]))
                    spring = list(set(dag_graph[2] + course_schedule[1]))
                    summer = list(set(dag_graph[3] + course_schedule[1]))
                    schedule_list = schedule_final_processor(fall, spring, summer)

                    if(special_course1 in pending_list):
                        pending_list.remove(special_course1)
                        flag_1 = True

                    if(special_course2 in pending_list):
                        pending_list.remove(special_course2)
                        flag_2 = True

                    raw_output = schedule_processor(pending_list, pre_requisite_graph, schedule_list)

                    final_output = special_course_processor(raw_output, flag_1, flag_2)
                    print("The Final Output is: ", final_output)

                    generate_output_excel(location,final_output)
                    return True

                else:
                    print("Please check your input 1 files and follow the instructions in the readme file to check the validity of your input 1 files")
                    return "Please check all your input 1 files and follow the instructions in the readme file to check the validity of your input 1 files"

            else:
                print("Please check your input 2 files and follow the instructions in the readme file to check the validity of your input 2 files")
                return "Please check all your input 2 files and follow the instructions in the readme file to check the validity of your input 2 files"

        else:
            print("Please check your input 1 files and follow the instructions in the readme file to check the validity of your input 1 files")
            return "Please check all your input files and follow the instructions in the readme file to check the validity of your input 1 files"

    else:
        print("Please check the path of the Input file and check if the input file is invalid")
        return False


advising_home()