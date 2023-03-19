#!/usr/bin/env python3
import os
import glob
import json

json_files = glob.glob("./data/*.json")

general_json_data = []

for i in json_files:
    fp = open(i)
    json_data = json.load(fp)
    general_json_data.append(json_data)
    fp.close()

out_fp = "./generated/resturants_flisa.json"
os.makedirs(os.path.dirname(out_fp), exist_ok=True)
with open(out_fp, "w", encoding="utf-8") as f:
    json.dump(general_json_data, f, ensure_ascii=False, indent=4)
