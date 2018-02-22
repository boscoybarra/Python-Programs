import urllib.request
import csv
import os

errorCount=0

file_list = "/Users/$USER/Desktop/YOUR-FILE-TO-DOWNLOAD-IMAGES/image_{0}.jpg"

# CSV file must separate by commas
# urls.csv is set to your current working directory make sure your cd into or add the corresponding path
with open ('urls.csv') as images:
    images = csv.reader(images)
    img_count = 1
    print("Please Wait.. it will take some time")
    for image in images:
        try:
            urllib.request.urlretrieve(image[0],
            file_list.format(img_count))
            img_count += 1
        except IOError:
            errorCount+=1
            # Stop in case you reach 100 errors downloading images
            if errorCount>100:
                break
            else:
                print ("File does not exist")

print ("Done!")
