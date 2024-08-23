This guide is intended to get you started with the DELPHI analysis framework [skelana](/record/80502).

An example can be found in the examples folder on the [DELPHI container](delphi_guide_docker) or on [CERN gitlab](https://gitlab.cern.ch/delphi/examples). Take a look e.g. at the *dump* folder there.


## The basics
The DELPHI analysis framework is called [skelana](/record/80502). The name is an abbreviation for *skeleton analysis (framework)*.
The way to write analysis code is by overriding one or more of the following *Fortran* subroutines:

* **USER00** for the initialisation at the start of the run. This is where you can declare *histograms* or *ntuples* using [hbook](https://cds.cern.ch/record/2296378/files/hbook.pdf), for example.
* **USER01** for the event selection. It should return 0 to skip the current event and 1 to read it.
* **USER02** is called for each selected event. Here, you can fill event specific *ntuples* or *histograms*.
* **USER99** is called at the end of the run. This is where you would close your open files if needed.

Note that the provided code ships with default versions of these routines.
Other bits of the code should not be touched. DELPHI software extensively uses the [ypatchy](https://cds.cern.ch/record/446554?ln=en) framework.

## Build script
The following *bash* script can be run interactively, e.g. in the [DELPHI container](delphi-guide-docker),
or submitted to a batch farm with access to the DELPHI setup, for example via the [CVMFS distribution](delphi-guide-cvmfs).
This example has been taken from the [*dump* folder in the CERN DELPHI gitlab](https://gitlab.cern.ch/delphi/examples) repository.

```
#!/bin/bash
pgm=dump

export DELLIBS=`dellib skelana dstana pxdst vfclap vdclap ux tanagra ufield bsaurus herlib trigger uhlib dstana`
export CERNLIBS=`cernlib  genlib packlib kernlib ariadne herwig jetset74`

# run patchy
ycmd=`which nypatchy`
command="$ycmd - ${pgm}.f $pgm.cra $pgm.ylog - - - ${pgm}.f .go"
echo "Running $command"
eval $command

# compile
for ending in .f .F ; do
    ls *$ending >/dev/null 2>&1
    if [ $? -eq 0 ]; then
	for file in *$ending  ; do
	    $FCOMP $FFLAGS -c $file
	done
    fi
done

# link
$FCOMP $LDFLAGS *.o -o $pgm.exe $ADDLIB $DELLIBS $CERNLIBS

# execute
./$pgm.exe 1>$pgm.log 2>$pgm.err

# cleanup
rm -f *.f *.c *.o

```
Let's name it `dump.sh`. This simple script will:

* get the sources
* run nypatchy to create the compilable Fortran input files
* compile the Fortran code to create an executable file
* run the job

It expects a couple of additional files

### Data input file
The framework will identify the samples to be read from a plain text file called *PDLINPUT*. It is expected to be located in the same folder where the executable is being started from. The *PDLINPUT* file can either refer to a local file, or a nickname.
For a local file, use the **FILE** keyword:

```
FILE = simana.sdst
```

For a nickname, use the **FAT** keyword instead, e.g.
```
FAT = dsto00z_e/c001
```
which would select Z0 peak data collected in the year 2000, first half, processing E, only the first cassette.

### Cradle
The *Patchy cradle* contains the build instructions for the creating the *Fortran* sources from the *Patchy* input files.
The full cradle file reads:

```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                      %
%         Machine independent cradle to create SKELANA library         %
%                                                                      %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
+OPTION VERbose
+USE, ${PLINAM}.
%
+USE, IBMVM, IF = CERNVM.
+USE, VMS  , IF = ALPHAVMS, VAXVMS.
+USE, UNIX , IF = ALPHAOSF, DECS, HPUX, IBMRT, LINUX.
%
+EXE.
+PARAM, CLASH, N=1.
+OPT, MAPASM, UREF, LOST, BIGUSE.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   Get all the KEEP's needed for SKELANA
%
% PHDST CDE's
+USE,P=PHDSTCDE.
+PAM,11,T=A,C, R=PHDSTCDE, IF=IBMVM.              PHDSTXX CARDS F
+PAM,11,T=A,C, R=PHDSTCDE, IF=VMS.     DELPHI_PAM:PHDSTXX.CAR
+PAM,11,T=A,C, R=PHDSTCDE, IF=UNIX.  (DELPHI_PAM)/phdstxx.car
%
% DELPHI standard CDE's
+USE,P=STDCDES.
+PAM,11,T=A,C, R=STDCDES,  IF=IBMVM.              STDCDES CARDS E
+PAM,11,T=A,C, R=STDCDES,  IF=VMS.     DELPHI_PAM:STDCDES.CAR
+PAM,11,T=A,C, R=STDCDES,  IF=UNIX.  (DELPHI_PAM)/stdcdes.car
%
% JETSET CDE's
+USE,P=JETCDES.
+PAM,11,T=A,C, R=JETCDES,  IF=IBMVM.              JETSET74 CAR W
+PAM,11,T=A,C, R=JETCDES,  IF=VMS.     DELPHI_PAM:JETSET74.CAR
+PAM,11,T=A,C, R=JETCDES,  IF=UNIX.  (DELPHI_PAM)/jetset74.car
%
% VECSUB CDE's
+USE,P=VECDES.
+PAM,11,T=A,C, R=VECDES,   IF=IBMVM.              VECSUB72 CARDS E
+PAM,11,T=A,C, R=VECDES,   IF=VMS.     DELPHI_PAM:VECSUB72.CAR
+PAM,11,T=A,C, R=VECDES,   IF=UNIX.  (DELPHI_PAM)/vecsub72.car
%
% MUID CDE's
+USE,P=FMUCDE.
+PAM,11,T=A,C, R=FMUCDE,   IF=IBMVM.              MUFLAG CARDS E
+PAM,11,T=A,C, R=FMUCDE,   IF=VMS.     DELPHI_PAM:MUFLAG.CAR
+PAM,11,T=A,C, R=FMUCDE,   IF=UNIX.  (DELPHI_PAM)/muflag.car
%
% HACCOR CDE's
+USE,P=MYCDES.
+PAM,11,T=A,C, R=MYCDES,   IF=IBMVM.              HACCORXX CARDS E
+PAM,11,T=A,C, R=MYCDES,   IF=VMS.     DELPHI_PAM:haccorxx.car
+PAM,11,T=A,C, R=MYCDES,   IF=UNIX.  (DELPHI_PAM)/haccorxx.car
%
% ELEPHANT CDE's
+USE,P=ELEPHCDE.
+PAM,11,T=A,C, R=ELEPHCDE, IF=IBMVM.              ELEPHA32 CARDS E
+PAM,11,T=A,C, R=ELEPHCDE, IF=VMS.     DELPHI_PAM:ELEPHA32.CAR
+PAM,11,T=A,C, R=ELEPHCDE, IF=UNIX.  (DELPHI_PAM)/elepha32.car
%
% B_TAGGING CDE's
+USE,P=AABTCDE.
+PAM,11,T=A,C, R=AABTCDE,  IF=IBMVM.              AABTAGXX CARDS E
+PAM,11,T=A,C, R=AABTCDE,  IF=VMS.     DELPHI_PAM:AABTAGXX.CAR
+PAM,11,T=A,C, R=AABTCDE,  IF=UNIX.  (DELPHI_PAM)/aabtagxx.car
%
% B_TAGGING CDE's
+USE,P=MAMCDE.
+PAM,11,T=A,C, R=MAMCDE,   IF=IBMVM.              MAMMOTH CARDS E
+PAM,11,T=A,C, R=MAMCDE,   IF=VMS.     DELPHI_PAM:MAMMOTH.CAR
+PAM,11,T=A,C, R=MAMCDE,   IF=UNIX.  (DELPHI_PAM)/mammoth.car
%
% RICH identification keeps
+USE,P=PXRIUN,D=RIBCDE.
+PAM,11,T=A,C,             IF=IBMVM.             PXRICH CARDS E
+PAM,11,T=A,C,             IF=VMS.    DELPHI_PAM:pxrich.car
+PAM,11,T=A,C,             IF=UNIX. (DELPHI_PAM)/pxrich.car
%
+USE,P=ANA_RIBCDE.
+PAM,11,T=A,C, R=ANA_RIBCDE, IF=IBMVM.             RIBMEAN CARDS E
+PAM,11,T=A,C, R=ANA_RIBCDE, IF=VMS.    DELPHI_PAM:ribmean.car
+PAM,11,T=A,C, R=ANA_RIBCDE, IF=UNIX. (DELPHI_PAM)/ribmean.car
%
%
+USE,P=REMCDE.
+PAM,11,T=A,C,            IF=IBMVM.              REMCLU CARDS E
+PAM,11,T=A,C,            IF=VMS.     DELPHI_PAM:remclu.car
+PAM,11,T=A,C,            IF=UNIX.  (DELPHI_PAM)/remclu.car
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   Define the necessary SKELANA modules/processors
%
%+USE,NOPSHORT.    NO Short DST    information
%+USE,NOPSFULL.    NO Full  DST    information
%
%+USE,NOIFLTRA.    NO Track       information
%+USE,NOIFLSIM.    NO Simulation  information
%+USE,NOIFLBSP.    NO Beam Spot   information
%+USE,NOIFLBTG.    NO Btagging    information
%+USE,NOIFLEMC.    NO Elm.        calorimetry
%+USE,NOIFLHAC.    NO Hadron      calorimetry
%+USE,NOIFLELE.    NO Electron    identification
%+USE,NOIFLPHO.    NO Photon      identification
%+USE,NOIFLPHC.    NO Photon      conversion
%+USE,NOIFLMUO.    NO Muon        identification
%+USE,NOIFLHAD.    NO Hadron      identification
%+USE,NOIFLVDH.    NO Vertex      Detector hits
%+USE,NOIFLRV0.    NO V0          reconstruction
%+USE,NOIFLUTE.    NO TE banks    information
%+USE,NOIFLSTC.    NO STIC        information
%+USE,NOIFLFIX.    NO Fixing      (full DST only)
%+USE,NOIFLRNQ.    NO Run quality selection
%+USE,NOIFLBHP.    NO Bad 97 HPC  event rejections
%+USE,NOIFLECL.    NO Elm.cluster reconstruction
%+USE,NOIFLJET.    NO Jet         reconstruction
%
%   Get the code of SKELANA and utility routines
%
+USE, P=PSMAIN, T=E.
%
+PAM,11,T=A,C,             IF=UNIX. dump.car
%
+QUIT.
```

Without going into the details, the important bit are the last lines which select the *PSMAIN* part (or *patch*, in *Patchy* terms) from the source file
**dump.car** for processing and reading.
The latter is essentially a copy of the file you can find in **$DELPHI_PAM/skelana.car**, which re-implements the subroutine **USER02** as

```
      SUBROUTINE USER02
************************************************************************
*                                                                      *
*     Name           :  USER02                                         *
*     Called by      :  PHPROC                                         *
*     Date of coding :  Nov 18, 1993                                   *
*     Last update    :  Mar 07, 1995                                   *
*     Task           :  To access the event for analysis               *
*                                                                      *
************************************************************************
      IMPLICIT NONE
+CDE, PHCDE.
+CDE, PSCVEC.
+CDE, PSCEVT.
+CDE, PSCTRA.
+CDE, PSCEMF.
+CDE, PSCHPC.
+CDE, PSCSTC.
+CDE, PSCHAC.

*
      INTEGER I, IERR
*
*
*--- (re)fill skelana commons
      CALL PSBEG

*---  Dump event information as plain text
      PRINT *, "--------------------------"
      WRITE(*,98)      "CHECK: EVENT   :",IIIRUN,":",IIIEVT
      WRITE(*, 99)     "CHECK: TRACKS  :", NVECP
      DO I=1, NVECP
         WRITE(*, 99)  "CHECK: TRACK NR:", I
         WRITE(*, 100) "CHECK: CHARGE  :", VECP(7,I)
         WRITE(*, 104) "CHECK: 4VEC    :", VECP(1,I),VECP(2,I),
     $        VECP(3,I),VECP(4,I)
         WRITE(*, 100) "CHECK: EMF     :", QEMF(8,I)
         WRITE(*, 100) "CHECK: HPC     :", QHPC(8,I)
         WRITE(*, 100) "CHECK: HAC     :", QHAC(8,I)
         WRITE(*, 100) "CHECK: STC     :", QSTIC(1,I)
      ENDDO
 98   FORMAT(A,I10,A,I10)
 99   FORMAT(A,I10)
 100  FORMAT(A,F12.6)
 104  FORMAT(A,"(",F12.6,",",F12.6,",",F12.6,",",F12.6,")")
      END
*

```
This prints the run and event number and then loops over all particles in the event and prints some basic information like the momentum, energy and energy deposits in some of the sub-detectors of DELPHI. This example does not touch the event selection, so the default implementation is being used here.

## Running the analysis code
Simply run the above script within the DELPHI environment.
```
[delphi ~] $ chmod +x dump.sh
[delphi ~] $ ./dump.sh
```
This example will print a lot on the screen but it will not create any output files.
