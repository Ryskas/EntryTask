import requests
import csv
import os


def CreateCSV(file, values):
    """
    Creating csv file from the values in the argument
    """
    file_exists = os.path.exists(file)

    with open(file, 'a') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Assignee","Type", "State", "Status"])

        writer.writerow(values)  


def GetValues(url):
    """
    Fetching data from url and calls `CreateCSV` 
    """
    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()

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
            
            if assignee != None:
                CreateCSV(file, [assignee, type, state, status])  
            else:  
                CreateCSV(file, ["None", type, state, status])

    else:
        print(f"Failed: {response.status_code}")


if __name__ == "__main__":

    url = "http://localhost:8080/api/jobs/"

    GetValues(url)
