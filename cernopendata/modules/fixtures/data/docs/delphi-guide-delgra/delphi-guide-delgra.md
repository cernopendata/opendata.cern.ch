## Introduction
The DELPHI event display, also known as 'DELGRA', is used to visualise reconstructed events. This document gives a brief introduction
on how to start up the display.

Important note: The event display only works on reconstructed data, not on raw data.

## Directory structure
DELGRA expects to see a folder called graexe in your home directory, with 4 subfolders in it. These are called `data`, `hcopy`, `macro`, `run`.
In case it does not find the graexe folder, it will try to create them. They have the following meaning

* graexe/data:  Default folder for reconstructed date files which are to be scanned.
* graexe/hcopy: DELGRA allows to print the current view into a file. This is where the output of these screenshots will go.
* graexe/macro: Folder for macros.
* graexe/run:   This folder contains log files from running the program. Consult it in case the program does not work correctly or crashed.

## Starting the event display

Start the event display from a shell from your home directory:

```
cd
rungra
```

It should start up showing an hour glass, and a welcome box, like this:

<p><center><img src="/static/docs/delphi-guide-docker/delgra_startup_1.png" width="60%"></center></p>

After pressing on OK in the welcome box, the program will bring up the file dialog where you can select the folder and the file to be read in:

<p><center><img src="/static/docs/delphi-guide-docker/delgra_startup_2.png" width="60%"></center></p>

Change into the ~/graexe/data folder and select a suitable file.
In the screenshot here, there is a file called `simana.sdst`. This is a short DST file of simulated data, so can be selected for viewing.
Select it and press `Ok` in that dialog.

Next, the event display will ask for the `event number` in this `run` to be read:

<p><center><img src="/static/docs/delphi-guide-docker/delgra_startup_3.png" width="60%"></center></p>

Just press OK or return to start reading the first event.

You will see the first event, can rotate it, zoom in, and analyze it, or you can skip to the next event, going through them one by one. Here's a screen shot of event number 5, viewed at a slightly different angle:

<p><center><img src="/static/docs/delphi-guide-docker/delgra_startup_4.png" width="60%"></center></p>

Note that due to possibly different random number seeds, the sequence may look different for you.

## Event display manual

The event display manual can be found [here](/record/80503)
