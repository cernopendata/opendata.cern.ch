The CMS-specific VM includes the [ROOT framework](http://root.cern.ch/) and [CMSSW](http://cms-sw.github.io/). Follow the instructions below to setup a CERN Virtual Machine on your computer for 2010 CMS Open Data. Then, go to [Getting Started with CMS data](/docs/cms-getting-started-2010)

1.  [How to install a CERN VM](#install2010)
2.  [How to Test & Validate?](#testvalidate2010)
3.  [Issues & Limitations](#issues2010)

## <a name="install2010"></a>Step 1: How to install a CERN Virtual Machine

### Installing VirtualBox

VirtualBox is a free, open source and multiplatform application to run virtual machines: you can [download](https://www.VirtualBox.org/wiki/Downloads) the package for your platform from the Downloads page.

You will need administrative ("root") privileges on every platform to perform the installation of VirtualBox.

Note: the latest tested version of VirtualBox working with this CMS-specific CernVM image is 6.1.10\. If you have troubles with the latest version of VirtualBox, pick that one: the full history of VirtualBox versions is available [on a different page.](https://www.VirtualBox.org/wiki/Download_Old_Builds)

### Downloading and Creating a Virtual Machine

**Important**: Before you download the CernVM, note that the imported settings may not always work on your host machine. Please see [Issues and Limitations](#issues2010) or [the CMS guide to troubleshooting](/docs/cms-guide-troubleshooting) if you encounter any problems with booting the VM.

Next download the CMS-specific CernVM image as OVA file from: [CMS VM Image for 2010 CMS Open Data](/record/250). It is recommended using the version "CMS-OpenData-1.1.4".

By double clicking the downloaded file, VirtualBox imports the image with ready-to-run settings. In VirtualBox version 6, you need to unselect "import disks as VDI" on the initial import screen. Then, you launch the CMS-specific CernVM, which boots into the graphical user interface and sets up the CMS environment. Be patient, it will take a while.

## <a name="testvalidate2010"></a>Step 2: How to Test & Validate?

The validation procedure tests that the CMS environment is installed and operational on your virtual machine, and that you have access to the ROOT files. You may skip this step if you want, and head straight to [Getting Started with CMS data](/docs/cms-getting-started-2010). However, these steps give you a quick introduction to the CMS environment.

### Set up the CMS environment and run a demo analyzer

In the "CMS-OpenData-1.1.4" VM, open a terminal from the "CMS Shell" icon from the desktop (note that the X terminal emulator from an icon bottom-left of the VM screen opens a shell with an operating system incompatible with the CMS software release to be used).

Execute the following command; this command builds the local release area (the directory structure) for [CMSSW](/glossary/CMSSW), and only needs to be run once (note that it may take a while):

```shell
cmsrel CMSSW_4_2_8
```

Note that if you get a warning message about the current OS being SLC7, you are using a wrong terminal. Open a "CMS Shell" terminal as explained above and execute the cmsrel command there.

Change to the <kbd>CMSSW_4_2_8/src/</kbd> directory:

```shell
cd CMSSW_4_2_8/src/
```

Then, run the following command to create the CMS runtime variables:

```shell
cmsenv
```

Create a working directory for the demo analyzer, change to that directory and create a "skeleton" for the analyzer:

```shell
mkdir Demo
cd Demo
mkedanlzr DemoAnalyzer
```

Compile the code:

```shell
cd DemoAnalyzer
scram b
```

Change the file name in the configuration file <kbd>demoanalyzer_cfg.py</kbd> in the DemoAnalyzer directory: i.e. replace <kbd>file:myfile.root</kbd> with <kbd>root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0000/00459D48-EB70-E011-AF09-90E6BA19A252.root</kbd>

Change the max number of events to 10 (i.e change -1 to 10 in <kbd>process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1)</kbd>).

Move two directories back using:

```shell
cd ../..
```

And then run:

```shell
cmsRun Demo/DemoAnalyzer/demoanalyzer_cfg.py
```

You can consider your VM "validated" — i.e it gets access to and compiles the CMS software, and reads the CMS open data files — if you get an output like:

```shell
08-Sep-2014 10:48:11 CEST Initiating request to open file root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0000/00459D48-EB70-E011-AF09-90E6BA19A252.root
08-Sep-2014 10:48:21 CEST Successfully opened file root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0000/00459D48-EB70-E011-AF09-90E6BA19A252.root
Begin processing the 1st record. Run 146436, Event 90626440, LumiSection 322 at 08-Sep-2014 10:48:25.836 CEST
Begin processing the 2nd record. Run 146436, Event 90634848, LumiSection 322 at 08-Sep-2014 10:48:25.839 CEST
Begin processing the 3rd record. Run 146436, Event 90649368, LumiSection 322 at 08-Sep-2014 10:48:25.839 CEST
Begin processing the 4th record. Run 146436, Event 90668184, LumiSection 322 at 08-Sep-2014 10:48:25.840 CEST
Begin processing the 5th record. Run 146436, Event 90703728, LumiSection 322 at 08-Sep-2014 10:48:25.842 CEST
Begin processing the 6th record. Run 146436, Event 90716480, LumiSection 322 at 08-Sep-2014 10:48:25.843 CEST
Begin processing the 7th record. Run 146436, Event 90735104, LumiSection 322 at 08-Sep-2014 10:48:25.844 CESTBegin processing the 8th record. Run 146436, Event 90745896, LumiSection 322 at 08-Sep-2014 10:48:25.844 CEST
Begin processing the 9th record. Run 146436, Event 90755600, LumiSection 322 at 08-Sep-2014 10:48:25.845 CEST
Begin processing the 10th record. Run 146436, Event 90778200, LumiSection 322 at 08-Sep-2014 10:48:25.849 CEST
08-Sep-2014 10:48:25 CEST Closed file root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0000/00459D48-EB70-E011-AF09-90E6BA19A252.root
MessageLogger Summary
type category sev module subroutine count total
1 fileAction           -s file_close                             1        1
2 fileAction           -s file_open                              2        2
type category Examples: run/evt run/evt run/evt
1 fileAction           PostEndRun
2 fileAction           pre-events       pre-events
Severity # Occurrences Total Occurrences
System 3 3
```

## <a name="issues2010"></a>Known Issues & Limitations

### Validation report

The CMS-specific CERN Virtual Machine has been tested on several operating systems, VM softwares and hardware configurations. However, we cannot guarantee that it will work under all conditions. Problems can often be traced to a user’s particular system settings.

Solutions to some of the common problems encountered are listed below. [This validation report](/VM/CMS/validation/report) contains more information, including a full list of tested machines and configurations, along with issues faced during testing.

### Known Issues FAQ

**Q:** The following error message appears when the Virtual Machine is started: "Could not start the machine CMS Open Data because the following physical network interfaces were not found: vboxnet0 (adapter 2). You can either change the machine's network settings or stop the machine."

**A:** Change the Network settings for adapter 2 from "Host-only Adapter" to "NAT". The VM should then start correctly.

**Q:** What is the root password for the CMS Open Data VM?

**A:** The root password for the CMS Open Data VM is password.

**Q:** The CMS Open Data VM does not open correctly

**A:** In some versions of VirtualBox, it has happened that the CMS Open Data VM does not open correctly. This was the case for example for VirtulBox 5.0.32, but more recent versions from the VirtualBox website have been tested and are working properly. Note that it can take a while to launch the CMS Open Data VM for the first time.

**Q:** In VirtualBox version 6, importing the CMS Open Data VM gives an error message '<vbox:Machine> element in OVF contains a medium attachment for the disk image but the OVF describes no such image.'

**A:** Uncheck the default option "Import hard drives as VDI" in the VirtualBox import menu. It may also happen that the folder in which VirtualBox writes the images ('/users/[username]/VirtualBox VMs') does not get created. In this case you can create it manually.

**Q:**  When/after installing CERN VM, I get a message that my VM uses too much memory

**A:** Reduce the memory allocated to VirtualBox by clicking on System in the VirtualBox graphical user interface and adjust the base memory with the sliding bar.

**Q:** On Ubuntu running the latest version of VirtualBox, an error appears when opening the CMS-specific virtual machine: the message is about a missing path to a definition file.

**A:** To fix this, open one of the (non-CMS-specific) CernVMs first, after which the CMS-specific one should load without the error message.

**Q:** On Windows 7 and 8, this error message appears: "VT-X/AMD-V hardware acceleration is not available on your system. Your 64-bit guest will fail to detect a 64-but CPU and will not be able to boot."

**A:** Check whether your processor supports the VT-X feature by going to [http://ark.intel.com/](http://ark.intel.com/): Intel® Virtualisation Technology (VT-x) should be checked as "yes". Then, when the host machine is booting (just after switching it on) press the appropriate function key to get to the setup, go to advanced settings, and enable the virtualisation extensions of the CPU. Note that some recent Acer Inspire laptop models do not give access to the VT-X feature in the BIOS setup even if the processor supports it.

**Q:** The VM does not inherit the keyboard layout of the host machine.

**A:** The layout can be changed by using setxkbmap from a terminal inside the Virtual Machine. For example a user with a Swiss keyboard with French variant would type <kbd>setxkbmap 'ch(fr)'</kbd> in the terminal and a user with a Finnish keyboard would type <kbd>setxkbmap fi</kbd>. This can also be solved by using the GUI, which can be launched either from the graphical menu in the lower left corner (Preferences → Keyboard) or by typing in the console: xfce4-keyboard-settings. In the Layout tab it is possible to change the keyboard model and the layout. If you wish to keep these settings after reboot, you should delete all the other layouts from the menu.

**Q:** The default terminal does not accept (not even from the clipboard) nor display certain language-specific characters such as [umlauts](http://en.wikipedia.org/wiki/Diaeresis_%28diacritic%29).

**A:** Using a terminal such as xterm will allow reading and writing special characters.

**Q:** Users who use high resolutions on small displays and have set their host machines DPI manually, for example through <kbd>.Xresources</kbd> on Linux (X11), may find that everything is too small to be read efficiently. (Also helpful to users who have difficulties in reading the fonts and other visual information on the image due to the size of the graphical components.)

**A:** The DPI can easily be adjusted from Xfce menu → Preferences → Appearance → Fonts → DPI. This enhances the readability and general usability significantly.

**Q:** Resizing the VM window doesn't resize its contents.

**A:** This appears to only occur when a new VM image is launched for the first time. The contents should resize after several minutes (up to half an hour), and the problem should not manifest when the VM image is opened a second time.
