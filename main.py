from os import listdir
from os.path import isfile, join
import re
import json

base_path = "icons/hero-icons"
catagories = listdir(base_path)

data = []
for catagory in catagories:
    path = base_path + "/" + catagory
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        svgPath = path + "/" + file
        svg=""
        with open(svgPath) as f:
            svg = f.read()
        svg = re.sub(r'(stroke=\"((?!none).*?)\")',' stroke="currentColor"', svg)
        svg = re.sub(r'(fill=\"((?!none).*?)\")',' fill="currentColor"', svg)
        svg = re.sub(r' width=\"[^\"]*\"', '', svg)
        svg = re.sub(r' height=\"[^\"]*\"', '', svg)

        name = "hero-icons" + "/" + catagory + "/" + file
        value = svg

        data.append({
            'name' : name,
            'value': value
        })

with open("icons.json", "w") as outfile:
    json.dump(data, outfile)