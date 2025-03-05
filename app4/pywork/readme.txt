
# convert index.txt to index.js and move to app4/ folder

python make_js_index.py index.txt index.js
cp index.js ../index.js  # move up to app4 directory

-------------------------------------------------
Preliminary file copying:
# cd to this app4/pywork directory
--- for index.txt
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93/vishva/index.txt .

--- for make_js_index.py
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue93/vishva/make_js_index.py .


