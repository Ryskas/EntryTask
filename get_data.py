import requests
import csv
import os

url = "http://localhost:8080/api/jobs/"

response = requests.get(url)


if response.status_code == 200:

    data = response.json()
    print(len(data["results"]))

    for item in data["results"]:
        assignee = item.get("assignee")
        type = item.get("type")
        status = item.get("status")
        state = item.get("state")


        if assignee != None:
            id = assignee.get("id")
            file = f"{id}.csv"
        else:
            file = f"None.csv"
        
        file_exists = os.path.exists(file)

        with open(file, 'a') as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(["Assignee","Type", "State", "Status"])

            if assignee != None:
                writer.writerow([assignee, type, state, status])  
            else:  
                writer.writerow(["None", type, state, status])

else:
    print(f"Failed: {response.status_code}")

