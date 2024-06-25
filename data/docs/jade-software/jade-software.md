## <a name="und">Understanding JADE software</a>

JADE software description can be found in the JADE computing notes and elsewhere.
Briefly it consists of approximately 50.000 lines of IBM Fortran77 and similar codes
that were compiled on AIX4.3 systems with IBM Fortran compiler and corresponding runtime.
The dependencies include CERNLIB.

## <a name="port">JADE software content</a>
The reviewed JADE software from 2003 is described elsewhere.
In the presented package the MC generator codes are dropped (not ported) and
three more components are added:

directory convert: the convert utility to produce .cprod files from moders forma MC records.
directory picocernlib to replace the CERNLIB routines
directory jtuple package that performs the analysis and was used in the past~\cite{Schieck:2012mp}.
All of the packages above use the cmake as a build system.
The directory examples contains the setups for MC production (external generators are needed) and simulation, data reconstruction,
event display usage.



## <a name="port">Porting JADE software</a>
This section describes the process of porting JADE software to modern systems.
Please skip it if you are not interested.
As of 2016 these systems are not available on the market,
therefore the idea is to port the software on modern wide
The main problems with the porting software to the modern systems are

1. [compiler-specific Fortran features]
2. [big-little endianess for the calculi]
3. [big-little endianess for the I/O]
4. [build system ]
5. [porting CERNLIB]


Because of cernlib issues everything was tested in 32 bit mode.
Maybe that would worth to copy the needed cernlib routines to have them separately?
Will minicernlib work?The hardest part is graphics.

The MC generation can be done on any platform and put into HepMC3 format.
Practically it is visible for G and H.
The conversion to any be and le JADE MC formats can be done on any platform between F and J,
as HepMC3 works only with gcc4 and compatible compilers.

FIXME Expand the above very concise notes into more readable sentences for non-JADE-specialist open data users.

## <a name="clr">CERNLIB replacement</a>
After a basic functionality of the software was archieved with these versions of CERNLIB,
a small set of basic  functions used from CERNLIB  was identified. The corresponding sources were
extracted from kernlib and packlib to form picocernlib package.

The histogramming routines that require a lot of HBOOK code were replaced with the ROOT code that emulates
the functionality, see JBOOK.cxx

The graphics routines that require a lot of HIGZ code were replaced with the ROOT code that emulates
the functionality, see JHIGZ.cxx To embedded the graphics display into a ROOT application,
the main program grphmain is called as a routine inside TApplication loop.

With these replacements it is possible to avoid complications with ZEBRA and drop dependence on CERNLIB, which is
rarely available on modern systems.




## <a name="clr">Endianness</a>
The I/O endianess  can be controled in gfortran runtime with the
GFORTRAN_CONVERT_UNIT environment variable, e.g.
export GFORTRAN_CONVERT_UNIT='big_endian;native:2'


## <a name="cmake">cmake as a build system</a>
The cmake file is self documented.
Since version 2 cmake  has a first class Fortran support with descent dependency tracking.
This replaces self developed scripts in kors shell.

## <a name="compiller">Compiler specific issues</a>
Few changes were needed after the porting in   was done.
In many places the types were changed from LOGICAL to CHARCTER
and from INTEGER to CHARECTER.

As the line length is not limited, some symbols were removed in the end of lines.

Some specials symbols in the line continuation positions  were replaced with plus sign, etc.

HOLLERITH constants are represented in IBM Fortran via
'ABCD' were replaced with 4HABCD
for GNU fortran. This format is also accepted by the IBM compilers.
Similar issue was with the hexademical constants, which are in the form
Z1000 in IBM fortran. These were replaced with  Z'1000'
The form is accepted by GNU Fortran and IBM compiuller.
One compiler specific routine was added: hfix (gfortran is missing it.)


## <a name="src">Sources treatment</a>
The modified  sources were put into a separate directory src2016 and main2016.
Some used scripts are in the directory scripts2016.
 While porting two bugs were found in the software.
 The reconstruction software packages were linked to use CERNLIB routines zbug and z  instead of the actually needed routines for the reconstruction
 from the JADE software. As a result the calibration of part of detector was disabled for the data samples.
 However, this bug had no influence on the results produced previously~\cite{Schieck:2012mp}, as these were using the
 data reconstructed with original software. The bug does not affect Monte Carlo.


