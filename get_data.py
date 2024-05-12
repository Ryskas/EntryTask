import requests
import csv

url = "http://localhost:8080/api/jobs/"

response = requests.get(url)


if response.status_code == 200:

    data = response.json()
    print(len(data["results"]))

    for item in data["results"]:
        assignee = item.get("assignee")
        status = item.get("status")

        if assignee != None:
            id = assignee.get("id")
            file = f"{id}.csv"

            with open(file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([assignee, status])
        else:
            with open("None.csv", mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["None", status])


    
    
else:
    print(f"Failed: {response.status_code}")

