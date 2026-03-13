
# 🧠 AI Kubernetes Probe Failure Healing Agent

![Kubernetes](https://img.shields.io/badge/Kubernetes-Automation-blue)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-purple)
![Python](https://img.shields.io/badge/Python-Controller-yellow)
![LLM](https://img.shields.io/badge/LLM-Llama3-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)

An **Agentic AI-powered Kubernetes controller** that automatically detects and fixes **probe failures** using **Llama3 (via Ollama)**.

Instead of manually debugging readiness or liveness probe issues, this AI agent:

✔ Detects probe failures
✔ Analyzes pod events
✔ Uses an LLM to determine corrective action
✔ Patches deployment configuration automatically
✔ Restores service health

---

# 🎯 Why This Project Exists

Kubernetes probe failures are one of the most common issues in production environments.

Typical causes:

* Incorrect health check endpoint
* Application startup delays
* Dependency services not ready
* Misconfigured probe timing

These failures often cause **unnecessary pod restarts and service disruption**.

This project demonstrates how **Agentic AI can act as an autonomous SRE assistant** to fix these issues.

---

# 🧠 How the AI Agent Works

The agent runs as a **controller loop** and performs the following steps:

```text
Detect → Analyze → Decide → Act → Verify
```

### Workflow

```text
Kubernetes Cluster
        │
        ▼
Probe Failure Detected
        │
        ▼
Python AI Controller
        │
        ▼
Llama3 (Ollama)
        │
        ▼
Decision Engine
        │
        ▼
Patch Deployment
        │
        ▼
Rolling Restart
        │
        ▼
Service Restored
```

---

# 🏗 Architecture Diagram

```text
              +----------------------+
              |   Kubernetes Cluster |
              +----------+-----------+
                         |
                         ▼
                Probe Failure Event
                         |
                         ▼
                +----------------+
                |  AI Controller |
                |   (Python)     |
                +--------+-------+
                         |
                         ▼
               +------------------+
               | Llama3 via Ollama|
               |  Reasoning Engine|
               +--------+---------+
                         |
                         ▼
                +----------------+
                | Action Engine  |
                | Patch Deploy   |
                +--------+-------+
                         |
                         ▼
                Kubernetes Rolling Restart
```

---

# ⚙️ Tech Stack

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Kubernetes | Container orchestration |
| Python     | AI controller logic     |
| Ollama     | Local LLM runtime       |
| Llama3     | Decision engine         |
| kubectl    | Cluster interaction     |

---

# 📁 Project Structure

```text
probe-healing-agent
│
├── agent.py
├── config.py
├── observer.py
├── actions.py
├── llm_brain.py
│
├── prompts
│   └── probe_prompt.txt
│
└── probe-demo.yaml
```

---

# 🧪 Demo Scenario

We intentionally deploy a workload with a **broken readiness probe**.

Example configuration:

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 80
```

Nginx does not expose `/health`, which produces:

```text
Readiness probe failed
```

The AI agent detects this issue and automatically fixes the probe configuration.

---

# ⚡ Setup Instructions

## 1️⃣ Install Ollama

Install Ollama:

[https://ollama.ai](https://ollama.ai)

Pull the LLM:

```bash
ollama pull llama3
```

Start Ollama:

```bash
ollama serve
```

---

## 2️⃣ Deploy Probe Failure Scenario

```bash
kubectl create namespace prod
kubectl apply -f probe-demo.yaml
```

Check probe failures:

```bash
kubectl describe pods -n prod
```

---

## 3️⃣ Run the AI Agent

```bash
python3 agent.py
```

Example output:

```text
Probe failure detected
LLM Decision: FIX_PROBE_PATH
Deployment patched
Rolling restart triggered
Pods healthy
```

---

# 🤖 AI Decision Actions

The LLM can choose one of the following actions:

| Action                 | Description                  |
| ---------------------- | ---------------------------- |
| FIX_PROBE_PATH         | Correct the health endpoint  |
| INCREASE_INITIAL_DELAY | Increase startup time        |
| DO_NOTHING             | Ignore temporary issue       |
| ESCALATE_TO_HUMAN      | Manual intervention required |

---


