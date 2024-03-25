import re

def key(result):
    result = result[0]
    match = re.search("\d+$", result)
    start, end = match.span()
    return int(result[start:end])



def migration(cur):

    query = """
select result, semester, heirarchy from result_heirarchy
"""

#     cur.execute(query)
#     results = list(cur.fetchall())
#     results.sort(key=key)
#     new_results = []
#     for i in range(len(results)):
#         new_results.append([results[i][0], results[i][1], i+1])
#     results = new_results

#     query = f"""
# replace into result_heirarchy(result, semester, heirarchy) values {','.join([f"('{result[0]}', {result[1]}, {result[2]+100})" for result in results])}
# """
#     cur.execute(query)

#     query = f"""
# replace into result_heirarchy(result, semester, heirarchy) values {','.join([f"('{result[0]}', {result[1]}, {result[2]})" for result in results])}
# """
#     cur.execute(query)

    cur.execute("set @row_number = 0;")
    query = """
update result_heirarchy as A join
(SELECT
    (@row_number:=@row_number+1) as new_heirarchy,
    result
FROM
    result_heirarchy rh
order by 
    REGEXP_SUBSTR(result, '\\d+$') asc,
    result asc
) as B on A.result = B.result
set A.heirarchy = B.new_heirarchy+1000;
    """
    cur.execute(query)

