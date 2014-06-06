import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:                              
        print "usage : %s path" % sys.argv[0]

    errlist = list() 

    path = sys.argv[1];                    
    files = os.listdir(path)
    for fname in files:
        fname = os.path.join(path, fname)
        name, ext = os.path.splitext(fname)
        if ext != ".png":
            continue
        r = os.system('pngquant.exe --force --verbose --speed=1 --quality=45-85 "%s"'%(fname))
        if r != 0:
            errlist.append((fname, r))
        else:
            os.system('move /Y "%s-fs8.png" "%s.png"'%(name, name))

    if len(errlist) == 0:
        print("===================OK=====================")
    else:
        log = path
        log = log.replace(".", "_")
        log = log.replace("/", "_")
        log = log.replace("\\", "_")
        log = "png_%s.log"%log
        print("!!!something error, please check the %s file"%log)
        f = open(log, "w")
        for v in errlist:
            f.write("%s, %d\n"%(v[0], v[1]))
        f.close()
        os.system(log)
