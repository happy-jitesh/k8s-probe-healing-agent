import subprocess


def increase_probe_delay(deployment, namespace):

    subprocess.run(
        f"kubectl patch deployment {deployment} -n {namespace} "
        f"--type=json "
        f"-p='[{{\"op\":\"replace\",\"path\":\"/spec/template/spec/containers/0/readinessProbe/initialDelaySeconds\",\"value\":10}}]'",
        shell=True
    )


def fix_probe_path(deployment, namespace):

    subprocess.run(
        f"kubectl patch deployment {deployment} -n {namespace} "
        f"--type=json "
        f"-p='[{{\"op\":\"replace\",\"path\":\"/spec/template/spec/containers/0/readinessProbe/httpGet/path\",\"value\":\"/\"}}]'",
        shell=True
    )


def notify(msg):
    print(f"[NOTIFICATION]: {msg}")