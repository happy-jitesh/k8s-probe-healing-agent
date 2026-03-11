import time

from observer import get_probe_failures
from llm_brain import llm_decide
from actions import increase_probe_delay, fix_probe_path, notify
from config import *

with open("prompts/probe_prompt.txt") as f:
    SYSTEM_PROMPT = f.read()


def controller():

    notify("Probe Healing Agent Started")

    while True:

        failed, context = get_probe_failures(NAMESPACE, APP_LABEL)

        if not failed:
            notify("No probe failures detected")
            time.sleep(CHECK_INTERVAL)
            continue

        notify("Probe failure detected")

        decision = llm_decide(context, SYSTEM_PROMPT)

        notify(f"LLM Decision: {decision}")

        if decision == "INCREASE_INITIAL_DELAY":
            increase_probe_delay(DEPLOYMENT_NAME, NAMESPACE)

        elif decision == "FIX_PROBE_PATH":
            fix_probe_path(DEPLOYMENT_NAME, NAMESPACE)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    controller()