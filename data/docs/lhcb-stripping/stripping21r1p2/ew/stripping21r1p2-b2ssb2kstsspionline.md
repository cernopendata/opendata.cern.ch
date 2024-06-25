[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2SSB2KstSSPionLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2SSB2KstSSPionLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseKstar2Kpi**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseKstar2Kpi /Particles',True) |

**FilterDesktop/KstarsForB2SS**

|                 |                                                                                                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 1250\*MeV)& ( MIPCHI2DV(PRIMARY)\> 55)& (PT \> 2000\*MeV )& (M \< ( 892\*MeV + 130\*MeV ) )& (M \> ( 892\*MeV - 130\*MeV ) )& (VFASPF(VCHI2/VDOF) \< 2.5 )& ( CHILD( MIPCHI2DV(PRIMARY), 1) \> 55 ) & ( CHILD( MIPCHI2DV(PRIMARY), 2) \> 55 ) & (BPVVDCHI2 \> 50 ) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r1p2-stdloosekstar2kpi) ' ]                                                                                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                                                                                       |
| Output          | Phys/KstarsForB2SS/Particles                                                                                                                                                                                                                                               |

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

**DaVinci::N5BodyDecays/B2SSB2KstSSPionLine**

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KstarsForB2SS' , 'Phys/PionsForB2SS' ]                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                             |
| CombinationCut   | (AM\>4900\*MeV) & (AM\<5800\*MeV) & (( (abs(MYAM12-MYAM34)\< 25\*MeV) \| (abs(MYAM13-MYAM24)\< 25\*MeV) \| (abs(MYAM14-MYAM23)\< 25\*MeV) ))& ((AMAXDOCA('')\< 0.2\*mm)) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 3)& (BPVDIRA \> 0)& (BPVVDCHI2\> 125)& (BPVIPCHI2()\< 10)                                                                                          |
| DecayDescriptor  | [B0 -\> pi+ pi- pi+ pi- K\*(892)0]cc                                                                                                                                   |
| DecayDescriptors | [ '[B0 -\> pi+ pi- pi+ pi- K\*(892)0]cc' ]                                                                                                                           |
| Output           | Phys/B2SSB2KstSSPionLine/Particles                                                                                                                                       |
