[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2SSBu2KSSPionLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/B2SSBu2KSSPionLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionEW**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & \~ALG_PASSED('StrippingStreamEWBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseKaons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseKaons /Particles',True) |

**FilterDesktop/KaonsForB2SS**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PIDK \> 0) &( PT \> 1250\*MeV)& ( MIPCHI2DV(PRIMARY)\> 55)           |
| Inputs          | [ 'Phys/ [StdAllLooseKaons](./stripping21r1p2-stdallloosekaons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/KaonsForB2SS/Particles                                           |

**LoKi::VoidFilter/SELECT:Phys/StdAllLoosePions**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLoosePions /Particles',True) |

**FilterDesktop/PionsForB2SS**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | ( PT \> 1500\*MeV)& ( MIPCHI2DV(PRIMARY)\> 64)                        |
| Inputs          | [ 'Phys/ [StdAllLoosePions](./stripping21r1p2-stdallloosepions) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/PionsForB2SS/Particles                                           |

**DaVinci::N5BodyDecays/B2SSBu2KSSPionLine**

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForB2SS' , 'Phys/PionsForB2SS' ]                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                             |
| CombinationCut   | (AM\>4900\*MeV) & (AM\<5800\*MeV) & (( (abs(MYAM12-MYAM34)\< 25\*MeV) \| (abs(MYAM13-MYAM24)\< 25\*MeV) \| (abs(MYAM14-MYAM23)\< 25\*MeV) ))& ((AMAXDOCA('')\< 0.2\*mm)) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 3)& (BPVDIRA \> 0)& (BPVVDCHI2\> 125)& (BPVIPCHI2()\< 10)                                                                                          |
| DecayDescriptor  | [B+ -\> pi+ pi- pi+ pi- K+]cc                                                                                                                                          |
| DecayDescriptors | [ '[B+ -\> pi+ pi- pi+ pi- K+]cc' ]                                                                                                                                  |
| Output           | Phys/B2SSBu2KSSPionLine/Particles                                                                                                                                        |
