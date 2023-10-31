import PyPDF2

def extract_course_schedule(schedule):

    text_from_file = ""
    with open(schedule, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
           text_from_file += f"\n{pdf_reader.pages[page_num].extract_text()}"

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

    return [fall,spring,summer]


def schedule_final_processor(fall,spring,summer):
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

    print("Fall semester course list is ",fall_f)
    print("Summer semester course list is ",summer_f)
    print("Spring semester course list is ",spring_f)
    print("-----------------------------------------")

    return [fall_f,spring_f,summer_f]