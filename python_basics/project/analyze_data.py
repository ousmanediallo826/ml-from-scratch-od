from parse_jobs import *



def get_department(jobs):
    department = set()
    for job in jobs:
        department.add(job['DEPT'])
    return f"Department: {department}"


def filter_by_status(jobs):
    filtered_jobs = []
    failed_jobs = []

    for job in jobs:
        if job['RC'] == '0000':
            status = f"Success: {job['JOBNAME']}"
            filtered_jobs.append(status)
        else:
            status = f"Failed: {job['JOBNAME']}"
            failed_jobs.append(status)

    return filtered_jobs, failed_jobs




def get_summary(jobs):

    summary = {
        "total_jobs": 0,
        "total_successful": 0,
        "total_failed": 0,
        "departments": set(),
        "total_runtime": 0.0
    }

    for job in jobs:
        if job['JOBNAME']:
            summary["total_jobs"] += 1



        if job['RC'] == '0000':
            summary["total_successful"] += 1
        else:
            summary["total_failed"] += 1

        summary["departments"].add(job['DEPT'])
        summary["total_runtime"] += float(job['TIME'].replace('s', ''))


    summary["average_runtime"] = summary["total_runtime"] / len(jobs)
    return summary



