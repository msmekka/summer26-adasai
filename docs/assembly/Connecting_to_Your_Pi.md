# Connecting to Your Yahboom Pi

*NCSSM Summer 2026 — ADAS AI Lab*

This guide covers every scenario you might encounter when trying to connect to your Yahboom G1 Tank Pi. Work through the scenarios in order — start with Method A and fall back to Method B if needed.

## Quick Reference

| | |
|---|---|
| Yahboom hotspot password | `12345678` |
| Yahboom hotspot IP | `192.168.50.1` |
| SSH username | `pi` |
| SSH password | `yahboom` |
| Jupyter Lab | `http://<pi-ip>:8888` (password: `yahboom`) |
| Find Pi on network | `ping raspberrypi.local` |
| Check WiFi status | `wpa_cli -i wlan0 status` |
| Reconfigure WiFi | `sudo wpa_cli -i wlan0 reconfigure` |
| Check IP address | `ip addr show wlan0` |

## Method A: SSH Over Home Network (Normal)

This is how you connect day-to-day once WiFi is configured. The Pi connects to your home network and you SSH in from your laptop on the same network.

- Make sure your laptop is on your home WiFi network.
- Find the Pi's IP address — check your router's admin page for connected devices, or run:
  ```
  ping raspberrypi.local
  ```
- SSH in:
  ```
  ssh pi@<ip-address>
  ```
- Enter password: `yahboom`

> **TIP:** The Pi's IP can change after a reboot if DHCP assigns a new address. If your saved IP stops working, check your router again.

> **CHECKPOINT:** You should see the `pi@yahboomtank:~ $` prompt. You are connected.

## Method B: Yahboom Hotspot (Fallback)

If the Pi is not on your home network — either because WiFi was never configured or the config was lost — the Pi will broadcast its own hotspot. Use this to get in and fix the WiFi config.

> **WARNING:** You cannot use Claude or browse the internet while connected to the Yahboom hotspot. Have these instructions open before switching networks, or open them on your phone.

- On your laptop, open WiFi settings and scan for networks.
- Look for a network starting with `Yahboom` — something like `Yahboom_XXXXXX`.
- Connect with password: `12345678`
- Open a terminal and SSH in:
  ```
  ssh pi@192.168.50.1
  ```
- Enter password: `yahboom`

> **CHECKPOINT:** You should see the `pi@yahboomtank:~ $` prompt. You are in.

Now fix the home WiFi config so you can switch back:

- Open the WiFi config file:
  ```
  sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
  ```
- The file should contain a network block. If it is missing or wrong, add or fix it:
  ```
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1
  country=US

  network={
      ssid="YourNetworkName"
      psk="YourPassword"
      key_mgmt=WPA-PSK
  }
  ```
- Save and exit: `Ctrl+X`, then `Y`, then `Enter`.
- Reconfigure the WiFi interface:
  ```
  sudo wpa_cli -i wlan0 reconfigure
  ```
- Check for an IP address:
  ```
  ip addr show wlan0
  ```
- Look for an `inet` line with an IP address. If you see one, the Pi is on your home network.
- Note the IP address, then reconnect your laptop to your home WiFi and SSH in normally using Method A.

> **TIP:** The dongle included in the kit is 2.4GHz only. If your network is 5GHz only, the dongle will not connect. Use a 2.4GHz SSID.

## Troubleshooting

**I can't find the Pi on my network**
- Check the Pi's lights — solid red PWR light means it is powered and booted.
- Check your router admin page for connected devices — look for `raspberrypi` or a device with MAC prefix `b8:27:eb` or `dc:a6:32`.
- Try pinging by hostname: `ping raspberrypi.local`
- If no response, fall back to Method B — the Pi may have lost its WiFi config.

**SSH connection refused**
- SSH may not be enabled. This happens on a fresh flash if the `ssh` file was not added to the boot partition.
- Connect via Method B and run:
  ```
  sudo systemctl enable ssh
  sudo systemctl start ssh
  ```

**Wrong password**
- Default password is `yahboom` — all lowercase, no spaces.
- If `yahboom` does not work try `raspberry`.
- If neither works the image may have a custom password — check with MsMekka.

**WiFi connects but no IP address**
- Run the following to check the connection state:
  ```
  wpa_cli -i wlan0 status
  ```
- Look for `wpa_state=` in the output:
  - `COMPLETED` = associated, should have an IP — try: `sudo dhclient wlan0`
  - `SCANNING` = looking for the network — check your SSID spelling
  - `DISCONNECTED` = credentials wrong or network not in range

**resolv.conf permission error when editing DNS**
- The file may be immutable. Unlock it first:
  ```
  sudo chattr -i /etc/resolv.conf
  ```
- Then edit it:
  ```
  sudo nano /etc/resolv.conf
  ```
- Add this line:
  ```
  nameserver 8.8.8.8
  ```

**Pi boots but I can't SSH — connection times out**
- The Pi may still be booting. Wait 60-90 seconds and try again.
- First boot after filesystem expansion takes 3-5 minutes — be patient.
- Check the green ACT light on the Pi — erratic flashing means it is still booting, no light means it is idle and ready.

**Yahboom hotspot not visible**
- The Pi may be connected to your home network successfully — try Method A first.
- Power cycle the Pi and wait 90 seconds for it to fully boot.
- If still not visible, the Pi may not have booted cleanly — check the PWR light.

**Everything was working, now it's not after a power cycle**
- The WiFi config may not have persisted. Connect via hotspot (Method B) and re-add the network block.
- To make the config persistent, run:
  ```
  sudo systemctl enable wpa_supplicant
  ```

## Pi Light Status Guide

| Light | State | Meaning |
|---|---|---|
| PWR (red) | Solid | Pi is powered and running normally |
| PWR (red) | Off | No power — check cable and power supply |
| ACT (green) | Rhythmic flash | Booting — wait for it to settle |
| ACT (green) | Erratic flash | Finishing boot — almost ready |
| ACT (green) | Off | Idle and ready to connect |
| ACT (green) | Rapid constant | High disk activity — filesystem expansion in progress |
| WiFi dongle | Flashing red | Scanning for networks — no connection yet |
| WiFi dongle | Solid or blue/green | Connected to a network |
| Expansion board | Solid blue | Booted cleanly and ready |
| Expansion board | Rapid flash | Power issue — check battery charge |

### Pro Tip: Use Two Terminal Windows

When running component tests or notebooks that might crash the Pi, always keep two SSH sessions open simultaneously.

- Terminal 1: Run your test or notebook
- Terminal 2: Ready to kill a stuck process or reboot if needed

If Terminal 1 hangs, use Terminal 2 to kill the process cleanly:
```
sudo pkill -9 -f <program_name>
```
Or reboot cleanly:
```
sudo reboot
```

> **TIP:** This saves you from having to power cycle the Pi when a program crashes and leaves GPIO pins in a bad state.

---

NCSSM Summer 2026 — ADAS AI Lab — Questions? Ask MsMekka.
