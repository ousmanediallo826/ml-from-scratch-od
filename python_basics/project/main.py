from parse_jobs import *
from analyze_data import *


def format_job(job):
    """Formats a single job dictionary into a clean string."""

    status = "SUCCESS" if job['RC'] == '0000' else "FAILED"
    return f"[{job['DEPT']}] {job['JOBNAME']} | RC: {job['RC']} | Runtime: {job['TIME']} | Status: {status}"
def format_jobs(jobs):
    if not jobs:
        return "No jobs found."
    return "\n".join([format_job(job) for job in jobs])
def main():
    jobs = parse_log(raw_log)

    print("=============================\n"
          "MAINFRAME JOB LOG ANALYZER\n"
          "=============================\n"
          "1. View Summary Report\n"
          "2. View Successful Jobs\n"
          "3. View Failed Jobs\n"
          "4. List All Departments\n"
          "5. Exit\n")

    while True:
        choice = input("Please enter your choice: (1,2,3,4,5) ")

        if choice == "1":
            s = get_summary(jobs)
            print(f"\n--- SUMMARY REPORT ---")
            print(f"Total Jobs:      {s['total_jobs']}")
            print(f"Successful:      {s['total_successful']}")
            print(f"Failed:          {s['total_failed']}")
            print(f"Avg Runtime:     {s['total_runtime']}s")
            print(f"Departments:     {', '.join(s['departments'])}")

        elif choice == "2":
            success_list = [j for j in jobs if j['RC'] == '0000']
            print("\n--- SUCCESSFUL JOBS ---")
            print(format_jobs(success_list))

        elif choice == "3":
            fail_list = [j for j in jobs if j['RC'] != '0000']
            print("\n--- FAILED JOBS ---")
            print(format_jobs(fail_list))

        elif choice == "4":
            depts = sorted(set(j['DEPT'] for j in jobs))
            print("\n--- DEPARTMENTS ---")
            for d in depts:
                print(f"- {d}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()