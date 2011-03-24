import os
import shutil

class ProjectAlreadyExists(Exception):
    pass

class Create(object):

    name = "create"

    def __call__(self, dest_dir, *args, **kwargs):
        while dest_dir.endswith('/'):
            dest_dir = dest_dir[:-1]
        src_dir = os.path.join(os.path.dirname(__file__), "structure")
        if os.path.exists(dest_dir):
            raise ProjectAlreadyExists()
        print "Populating directory %s" % dest_dir
        os.mkdir(dest_dir)
        for base, dirs, files in os.walk(src_dir):
            base_dir = base.replace(src_dir, dest_dir)
            for d in dirs:
                new_dir = os.path.join(base_dir, d)
                print "\tCreating directory %s" % new_dir
                os.mkdir(new_dir)
            for f in files:
                # skipping binaries
                if f.endswith('.pyc'):
                    continue
                orig_path = os.path.join(base, f)
                new_path = os.path.join(base_dir, f)
                print "\tCreating file      %s" % new_path
                shutil.copy2(orig_path, new_path)
        print "You're done!"
        print "Start the app with torn-admin.py start %s" % dest_dir 