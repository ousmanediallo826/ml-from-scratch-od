
parsed_jobs = []
raw_log = "./files/data.txt"
def parse_log(raw_log):
    parsed_jobs = []
    with open(raw_log, "r") as file:
        for line in file:
            parts = line.strip().replace('"', '').split()
            pairs = [part.split("=") for part in parts]
            convert_dict = dict(pairs)
            parsed_jobs.append(convert_dict)
    return parsed_jobs


print(parse_log(raw_log))