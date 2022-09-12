[[stripping21 lines]](./stripping21-index)

# StrippingLc23MuLinesLc2pKpiLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Lc23MuLinesLc2pKpiLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 0.010000000                           |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKaons](./stripping21-stdloosekaons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePions](./stripping21-stdloosepions) /Particles')\>0 |

**DaVinci::N3BodyDecays/Lc23MuLinesLc2pKpiLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseKaons](./stripping21-stdloosekaons) ' , 'Phys/ [StdLoosePions](./stripping21-stdloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDK-PIDpi)\>5) & ((PIDK-PIDp)\>0)' , 'K-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDK-PIDpi)\>5) & ((PIDK-PIDp)\>0)' , 'p+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'pi+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'pi-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'p\~-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+')\<150\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/Lc23MuLinesLc2pKpiLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
