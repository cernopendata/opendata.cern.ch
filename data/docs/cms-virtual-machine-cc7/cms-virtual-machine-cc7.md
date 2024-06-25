The CMS-specific VM includes the [ROOT framework](http://root.cern.ch/) and [CMSSW](http://cms-sw.github.io/). Follow the instructions below to set it up on your computer for Run2 CMS MiniAOD open data from 2016 - 2018. Then, go to [Getting Started with CMS MiniAOD data][getstartedcms]

1. [How to install a CERN VM](#vbox)
2. [How to set up the CMSSW working area](#test)
3. [Issues & Limitations](#issue)

## <a name="vbox"> Step 1: How to install a CERN Virtual Machine</a>

### Installing VirtualBox

VirtualBox is a free, open source and multiplatform application to run virtual machines: you can [download][installVB] the package for your platform from the Downloads page.

You will need administrative ("root") privileges on every platform to perform the installation of VirtualBox.

Note: the latest version of VirtualBox tested with this CMS-specific CernVM image is 7.0.4. If you have troubles with other versions of VirtualBox, pick that one: the full history of VirtualBox versions is available [on a different page][installVB2].


### Downloading and Creating a Virtual Machine

Download the CMS-specific CernVM image as OVA file from [CMS CC7 VM Image, for CMS MiniAOD open data from 2016 - 2018][cmsvmimagecc7].

By double clicking the downloaded file, VirtualBox imports the image with default settings. In VirtualBox version 6 or later, you need to unselect "import disks as VDI" on the initial import screen. Before launching the image, change the network settings: select the image from the left bar of the VirtualBox window, go to Settings and select Networks and change the network setting for network adaptor 2 to "NAT". Then, launch the CMS-specific CernVM, which boots into the graphical user interface and sets up the CMS environment. Then, be patient, the boot will take a while.


## <a name="test">Step 2: How to set up the CMSSW working area</a>

### Set up the CMS environment

In the "CMS-OpenData-1.6.0" VM, open a terminal from the "CMS Shell" icon from the desktop as shown in the figure (note that the X terminal emulator from an icon bottom-left of the VM screen opens a shell with an operating system that might get updated to become incompatible with the CMS software release to be used but can be used e.g. for the git commands or ROOT).

<img src="/static/docs/cms-virtual-machine-cc7/cms_vm_cc7_1.png" width="70%">

Build the local release area (the directory structure) for CMSSW. This only needs to be run once (note that it may take a while):

```
cmsrel CMSSW_10_6_30
```

Change to the ```CMSSW_10_6_30/src/``` directory:

```
cd CMSSW_10_6_30/src/
```

Set up the CMS environment with:

```
cmsenv
```

Then, head straight to [Getting Started with CMS MiniAOD Open Data](/docs/cms-getting-started-miniaod#data) to see how to acces data.


## <a name="issue">Known Issues & Limitations</a>

### Known Issues FAQ

**Question:** The following error message appears when the Virtual Machine is started: "Could not start the machine CMS Open Data because the following physical network interfaces were not found: vboxnet0 (adapter 2). You can either change the machine's network settings or stop the machine."

> **Answer:** Change the Network settings for adapter 2 from "Host-only Adapter" to "NAT". The VM should then start correctly.


**Question:** What is the root password for the CMS Open Data VM?

> **Answer:** The root password for the CMS Open Data VM is password, but if you need it when starting the VM, something has most likely gone wrong.

**Question:** The CMS Open Data VM does not open correctly

> **Answer:** In some versions of VirtualBox, it has happened that the CMS Open Data VM does not open correctly. This was the case for example for VirtulBox 5.0.32, but more recent versions from the VirtualBox website have been tested and are working properly. Note that it can take a while to launch the CMS Open Data VM for the first time.

**Question:** In VirtualBox version 6, importing the CMS Open Data VM gives an error message '<vbox:Machine> element in OVF contains a medium attachment for the disk image but the OVF describes no such image.'

> **Answer:** Uncheck the default option "Import hard drives as VDI" in the VirtualBox import menu. It may also happen that the folder in which VirtualBox writes the images ('/users/[username]/VirtualBox VMs') does not get created. In this case you can create it manually.

**Question:** When/after installing CERN VM, I get a message that my VM uses too much memory

> **Answer:** Reduce the memory allocated to VirtualBox by clicking on System in the VirtualBox graphical user interface and adjust the base memory with the sliding bar.

<!-- **Question:** When I try to compile with 'scram b', I get a warning 'SCRAM warning: You are trying to compile/build for architecture slc6_amd64_gcc493 on SLC7 OS which might not work. If you know this SCRAM_ARCH/OS combination works then please first run 'scram build --ignore-arch'.'

> **Answer:** You are very likely in the wrong shell of the VM machine. When using the "CMS-OpenData-1.5.X" VM, all CMSSW-specific commands (compilation, run) must be given in the "CMS Shell", which can be opened from the desk top icon, not in the "Outer shell". -->

**Question:** On Ubuntu running the latest version of VirtualBox, an error appears when opening the CMS-specific virtual machine: the message is about a missing path to a definition file.

> **Answer:** To fix this, open one of the (non-CMS-specific) CernVMs first, after which the CMS-specific one should load without the error message.

<!-- **Question:** On Windows 7 and 8, this error message appears: "VT-X/AMD-V hardware acceleration is not available on your system. Your 64-bit guest will fail to detect a 64-but CPU and will not be able to boot."

> **Answer:** Check whether your processor supports the VT-X feature by going to http://ark.intel.com/: Intel® Virtualisation Technology (VT-x) should be checked as "yes". Then, when the host machine is booting (just after switching it on) press the appropriate function key to get to the setup, go to advanced settings, and enable the virtualisation extensions of the CPU. Note that some recent Acer Inspire laptop models do not give access to the VT-X feature in the BIOS setup even if the processor supports it. -->

**Question:** The VM does not inherit the keyboard layout of the host machine.

> **Answer:** The layout can be changed by using setxkbmap from a terminal inside the Virtual Machine. For example a user with a Swiss keyboard with French variant would type ```setxkbmap 'ch(fr)'``` in the terminal and a user with a Finnish keyboard would type ```setxkbmap fi```. This can also be solved by using the GUI, which can be launched either from the graphical menu in the lower left corner (Preferences → Keyboard) or by typing in the console: xfce4-keyboard-settings. In the Layout tab it is possible to change the keyboard model and the layout. If you wish to keep these settings after reboot, you should delete all the other layouts from the menu.

**Question:** The default terminal does not accept (not even from the clipboard) nor display certain language-specific characters such as umlauts.

> **Answer:** Using a terminal such as xterm will allow reading and writing special characters.

**Question:** Users who use high resolutions on small displays and have set their host machines DPI manually, for example through .Xresources on Linux (X11), may find that everything is too small to be read efficiently. (Also helpful to users who have difficulties in reading the fonts and other visual information on the image due to the size of the graphical components.)

> **Answer:** The DPI can easily be adjusted from Xfce menu → Preferences → Appearance → Fonts → DPI. This enhances the readability and general usability significantly.

**Question:** Resizing the VM window doesn't resize its contents.

> **Answer:** This appears to only occur when a new VM image is launched for the first time. The contents should resize after several minutes (up to half an hour), and the problem should not manifest when the VM image is opened a second time.



[installVB]: <https://www.virtualbox.org/wiki/Downloads>
[installVB2]: <https://www.virtualbox.org/wiki/Download_Old_Builds>
[cmsvmimagecc7]: </record/258>
[getstartedcms]: </docs/cms-getting-started-miniaod>
