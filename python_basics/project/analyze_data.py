from parse_jobs import *



def get_department(jobs):
    department = set()
    for job in jobs:
        department.add(job['DEPT'])
    return f"Department: {department}"

jobs = get_department(parse_log(raw_log))
print(jobs)