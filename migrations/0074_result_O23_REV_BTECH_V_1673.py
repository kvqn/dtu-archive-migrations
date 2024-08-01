
# This migration file was made by the scraper utility.
# Result PDF : O23_REV_BTECH_V_1673

def migration(cur):

    cur.execute("select max(heirarchy) from result_heirarchy")
    result = cur.fetchall()
    if (result[0][0] is None):
        n_heirarchy = 1
    else:
        n_heirarchy = result[0][0] + 1

    cur.execute(f"insert into result_heirarchy values ('O23_REV_BTECH_V_1673', 5, {n_heirarchy})")

    query = """insert into result_student_details values
('O23_REV_BTECH_V_1673','2K21/CO/149', 'DEV GUPTA', 23, 8.57, '', False),
('O23_REV_BTECH_V_1673','2K21/CO/09', 'ABHINAV DAHIYA', 27, 9.41, '', False),
('O23_REV_BTECH_V_1673','2K21/CO/151', 'DEVANSH GUPTA', 27, 9.0, '', False),
('O23_REV_BTECH_V_1673','2K21/EE/218', 'PRATHAM JAISWAL', 23, 7.78, '', False),
('O23_REV_BTECH_V_1673','2K21/IT/134', 'PRERAK VARSHNEY', 27, 9.85, '', False),
('O23_REV_BTECH_V_1673','2K21/IT/149', 'ROHIT DEY', 27, 9.44, '', False),
('O23_REV_BTECH_V_1673','2K21/IT/185', 'URVASHI SINHA', 27, 9.44, '', False),
('O23_REV_BTECH_V_1673','2K21/ME/206', 'PRIYANSHU KUMAR', 31, 8.48, '', False)
;
"""
    cur.execute(query)

    query = """insert into result_grades values
('O23_REV_BTECH_V_1673', '2K21/CO/149', 'CO301', 'B+'),
('O23_REV_BTECH_V_1673', '2K21/CO/149', 'CO303', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/149', 'HU301a', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/149', 'CE201', 'B+'),
('O23_REV_BTECH_V_1673', '2K21/CO/149', 'CO327', 'O'),
('O23_REV_BTECH_V_1673', '2K21/CO/149', 'MOOC301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/CO/149', 'MOOC303', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'CO301', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'CO303', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'HU301a', 'O'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'CO313', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'CO325', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'CO327', 'O'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'MOOC301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/CO/09', 'MOOC303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'CO301', 'A'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'CO303', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'HU301a', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'CO313', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'EN311', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'MC207', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'MOOC301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/CO/151', 'MOOC303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/EE/218', 'EE301', 'B+'),
('O23_REV_BTECH_V_1673', '2K21/EE/218', 'EE303', 'A'),
('O23_REV_BTECH_V_1673', '2K21/EE/218', 'HU301a', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/EE/218', 'EE307', 'B+'),
('O23_REV_BTECH_V_1673', '2K21/EE/218', 'EE325', 'B+'),
('O23_REV_BTECH_V_1673', '2K21/EE/218', 'MOOC301', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/EE/218', 'MOOC303', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'IT301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'IT303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'HU301a', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'HU309', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'IT321', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'IT433', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'MOOC301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/134', 'MOOC303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'IT301', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'IT303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'HU301a', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'HU309', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'IT321', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'IT433', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'MOOC301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/149', 'MOOC303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'IT301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'IT303', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'HU301a', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'HU309', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'IT321', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'IT433', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'MOOC301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/IT/185', 'MOOC303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'CO205', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'ME361', 'B+'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'ME301', 'A'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'ME303', 'B+'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'MOOC301', 'O'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'MOOC303', 'O'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'MG301', 'A+'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'CO201', 'O'),
('O23_REV_BTECH_V_1673', '2K21/ME/206', 'CO203', 'A')
;
"""
    cur.execute(query)

