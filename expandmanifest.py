#!/usr/bin/python

import json
import os
import shutil
from base.bungie import manifest


def DumpDir(obj, path, depth):
  with open(path + '.json', 'w') as f:
    json.dump(obj, f, indent=4, sort_keys=True)

  if depth and isinstance(obj, dict):
    os.mkdir(path)
    for k, v in obj.iteritems():
      DumpDir(v, '%s/%s' % (path, k), depth - 1)


if __name__ == '__main__':
  man = manifest.Manifest()
  shutil.rmtree('definitions/', ignore_errors=True)
  DumpDir(man['definitions'], 'definitions', 2)
