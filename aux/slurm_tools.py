import subprocess


def srun(job_string, error, out, queue, timelim, wait):
    full_command = "slurm -p " + queue + " -t " + str(timelim) + " -o " + bsub_output + " -e " + bsub_error + " " + command
    proc = subprocess.Popen([full_command])
    if wait:
        proc.wait()
    return proc