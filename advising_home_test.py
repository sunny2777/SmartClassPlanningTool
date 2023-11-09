import unittest
from advising_home import advising_home
from extract_course_schedule import extract_course_schedule, schedule_final_processor
from node_processor import extract_pre_requisite
from output_excel import generate_output_excel
from extract_course_schedule import extract_course_schedule
from pending_course_processor import extract_pending_course

l1=['POLS 1101', 'CPSC 3165', 'CPSC 4000', 'CPSC 3121', 'CPSC 5115', 'CPSC 4175', 'CPSC 4176', 'CPSC 5135', 'CPSC 5128', 'CPSC 5155', 'CPSC 5157']
l2=['ASTR 1105', 'ASTR 1305', 'CHEM 1151', 'CHEM 1151L', 'CHEM 1152', 'CHEM 1152L', 'CHEM 1212', 'CHEM 1212L', 'ATSC 1112', 'ATSC 1112L', 'GEOL 1121', 'GEOL 1121L', 'GEOL 1122', 'GEOL 1322', 'PHYS 1111', 'PHYS 1311', 'PHYS 1125', 'PHYS 1325', 'PHYS 2211', 'PHYS 2311', 'PHYS 2212', 'PHYS 2312', 'ENVS 1205K', 'STAT 1401', 'CPSC 1302', 'CPSC 2105', 'CPSC 2108', 'CPSC 3125', 'CPSC 3131', 'CPSC 3165', 'CPSC 3175', 'CPSC 4000', 'MATH 5125', 'CPSC 3121', 'CPSC 5115', 'CPSC 4175', 'CPSC 4176', 'GEOL 1121K', 'GEOL 2225', 'CPSC 5135', 'CPSC 5128', 'CPSC 5155', 'CPSC 5157', 'BIOL 1225K', 'CHEM 1211']
l3=['ASTR 1105', 'ASTR 1305', 'CHEM 1151', 'CHEM 1151L', 'CHEM 1152', 'CHEM 1152L', 'CHEM 1212', 'CHEM 1212L', 'ATSC 1112', 'ATSC 1112L', 'GEOL 1122', 'GEOL 1322', 'PHYS 1111', 'PHYS 1311', 'PHYS 1125', 'PHYS 1325', 'PHYS 2211', 'PHYS 2311', 'PHYS 2212', 'PHYS 2312', 'ENVS 1205K', 'STAT 1401', 'CPSC 1302', 'CPSC 2105', 'CYBR 2159', 'CYBR 2160', 'CPSC 2108', 'CPSC 3125', 'CPSC 3131', 'CPSC 3165', 'CPSC 3175', 'CPSC 4000', 'MATH 5125', 'CPSC 3121', 'CPSC 5115', 'CPSC 4175', 'CPSC 4176', 'GEOL  1121L', 'GEOL 1121K', 'GEOL 2225', 'CPSC 5135', 'CPSC 5128', 'CPSC 5155', 'CPSC 5157', 'BIOL 1215K', 'BIOL 1225K', 'CHEM 1211']
r_output= {2023: {'Fall': ['CPSC 1302', 'CPSC 2105', 'MATH 5125'], 'Spring': [], 'Summer': []}, 2024: {'Fall': ['CPSC 3125', 'CPSC 5115', 'CPSC 4175', 'CPSC 5155'], 'Spring': ['STAT 1401', 'CPSC 2108', 'CPSC 3131', 'CPSC 3121'], 'Summer': ['CPSC 3175', 'CPSC 5157']}, 2025: {'Fall': [], 'Spring': ['CPSC 4176', 'CPSC 5135', 'CPSC 5128', 'CPSC 3165'], 'Summer': ['CPSC 4000']}}
r_output_invalid= {2023: {'Fall': ['CPSC 1302', 'CPSC 2105', 'MATH 5125']}}
l = [['ENGL 1101 English Composition I (minimum grade of C)', 'MATH 1113 Pre-Calculus (minimum grade of C)', 'Area B1  COMM 1110 Public Speaking or foreign language 1001, 1002, 2001, 2002', 'CPSC 1301K Computer Science I (minimum grade of C)', 'KINS 1106 or PHED 1205 Lifetime Wellness or Concepts of Fitness', 'MATH 5125U Discrete Mathematics', 'CPSC 2108 Data Structures (minimum grade of C)', 'CYBR 2159 Fundamentals of Computer Networks (minimum grade of C)', 'AREA C Humanities Elective', 'AREA D Science Elective with Lab', 'CPSC 3125 Operating Systems (minimum grade of C)', 'CPSC 3131 Database Systems I (minimum grade of C)', 'POLS 1101 American Government', 'AREA E Social Sciences Elective (Behavioral Science)', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'Area W PEDS Elective', 'CPSC 4115 Algorithms (minimum grade of C)', 'CPSC 4157 Computer Networks (minimum grade of C)', 'CPSC 4155 Computer Architecture (minimum grade of C)', 'AREA H CPSC Upper-Division (minimum grade of C)', 'AREA I General Electives'], ['ENGL 1102 English Composition II (minimum grade of C)', 'MATH 2125 Introduction to Discrete Mathematics (minimum grade of C)', 'CPSC 1302K Computer Science II (minimum grade of C)', 'CPSC 2105 Computer Organization (minimum grade of C)', 'AREA C Fine Arts', 'Area B2  ITDS 1779 (2), LEAD 1705 (2), PERS 1506 (1; may be repeated with different topic), PERS 1507 (2)', 'CPSC 3175 Object-Oriented Design (minimum grade of C)', 'CYBR 2160 Intro to Information Security (minimum grade of C)', 'STAT 1401 Elementary Statistics', 'HIST 2111 or HIST 2112 U. S. History to 1865 or U. S. History since 1865', 'AREA D Science Elective with Lab', 'CPSC 4175 Software Engineering (minimum grade of C)', 'CPSC 3165 Professionalism in Computing (minimum grade of C)', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'AREA E Social Science Elective (World Culture)', 'AREA I General Elective', 'CPSC 4176 Senior Software Engineering Project (minimum grade of C)', 'CPSC 4148 Theory of Computation (minimum grade of C)', 'CPSC 4000 Baccalaureate Survey', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'AREA I General Electives'], []]
pre = [['CPSC 1301K Computer Science 1', 'CPSC 1302 Computer Science 2'], ['CPSC 1301K Computer Science 1', 'CPSC 1302 Computer Science 2'], ['CPSC 1301K Computer Science 1', 'CPSC 1302 Computer Science 2']]
fall = ['CPSC 5157 Computer Networks', 'CPSC 2108 Data Structures', 'MATH 1113 Pre-Calculus', 'CYBR 2159 Fundamentals of Computer Networking', 'CPSC 3131 Database Systems I (minimum grade of C)', 'KINS 1106 or PHED 1205 Lifetime Wellness or Concepts of Fitness', 'AREA C Humanities Elective', 'CPSC 4157 Computer Networks (minimum grade of C)', 'CPSC 4175 Software Engineering', 'Area W PEDS Elective', 'CPSC 5115 Algorithm Analysis & Design', 'AREA I General Electives', 'CPSC 1301K Computer Science I (minimum grade of C)', 'MATH 2125 Intro to Discrete Math', 'CPSC 3131 Database Systems I', 'CPSC 3175 Object-Oriented Design', 'CPSC 1302 Computer Science 2', 'CPSC 4115 Algorithms (minimum grade of C)', 'AREA E Social Sciences Elective (Behavioral Science)', 'AREA H CPSC Upper-Division (minimum grade of C)', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'POLS 1101 American Government', 'CYBR 2159 Fundamentals of Computer Networks (minimum grade of C)', 'CPSC 2108 Data Structures (minimum grade of C)', 'CPSC 5155 Computer Architecture', 'CYBR 2106 Intro to Information Security', 'MATH 1113 Pre-Calculus (minimum grade of C)', 'Area B1  COMM 1110 Public Speaking or foreign language 1001, 1002, 2001, 2002', 'AREA D Science Elective with Lab', 'CPSC 4155 Computer Architecture (minimum grade of C)', 'CPSC 1301K Computer Science 1', 'ENGL 1101 English Composition I (minimum grade of C)', 'MATH 5125U Discrete Mathematics', 'CPSC 3125 Operating Systems', 'MATH 5125 Discrete Math', 'CPSC 2105 Computer Organization', 'CPSC 3125 Operating Systems (minimum grade of C)']
spring = ['CPSC 4175 Software Engineering (minimum grade of C)', 'CPSC 4176 Senior Software Engineering Project (minimum grade of C)', 'CPSC 2108 Data Structures', 'MATH 1113 Pre-Calculus', 'CPSC 1302K Computer Science II (minimum grade of C)', 'HIST 2111 or HIST 2112 U. S. History to 1865 or U. S. History since 1865', 'CYBR 2159 Fundamentals of Computer Networking', 'CPSC 5135 Programming Languages', 'Area B2  ITDS 1779 (2), LEAD 1705 (2), PERS 1506 (1; may be repeated with different topic), PERS 1507 (2)', 'ENGL 1102 English Composition II (minimum grade of C)', 'CPSC 4000 Baccalaureate Survey', 'CPSC 3165 Professionalism in Computing (minimum grade of C)', 'AREA I General Electives', 'CPSC 3121 Assembly I', 'MATH 2125 Intro to Discrete Math', 'CPSC 3131 Database Systems I', 'CPSC 3175 Object-Oriented Design', 'CPSC 1302 Computer Science 2', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'CPSC 2105 Computer Organization (minimum grade of C)', 'AREA I General Elective', 'CPSC 4148 Theory of Computation (minimum grade of C)', 'CPSC 3175 Object-Oriented Design (minimum grade of C)', 'CPSC 5128 Theory of Computation', 'CYBR 2106 Intro to Information Security', 'MATH 2125 Introduction to Discrete Mathematics (minimum grade of C)', 'CYBR 2160 Intro to Information Security (minimum grade of C)', 'AREA D Science Elective with Lab', 'CPSC 1301K Computer Science 1', 'CPSC 3125 Operating Systems', 'STAT 1401 Elementary Statistics', 'AREA C Fine Arts', 'AREA E Social Science Elective (World Culture)', 'CPSC 4176 Senior Software Eng. Project', 'MATH 5125 Discrete Math', 'CPSC 2105 Computer Organization']
summer = ['CPSC 5157 Computer Networks', 'CPSC 4175 Software Engineering (minimum grade of C)', 'CPSC 4176 Senior Software Engineering Project (minimum grade of C)', 'CPSC 2108 Data Structures', 'MATH 1113 Pre-Calculus', 'CPSC 1302K Computer Science II (minimum grade of C)', 'HIST 2111 or HIST 2112 U. S. History to 1865 or U. S. History since 1865', 'Area B2  ITDS 1779 (2), LEAD 1705 (2), PERS 1506 (1; may be repeated with different topic), PERS 1507 (2)', 'ENGL 1102 English Composition II (minimum grade of C)', 'CPSC 4000 Baccalaureate Survey', 'CPSC 3165 Professionalism in Computing (minimum grade of C)', 'AREA I General Electives', 'MATH 2125 Intro to Discrete Math', 'CPSC 1302 Computer Science 2', 'AREA H CPSC Upper-Division Elective (minimum grade of C)', 'CPSC 2105 Computer Organization (minimum grade of C)', 'AREA I General Elective', 'CPSC 4148 Theory of Computation (minimum grade of C)', 'CPSC 3175 Object-Oriented Design (minimum grade of C)', 'CYBR 2106 Intro to Information Security', 'MATH 2125 Introduction to Discrete Mathematics (minimum grade of C)', 'CYBR 2160 Intro to Information Security (minimum grade of C)', 'AREA D Science Elective with Lab', 'CPSC 1301K Computer Science 1', 'STAT 1401 Elementary Statistics', 'AREA C Fine Arts', 'AREA E Social Science Elective (World Culture)', 'MATH 5125 Discrete Math', 'CPSC 2105 Computer Organization']
message_input2 = """Please check the information provided in the pre-req file. Please provide course code,name,schedule info and list of pre-req courses by providing pre-'list of courses seperated by comma' if in case of no pre-req present provide as None"""
d_list = [{'CPSC 5157': 'Computer Networks', 'CPSC 2108': 'Data Structures (minimum grade of C)', 'MATH 1113': 'Pre-Calculus (minimum grade of C)', 'CYBR 2159': 'Fundamentals of Computer Networks (minimum grade of C)', 'CPSC 3131': 'Database Systems I', 'KINS 1106': 'or PHED 1205 Lifetime Wellness or Concepts of Fitness', 'AREA C': 'Humanities Elective', 'CPSC 4157': 'Computer Networks (minimum grade of C)', 'CPSC 4175': 'Software Engineering', 'Area W': 'PEDS Elective', 'CPSC 5115': 'Algorithm Analysis & Design', 'AREA I': 'General Electives', 'CPSC 1301K': 'Computer Science 1', 'MATH 2125': 'Intro to Discrete Math', 'CPSC 3175': 'Object-Oriented Design', 'CPSC 1302': 'Computer Science 2', 'CPSC 4115': 'Algorithms (minimum grade of C)', 'AREA E': 'Social Sciences Elective (Behavioral Science)', 'AREA H': 'CPSC Upper-Division Elective (minimum grade of C)', 'POLS 1101': 'American Government', 'CPSC 5155': 'Computer Architecture', 'CYBR 2106': 'Intro to Information Security', 'Area B1': ' COMM 1110 Public Speaking or foreign language 1001, 1002, 2001, 2002', 'AREA D': 'Science Elective with Lab', 'CPSC 4155': 'Computer Architecture (minimum grade of C)', 'ENGL 1101': 'English Composition I (minimum grade of C)', 'MATH 5125U': 'Discrete Mathematics', 'CPSC 3125': 'Operating Systems (minimum grade of C)', 'MATH 5125': 'Discrete Math', 'CPSC 2105': 'Computer Organization'}, {'CPSC 4175': 'Software Engineering (minimum grade of C)', 'CPSC 4176': 'Senior Software Eng. Project', 'CPSC 2108': 'Data Structures', 'MATH 1113': 'Pre-Calculus', 'CPSC 1302K': 'Computer Science II (minimum grade of C)', 'HIST 2111': 'or HIST 2112 U. S. History to 1865 or U. S. History since 1865', 'CYBR 2159': 'Fundamentals of Computer Networking', 'CPSC 5135': 'Programming Languages', 'Area B2': ' ITDS 1779 (2), LEAD 1705 (2), PERS 1506 (1; may be repeated with different topic), PERS 1507 (2)', 'ENGL 1102': 'English Composition II (minimum grade of C)', 'CPSC 4000': 'Baccalaureate Survey', 'CPSC 3165': 'Professionalism in Computing (minimum grade of C)', 'AREA I': 'General Elective', 'CPSC 3121': 'Assembly I', 'MATH 2125': 'Introduction to Discrete Mathematics (minimum grade of C)', 'CPSC 3131': 'Database Systems I', 'CPSC 3175': 'Object-Oriented Design (minimum grade of C)', 'CPSC 1302': 'Computer Science 2', 'AREA H': 'CPSC Upper-Division Elective (minimum grade of C)', 'CPSC 2105': 'Computer Organization', 'CPSC 4148': 'Theory of Computation (minimum grade of C)', 'CPSC 5128': 'Theory of Computation', 'CYBR 2106': 'Intro to Information Security', 'CYBR 2160': 'Intro to Information Security (minimum grade of C)', 'AREA D': 'Science Elective with Lab', 'CPSC 1301K': 'Computer Science 1', 'CPSC 3125': 'Operating Systems', 'STAT 1401': 'Elementary Statistics', 'AREA C': 'Fine Arts', 'AREA E': 'Social Science Elective (World Culture)', 'MATH 5125': 'Discrete Math'}, {'CPSC 5157': 'Computer Networks', 'CPSC 4175': 'Software Engineering (minimum grade of C)', 'CPSC 4176': 'Senior Software Engineering Project (minimum grade of C)', 'CPSC 2108': 'Data Structures', 'MATH 1113': 'Pre-Calculus', 'CPSC 1302K': 'Computer Science II (minimum grade of C)', 'HIST 2111': 'or HIST 2112 U. S. History to 1865 or U. S. History since 1865', 'Area B2': ' ITDS 1779 (2), LEAD 1705 (2), PERS 1506 (1; may be repeated with different topic), PERS 1507 (2)', 'ENGL 1102': 'English Composition II (minimum grade of C)', 'CPSC 4000': 'Baccalaureate Survey', 'CPSC 3165': 'Professionalism in Computing (minimum grade of C)', 'AREA I': 'General Elective', 'MATH 2125': 'Introduction to Discrete Mathematics (minimum grade of C)', 'CPSC 1302': 'Computer Science 2', 'AREA H': 'CPSC Upper-Division Elective (minimum grade of C)', 'CPSC 2105': 'Computer Organization', 'CPSC 4148': 'Theory of Computation (minimum grade of C)', 'CPSC 3175': 'Object-Oriented Design (minimum grade of C)', 'CYBR 2106': 'Intro to Information Security', 'CYBR 2160': 'Intro to Information Security (minimum grade of C)', 'AREA D': 'Science Elective with Lab', 'CPSC 1301K': 'Computer Science 1', 'STAT 1401': 'Elementary Statistics', 'AREA C': 'Fine Arts', 'AREA E': 'Social Science Elective (World Culture)', 'MATH 5125': 'Discrete Math'}]


class advisingHome_test(unittest.TestCase):

    def test_home_invalid(self):
        self.assertFalse(advising_home("test","pre_requisite_list.txt","program_map.pdf"),False)

    def test_home_valid(self):
        self.assertTrue(advising_home("Sample Input2.pdf","pre_requisite_list.txt","program_map.pdf"),True)

    def test_input3_valid(self):
        self.assertEqual(l,extract_course_schedule("program_map.pdf"))

    def test_input3_invalid(self):
        self.assertEqual([],extract_course_schedule("program_map1.pdf"))

    def test_input3_invalid_d(self):
        self.assertEqual([],schedule_final_processor([],[],[]))

    def test_input3_valid_d(self):
        self.assertEqual(d_list,schedule_final_processor(fall,spring,summer))

    def test_input3_invalid_text(self):
        self.assertEqual("Please check your Program map file and pass in a valid schedule file",extract_course_schedule("program_map2.pdf"))

    def test_input2_invalid(self):
        self.assertEqual([],extract_pre_requisite("empty_file.txt"))

    def test_input2_invalid_info(self):
        self.assertEqual(message_input2,extract_pre_requisite("incorrect_pre.txt"))

    def test_input2_invalid_pre(self):
        self.assertEqual("Please provide None in the input file if a course has no pre-req's",extract_pre_requisite("incorrect_pre2.txt"))

    def test_input2_valid(self):
        self.assertEqual(pre,(extract_pre_requisite("pre_requisite_list.txt"))[1:])

    def test_excel_1(self):
        self.assertTrue(generate_output_excel(r_output_invalid), True)

    def test_excel_2(self):
        self.assertFalse(generate_output_excel(""), False)

    def test_excel_3(self):
        self.assertFalse(generate_output_excel({}), False)

    def test_excel_4(self):
        self.assertTrue(generate_output_excel(r_output), True)
#------------------------------------------
    def test_input1_invalid1(self):
        self.assertFalse(extract_pending_course("test.pdf"), False)

    def test_input1_valid1(self):
        self.assertTrue(extract_pending_course("Sample Input1.pdf"), True)

    def test_input1_valid2(self):
        self.assertTrue(extract_pending_course("Sample Input2.pdf"), True)

    def test_input1_valid3(self):
        self.assertTrue(extract_pending_course("Sample Input3.pdf"), True)

    def test_input1_valid4(self):
        self.assertEqual(l1, extract_pending_course("Sample Input1.pdf"))

    def test_input1_valid5(self):
        self.assertEqual(l2, extract_pending_course("Sample Input2.pdf"))

    def test_input1_valid6(self):
        self.assertEqual(l3, extract_pending_course("Sample Input3.pdf"))

    def test_input1_invalid2(self):
        self.assertEqual([], extract_pending_course("program_map1.pdf"))
