[[stripping21 lines]](./stripping21-index)

# StrippingLb2LcTauNuNonPhysTauForB2XTauNu

## Properties:

|                |                                                |
|----------------|------------------------------------------------|
| OutputLocation | Phys/Lb2LcTauNuNonPhysTauForB2XTauNu/Particles |
| Postscale      | 1.0000000                                      |
| HLT            | None                                           |
| Prescale       | 0.10000000                                     |
| L0DU           | None                                           |
| ODIN           | None                                           |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

FilterDesktop/SelLcForB2XTauNu

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1200.0\*MeV) & (ADMASS('Lambda_c+') \< 30.0 \*MeV )& (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 50.0) & (VFASPF(VCHI2/VDOF)\<10.0) & (MIPCHI2DV(PRIMARY)\> 10.0)& INTREE( ('p+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 0.01) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0) & (PIDp \> 5.0))& INTREE ( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 0.01) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (PIDK \< 50.0))& INTREE( ('K-'==ABSID) & (PT \> 150.0\*MeV) & (TRCHI2DOF \< 3.0 ) & (TRPCHI2 \> 0.01) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3.0)) |
| Inputs          | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output          | Phys/SelLcForB2XTauNu/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3piNonPhys_Particles

|      |                                                             |
|------|-------------------------------------------------------------|
| Code | CONTAINS('Phys/StdLooseDetachedTau3piNonPhys/Particles')\>0 |

CombineParticles/SelLb2LcTauNuNonPhysTau

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLcForB2XTauNu' , 'Phys/StdLooseDetachedTau3piNonPhys' ]                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.995)' , 'tau-' : '(BPVDIRA \> 0.995)' } |
| CombinationCut   | (DAMASS('Lambda_b0') \< 300.0\*MeV) & (AMAXDOCA('') \< 0.15\*mm)                                                            |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                          |
| DecayDescriptor  | None                                                                                                                        |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ tau-]cc' ]                                                                                  |
| Output           | Phys/SelLb2LcTauNuNonPhysTau/Particles                                                                                      |

TisTosParticleTagger/Lb2LcTauNuNonPhysTauForB2XTauNu

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/SelLb2LcTauNuNonPhysTau' ]           |
| DecayDescriptor | None                                           |
| Output          | Phys/Lb2LcTauNuNonPhysTauForB2XTauNu/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 }           |
