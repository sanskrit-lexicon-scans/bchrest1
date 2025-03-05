
# convert index.txt to index.js and move to app3/ folder

python make_js_index.py index.txt index.js
cp index.js ../index.js  # move up to app3 directory

-------------------------------------------------
Preliminary file copying:
# cd to this app3/pywork directory
--- for index.txt
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93/vid/index.txt .

--- for make_js_index.py
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93/vid/make_js_index.py .


