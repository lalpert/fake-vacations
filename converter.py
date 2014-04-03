import random
import commands

def convert_images(overlay, background):
    """Return a filename for the new image"""
    filename = "%s.png" % random.randint(0, 0xffffffffffff)
    commands.getstatusoutput("./compositer.sh %s %s ./static/%s" %
            (overlay, background, filename))
    return filename
