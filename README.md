# XPilot AI Driver

Python bots for **XPilot Classic** using the `libpyAI` client API. The main bot in this repo is `algo.py`, which can run **movement**, **attack**, or **defense** modes and is parameterized by a **bitstring genome** (intended for evolutionary tuning).

## What XPilot is
XPilot Classic is a 2D multiplayer space-combat game. Bots connect to a running XPilot server (`xpilots`) and operate in a loop:
- **Sense**: walls (`wallFeeler`), bullets (`shotDist`, `shotVel`, …), enemies (`lockClose`, …), self state (`selfSpeed`, `selfHeadingDeg`, …)
- **Act**: thrust/turn/fire (`thrust`, `turnToDeg`, `fireShot`, …)

This project uses the Python interface exposed by `libpyAI`.

## Files that matter
- **`algo.py`**: canonical bot with 3 modes:
  - `--typ move` (wall-avoidance navigation)
  - `--typ atk` (lock/aim/fire heuristics)
  - `--typ def` (bullet avoidance / dodging heuristics)
- **`bin2num.py`**: helper to decode bit sequences into integers.

## Prerequisites
- XPilot Classic server (`xpilots`) installed and runnable
- Python 3
- `libpyAI` available in your Python environment (provided by XPilot-AI / XPilot tooling)

## Run
Start an XPilot server (example):

```bash
./xpilots -map CI/simple.xp -noQuit -switchBase 1 -port 15345
```

Run the bot (genome as a bitstring):

```bash
python3 algo.py --gene 010101010101010101010101010101010101010101010101 --num 0 --port 15345 --typ move --limit 5000
```

Notes:
- `--gene` can be either a **bitstring** (`0101...`) or a **Python literal list** (legacy).
- Output files are written under `botData/<move|atk|def>/bot_<num>.txt`.

## Genome decoding (high level)
`algo.py` slices the genome into small bitfields and decodes them into numeric parameters like:
- speed limits
- wall reaction distances
- aiming shift/tolerance
- bullet dodge settings

These parameters are then used by the corresponding mode logic.