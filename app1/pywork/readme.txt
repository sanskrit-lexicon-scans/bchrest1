
# convert index.txt to index.js and move to app1/ folder

python make_js_index.py index.txt index.js
cp index.js ../index.js  # move up to app1 directory

-------------------------------------------------
Preliminary file copying:
# cd to this app1/pywork directory
--- for index.txt
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93/nala/index.txt .

--- for make_js_index.py
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93/nala/make_js_index.py .


