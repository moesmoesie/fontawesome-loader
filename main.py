from os import listdir
from os.path import isfile, join
import json

data = {}

paths = [
    "brands", 
    "solid",
    "regular"
]

github = 'https://raw.githubusercontent.com/moesmoesie/fontawesome-loader/master'

for path in paths:
    localPath = "fontawesome-6.1.2-web/svgs/" + path
    onlyfiles = [f for f in listdir(localPath) if isfile(join(localPath, f))]
    for file in onlyfiles:
        name = path + "/" + file.split(".")[0]
        value = github + "/" + localPath + "/" + file
        data[name] = value

with open("fontawesome.json", "w") as outfile:
    json.dump(data, outfile)