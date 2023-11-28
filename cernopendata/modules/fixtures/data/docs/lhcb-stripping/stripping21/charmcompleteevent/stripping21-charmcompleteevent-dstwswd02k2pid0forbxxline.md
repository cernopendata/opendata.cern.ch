[[stripping21 lines]](./stripping21-index)

# StrippingDstWSwD02K2PiD0forBXXLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/DstWSwD02K2PiD0forBXXLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 0.20000000                               |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/D02K2PiforD0forBXX

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                                                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 3.0) & (PT \> 400 \*MeV) & (P\>2.0\*GeV) & (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\> 4.0)' , 'K-' : '(TRCHI2DOF \< 3.0) & (PT \> 400 \*MeV) & (P\>2.0\*GeV) & (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\> 4.0)' , 'pi+' : '(TRCHI2DOF \< 3.0) & (P\>2.0\*GeV) & (PT \> 400 \*MeV)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\< 10.0) & (PIDmu\< 10)' , 'pi-' : '(TRCHI2DOF \< 3.0) & (P\>2.0\*GeV) & (PT \> 400 \*MeV)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\< 10.0) & (PIDmu\< 10)' } |
| CombinationCut   | (AM\>1.4\*GeV) & (AM\<1.7\*GeV) & (AM12\>575.5\*MeV) & (AM12\<975.5\*MeV) & (APT \> 3000\*MeV) & (ADOCACHI2CUT( 20, ''))                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<6.0) & (BPVVD\>4\*mm) & (BPVVDCHI2\>120) & (BPVDIRA\>0.9997) & (BPVIPCHI2()\<25.)                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[D0 -\> pi+ pi- K-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Output           | Phys/D02K2PiforD0forBXX/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/DstWSwD0K2PiD0forBXX

|                  |                                                                                                                                                                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02K2PiforD0forBXX' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(PT \> 250\*MeV) & (TRCHI2DOF \< 3.0) & (MIPDV(PRIMARY)\< 0.3\*mm) & (MIPCHI2DV(PRIMARY)\<4.0) & (PIDK \< 10)' , 'pi-' : '(PT \> 250\*MeV) & (TRCHI2DOF \< 3.0) & (MIPDV(PRIMARY)\< 0.3\*mm) & (MIPCHI2DV(PRIMARY)\<4.0) & (PIDK \< 10)' } |
| CombinationCut   | (AM-AM1-139.57\*MeV\<40.0\*MeV) & (APT\>3.0\*GeV)                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<5.0) & (BPVVDCHI2 \< 25) & (BPVIPCHI2() \< 25.)                                                                                                                                                                                                                              |
| DecayDescriptor  | [D\*(2010)- -\> D0 pi-]cc                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[D\*(2010)- -\> D0 pi-]cc' ]                                                                                                                                                                                                                                                               |
| Output           | Phys/DstWSwD0K2PiD0forBXX/Particles                                                                                                                                                                                                                                                               |

TisTosParticleTagger/DstWSwD02K2PiD0forBXXLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/DstWSwD0K2PiD0forBXX' ]        |
| DecayDescriptor | None                                     |
| Output          | Phys/DstWSwD02K2PiD0forBXXLine/Particles |
| TisTosSpecs     | { 'Hlt2Global%TOS' : 0 }                 |
