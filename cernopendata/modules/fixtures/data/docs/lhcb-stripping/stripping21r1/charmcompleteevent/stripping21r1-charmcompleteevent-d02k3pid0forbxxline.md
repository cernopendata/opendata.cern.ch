[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD02K3PiD0forBXXLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/D02K3PiD0forBXXLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 0.0050000000                       |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/D02K3PiD0forBXXLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 3.0) & (PT \> 300.0 \*MeV) & (P\>2.0\*GeV) & (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\> 4.0)' , 'K-' : '(TRCHI2DOF \< 3.0) & (PT \> 300.0 \*MeV) & (P\>2.0\*GeV) & (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\> 4.0)' , 'pi+' : ' (PT \> 250 \*MeV) & (P\>2.0\*GeV)& (TRCHI2DOF \< 3.0)' , 'pi-' : ' (PT \> 250 \*MeV) & (P\>2.0\*GeV)& (TRCHI2DOF \< 3.0)' } |
| CombinationCut   | (ADAMASS('D0') \< 100.0 \*MeV) & (APT \> 1500.\*MeV) & (ADOCACHI2CUT( 20, ''))                                                                                                                                                                                                                                                                                                       |
| MotherCut        | (ADMASS('D0') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0) & (INTREE((ABSID=='pi+')& (PT \> 300.0 \*MeV) &(MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\< 10.0)))& (BPVVDCHI2 \> 100.0) & (BPVDIRA\> 0.9999) & (BPVIP()\< 0.2 \*mm)                                                                                                                                                             |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/D02K3PiD0forBXXLine/Particles                                                                                                                                                                                                                                                                                                                                                   |
