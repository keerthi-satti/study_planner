import csv

input_file = "study_input.csv"
output_file = "study_output.csv"

with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    data = []
    for row in reader:
        subject = row[0]
        weekly_hours = int(row[1])
        daily_hours = round(weekly_hours / 7, 2)
        data.append([daily_hours])

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Daily_Hours"])
    writer.writerows(data)

print("Daily study plan generated successfully.")