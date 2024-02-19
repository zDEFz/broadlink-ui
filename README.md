# broadlink-ui
Hacked together UI for Broadlink devices like the Broadlink RM4 Pro

# Depends
- https://github.com/mjg59/python-broadlink
- https://github.com/topics/tkinter-python
- https://github.com/TkinterEP/ttkthemes
- https://github.com/mjg59/python-broadlink/tree/master/cli

# Installation
```bash
git clone https://github.com/zDEFz/broadlink-ui
cd ~/broadlink-ui
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
yay python-broadlink
```
# Configuration

Please follow https://github.com/mjg59/python-broadlink/tree/master/cli
```bash
nano KITCHEN.device
# 0x5213 192.168.178.98 ec0baed88fcb
<yourdeviceidentifier> <IP> <deviceID>
```


# Running regularly
Currently we just use broadlink_cli and broadlink_discovery binaries.
Therefore, we need to run from the binaries.
Admittedly, this is not the best solution.

```bash
function broadlink_ui() {
  cd ~/broadlink-ui
  source venv/bin/activate
  python3 broadlink_ui.py
}
```
![Broadlink_ui](https://raw.githubusercontent.com/zDEFz/broadlink-ui/main/broadlink-ui.png)
