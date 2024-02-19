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
# nano BEDROOM.device
# 0x5213 192.168.178.98 ec0baed88fcb
<yourdeviceidentifier> <IP> <deviceID>

# nano broadlink_ui.py
# adjust as needed

device_path = "/home/blu/broadlink/BEDROOM.device"
file_path = "/home/blu/broadlink/broadlink-devices.json"
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
# Usage
You left click a button to send the comman.d
You right click a button to copy the open a menu to copy the command line.
Would get you for instance `broadlink_cli --device @/home/blu/broadlink/BEDROOM.device --send @/home/blu/broadlink/RME/ADI2-DAC-FS/1-ana`

![08ece0fd-528a-4955-9804-ecc05fc8ddda](https://github.com/zDEFz/broadlink-ui/assets/24463722/7d21de93-0343-4321-adce-d55087924e49)
