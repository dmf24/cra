print "running..."
import sys
import os
import aux.jobs
from datetime import datetime
"""
#Interface for running run_cra from php
"""

"""
Toolbox for working with LOGS
"""

CONTACT_EMAIL = "<contact-email>"

def add_line_to_log(log_file, line):
    with open(log_file, "a") as lfil:
        lfil.write(str(line) + "\n")

if __name__ == '__main__':
    sys.stdout.write('%s\n' % os.getcwd())
    sys.stdout.flush()
    sys.stderr.flush()
    tag=datetime.today().strftime("%Y%m%d-%H%M%S-%f")
    opfile="interface.%s.out" % tag
    erfile="interface.%s.err" % tag
    os.environ['CRA_SCRATCH']='/n/groups/kirschner_www/corecop/'
    command_string = "python run_cra.py %s" % ' '.join(sys.argv[1:])
    sys.stdout.write(command_string + "\n\n")
    job = aux.jobs.Job(command_string)
    job.run(wait=False, output=opfile, error=erfile)
    sys.stdout.write("done\n")
