
def special_course_processor(raw_output, flag1, flag2):
    del_list = []
    for i in raw_output.keys():
        if(len(raw_output[i]["Fall"]) == 0 and len(raw_output[i]["Spring"]) == 0 and len(raw_output[i]["Summer"]) == 0):
            del_list.append(i)
    while(len(del_list) > 0):
        del raw_output[del_list.pop()]

    get_max = max(list(raw_output.keys()))

    if(flag2):
        if(len(raw_output[get_max]["Spring"]) < 4):
            raw_output[get_max]["Spring"].append("CPSC 3165")
        elif(len(raw_output[get_max]["Summer"]) < 2):
            raw_output[get_max]["Summer"].append("CPSC 3165")
        else:
            raw_output[get_max]["Fall"].append("CPSC 3165")

    if(flag1):
        if(len(raw_output[get_max]["Fall"]) > 0 and len(raw_output[get_max]["Fall"]) < 4):
            raw_output[get_max]["Fall"].append("CPSC 4000")
        elif(len(raw_output[get_max]["Summer"]) > 0 and len(raw_output[get_max]["Summer"]) < 2):
            raw_output[get_max]["Summer"].append("CPSC 4000")
        elif(len(raw_output[get_max]["Spring"]) > 0 and len(raw_output[get_max]["Spring"]) < 4):
            raw_output[get_max]["Spring"].append("CPSC 4000")
        else:
            raw_output[get_max]["Summer"].append("CPSC 4000")
    return raw_output
