import networkx as nx
import datetime
def find_if_scheduled (raw_output, course_code, dag):
    academic_year = 0
    semester = ""
    course_codes_list = []

    if(course_code in dag.nodes):
        course_codes_list = list(dag.predecessors(course_code))
    group = []
    fkeys = list(raw_output.keys())
    fkeys.sort()

    for i in course_codes_list:
        for j in fkeys:
            for k in list(raw_output[j].keys()):
                for l in raw_output[j][k]:
                    if(i.startswith(l)):
                        group.append([j,k])

    if(len(group) == 0):
        #print("Current course is not scheduled in any available semesters.")
        return []

    elif(len(group) == 1):
        if(group[0][1] == "Fall"):
            return [group[0][0] + 1,"Spring"]
        elif(group[0][1] == "Spring"):
            return [group[0][0],"Summer"]
        elif(group[0][1] == "Summer"):
            return [group[0][0],"Fall"]

    elif(len(group) > 1):
        if(group[0][0] == group[1][0]):
            temp = [group[0][1],group[1][1]]
            temp.sort()
            if("Fall" in temp):
                return [group[1][0]+1,"Spring"]
            elif("Summer" in temp):
                return [group[1][0],"Fall"]
            else:
                return [group[1][0],"Summer"]
        else:
            get_max = max(group[0][0],group[1][0])

            if(group[0][0] == get_max):
                if(group[0][1] == "Fall"):
                    return [get_max+1,"Spring"]
                elif(group[0][1] == "Summer"):
                    return [get_max,"Fall"]
                elif(group[0][1] == "Spring"):
                    return [get_max,"Summer"]

            elif(group[1][0] == get_max):
                if (group[1][1] == "Fall"):
                    return [get_max + 1, "Spring"]
                elif (group[1][1] == "Summer"):
                    return [get_max, "Fall"]
                elif (group[1][1] == "Spring"):
                    return [get_max, "Summer"]
                    