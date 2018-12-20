from csv import DictReader
from csv import DictWriter
from os.path import isfile
from os import environ
from os.path import join


inpath = environ['PATH_TO_UNUM']

baseoutpath = environ['UNUM_OUT_PATH']

count = 0

with open(inpath) as f:
  reader = DictReader(f, delimiter="\t")
  for line in reader:
    count += 1
    country_code = line["country_code"].lower() or "unknown"
    outpath = join(baseoutpath, country_code + ".tsv")
    if isfile(outpath):
      f = open(outpath, "a")
      writer = DictWriter(f, fieldnames=reader.fieldnames)
    else:
      f = open(outpath, "w")
      writer = DictWriter(f, fieldnames=reader.fieldnames)
      writer.writeheader()
    writer.writerow(line)
    f.close()

    if count % 100000 == 0:
      print("processed ", float(count)/38000000)
