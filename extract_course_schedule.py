import os.path

import PyPDF2
import pathlib



def extract_course_schedule(schedule):

    text_from_file = ""
    with open(schedule, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
           text_from_file += f"\n{pdf_reader.pages[page_num].extract_text()}"
    text_from_file = text_from_file.strip()
    #print("printing a text  ----- ",len(text_from_file))
    if(len(text_from_file) > 0):
        if("Second Year" in text_from_file and "Third Year" in text_from_file and "Fourth Year" in text_from_file
        and "FALL" in text_from_file and "SPRING" in text_from_file and "CREDIT" in text_from_file and "HOURS" in text_from_file):
            first_year = text_from_file.split("Second Year")[0].replace("\n","")
            second_year = (((text_from_file.split("Third Year")[0]).split("Second Year"))[1]).replace("\n","")
            third_year = (((text_from_file.split("Fourth Year")[0]).split("Third Year"))[1]).replace("\n","")
            fourth_year = (text_from_file.split("Fourth Year")[1]).replace("\n","")

            first_year_fall = (first_year.split("SPRING")[0].strip()).split("FALL")[1].strip().split(" ")
            first_year_spring = first_year.split("SPRING")[1].strip().split(" ")

            second_year_fall = (second_year.split("SPRING")[0].strip()).split("FALL")[1].strip().split(" ")
            second_year_spring = second_year.split("SPRING")[1].strip().split(" ")

            third_year_fall = (third_year.split("SPRING")[0].strip()).split("FALL")[1].strip().split(" ")
            third_year_spring = third_year.split("SPRING")[1].strip().split(" ")

            fourth_year_fall = (fourth_year.split("SPRING")[0].strip()).split("FALL")[1].strip().split(" ")
            fourth_year_spring = fourth_year.split("SPRING")[1].strip().split(" ")

            complete_years = {"f_f":first_year_fall,"f_s":first_year_spring,"s_f":second_year_fall,"s_s":second_year_spring,"t_f":third_year_fall,"t_s":third_year_spring,"fo_f":fourth_year_fall,"fo_s":fourth_year_spring}

            fall = []
            spring = []
            summer = []

            for k in complete_years.keys():
                prev = 0
                if(k.endswith("f")):
                    j = complete_years[k]
                    for i in range(0,len(j)):
                        if(j[i] == " "):
                            continue
                        elif (j[i] == "CREDIT" or j[i] == "HOURS"):
                            if (prev == 0):
                                prev = i
                            else:
                                prev = i
                        elif(len(j[i]) == 1 and j[i].isdigit()):
                            if(prev == 0):
                                temp_str = " ".join(j[:i])
                                prev = i
                                fall.append(temp_str.strip())
                            else:
                                temp_str = " ".join(j[prev+1:i])
                                prev = i
                                fall.append(temp_str.strip())
                elif(k.endswith("s")):
                    j = complete_years[k]
                    for i in range(0,len(j)):
                        if(j[i] == " "):
                            continue
                        elif(j[i] == "CREDIT" or j[i] == "HOURS"):
                            if(prev == 0):
                                prev = i
                            else:
                                prev = i
                        elif(len(j[i]) == 1 and j[i].isdigit()):
                            if(prev == 0):
                                temp_str = " ".join(j[:i])
                                prev = i
                                spring.append(temp_str.strip())
                            else:
                                temp_str = " ".join(j[prev+1:i])
                                prev = i
                                spring.append(temp_str.strip())
                else:
                    j = complete_years[k]
                    for i in range(0,len(j)):
                        if(j[i] == " "):
                            continue
                        elif (j[i] == "CREDIT" or j[i] == "HOURS"):
                            if (prev == 0):
                                prev = i
                            else:
                                prev = i
                        elif(len(j[i]) == 1 and j[i].isdigit()):
                            if(prev == 0):
                                temp_str = " ".join(j[:i])
                                prev = i
                                summer.append(temp_str.strip())
                            else:
                                temp_str = " ".join(j[prev+1:i])
                                prev = i
                                summer.append(temp_str.strip())
            #print("test case practice is -------- ",[fall,spring,summer])
            return [fall,spring,summer]
        else:
            print("Please check your Program map file and pass in a valid schedule file")
            return "Please check your Program map file and pass in a valid schedule file"
    else:
        print("Please send in a file with all the details of schedule")
        return []


def schedule_final_processor(fall,spring,summer):
    if(len(fall) > 0 and len(spring) > 0 and len(summer) > 0):
        fall_f = {}
        spring_f = {}
        summer_f = {}
        for i in fall:
            temp = i.split(" ")
            fall_f[temp[0] + " "+temp[1]] = " ".join(temp[2:])

        for i in spring:
            temp = i.split(" ")
            spring_f[temp[0] + " "+temp[1]] = " ".join(temp[2:])

        for i in summer:
            temp = i.split(" ")
            summer_f[temp[0] + " "+temp[1]] = " ".join(temp[2:])

        # print("Fall semester course list is ",fall_f)
        # print("Summer semester course list is ",summer_f)
        # print("Spring semester course list is ",spring_f)
        # print("-----------------------------------------")

        return [fall_f,spring_f,summer_f]
    else:
        return []
#fall = ['CPSC 5157 Computer Networks', 'CPSC 2108 Data Structures', 'MATH 1113 Pre-Calculus', 'CYBR 2159 Fundamentals of Computer Networking', 'CPSC 3131 Database Systems I (minimum grade of C)', 'KINS 1106 or PHED 1205 Lifetime Wellness or Concepts of Fitness', 'AREA C Humanities Elective', 'CPSC 4157 Computer Networks (minimum grade of C)', 'CPSC 4175 Software Engineering', 'Area W PEDS Elective', 'CPSC 5115 Algorithm Analysis & Design', 'AREA I General Electives', 'CPSC 1301K Computer Science I (minimum grade of C)', 'MATH 2125 Intro to Discrete Math', 'CPSC 3131 Database Systems I', 'CPSC 3175 Object-Oriented Design', 'CPSC 1302 Computer Science 2', 'CPSC 4115 Algorithms (minimum grade of C)', 'AREA E Social Sciences Elective (Behavioral Science)', 'AREA H CPSC Upper-Division (minimum grade of C)', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'POLS 1101 American Government', 'CYBR 2159 Fundamentals of Computer Networks (minimum grade of C)', 'CPSC 2108 Data Structures (minimum grade of C)', 'CPSC 5155 Computer Architecture', 'CYBR 2106 Intro to Information Security', 'MATH 1113 Pre-Calculus (minimum grade of C)', 'Area B1  COMM 1110 Public Speaking or foreign language 1001, 1002, 2001, 2002', 'AREA D Science Elective with Lab', 'CPSC 4155 Computer Architecture (minimum grade of C)', 'CPSC 1301K Computer Science 1', 'ENGL 1101 English Composition I (minimum grade of C)', 'MATH 5125U Discrete Mathematics', 'CPSC 3125 Operating Systems', 'MATH 5125 Discrete Math', 'CPSC 2105 Computer Organization', 'CPSC 3125 Operating Systems (minimum grade of C)']
#spring = ['CPSC 4175 Software Engineering (minimum grade of C)', 'CPSC 4176 Senior Software Engineering Project (minimum grade of C)', 'CPSC 2108 Data Structures', 'MATH 1113 Pre-Calculus', 'CPSC 1302K Computer Science II (minimum grade of C)', 'HIST 2111 or HIST 2112 U. S. History to 1865 or U. S. History since 1865', 'CYBR 2159 Fundamentals of Computer Networking', 'CPSC 5135 Programming Languages', 'Area B2  ITDS 1779 (2), LEAD 1705 (2), PERS 1506 (1; may be repeated with different topic), PERS 1507 (2)', 'ENGL 1102 English Composition II (minimum grade of C)', 'CPSC 4000 Baccalaureate Survey', 'CPSC 3165 Professionalism in Computing (minimum grade of C)', 'AREA I General Electives', 'CPSC 3121 Assembly I', 'MATH 2125 Intro to Discrete Math', 'CPSC 3131 Database Systems I', 'CPSC 3175 Object-Oriented Design', 'CPSC 1302 Computer Science 2', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'CPSC 2105 Computer Organization (minimum grade of C)', 'AREA I General Elective', 'CPSC 4148 Theory of Computation (minimum grade of C)', 'CPSC 3175 Object-Oriented Design (minimum grade of C)', 'CPSC 5128 Theory of Computation', 'CYBR 2106 Intro to Information Security', 'MATH 2125 Introduction to Discrete Mathematics (minimum grade of C)', 'CYBR 2160 Intro to Information Security (minimum grade of C)', 'AREA D Science Elective with Lab', 'CPSC 1301K Computer Science 1', 'CPSC 3125 Operating Systems', 'STAT 1401 Elementary Statistics', 'AREA C Fine Arts', 'AREA E Social Science Elective (World Culture)', 'CPSC 4176 Senior Software Eng. Project', 'MATH 5125 Discrete Math', 'CPSC 2105 Computer Organization']
#summer = ['CPSC 5157 Computer Networks', 'CPSC 4175 Software Engineering (minimum grade of C)', 'CPSC 4176 Senior Software Engineering Project (minimum grade of C)', 'CPSC 2108 Data Structures', 'MATH 1113 Pre-Calculus', 'CPSC 1302K Computer Science II (minimum grade of C)', 'HIST 2111 or HIST 2112 U. S. History to 1865 or U. S. History since 1865', 'Area B2  ITDS 1779 (2), LEAD 1705 (2), PERS 1506 (1; may be repeated with different topic), PERS 1507 (2)', 'ENGL 1102 English Composition II (minimum grade of C)', 'CPSC 4000 Baccalaureate Survey', 'CPSC 3165 Professionalism in Computing (minimum grade of C)', 'AREA I General Electives', 'MATH 2125 Intro to Discrete Math', 'CPSC 1302 Computer Science 2', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'CPSC 2105 Computer Organization (minimum grade of C)', 'AREA I General Elective', 'CPSC 4148 Theory of Computation (minimum grade of C)', 'CPSC 3175 Object-Oriented Design (minimum grade of C)', 'CYBR 2106 Intro to Information Security', 'MATH 2125 Introduction to Discrete Mathematics (minimum grade of C)', 'CYBR 2160 Intro to Information Security (minimum grade of C)', 'AREA D Science Elective with Lab', 'CPSC 1301K Computer Science 1', 'STAT 1401 Elementary Statistics', 'AREA C Fine Arts', 'AREA E Social Science Elective (World Culture)', 'MATH 5125 Discrete Math', 'CPSC 2105 Computer Organization']
#
#d = schedule_final_processor(fall,spring,summer)
# print(d)