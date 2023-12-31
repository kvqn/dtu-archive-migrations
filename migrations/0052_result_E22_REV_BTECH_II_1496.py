
# This migration file was made by the scraper utility.
# Result PDF : E22_REV_BTECH_II_1496

def migration(cur):

    cur.execute("select min(heirarchy) from result_heirarchy")
    result = cur.fetchall()
    if (result[0][0] is None):
        n_heirarchy = 1
    else:
        n_heirarchy = result[0][0] - 1

    cur.execute(f"insert into result_heirarchy values ('E22_REV_BTECH_II_1496', 2, {n_heirarchy})")

    query = """insert into result_student_details values
('E22_REV_BTECH_II_1496','2K21/A18/09', 'SAINYAM SETHI', 22, 7.45, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/15', 'SATENDER', 22, 6.91, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/21', 'SAURABH MEENA', 22, 5.91, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/26', 'SHIVAM', 22, 6.09, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/28', 'SHIVAM KUMAR', 18, 5.0, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/39', 'SINCHAN ROY', 22, 7.82, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/40', 'SOHAN SINGH MEENA', 20, 5.0, 'FEC1,', False),
('E22_REV_BTECH_II_1496','2K21/A18/41', 'SOMYA SINGH', 22, 7.91, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/51', 'TINA JAIN', 22, 8.82, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/58', 'VANSH MALHOTRA', 22, 5.45, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/67', 'VIVEK DHIR', 22, 7.82, '', False),
('E22_REV_BTECH_II_1496','2K21/A18/72', 'YASH KUMAR', 22, 6.82, '', False),
('E22_REV_BTECH_II_1496','2K21/B1/022', 'AADITHYA MURALIDHARAN', 22, 7.36, '', False),
('E22_REV_BTECH_II_1496','2K21/B9/53', 'SIDDHANT BANGER', 22, 7.82, '', False),
('E22_REV_BTECH_II_1496','2K21/B14/09', 'DEVANSH GUPTA', 22, 7.91, '', False)
;
"""
    cur.execute(query)

    query = """insert into result_grades values
('E22_REV_BTECH_II_1496', '2K21/A18/09', 'MA102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/09', 'AP102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/09', 'EE102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/09', 'CO102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/09', 'ME102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/09', 'MS199', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/09', 'FEC47', 'O'),
('E22_REV_BTECH_II_1496', '2K21/A18/15', 'MA102', 'C'),
('E22_REV_BTECH_II_1496', '2K21/A18/15', 'AP102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/15', 'EE102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/15', 'CO102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/15', 'ME102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/15', 'MS199', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/15', 'FEC52', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/21', 'MA102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/21', 'AP102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/21', 'EE102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/21', 'CO102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/21', 'ME102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/21', 'MS199', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/21', 'FEC1', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/26', 'MA102', 'C'),
('E22_REV_BTECH_II_1496', '2K21/A18/26', 'AP102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/26', 'EE102', 'C'),
('E22_REV_BTECH_II_1496', '2K21/A18/26', 'CO102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/26', 'ME102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/26', 'MS199', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/26', 'FEC47', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/28', 'MA102', 'F'),
('E22_REV_BTECH_II_1496', '2K21/A18/28', 'AP102', 'C'),
('E22_REV_BTECH_II_1496', '2K21/A18/28', 'EE102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/28', 'CO102', 'C'),
('E22_REV_BTECH_II_1496', '2K21/A18/28', 'ME102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/28', 'MS199', 'O'),
('E22_REV_BTECH_II_1496', '2K21/A18/28', 'FEC28', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/39', 'MA102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/39', 'AP102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/39', 'EE102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/39', 'CO102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/39', 'ME102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/39', 'MS199', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/39', 'FEC1', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/40', 'MA102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/40', 'AP102', 'C'),
('E22_REV_BTECH_II_1496', '2K21/A18/40', 'EE102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/40', 'CO102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/40', 'ME102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/40', 'MS199', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/40', 'FEC1', 'F'),
('E22_REV_BTECH_II_1496', '2K21/A18/41', 'MA102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/41', 'AP102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/41', 'EE102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/41', 'CO102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/41', 'ME102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/41', 'MS199', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/41', 'FEC13', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/51', 'MA102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/51', 'AP102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/51', 'EE102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/51', 'CO102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/51', 'ME102', 'O'),
('E22_REV_BTECH_II_1496', '2K21/A18/51', 'MS199', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/51', 'FEC7', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/58', 'MA102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/58', 'AP102', 'P'),
('E22_REV_BTECH_II_1496', '2K21/A18/58', 'EE102', 'C'),
('E22_REV_BTECH_II_1496', '2K21/A18/58', 'CO102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/58', 'ME102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/58', 'MS199', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/58', 'FEC7', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/67', 'MA102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/67', 'AP102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/67', 'EE102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/67', 'CO102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/67', 'ME102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/67', 'MS199', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/A18/67', 'FEC2', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/72', 'MA102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/72', 'AP102', 'B'),
('E22_REV_BTECH_II_1496', '2K21/A18/72', 'EE102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/72', 'CO102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/72', 'ME102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/A18/72', 'MS199', 'A'),
('E22_REV_BTECH_II_1496', '2K21/A18/72', 'FEC27', 'A'),
('E22_REV_BTECH_II_1496', '2K21/B1/022', 'MA102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B1/022', 'AP102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/B1/022', 'AC102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B1/022', 'ME104', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B1/022', 'ME106', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B1/022', 'MS199', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/B1/022', 'FEC9', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B9/53', 'MA102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/B9/53', 'AP102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B9/53', 'AC102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/B9/53', 'ME104', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B9/53', 'ME106', 'A'),
('E22_REV_BTECH_II_1496', '2K21/B9/53', 'MS199', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/B9/53', 'FEC51', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/B14/09', 'MA102', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/B14/09', 'AP102', 'A'),
('E22_REV_BTECH_II_1496', '2K21/B14/09', 'AC102', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B14/09', 'ME104', 'B+'),
('E22_REV_BTECH_II_1496', '2K21/B14/09', 'ME106', 'A'),
('E22_REV_BTECH_II_1496', '2K21/B14/09', 'MS199', 'A+'),
('E22_REV_BTECH_II_1496', '2K21/B14/09', 'FEC32', 'A')
;
"""
    cur.execute(query)

