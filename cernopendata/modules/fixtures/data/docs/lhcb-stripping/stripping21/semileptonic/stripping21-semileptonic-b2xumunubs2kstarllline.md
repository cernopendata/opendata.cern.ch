[[stripping21 lines]](./stripping21-index)

# StrippingB2XuMuNuBs2KstarLLLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2XuMuNuBs2KstarLLLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XuMuNuBs2KstarLLLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/Mu_forB2XuMuNu

|                 |                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                             |
| Output          | Phys/Mu_forB2XuMuNu/Particles                                                                                                                                                    |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KSLL02PiPi_forB2XuMuNu

|                 |                                                                                                                                                                                                                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (BPVVDZ \< 650.0 \* mm) &(BPVVD \>20.0\*mm)& (MM\>456.0\*MeV)&(MM\<536.0\*MeV) & (BPVVDCHI2\> 100.0 ) & (PT \> 700.0\*MeV) & (VFASPF(VCHI2PDOF) \< 10.0) & CHILDCUT((TRCHI2DOF \< 4.0),1) & CHILDCUT((TRCHI2DOF \< 4.0),2) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),1) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),2) & (MIPCHI2DV(PRIMARY) \> 8.0) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                           |
| Output          | Phys/KSLL02PiPi_forB2XuMuNu/Particles                                                                                                                                                                                                                                                                                                          |

CombineParticles/KstarLLMu_forB2XuMuNu

|                  |                                                                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KSLL02PiPi_forB2XuMuNu' , 'Phys/Mu_forB2XuMuNu' , 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : '(PT\> 100.0\*MeV) &(P\> 2000.0\*MeV)& (TRCHI2DOF \< 10.0 )& (MIPCHI2DV(PRIMARY)\>9.0)& (PIDpi-PIDK\>-10.0)' , 'pi-' : '(PT\> 100.0\*MeV) &(P\> 2000.0\*MeV)& (TRCHI2DOF \< 10.0 )& (MIPCHI2DV(PRIMARY)\>9.0)& (PIDpi-PIDK\>-10.0)' } |
| CombinationCut   | (AM\>2500.0\*MeV) & (AM\<5500.0\*MeV)                                                                                                                                                                                                                                                                        |
| MotherCut        | ( ((((5366.3\*5366.3) -(MASS(1,2,3))\*(MASS(1,2,3))))/(2\*5366.3)) \< 1850.0\*MeV)& (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.99)                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[B_s~0 -\> KS0 pi+ mu-]cc' ]                                                                                                                                                                                                                                                                          |
| Output           | Phys/KstarLLMu_forB2XuMuNu/Particles                                                                                                                                                                                                                                                                         |

TisTosParticleTagger/B2XuMuNuBs2KstarLLLine

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/KstarLLMu_forB2XuMuNu' ]                                                                                             |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/B2XuMuNuBs2KstarLLLine/Particles                                                                                          |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu3Body.\*Decision%TOS' : 0 } |
