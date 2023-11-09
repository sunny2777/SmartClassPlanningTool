import sys

import PyPDF2
import re
import os


def extract_pending_course(pending_course_file):
    if (os.path.exists(pending_course_file)  and os.path.isfile(pending_course_file)):

        text1 = "or"
        text2 = "and"
        text3 = "Classes in"
        text4 = "Credits in"
        inputcourseslist = []
        all_sequences = []
        found_still_needed = False
        initial_processed = []
        secondary_processing = []
        with open(pending_course_file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                lines = page_text.split('\n')
                for i in lines:
                    if ("Class" in i and "Still Needed" not in i):
                        initial_processed.append(i.strip())
                    elif ("Credit" in i and "Still Needed" not in i):
                        initial_processed.append(i.strip())
                    elif ("Credits" in i and "Still Needed" not in i):
                        initial_processed.append(i.strip())
                    elif ("Classes" in i and "Still Needed" not in i):
                        initial_processed.append(i.strip())
                    elif ("Still Needed" not in i):
                        initial_processed.append(i.strip())
        if(len(initial_processed) > 0):
            for i in initial_processed:

                if ("Class" in i):
                    secondary_processing.append(i)
                elif ("Classes" in i):
                    secondary_processing.append(i)
                elif ("Credits" in i):
                    secondary_processing.append(i)
                elif ("Credit" in i):
                    secondary_processing.append(i)
                elif (i.startswith("PERS") or i.startswith("STAT")):
                    secondary_processing.append(i)


            result1 = [item for item in secondary_processing if "Classes in" in item]
            result2 = [item for item in secondary_processing if "Class in" in item]
            result3 = [item for item in secondary_processing if "Credits in" in item]
            result4 = [item for item in secondary_processing if "Credit in" in item]
            # Print the extracted items

            # for item in result1:
            #     print(item)

            for item in result1:
                parts = item.split("or")
                if len(parts) >= 2:
                    value_0 = parts[0].strip()
                    value_1 = parts[1].strip()
                    #print(f"0 Index: {value_0}, 1 Index: {value_1}")
                    sizing = len(value_1)
                    if len(value_1) == 0:
                        first_part = (((value_0.split("Classes in")[1]).split("and"))[0]).strip()
                        if (first_part.endswith("*")):
                            first_part = first_part[:-1]
                        if (first_part.endswith("U")):
                            first_part = first_part[:-1]
                        second_part = (((value_0.split("Classes in")[1]).split("and"))[1]).strip()
                        second_part = first_part[:4] + " " + second_part
                        second_part = second_part[:-3]
                        #print(first_part, second_part)
                        inputcourseslist.append(first_part)
                        inputcourseslist.append(second_part)
            #print(inputcourseslist)

            for item in result2:
                #print(item)
                if text1 not in item and text2 not in item:
                    first_part = ((item.split("Class in")[1])).strip()
                    if (first_part.endswith("*")):
                        first_part = first_part[:-1]
                    if (first_part.endswith("U")):
                        first_part = first_part[:-1]
                    if (first_part.endswith(")")):
                        first_part = first_part[:-1]
                        first_part = first_part.strip()
                    #print(first_part)
                    inputcourseslist.append(first_part)

            #print(inputcourseslist)

            for item in result2:
                parts = item.split("or")
                if len(parts) >= 2:
                    value_0 = parts[0].strip()
                    value_1 = parts[1].strip()
                    #print(f"0 Index: {value_0}, 1 Index: {value_1}")
                    sizing = len(value_1)
                    #print(sizing)
                    if len(value_1) == 0:
                        parts1 = value_0.split("Class in")
                        if len(parts1) >= 2:
                            value_first = parts1[0].strip()
                            value_second = parts1[1].strip()
                            if (value_second[:-2].endswith("*")):
                                value_second = value_second[:-1]
                            if (value_second[:-2].endswith("U")):
                                value_second = value_second[:-1]
                            value_second = value_second[:-2]
                            #print(value_second)
                            inputcourseslist.append(value_second)

                    if len(value_1) > 0:
                        first_part = ((value_0.split("Class in")[1])).strip()
                        second_part = value_1
                        second_part = first_part[:4] + " " + second_part
                        second_part = second_part[:-2]
                        #print(second_part)
                        inputcourseslist.append(second_part)

            #print(inputcourseslist)

            for item in result3:
                parts = item.split("or")
                if len(parts) >= 2:
                    value_0 = parts[0].strip()
                    value_1 = parts[1].strip()
                    if len(value_1) == 0:
                        parts1 = value_0.split("Credits in")
                        if len(parts1) >= 2:
                            value_first = parts1[0].strip()
                            value_second = parts1[1].strip()
                            if value_second[:-2].endswith("*"):
                                value_second = value_second[:-1]
                            if value_second[:-2].endswith("U"):
                                value_second = value_second[:-1]
                            if value_second[:-2].endswith("@"):
                                value_second = value_second[:-1]
                            value_second = value_second[:-2]
                            inputcourseslist.append(value_second)

            #print(inputcourseslist)
            if(len(inputcourseslist) == 0):
                print("Please provide in a valid student pending course list as per the degree works")
                return inputcourseslist
            return inputcourseslist
#extract_pending_course(pending_course_file)
#extract_pending_course("Sample Input3.pdf")