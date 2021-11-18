import csv
import json

from datetime import datetime, timedelta

with open("./data/neos.csv", "r") as infile:
    reader = csv.reader(infile)
   # Q1
    data = list(reader)
    print(f"Ans1: Total number of data points is: {len(data) - 1}")
    # Q2
    pde = data[1][3]
    print(f"Ans2: Primary designation is: {pde}")

with open("./data/neos.csv", "r") as infile:
    reader_dict = csv.DictReader(infile)
    total_count = []
    total_diameters_count = []

    for e in reader_dict:
        if e["name"] == "Apollo":
            print(f'Ans3: The diameter is: {e["diameter"]}')
            # print(e)



with open("./data/neos.csv", "r") as f:
    reader_names = csv.DictReader(f)

    for e in reader_names:
        if e["name"] != "":
            total_count.append(e)
        if e["diameter"] != "":
            total_diameters_count.append(e)




print(f"Ans4: Neos having IAU Names: {len(total_count)}")
print(f"Ans5: Neos having diametrs in the data set: {len(total_diameters_count)}")
contents_data = []
ref_date = datetime(2000, 1, 1)

with open("./data/cad.json", "r") as f:
    contents = json.load(f)
    print(type(contents))
    print(f'Ans6: Total count of close approaches are: {contents["count"]}')
    contents_data = contents["data"]
    print(type(contents_data))

    for d in contents_data:
        dt = datetime.strptime(d[3], "%Y-%b-%d %H:%M")

        if dt.date() == ref_date.date() and d[0] == "2015 CL" :
            vel = round(float(d[4]), 3)
            print(f'Ans7: How close was ,the NEO whose primary designation is "2015 CL", pass by Earth on January 1st, 2000: {vel} au')

        if dt.date() == ref_date.date() and d[0] == "2002 PB":
            num = round(float(d[7]), 2)
            print(f'Ans8: How fast did,the NEO whose primary designation is "2002 PB", pass by Earth on January 1st, 2000: {num} km/s')




