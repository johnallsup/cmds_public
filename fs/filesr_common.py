#!/usr/bin/env python3

import sys,os,re
import uuid,os.path
from icecream import ic; ic.configureOutput(includeContext=True)

class Renamer:
  def __init__(self,forreal = False, overwrite = False, verbose = False):
    self.renner = None
    self.forreal = forreal
    self.verbose = verbose
    self.overwrite = overwrite

  def sr(self,search,replacement):
    def filesr(filename):
      return filename.replace(search,replacement)
    self.renner = filesr

  def srx(self,search,replacement):
    regex = re.compile(search)
    def filesr(filename):
      try:
        m = regex.search(filename)
        if m is None and self.verbose:
          print(f"File {filename} does not match {s}")
        return regex.sub(replacement,filename)
      except Exception as e:
        ic(f"Regex {search} failed for file {filename}",e)
        return None
    self.renner = filesr

  def tr(self,search,replacement):
    trans = str.maketrans(search,replacement)
    def filesr(filename):
      return filename.translate(trans)
    self.renner = filesr

  def process(self,filenames):
    while True:
        t = str(uuid.uuid4())
        if not os.path.exists(t):
            break
    print("Temp name {}".format(t))
    temp_name = t
    for x in filenames:
      y = self.renner(x)
      if y is None:
        print(f"replacment func failed for {x}")
        continue
      if x == y:
        pass
      elif os.path.exists(y):
        sx = os.stat(x)
        sy = os.stat(y)
        if not sx.st_ino == sy.st_ino:
          print("{} already exists".format(y))
        else: # x and y are the same file
          print("Capitalisation issue")
          print(f"Using temp name {t}: {x} --> {y}")
          self.rn(x,t)
          self.rn(t,y)
      else:
          print(f"Rename {x} --> {y}")
          self.rn(x,y)

  def rn(self,x,y):
    if x == y:
      print(f"No change in {x}")
      return
    if self.forreal:
      if os.path.exists(y):
        print(f"{y} exists")
      if self.overwrite:
        try:
          print(f"Overwritten {y}")
          os.rename(x,y)
        except IsADirectoryError:
          print(f"{y} is a directory")
      else:
        os.rename(x,y)
          

