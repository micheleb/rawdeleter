#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
from os.path import isfile, join, splitext
import sys

if len(sys.argv) != 2:
    sys.exit('Usage: rawdeleter.py /path/to/folder/containing/raw/images')

root = sys.argv[1]

files = [join(root, f) for f in os.listdir(root) if isfile(join(root, f))]

if not files:
    print('{} does not contain any file'.format(root))
else:
    jpeg_names = [splitext(f)[0] for f in files
                  if splitext(f)[1].lower() in ['.jpg', '.jpeg']]
    raws = {splitext(f)[0]: f for f in files
            if splitext(f)[1].lower() == '.arw'}
    print('root {} contains {} jpegs and {} raw images'
          .format(root, len(jpeg_names), len(raws)))
    delete = [v for k, v in raws.iteritems() if k not in jpeg_names]
    if not len(delete):
        print('No raws without a corresponding jpg. Nothing to do')
        sys.exit(0)
    confirm = raw_input('delete {} raws with no corresponding jpgs? [Y/n] '
          .format(len(delete))).strip().lower()
    if not confirm or confirm == 'y':
        for f in delete:
            os.remove(f)

