#!/usr/bin/python3
def converter(filein,fileout,filelog):
 blocksize=9
 print ("convert py")
 
 while True:
  s=filein.read(blocksize)
  if not s:
   break
  print ("convert data",s)
  s2=filelog.read(blocksize)
  if not s2:
   break
  fileout.write(s)
  fileout.write(s2)
  s=filein.read(blocksize)
  if not s:
   break
