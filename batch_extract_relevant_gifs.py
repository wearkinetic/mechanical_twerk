import sys
from subprocess import run, PIPE
with open(sys.argv[1],'r') as f:
    for uuid in f.readlines():
        cmd = 'sh extract_relevant_gifs.sh {:s}'.format(uuid)
        completed_process = run(cmd,shell=True, stdout=PIPE, stderr=PIPE, text=True)
        with open('logs/{:s}.log'.format(uuid),'r') as flog:
            flog.write(completed_process.stderr)
        with open('logs/{:s}.out'.format(uuid),'r') as fout:
            fout.write(completed_process.stdout)
        print('completed processing of {:s}'.format(uuid))
