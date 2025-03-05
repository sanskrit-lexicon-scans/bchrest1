
https://github.com/sanskrit-lexicon-scans/bchrest1/

cd /c/xampp/htdocs/sanskrit-lexicon-scans/bchrest1

mkdir app1  for nala
mkdir app1/pywork

-------------------------------------------
# Copy files from other sources.
# These will be adapted to bchrest1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bchrest1

# README.md
# model after 
cp /c/xampp/htdocs/sanskrit-lexicon-scans/sahityadarpana/README.md

# app1/pywork/index.txt
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101/sahd_index_v1.txt app1/pywork/index.txt

# app1/pywork/make_js_index.py
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101/make_js_index.py app1/pywork/make_js_index.py

# app1/index.html, info.html, main.js, main.css
cp /c/xampp/htdocs/sanskrit-lexicon-scans/yajnyavalkya/app1/index.html app1/index.html

cp /c/xampp/htdocs/sanskrit-lexicon-scans/yajnyavalkya/app1/info.html app1/info.html

cp /c/xampp/htdocs/sanskrit-lexicon-scans/yajnyavalkya/app1/main.css app1/main.css

cp /c/xampp/htdocs/sanskrit-lexicon-scans/yajnyavalkya/app1/main.js app1/main.js


-------------------------------------------
# bchrest1/README.md
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bchrest1
# manual edit README.md
# commit and push to github


-------------------------------------------
# app1/index.js
cd /c/xampp/htdocs/sanskrit-lexicon-scans/bchrest1/app1/pywork
# follow instructions in app1/pywork/readme.txt to get app1/index.js

-------------------------------------------------
# app1/index.html
Manual edit
1. <title>bchrest1</title>
2. <span style="font-size:20px;">Sāhityadarpaṇa by Viśvanātha, James R. Ballantyne, 1851</span>

-------------------------------------------------
# app1/info.html
Manual edit
1. <title>bchrest1 info</title>
2. <span style="font-size:20px;">Sāhityadarpaṇa by Viśvanātha, James R. Ballantyne, 1851</span>

-------------------------------------------------
# app1/main.js
Various changes
The app for bchrest1 takes
 2 numeric parameters  (adhyAya, verse)

pdf file names: bchrest-NNN.pdf   NNN is the 'external' page number
  NNN range 001 - 497 

-------------------------------------------------
