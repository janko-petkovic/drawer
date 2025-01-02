# Tchumatchenko Ubuntu Server Setup

Step by step log on how the two ubuntu servers were setup.
For the OS we chose Ubuntu Server 22.04 LTS.

At the time of writing we have two Ubuntu servers, with same specifics:

1. Uranus (Tchumatchenko Lab, sudo user jankopetkovic)
2. Tethys (Tchumatchenko Lab, sudo user jankopetkovic)

## Before installation

1. Create the bootable USB in the usual manner (`dd` on linux, idk on windows or
   mac)
2. Insert the key, connect mouse, keyboard, LAN and power, fire up the server.
3. The first time, especially if the servers come with windows, it'll take a lot
   of time for them to post. Wait a *lot* and Lenovo will pop up on the screen.
4. **Enter bios** (press `F1`) and **disable secure boot**. Save and restart.
5. **Enter boot menu**: press `F12` (or `F10`) during the Lenovo screen. Boot
   from the USB

## OS installation

1. Select language (English I guess)
2. I continued without updating the installer
3. Setup keyboard layout
4. Install **Ubuntu server** (not minimized), and tick the **third party driver
   search** for NVIDIA
5. Let the guy setup the LAN connection (`eno1` with `DHCPv4` in my case, it
   could take a bit)
6. Don't setup any proxies
7. Accept the default mirrors
8. Storage: I went for custom storage layout:
   1. reformat the main drive
   2. add a GPT partition in the free space (max size, `xfs` filesystem, mounted
      on `/`)
      You end up with 3.72 Tb of `xfs` on `/`, and roughly 1 Gb of `fat32` on
      `/boot/efi`.
      Since we had only 1 physical volume per machine, there was no need to setup
      logical volumes with LVM. In that case maybe go for something like RAID1/5
9. Names: I put "Tchumatchenko Lab" as "Your name". The rest is up to you. The
   server names are taken from greek titans (bc they are so powerful wow).
10. Skip ubuntu pro
11. Install OpenSSH server as we'll need it later
12. Tick "Install third party drivers" (nvidia drivers)
13. Don't pick popular snaps
14. Stare at the screen while installing
15. Reboot (take out the USB when it asks to do so)

## After installation

1. `sudo apt update && sudo apt upgrade`
2. Packages that I needed to install manually: `pip`, `python3.12-venv`,
   `nvidia-cuda-toolkit`, `network-manager`
3. Activate the firewall `sudo ufw enable`
4. Setup quotas if you want

### Setup and test nvidia drivers

**Setup nvidia drivers**:

1. despite the guy asking, some drivers could still be missing
2. following https://ubuntu.com/server/docs/nvidia-drivers-installation: run
   `sudo ubuntu-drivers install --gpgpu nvidia:550`. This package seems to
   contain all the possible drivers, despite officially referring to the desktop
   550 version. Wtf.
3. you should be able to load the new driver with `sudo modprobe nvidia`

**Test the drivers**:

1. Create a virtual environment `python -m venv testenv`
2. Activate the VE `source testenv/bin/activate`
3. Check that `pip` and `python` are from your environment (`which pip`, `which
   python`)
4. Install torch `pip install torch`
5. Open a torch console, import `torch` and check the output of
   `torch.cuda.is_available()`: it has to be `true`.

If you followed the previous step but you are still are getting `false`, that's
where the troubleshooting begins. Best of luck. 

### `ssh` setup

By default, `ufw` blocks incoming and outgoing traffic for each port. To allow
ssh login from remote clients, we proceed as follows:

1. `/etc/ssh/sshd_config`
   - change the default port to 12345 (default 22 is not very safe)
   - decide if to use password authentication or key-pair authentication
     (everything is enabled by default I think)
2. open the selected port in the firewall: `ufw allow <port_nr>/tcp comment
   'open alternative ssh port'`
3. limit incoming login attempts: `ufw limit <port_nr>/tcp comment 'SSH port
   rate limit'`

In order to allow users to have a reliable config `.ssh` file, we want to
reserve a static ip for the servers. For this, we follow the steps on
https://www.freecodecamp.org/news/setting-a-static-ip-in-ubuntu-linux-ip-address-tutorial/:

1. create a new file `/etc/netplan/01-static-ip-config.yaml`
   
   ```{yaml}
   network:
    renderer: networkd
    ethernets:
        <ethernet-device>:
            dhcp4: false
            addresses: [<static address to reserve>]
            gateway4: <gateway ip>
   
    version: 2
   ```
   
   The ethernet device was `eno4` in my case. 
   For the static address, I used `131.220.127.46/32` on `uranus` and `131.220.127.47/32` on `tethys`.
   The gateway address is the first ip that pops out after running `ip r | grep
   ^def` (after 'via').

2. run `sudo netplan try` to attempt applying the new configuration. Check if
   everything is working as expected (e.g. ping google to see if the network
   crashed). **Remember**: if anything is wrong, just delete the config file you
   created and rerun `sudo netplan try`; everything should go back to normal.
   Don't panic and format everything from scratch.

3. if you're happy, run `sudo netplan apply` to confirm the changes.

### `docker` setup

Follow directly the [official documentation](https://docs.docker.com/engine/install/ubuntu/). To enable the usage of
`docker` for non-sudo users, implement the [group trick](https://docs.docker.com/engine/install/linux-postinstall/).





**Notes to self**:

Nvidia drivers:

- try installing manually the drivers, deselecting the third-party drivers
  during the main installation
- is there any difference between installing 550 with and without the `--gpgpu`
  flag?
