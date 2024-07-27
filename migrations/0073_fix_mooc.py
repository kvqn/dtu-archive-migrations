
def migration(cur):
    cur.execute("update result_grades set subject = 'MOOC303*' where result = 'O23_BTECH_V_R1_1654' and subject = 'MOOC303'")
    cur.execute("update result_grades set subject = 'MOOC301*' where result = 'O23_BTECH_V_R1_1654' and subject = 'MOOC301'")
