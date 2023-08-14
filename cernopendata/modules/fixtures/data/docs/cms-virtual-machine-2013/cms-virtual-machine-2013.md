The CMS-specific VM includes the [ROOT framework](http://root.cern.ch/) and [CMSSW](http://cms-sw.github.io/). Follow the instructions below to setup a CERN Virtual Machine on your computer for 2013 CMS Open Data. Then, go to [Getting Started with CMS 2013 and 2015 Heavy-Ion Open Data][getstartedcms]

1. [How to install a CERN VM](#vbox)
2. [How to Test & Validate?](#test)
3. [Issues & Limitations](#issue)

## <a name="vbox"> Step 1: How to install a CERN Virtual Machine</a>

### Installing VirtualBox

VirtualBox is a free, open source and multiplatform application to run virtual machines: you can [download][installVB] the package for your platform from the Downloads page.

You will need administrative ("root") privileges on every platform to perform the installation of VirtualBox.

Note: the latest tested version of VirtualBox working with this CMS-specific CernVM image is 7.0.4. If you have troubles with other versions of VirtualBox, pick that one: the full history of VirtualBox versions is available [on a different page][installVB2].


### Downloading and Creating a Virtual Machine

**Important**: Before you download the CernVM, note that the imported settings may not always work on your host machine. Please see [Issues and Limitations](#issue) or [the CMS guide to troubleshooting](/docs/cms-guide-troubleshooting) if you encounter any problems with booting the VM.

Next download the CMS-specific CernVM image as OVA file from: [CMS VM Image for 2011 CMS Open Data][cmsvmimage2011]. It is recommended using the version "CMS-OpenData-1.5.3". This VM Image is the same that is used for data from 2011 and 2012, but the CMS software version to be used is different.

By double clicking the downloaded file, VirtualBox imports the image with ready-to-run settings. In VirtualBox version 6 or later, you need to unselect "import disks as VDI" on the initial import screen. Before launching the image, change the network settings: select the image from the left bar of the VirtualBox window, go to Settings and select Networks and change the network setting for network adaptor 2 to "NAT". Then, launch the CMS-specific CernVM, which boots into the graphical user interface and sets up the CMS environment. Then, be patient, the boot will take a while.


## <a name="test">Step 2: How to Test & Validate?</a>

The validation procedure tests that the CMS environment is installed and operational on your virtual machine, and that you have access to the CMS Open Data files. It gives you a quick introduction to the CMS environment. You may skip this step if you want, and head straight to [Getting Started with CMS 2013 and 2015 Heavy-Ion Open Data][getstartedcms].

### Set up the CMS environment and inspect file contents

In the "CMS-OpenData-1.5.3" VM, open a terminal from the "CMS Shell" icon from the desktop as shown in the figure (note that the X terminal emulator from an icon bottom-left of the VM screen opens a shell with an operating system incompatible with the CMS software release to be used but can be used e.g. for the git commands or ROOT).

<img src="/static/docs/cms-virtual-machine-2013/cms_vm_2013_1.png" width="70%">

Execute the following commands; first to select the build architecture corresponding to the CMSSW version that is needed, and then to build the local release area (the directory structure) for CMSSW. This only needs to be run once (note that it may take a while):

```
cmsrel CMSSW_5_3_20
```

Note that if you get a warning message about the current OS being SLC7, you are using a wrong terminal. Open a "CMS Shell" terminal as explained above and execute the cmsrel command there.

Change to the ```CMSSW_5_3_20/src/``` directory:

```
cd CMSSW_5_3_20/src/
```

Then, run the following command to create the CMS environment:

```
cmsenv
```

To test that the environment is properly set up, you can try a CMSSW command and see that it works. For example, you can run a helper script to inspect the contents of a CMS open data file:

```
edmDumpEventContent root://eospublic.cern.ch//eos/opendata/cms/hidata/HIRun2013/PAHighPt/RECO/28Sep2013-v1/10000/0006E29D-F02B-E311-8A9D-003048CB7A80.root
```

On slower connnections, this may take a while, not because of data access itself, but because evoking the script triggers downloading things to the local cache of the VM. Next occasions will be faster.

You can consider your VM "validated" — i.e it gets access to the CMS software, and reads the CMS Open Data files — if you get an output like:


```
Type                                  Module                      Label             Process
----------------------------------------------------------------------------------------------
L1GlobalTriggerObjectMapRecord        "hltL1GtObjectMap"          ""                "HLT"
edm::TriggerResults                   "TriggerResults"            ""                "HLT"
trigger::TriggerEvent                 "hltTriggerSummaryAOD"      ""                "HLT"
ClusterSummary                        "clusterSummaryProducer"    ""                "reRECO"
EBDigiCollection                      "selectDigi"                "selectedEcalEBDigiCollection"   "reRECO"
EEDigiCollection                      "selectDigi"                "selectedEcalEEDigiCollection"   "reRECO"
[...]
vector<reco::Vertex>                  "offlinePrimaryVertices"    ""                "reRECO"
vector<reco::Vertex>                  "offlinePrimaryVerticesWithBS"   ""                "reRECO"
vector<reco::Vertex>                  "pixelVertices"             ""                "reRECO"
vector<reco::VertexCompositeCandidate>    "generalV0Candidates"       "Kshort"          "reRECO"
vector<reco::VertexCompositeCandidate>    "generalV0Candidates"       "Lambda"          "reRECO"
```

## <a name="issue">Known Issues & Limitations</a>

### Known Issues FAQ

**Question:** The following error message appears when the Virtual Machine is started: "Could not start the machine CMS Open Data because the following physical network interfaces were not found: vboxnet0 (adapter 2). You can either change the machine's network settings or stop the machine."

> **Answer:** Change the Network settings for adapter 2 from "Host-only Adapter" to "NAT". The VM should then start correctly.

**Question:** What is the root password for the CMS Open Data VM?

> **Answer:** The root password for the CMS Open Data VM is password.

**Question:** The CMS Open Data VM does not open correctly

> **Answer:** In some versions of VirtualBox, it has happened that the CMS Open Data VM does not open correctly. This was the case for example for VirtulBox 5.0.32, but more recent versions from the VirtualBox website have been tested and are working properly. Note that it can take a while to launch the CMS Open Data VM for the first time.

**Question:** In VirtualBox version 6, importing the CMS Open Data VM gives an error message '<vbox:Machine> element in OVF contains a medium attachment for the disk image but the OVF describes no such image.'

> **Answer:** Uncheck the default option "Import hard drives as VDI" in the VirtualBox import menu. It may also happen that the folder in which VirtualBox writes the images ('/users/[username]/VirtualBox VMs') does not get created. In this case you can create it manually.

**Question:** When/after installing CERN VM, I get a message that my VM uses too much memory

> **Answer:** Reduce the memory allocated to VirtualBox by clicking on System in the VirtualBox graphical user interface and adjust the base memory with the sliding bar.

**Question:** When I try to compile with 'scram b', I get a warning 'SCRAM warning: You are trying to compile/build for architecture slc6_amd64_gcc493 on SLC7 OS which might not work. If you know this SCRAM_ARCH/OS combination works then please first run 'scram build --ignore-arch'.'

> **Answer:** You are very likely in the wrong shell of the VM machine. When using the "CMS-OpenData-1.5.X" VM, all CMSSW-specific commands (compilation, run) must be given in the "CMS Shell", which can be opened from the desk top icon, not in the "Outer shell".

**Question:** On Ubuntu running the latest version of VirtualBox, an error appears when opening the CMS-specific virtual machine: the message is about a missing path to a definition file.

> **Answer:** To fix this, open one of the (non-CMS-specific) CernVMs first, after which the CMS-specific one should load without the error message.

**Question:** An error message appears: "VT-X/AMD-V hardware acceleration is not available on your system. Your 64-bit guest will fail to detect a 64-but CPU and will not be able to boot."

> **Answer:** When the host machine is booting (just after switching it on) press the appropriate function key to get to the setup, go to advanced settings, and enable the virtualisation extensions of the CPU.

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
[cmsvmimage2011]: </record/252>
[getstartedcms]: </docs/cms-getting-started-hi-2013-2015>
