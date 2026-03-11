import subprocess


def get_probe_failures(namespace, label):

    cmd = f"kubectl describe pods -n {namespace} -l {label}"
    output = subprocess.getoutput(cmd)

    if "Readiness probe failed" in output:
        return True, output

    if "Liveness probe failed" in output:
        return True, output

    return False, ""