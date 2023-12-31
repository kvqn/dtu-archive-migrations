
# This migration file was made by the scraper utility.
# Result PDF : O22_REV_BTECH_I_1559

def migration(cur):

    cur.execute("select min(heirarchy) from result_heirarchy")
    result = cur.fetchall()
    if (result[0][0] is None):
        n_heirarchy = 1
    else:
        n_heirarchy = result[0][0] - 1

    cur.execute(f"insert into result_heirarchy values ('O22_REV_BTECH_I_1559', 1, {n_heirarchy})")

    query = """insert into result_student_details values
('O22_REV_BTECH_I_1559','2K22/A1/13', 'ABHISHEK SHAH', 20, 7.9, '', False),
('O22_REV_BTECH_I_1559','2K22/A6/51', 'ROHIT MEENA', 20, 5.5, '', False),
('O22_REV_BTECH_I_1559','2K22/A10/08', 'RAHUL GUPTA', 20, 9.0, '', False),
('O22_REV_BTECH_I_1559','2K22/A13/61', 'AYAN MAHAJAN', 20, 8.8, '', False),
('O22_REV_BTECH_I_1559','2K22/A13/69', 'DAKSH GUPTA', 20, 9.3, '', False),
('O22_REV_BTECH_I_1559','2K22/A14/20', 'JATIN', 2, 0.7, 'MA101AP101 AC101  ME101, ME103,', False),
('O22_REV_BTECH_I_1559','2K22/A14/29', 'KUNAL THAPLIYAL', 20, 5.5, '', False),
('O22_REV_BTECH_I_1559','2K22/A14/68', 'REYANSH SINHA', 0, 0.0, 'MA101AP101 AC101  ME101, ME103, FEC58,', False),
('O22_REV_BTECH_I_1559','2K22/A15/55', 'YASH VERMA', 20, 4.7, '', False),
('O22_REV_BTECH_I_1559','2K22/B2/29', 'KSHITIJ KUMAR OJHA', 20, 7.3, '', False),
('O22_REV_BTECH_I_1559','2K22/B2/31', 'KUSHAGRA SHRIVASTAVA', 20, 7.1, '', False),
('O22_REV_BTECH_I_1559','2K22/B3/51', 'RACHIT', 16, 4.6, 'MA101', False),
('O22_REV_BTECH_I_1559','2K22/B8/60', 'ABHIGYAN GOYAL', 12, 3.6, 'MA101 CO101,', False),
('O22_REV_BTECH_I_1559','2K22/B18/60', 'VAIBHAV SHARMA', 16, 3.9, 'MA101', False)
;
"""
    cur.execute(query)

    query = """insert into result_grades values
('O22_REV_BTECH_I_1559', '2K22/A1/13', 'MA101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A1/13', 'AP101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A1/13', 'AC101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A1/13', 'ME101', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/A1/13', 'ME103', 'A+'),
('O22_REV_BTECH_I_1559', '2K22/A1/13', 'FEC7', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A6/51', 'MA101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/A6/51', 'AP101', 'B'),
('O22_REV_BTECH_I_1559', '2K22/A6/51', 'AC101', 'B'),
('O22_REV_BTECH_I_1559', '2K22/A6/51', 'ME101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/A6/51', 'ME103', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/A6/51', 'FEC9', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A10/08', 'MA101', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/A10/08', 'AP101', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A10/08', 'AC101', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A10/08', 'ME101', 'A+'),
('O22_REV_BTECH_I_1559', '2K22/A10/08', 'ME103', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A10/08', 'FEC18', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A13/61', 'MA101', 'A+'),
('O22_REV_BTECH_I_1559', '2K22/A13/61', 'AP101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A13/61', 'AC101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A13/61', 'ME101', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A13/61', 'ME103', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A13/61', 'FEC7', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A13/69', 'MA101', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A13/69', 'AP101', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A13/69', 'AC101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A13/69', 'ME101', 'O'),
('O22_REV_BTECH_I_1559', '2K22/A13/69', 'ME103', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A13/69', 'FEC7', 'A+'),
('O22_REV_BTECH_I_1559', '2K22/A14/20', 'MA101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/20', 'AP101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/20', 'AC101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/20', 'ME101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/20', 'ME103', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/20', 'FEC2', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/A14/29', 'MA101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/A14/29', 'AP101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/A14/29', 'AC101', 'B'),
('O22_REV_BTECH_I_1559', '2K22/A14/29', 'ME101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/A14/29', 'ME103', 'A'),
('O22_REV_BTECH_I_1559', '2K22/A14/29', 'FEC32', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/A14/68', 'MA101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/68', 'AP101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/68', 'AC101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/68', 'ME101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/68', 'ME103', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A14/68', 'FEC58', 'F'),
('O22_REV_BTECH_I_1559', '2K22/A15/55', 'MA101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/A15/55', 'AP101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/A15/55', 'AC101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/A15/55', 'ME101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/A15/55', 'ME103', 'C'),
('O22_REV_BTECH_I_1559', '2K22/A15/55', 'FEC54', 'B'),
('O22_REV_BTECH_I_1559', '2K22/B2/29', 'MA101', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/B2/29', 'AP101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/B2/29', 'EE101', 'B'),
('O22_REV_BTECH_I_1559', '2K22/B2/29', 'CO101', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/B2/29', 'ME105', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/B2/29', 'FEC52', 'O'),
('O22_REV_BTECH_I_1559', '2K22/B2/31', 'MA101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/B2/31', 'AP101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/B2/31', 'EE101', 'B'),
('O22_REV_BTECH_I_1559', '2K22/B2/31', 'CO101', 'A'),
('O22_REV_BTECH_I_1559', '2K22/B2/31', 'ME105', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/B2/31', 'FEC48', 'O'),
('O22_REV_BTECH_I_1559', '2K22/B3/51', 'MA101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/B3/51', 'AP101', 'B'),
('O22_REV_BTECH_I_1559', '2K22/B3/51', 'EE101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/B3/51', 'CO101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/B3/51', 'ME105', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/B3/51', 'FEC7', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/B8/60', 'MA101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/B8/60', 'AP101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/B8/60', 'EE101', 'B'),
('O22_REV_BTECH_I_1559', '2K22/B8/60', 'CO101', 'UFM'),
('O22_REV_BTECH_I_1559', '2K22/B8/60', 'ME105', 'B+'),
('O22_REV_BTECH_I_1559', '2K22/B8/60', 'FEC57', 'A+'),
('O22_REV_BTECH_I_1559', '2K22/B18/60', 'MA101', 'F'),
('O22_REV_BTECH_I_1559', '2K22/B18/60', 'AP101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/B18/60', 'EE101', 'P'),
('O22_REV_BTECH_I_1559', '2K22/B18/60', 'CO101', 'C'),
('O22_REV_BTECH_I_1559', '2K22/B18/60', 'ME105', 'C'),
('O22_REV_BTECH_I_1559', '2K22/B18/60', 'FEC52', 'A')
;
"""
    cur.execute(query)

