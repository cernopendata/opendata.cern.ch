Learn how to use the ALICE virtual machine to have a first look at ALICE events and use analysis tools:

1. ["How do I start the ALICE software?"](#start)
2. [“How should I use the graphics user interface?”](#gui)
3. ["But where is ALICE data?"](#data)
4. ["How can I see the content of ALICE data?"](#content)

## <a name="start">"How do I start the ALICE software?"</a>

After successfully installing the ALICE VM you should contextualise it as described here [link to installation guide](/docs/alice-virtual-machine). Note that you should pick from the CernVM market the "ALICE OpenAccess" item from the list of available ALICE contexts. When starting the VM, this will automatically login the user “alice” (password “alice”) and start a graphical user interface allowing to run the ALICE masterclasses as well as a basic tutorial on how to run a custom analysis on ALICE data. There is no need to setup the software; both the software tools and the environment are automatically set to use the supplied analysis tools.

<img src="/static/docs/getting-started-with-alice/get_started_1.png" width="70%" align="middle">

## <a name="gui">“How should I use the graphics user interface?”</a>

The interface can be quit at any time by clicking the `Exit` button. To re-enter the interface, one can type in a terminal:

```shell
[alice@localhost analysis]$ root masterclass.C
```

Just a fast introduction on what the ROOT program is. This is an object-oriented analysis toolkit widely used in high-energy physics among many other fields. ROOT can be used as a library to link in your program - the ALICE software is built like that - or to run simple C++ programs in the form of macros, such as the user interface `masterclass.C`. You may want to have a closer look of what ROOT is an how you can use it if you want to go deeper and write your own analysis for ALICE data.

Coming back to the user interface, you will notice that every analysis module or masterclass is represented as a separate tab which can be clicked and will present a different interface for each module. In general, these contain an `Info` button, some data or parameter selection interface and the `Exit` button. Clicking the picture button for each analysis module will run the selected module with the selected dataset and settings. Just follow the instructions provided with each example.

You can bring up the general documentation for the masterclasses by clicking the big picture button with the ALICE logo:

<img src="/static/docs/getting-started-with-alice/get_started_2.png" width="70%" align="middle">

## <a name="data">"But where is ALICE data?"</a>

You do not need to manually download the data, it will be automatically downloaded when you run a given module. The interface will allow you in some cases to select a given dataset, then it will download it in a local folder. In general, every module will create a local folder on the VM file system: `/home/alice/analysis/`. For example, the “Pt” analysis will create the folder `/home/alice/analysis/PtAnalysis` and download the selected data in folders like `data/LHC2010b_pp_ESD_117222/0000/AliESDs.root`

## <a name="content">"How can I see the content of ALICE data?"</a>

ALICE data are written in ROOT format, which allows to store objects like events, tracks, vertices in a compact form and read them with random access. You can use the ROOT program to open any of the data files having the extension `.root` and inspect their content, but you will have to write a simple program to do a bit more than that. You can do this after you get more familiar with ROOT and with the tutorials available in the ALICE VM.

