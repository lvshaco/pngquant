set SVN_RES=http://i.shengjoy.com/gd/svn/wa-client/trunk/bin
svn export %SVN_RES%/GUI00 GUI00 --force 
svn export %SVN_RES%/res/char res/char --force 
svn export %SVN_RES%/res/eff res/eff --force 
svn export %SVN_RES%/res/field res/field --force 
svn export %SVN_RES%/res/item res/item --force 
python png_compress.py GUI00
python png_compress.py res/char
python png_compress.py res/eff
python png_compress.py res/field
python png_compress.py res/item
pause
