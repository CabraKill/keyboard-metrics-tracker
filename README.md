# keyboard-metrics-tracker

A python keyboard tracker to show metrics for most used keys.

## Access

You will need to give access to keystrokes on mac at least. This should be prompted for you by your system.

* Mac
  * Enable the terminal on Input Monitoring
  * Enable the terminal on Acessibility

```bash
open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"
```

* OSError: Error 13 - Must be run as administrator

```bash
sudo python3 main.py
```

## Env

* Install

```bash
python3 -m venv .venv && \
source .venv/bin/activate && \
pip3 install pynput
```

* Source it and run

```bash
source .venv/bin/activate && python3 main.py
```
