[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLb2LcTauNuInvVertForB2XTauNu

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/Lb2LcTauNuInvVertForB2XTauNu/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21r1-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

FilterDesktop/SelLcForLbInvVertB2XTauNu

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda_c+') \< 30.0 \*MeV )& (BPVVDCHI2 \> 50.0) & (VFASPF(VCHI2/VDOF)\<10.0)& (MIPCHI2DV(PRIMARY)\> 10.0) & INTREE( ('p+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 0.01) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0) & (PIDp \> 5.0))& INTREE( ('K-'==ABSID) & (PT \> 150.0\*MeV) & (TRCHI2DOF \< 3.0 ) & (TRPCHI2 \> 0.01) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3.0)) |
| Inputs          | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21r1-commonparticles-stdlooselambdac2pkpi)' ]                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output          | Phys/SelLcForLbInvVertB2XTauNu/Particles                                                                                                                                                                                                                                                                                                                                                                                        |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3pi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedTau3pi](./stripping21r1-commonparticles-stdloosedetachedtau3pi)/Particles')\>0 |

CombineParticles/SelLb2LcTauNuInvVert

|                  |                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLcForLbInvVertB2XTauNu' , 'Phys/[StdLooseDetachedTau3pi](./stripping21r1-commonparticles-stdloosedetachedtau3pi)' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                         |
| CombinationCut   | (ACHILD(VFASPF(VZ),2) - ACHILD(VFASPF(VZ),1) \> 1.0 \*mm)& (ACHILD(VFASPF(VZ),2) - ACHILD(VFASPF(VZ),1) \<50. ) & (DAMASS('Lambda_b0') \< 300.0\*MeV) |
| MotherCut        | (BPVDIRA \>0.995)                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                  |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ tau-]cc' ]                                                                                                            |
| Output           | Phys/SelLb2LcTauNuInvVert/Particles                                                                                                                   |

TisTosParticleTagger/Lb2LcTauNuInvVertForB2XTauNu

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/SelLb2LcTauNuInvVert' ]           |
| DecayDescriptor | None                                        |
| Output          | Phys/Lb2LcTauNuInvVertForB2XTauNu/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 }        |
