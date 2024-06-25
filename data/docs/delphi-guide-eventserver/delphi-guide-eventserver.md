Raw data reconstruction is possible for the years 1992 and later, for individual events, via the DELPHI event server, `des`.

## Requirements
Running the even server requires access to the full DELPHI database, as well as the DELPHI raw data samples. It can be run from a container with access to the EOS file system, or locally from a machine with access to CVMFS and EOS.

## Running the DELPHI event server

A quick overview over the options is available from the tool itself, by just running

```
[delphi $] des
```

It supports different modes:

* `list` mode just lists raw data for individual events.
* `pick` mode selects individual events from raw data. The resulting output file is of type *raw*.
* `delana` mode picks an event from raw data and runs the reconstruction code on it, returning a full dst file
* `dstana` mode picks the event from raw data and runs first the reconstruction and then the dst creation on it. The result is either [short DST](/record/80506)` for the LEP1 phase, or [extended short DST](/record/80505) for LEP2.

The *wired* option is no longer supported as the wired code no longer exists.

Example:

```
[delphi $] des -m dstana -e 84078:10815
```

The options are

* `-m dstana <mode>` selects the mode *<mode>* to run in. Supported values for *<mode>* are `list`, `pick`, `delana` or `dstana`.
* `-e 84078:10815` defines the event. The first number is the run number, the second the event number in this run. Please make sure that run and event numbers do not contain any leading zeros, e.g. using `-e 084078:0010815` will **not** work.

Note that reading the database can take a bit of time when it is read over the network so be patient. To speed this up, you can copy it locally and update the environment variable `DELPHI_DDB` to point to the local copy.

By default, `des` creates a temporary working directory in /tmp which also contains the output. Output files, including intermediate files, can be found in this temporary folder after the program has finished.
