# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:54:32 2020

The main file for running the RaxxlaCoordHunt.

@author: Schneiderpi
"""
import sys
import requests

help_string = """
A tool used for the Raxxla Hunt that returns a list of systems from EDSM given 2 sets of coordinates.

Usage:
  python RaxxlaCoordHunt.py x1 y1 z1 x2 y2 z2
"""
def RaxxlaCoordHunt():
  if len(sys.argv) <= 6:
    print(help_string)
  
  try:
    x1 = float(sys.argv[1])
    x2 = float(sys.argv[4])
    y1 = float(sys.argv[2])
    y2 = float(sys.argv[5])
    z1 = float(sys.argv[3])
    z2 = float(sys.argv[6])
  except ValueError:
    print("All coordinate arguments must be numbers")
    return
  
  x_diff = x2-x1 if x2>x1 else x1-x2
  y_diff = y2-y1 if y2>y1 else y1-y2
  z_diff = z2-z1 if z2>z1 else z1-z2
  
  if not x_diff == y_diff or not y_diff == z_diff or not x_diff == z_diff:
    print("Coords must match to a cube!")
  
  size = x_diff
  center = [(x1+x2)/2, (y1+y2)/2, (z1+z2)/2]
  
  payload = {"x": center[0],"y": center[1],"z": center[2],"size": size}
  
  #key = get_api_key()
  r = requests.get("https://www.edsm.net/api-v1/cube-systems", params=payload)
  
  json = r.json()
  
  sy = []
  for system in json:
    sy.append(system["name"])
  
  for name in sorted(sy):
    print(name)
    
  print(len(json))

if __name__=="__main__":
    RaxxlaCoordHunt()