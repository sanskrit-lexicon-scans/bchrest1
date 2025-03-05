# coding=utf-8
""" make_js_index.py for story of VIDŪṢAKA
"""
from __future__ import print_function
import sys, re, codecs
import json

def roman_to_int(roman):
 droman_int = {'I':1, 'II':2, 'III':3, 'IV':4,
                'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,
                'X':10, 'XI':11, 'XII':12,'':0}
 if roman in droman_int:
  return droman_int[roman]
 else:
  # error condition
  return None
 
# global parameters
parm_regex_split = '\t' #    r'[ ]+'
parm_numcols = 4
parm_numparm = 1
# parm_vol = r'^(I|II|III)$'
parm_page = r'^([0-9]+)$'
# parm_adhy = r'^([0-9]+)$'
parm_fromv = r'^([0-9]+)([b])?$'  # the 2nd part not used
parm_tov = r'^([0-9]+)([a])?$'    # the 2nd part not used
parm_ipage = r'^([0-9]+)$'
parm_vpstr_format = '%03d'  # pdf has 459 pages

class Pagerec(object):
 """
Format of nala index
page	from v.	to v.	ipage
232	1	9	214

Note the first line (column names) is ignored
""" 
 def __init__(self,line,iline):
  line = line.rstrip('\r\n')
  self.line = line
  self.iline = iline
  parts = re.split(parm_regex_split,line)
  self.status = True  # assume all is well
  self.status_message = 'All is ok'
  if len(parts) != parm_numcols:
   self.status = False
   self.message = 'Expected %s values. Found %s value' %(parm_numcols,len(parts))
   return
  # give names to the column values
  # raw_vol = parts[0]  
  raw_page = parts[0] # internal to volume. digits
  # raw_adhy = parts[1]
  raw_fromv = parts[1]
  raw_tov = parts[2]
  raw_ipage = parts[3]
  # check page 
  m_page = re.search(parm_page,raw_page)
  if m_page == None:
   self.status = False
   self.status_message = 'Unexpected page: %s' % raw_page
   return
  # check fromv 
  m_fromv = re.search(parm_fromv,raw_fromv)
  if m_fromv == None:
   self.status = False
   self.status_message = 'Unexpected fromv: %s' % raw_fromv
   return
  # check tov 
  m_tov = re.search(parm_tov,raw_tov)
  if m_tov == None:
   self.status = False
   self.status_message = 'Unexpected tov: %s' % raw_tov
   return
  # check ipage
  m_ipage = re.search(parm_ipage,raw_ipage)
  if m_ipage == None:
   self.status = False
   self.status_message = 'Unexpected ipage: %s' % raw_ipage
   return ipage
  # set self.page as integer
  self.page = int(m_page.group(1))
  # set self.adhy as integer
  #self.adhy = int(m_adhy.group(1))
  # set self.fromv as integer
  self.fromv = int(m_fromv.group(1))
  x1 =  m_fromv.group(2)
  if x1 == None:
   self.fromvx = ''
  else:
   self.fromvx = x1;
  # set self.tov as integer
  self.tov = int(m_tov.group(1))
  x2 =  m_tov.group(2)
  if x2 == None:
   self.tovx = ''
  else:
   self.tovx = x2;
  # set self.ipage as integer
  self.ipage = int(m_ipage.group(1))
  # vpstr  # format consistent with format of filename of scanned page
  self.vpstr = parm_vpstr_format % self.page

 def todict(self):
  if self.fromvx == None:
   self.fromx = ''
  e = {
   'page':int(self.page),
   # 'adhy':int(self.adhy),
   'v1':int(self.fromv), 'v2':int(self.tov),
   'x1':self.fromvx, 'x2':self.tovx,
   'ipage':int(self.ipage),
   'vp':self.vpstr
  }
  return e

def init_pagerecs(filein):
 """ filein is a csv file, with first line as fieldnames
 """
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for iline,line in enumerate(f):
   if (iline == 0):
    # assert line.startswith('volume') # skip column-title line
    print('Skipping column title line:',line)
    continue
   pagerec = Pagerec(line,iline)
   if pagerec.status:
    # No problems noted
    recs.append(pagerec)
   else:
    lnum = iline + 1
    print('Problem at line # %s:' % lnum)
    print('line=',line)
    print('message=',pagerec.status_message)
    exit(1)
 print(len(recs),'Success: Page records read from',filein)
 return recs


def make_js(recs):
 outarr = []
 outarr.append('indexdata = [')
 arr = [] # array of Python dicts
 for rec in recs:
  d = rec.todict()  # a Python dictionary
  arr.append(d)
 return arr

def write_recs(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('indexdata = \n')
  jsonstring = json.dumps(data,indent=1)
  f.write( jsonstring +  '\n')
  f.write('; // end of indexdata\n')
  
 print('json data written to',fileout)

def unused_check1_adhy(pagerecs):
 prev = None
 for irec,rec in enumerate(pagerecs):
  lnum = rec.iline + 1
  line = rec.line
  if irec == 0:
   # first record has adhy = 1
   if rec.adhy != 1:
    print('check1_adhy: first adhy not 1.')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
   prev = rec
   continue
  if prev.adhy == rec.adhy:
   pass # no problem
  elif (prev.adhy + 1) == rec.adhy:
   pass
  else:
   # unexpected
   print('check1_adhy. adhy=%s, expected %s' %(rec.adhy,prev.adhy + 1))
   print('lnum=%s, line=%s' % (lnum,line))
   exit(1)
  # reset prev
  prev = rec
 print('pagerecs passes check1_adhy ')
 

def check1(pagerecs):
 """ check that v1 = v2_prev + 1 when 
 """
 # check1_adhy(pagerecs)
 
 nerr = 0
 for irec,rec in enumerate(pagerecs):
  lnum = rec.iline + 1
  line = rec.line
  if irec == 0:
   # first verse should be 1
   if rec.fromv != 1:
    print('first verse not 1')
    #print('check1_adhy: first adhy not 1.')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)    
   prev = rec
   continue
  # rec.adhy = prev.adhy
  if (rec.fromvx == '') and (prev.tovx == ''):
   if rec.fromv != (prev.tov + 1):
    print('fromv problem A')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
  else:
   if (prev.tovx == 'a') and (rec.fromvx == 'b') and (rec.fromv == prev.tov):
    # no problem
    pass
   else:
    print('fromv problem B')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
  prev = rec
 print("check1 finds no problems")


if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 pagerecs = init_pagerecs(filein)
 outrecs = make_js(pagerecs)
 write_recs(fileout,outrecs)
 check1(pagerecs)
 
 
