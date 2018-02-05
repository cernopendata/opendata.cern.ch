The CMS-specific CERN Virtual Machine has been tested on several operating systems, VM softwares and hardware configurations. Below you will find a full list of tested machines and configurations, along with issues faced during testing. Please note that we cannot guarantee that the VM will work under all conditions.

## Overview

### Testing Process

Usually the testing chain starts from setting up the environment from the very start, including installing the host operating system. These host systems are usually installed as a native system, though some systems were only (or in addition) tested as a virtual machine host. For example an iMac with OS X installed on it hosts a Ubuntu virtual machine which in turn hosts the actual Cern VM machine.

Also the process has often included testing images on a system that already has many packages/applications installed and is used daily for different tasks. This is done to find possible conflicts between applications on different setups and to mimic a “normal system” that a person interested in using the CernVM could be using.

On many systems, I also test several GPU drivers and versions. After I've got all the basic necessities to run an operating system, I install some basic drivers or leave the default ones, if there is some. After that I shortly test the functionality of the VM including mostly graphic rendering related stuff such as GUI behaviour and just basic usability. After this I continue to install some more often used and/or powerful drivers, such as Nvidia proprietary drivers over open source Nouveau on some Linux distributions and hardware setups for example. On Windows this stage often consists more of testing different proprietary software driver versions from GPU manufacturers.

After setting up the environment I continue to follow the process mainly the same way as the “User Instructions” wiki page states, producing an .ig file for the event displayer. After reading the data and getting a file, I continue to transferring the file to a location where it's accessible by an operating system running an event displayer and making sure that the produced file actually works.

### Tested Environments

The tested hardware and software has basically depended on availability. Software-wise there has been some limitations mainly due to licensing issues and delays in getting the licenses. These include some delays on testing proprietary operating systems, usually when they have to be installed on new hardware. Also testing of Vmware virtualisation software have been very limited in comparison to VirtualBox mainly due to licensing and differences in the testing process, of course lack of time has its part to play as well. Also, one of the main things that affect the choices when deciding what to prioritise is the size of the user base. For these reasons I've mainly tested the image on VirtualBox when it comes to hypervisors, and that's also the suggested software to be used with the image. Same goes for example for testing outdated/unsupported versions of operating systems.

When it comes to hardware, there hasn't been limitations other than the availability. I've tested several processor and motherboard combinations and a lot of GPUs. Also the amount of RAM has been easy to increase or decrease on some combinations.

### Specific listing of the tested environments

(This is a list of all components used during this testing)


CPUs

*   Intel Core i7-3770K - Overclocked from stock and stable 3.5GHz to unstable 4.9GHz - Completed test chain once with 4.9GHz producing a working file for event displayer. Second time host machine failed to run stable, as expected to happen at some point. No damage/corruption to Virtual Machine.

*   Intel Core i5-4258U

*   Intel Core i7-3635QM

*   Intel Core i5-750

*   Intel Core i7-2600K

*   AMD A10-6700

GPUs

*   Nvidia GeForce GTX 660

*   Nvidia GeForce GTX 660 x2 multi-GPU, Scalable Link Interface (SLI) Nvidia GeForce GTX 560

*   Nvidia GeForce GTS 450

*   Nvidia GT 840M

*   Nvidia GT 650M

*   Intel HD4400 Intel HD5100 Intel HD5200

*   AMD Radeon HD 6750 Graphics

GPU Drivers

*   AMD Catalyst

*   AMD Open Source (xf86-video-ati) Nvidia proprietary

*   Nouveau (for Nvidia cards)

*   Intel graphics

Motherboards (laptops not included)

*   Asus Maximus V Gene mATX Z77

*   Asus P8P67 PRO

*   Gigabyte P55M-UD2

*   Asrock Z68 Extreme3 Gen3

Operating systems

*   Arch Linux

*   Linux Mint

*   Ubuntu

*   Kali Linux

*   Windows Vista

*   Windows 7

*   Windows 8

*   Windows 8.1

*   OS X 10.8

*   OS X 10.9

Desktop Environments

*   KDE

*   Gnome

*   BSPWM

*   DWM

*   Openbox

*   LXDE

*   XFCE

*   Cinnamon

*   Mate

## Results

From the platforms I've tested so far, it seems that the functionality of the guest machines are mainly identical as it is supposed to be. Only differences being the handling of some host depending operations such as transferring files and handling DPI settings. All the problems I've encountered have either depended on fault in host configuration, or it's an issue on every platform.

## Issues

#### DPI
This concerns users who use high resolutions on small displays and have set their host machines DPI manually, for example through `.Xresources` on Linux (X11). The problem is that everything is too small to be read efficiently due to DPI set incorrectly. This can also be helpful to users who have difficulties in reading the fonts and other visual information on the image due to the size of the graphical components.

DPI can easily be adjusted from Xfce menu -> Preferences -> Appearance -> Fonts -> DPI. This enhances the readability and general usability significantly.

#### Hardware virtualisation support
Enabling the "virtual technology" on some hardware combinations is necessary. This can be done from the BIOS/UEFI when host machine is booting by accessing the settings. User should refer to the documentation of the host machine or the documentation of the motherboard to access these settings. Common terms for these are Intel VT-x or AMD-V depending on motherboard.

#### Keyboard layout
The VM doesn’t inherit the keyboard layout of the host machine. The layout can be changed by using `setxkbmap` from a terminal. For example a user with a Swiss keyboard with French variant would type in the console: `setxkbmap` 'ch(fr)' and a user with a Finnish keyboard would do: `setxkbmap` fi.

This can also be solved by using the GUI, which can be launched either from the graphical menu in the lower left corner (Preferences -> Keyboard) or by typing in the console: `xfce4-keyboard-settings`. In the Layout tab it’s possible to change the keyboard model and the layout. To keep these settings after reboot, all the other layouts from the menu should be deleted.

#### Special characters
The default terminal doesn’t accept (not even from clipboard) nor display certain language specific characters such as umlauts. Using an alternative terminal such as xterm will allow reading and writing special characters.

#### Launching applications
The shortcut for the text editor that can be found in the panel points to a wrong application thus producing an error message: Failed to launch “Editor”: Failed to execute child process “mousepad” (No such file or directory).

This can be fixed by referring to the correct application by right clicking the shortcut, choosing properties and changing the command section from “mousepad” to “leafpad”.

Also when opening the web browser, the default home page `file:///usr/share/doc/HTML/index.html` isn't found and doesn't even exist on the image.

#### Terminal color scheme

Colors of the default terminal emulator are pretty unreadable even with good displays. For example some basic commands such as ls will produce too dark output compared against the background to be easy and pleasant to read. This problem is even more true for weaker displays and in a brighter work environment. The colors can be tweaked from the preferences of the terminal emulator, but the default settings should probably be changed.

#### Network

The error message "Could not start the machine CMS Open Data because the following physical network interfaces were not found: `vboxnet0` (adapter 2). You can either change the machine's network settings or stop the machine." comes up with every combination of hardware and software that I have tested. Changing the network adapter 2 to use NAT from Virtual Machine settings fixes the problem.

#### Conflicts between applications

There has been issues in the latest releases of VirtualBox (4.3.14) when used on a host with an antivirus software. The problem is the VirtualBox build, not the antivirus software of choice, and is currently being worked on by Oracle. Upgrading to latest version or to a test build fixes some of these issues and will continue to do so in the future, so highlighting the importance of having the latest version of VirtualBox to the user is important. These problems also seem to rise only when it's a new virtual machine.

#### Host modules

On Linux, it's necessary to manually load VirtualBox kernel modules after host machine's kernel upgrade if the host machine hasn't been rebooted after the update.

#### Kernel headers

Vmware will produce an error about kernel headers not found if they don't exist on the host. After installing and/or upgrading the headers and the kernel, the host machine must be booted to match the versions of current kernel headers.

Some of the issues and solutions I've reported could improve the user experience significantly and make the whole concept to feel more complete and reliable. In addition to improvements on color schemes and other minor fixes such as correcting the text editor shortcut path, the location of shared folders (between host and guest) on the guest could be indicated somewhere. Even if users are familiar with linux mount points and such there are differences between distros (eg. `/media` vs `/mnt`). This is even more important to users who are unable to use scp (Windows users for example) and have to use shared folders and find the created folder from the guest machine.