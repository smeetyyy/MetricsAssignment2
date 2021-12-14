import json
from selenium import webdriver

metrics_values = {}
with open("Output_metrics.txt", 'w') as outfile: # This opens a output_metrics.txt file where output of url and duration is save
    #the following is the file location of the webdriver
    chromebrowser = webdriver.Chrome(executable_path="C:/Users/stefa/PycharmProjects/SM2/chromedriver.exe")
    # The following is the loop up to 10 times for getting metrics
    for metric in range(10):

        chromebrowser.get("https://en.wikipedia.org/wiki/Software_metric")
        metrics = chromebrowser.execute_script('return window.performance.getEntries()')
        # The above is a javascript command to get metrics entries
        # The following is a loop to get values of name as url and duration
        for m in metrics:

            url = m['name']
            # This is for getting the name from metrics
            metrics_list = metrics_values.get(url, [])
            metrics_list.append(m['duration'])
            # The above is to get the duration of metrics
            metrics_values[url] = metrics_list
            outfile.write(f"{m['name']}, {m['duration']}\n")

            #The above gets the values which are also written in the output text file

 # The following creates a csv file and calculates the average duration
with open("avrduration.csv", "w") as csv_file:
    for key, value in metrics_values.items():
        average = sum(value) / len(metrics_values)
        csv_file.write(f"{key}, {average}\n")

# This makes a JSON output file and prettifies it
with open("json_output" + ".json", "w", encoding="utf-8") as json_file:
    json.dump(metrics, json_file, ensure_ascii=False, indent=4)

chromebrowser.sleep(5)
chromebrowser.quit() #this closes the browser