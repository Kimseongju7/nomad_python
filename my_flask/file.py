import csv

def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["Company", "Title", "Description", "URL"])
    for job in jobs:
        writer.writerow(list(job.values()))