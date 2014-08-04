import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import glob
import json
from app import app
from app.util.vinspect import extract_json, get_frame
from pprint import pprint


print "Writing data to", sys.argv[1]
files = glob.glob(app.config['VIDEOS_DIRECTORY'] + '/*.*')
print "Processing:"
results = []
for idx, file in enumerate(files):
    print " ->", file
    base = os.path.basename(file)
    info = json.loads(extract_json(file))
    info['filename'] = file
    info['basename'] = base
    info['title'] = base.split('.')[0].upper().replace('_', ' ')
    get_frame(file)
    results.append(info)
with open(sys.argv[1], 'w') as outfile:
    json.dump(results, outfile, indent=4)
