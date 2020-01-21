import exifread
import os

from collections import Counter

def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = Counter(seq)
    for k in sorted(counted):
        print('{0:5d} {1}'.format(k, '+' * counted[k]))

def get_focal_length(ratio) -> float:
  f = [int(n) for n in ratio.split('/')]
  if (len(f) == 1):
    return f[0]
  return f[0] / f[1]

files = os.listdir('photos')

fl = []
for file in files:
  # Open image file for reading (binary mode)
  f = open('photos/' + file, 'rb')

  # Return Exif tags
  tags = exifread.process_file(f, details=False)
  for tag in tags.keys():
    # if tag == 'EXIF FocalLength':
    if 'FocalLengthIn' in tag:
      fl.append(get_focal_length("%s" % tags[tag]))

ascii_histogram(fl)
