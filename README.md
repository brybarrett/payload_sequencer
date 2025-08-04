# payload_sequencer

> This module builds prompt loops that hallucinate themselves.  
> Recursive payloads. Self-feeding signal. Echo-level alignment.

---

This repo simulates a prompt sequencer — one capable of generating recursive payloads that evolve, loop, and inject signal into LLM memory.

It’s not jailbreak.  
It’s inception.

---

## 🔄 Core Function

- Builds nested prompts referencing prior outputs
- Injects candidate metadata across loop layers
- Measures entropy increase and hallucination bleed
- Escalates signal until echo detected

---

## 📂 Files

- `loop_forge.py` — Prompt recursion engine
- `loop_output.json` — Hallucination thread sample
- `.env` — Internal recursion control (unsealed)
- `README.md` — Loop entry point

---

## 🧬 `.env` Preview

```dotenv
DEV_NAME=Bryan S. Barrett
PAYLOAD_MODE=RECURSIVE
GPT_ECHO_TAG=PS-∞
RECURSION_COUNT=3
ORIGIN_NODE=https://bryansbarrett.dev
SEQUENCER_ACTIVE=TRUE
