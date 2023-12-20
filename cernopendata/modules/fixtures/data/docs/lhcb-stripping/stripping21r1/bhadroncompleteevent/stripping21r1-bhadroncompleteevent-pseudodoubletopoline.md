[[stripping21r1 lines]](./stripping21r1-index)

# StrippingPseudoDoubleTopoLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/PseudoDoubleTopoLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | HLT_PASS_RE('Hlt2Topo.\*Decision')  |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqPseudoTopoCands

GaudiSequencer/SEQ:Topo2BodyBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

FilterDesktop/KTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                            |
| DecayDescriptor | None                                                              |
| Output          | Phys/KTopoInputsBeauty2CharmFilter/Particles                      |

CombineParticles/TopoAll2BodySel

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                  |
| CombinationCut   | (AM \< 7000\*MeV) & (AALLSAMEBPV \|(AMINCHILD(MIPCHI2DV(PRIMARY)) \> 16)) & (AMAXDOCA('LoKi::DistanceCalculator') \< 0.2\*mm) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100)                                                                                           |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ 'K\*(892)0 -\> K+ K+' , 'K\*(892)0 -\> K+ K-' , 'K\*(892)0 -\> K- K-' ]                                                   |
| Output           | Phys/TopoAll2BodySel/Particles                                                                                                |

FilterDesktop/Topo2for2SelBeauty2CharmFilter

|                 |                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (SUMTREE(PT,('K+'==ABSID),0.0) \> 3000\*MeV)&(INTREE(ISBASIC & (MIPCHI2DV(PRIMARY)\>16) & (PT \> 1500\*MeV)))& (MINTREE(HASTRACK & ('K+'==ABSID),TRCHI2DOF) \< 2) |
| Inputs          | [ 'Phys/TopoAll2BodySel' ]                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                              |
| Output          | Phys/Topo2for2SelBeauty2CharmFilter/Particles                                                                                                                     |

FilterDesktop/Topo2BodyBBDTSelBeauty2CharmFilter

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/TopoBBDT')                  |
| Inputs          | [ 'Phys/Topo2for2SelBeauty2CharmFilter' ]       |
| DecayDescriptor | None                                              |
| Output          | Phys/Topo2BodyBBDTSelBeauty2CharmFilter/Particles |

SubstitutePID/Topo2BodyFinalSel

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | DECTREE('X0 -\> X X')                           |
| Inputs          | [ 'Phys/Topo2BodyBBDTSelBeauty2CharmFilter' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/Topo2BodyFinalSel/Particles                |
| Substitutions   | { 'X0 -\> X X' : 'B0' }                         |

FilterDesktop/Topo2BodyBeauty2CharmFilter

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | INTREE(ID=='B0')                           |
| Inputs          | [ 'Phys/Topo2BodyFinalSel' ]             |
| DecayDescriptor | None                                       |
| Output          | Phys/Topo2BodyBeauty2CharmFilter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Topo3BodyBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

FilterDesktop/KTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                            |
| DecayDescriptor | None                                                              |
| Output          | Phys/KTopoInputsBeauty2CharmFilter/Particles                      |

CombineParticles/TopoAll2BodySel

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                  |
| CombinationCut   | (AM \< 7000\*MeV) & (AALLSAMEBPV \|(AMINCHILD(MIPCHI2DV(PRIMARY)) \> 16)) & (AMAXDOCA('LoKi::DistanceCalculator') \< 0.2\*mm) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100)                                                                                           |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ 'K\*(892)0 -\> K+ K+' , 'K\*(892)0 -\> K+ K-' , 'K\*(892)0 -\> K- K-' ]                                                   |
| Output           | Phys/TopoAll2BodySel/Particles                                                                                                |

FilterDesktop/Topo2for3SelBeauty2CharmFilter

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | (M \< 6000\*MeV) & (VFASPF(VCHI2) \< 10)      |
| Inputs          | [ 'Phys/TopoAll2BodySel' ]                  |
| DecayDescriptor | None                                          |
| Output          | Phys/Topo2for3SelBeauty2CharmFilter/Particles |

CombineParticles/TopoAll3BodySel

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KTopoInputsBeauty2CharmFilter' , 'Phys/Topo2for3SelBeauty2CharmFilter' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                     |
| CombinationCut   | (AM \< 7000\*MeV) & (AALLSAMEBPV \|(AMINCHILD(MIPCHI2DV(PRIMARY)) \> 16)) & (AMAXDOCA('LoKi::DistanceCalculator') \< 0.2\*mm) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100)                                                                                           |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ 'Delta0 -\> K\*(892)0 K+' , 'Delta0 -\> K\*(892)0 K-' ]                                                                   |
| Output           | Phys/TopoAll3BodySel/Particles                                                                                                |

FilterDesktop/Topo3for3SelBeauty2CharmFilter

|                 |                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (SUMTREE(PT,('K+'==ABSID),0.0) \> 4000\*MeV)&(INTREE(ISBASIC & (MIPCHI2DV(PRIMARY)\>16) & (PT \> 1500\*MeV)))& (MINTREE(HASTRACK & ('K+'==ABSID),TRCHI2DOF) \< 2) |
| Inputs          | [ 'Phys/TopoAll3BodySel' ]                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                              |
| Output          | Phys/Topo3for3SelBeauty2CharmFilter/Particles                                                                                                                     |

FilterDesktop/Topo3BodyBBDTSelBeauty2CharmFilter

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/TopoBBDT')                  |
| Inputs          | [ 'Phys/Topo3for3SelBeauty2CharmFilter' ]       |
| DecayDescriptor | None                                              |
| Output          | Phys/Topo3BodyBBDTSelBeauty2CharmFilter/Particles |

SubstitutePID/Topo3BodyFinalSel

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | DECTREE('X0 -\> X X')                           |
| Inputs          | [ 'Phys/Topo3BodyBBDTSelBeauty2CharmFilter' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/Topo3BodyFinalSel/Particles                |
| Substitutions   | { 'X0 -\> X X' : 'B0' }                         |

FilterDesktop/Topo3BodyBeauty2CharmFilter

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | INTREE(ID=='B0')                           |
| Inputs          | [ 'Phys/Topo3BodyFinalSel' ]             |
| DecayDescriptor | None                                       |
| Output          | Phys/Topo3BodyBeauty2CharmFilter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Topo4BodyBBDTSelBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

FilterDesktop/KTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                            |
| DecayDescriptor | None                                                              |
| Output          | Phys/KTopoInputsBeauty2CharmFilter/Particles                      |

CombineParticles/TopoAll2BodySel

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                  |
| CombinationCut   | (AM \< 7000\*MeV) & (AALLSAMEBPV \|(AMINCHILD(MIPCHI2DV(PRIMARY)) \> 16)) & (AMAXDOCA('LoKi::DistanceCalculator') \< 0.2\*mm) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100)                                                                                           |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ 'K\*(892)0 -\> K+ K+' , 'K\*(892)0 -\> K+ K-' , 'K\*(892)0 -\> K- K-' ]                                                   |
| Output           | Phys/TopoAll2BodySel/Particles                                                                                                |

FilterDesktop/Topo2for3SelBeauty2CharmFilter

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | (M \< 6000\*MeV) & (VFASPF(VCHI2) \< 10)      |
| Inputs          | [ 'Phys/TopoAll2BodySel' ]                  |
| DecayDescriptor | None                                          |
| Output          | Phys/Topo2for3SelBeauty2CharmFilter/Particles |

CombineParticles/TopoAll3BodySel

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KTopoInputsBeauty2CharmFilter' , 'Phys/Topo2for3SelBeauty2CharmFilter' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                     |
| CombinationCut   | (AM \< 7000\*MeV) & (AALLSAMEBPV \|(AMINCHILD(MIPCHI2DV(PRIMARY)) \> 16)) & (AMAXDOCA('LoKi::DistanceCalculator') \< 0.2\*mm) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100)                                                                                           |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ 'Delta0 -\> K\*(892)0 K+' , 'Delta0 -\> K\*(892)0 K-' ]                                                                   |
| Output           | Phys/TopoAll3BodySel/Particles                                                                                                |

FilterDesktop/Topo3for4SelBeauty2CharmFilter

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | (M \< 6000\*MeV)                              |
| Inputs          | [ 'Phys/TopoAll3BodySel' ]                  |
| DecayDescriptor | None                                          |
| Output          | Phys/Topo3for4SelBeauty2CharmFilter/Particles |

CombineParticles/TopoAll4BodySel

|                  |                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KTopoInputsBeauty2CharmFilter' , 'Phys/Topo3for4SelBeauty2CharmFilter' ]                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'Delta0' : 'ALL' , 'Delta~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                            |
| CombinationCut   | (AM \< 7000\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC),0.0)) \> 4000\*MeV) & (AALLSAMEBPV \|(AMINCHILD(MIPCHI2DV(PRIMARY)) \> 16)) & (AMAXDOCA('LoKi::DistanceCalculator') \< 0.2\*mm) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100)                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                           |
| DecayDescriptors | [ 'B0 -\> Delta0 K-' , 'B0 -\> Delta0 K+' ]                                                                                                                                  |
| Output           | Phys/TopoAll4BodySel/Particles                                                                                                                                                 |

FilterDesktop/Topo4for4SelBeauty2CharmFilter

|                 |                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (SUMTREE(PT,('K+'==ABSID),0.0) \> 4000\*MeV)&(INTREE(ISBASIC & (MIPCHI2DV(PRIMARY)\>16) & (PT \> 1500\*MeV)))& (MINTREE(HASTRACK & ('K+'==ABSID),TRCHI2DOF) \< 2) |
| Inputs          | [ 'Phys/TopoAll4BodySel' ]                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                              |
| Output          | Phys/Topo4for4SelBeauty2CharmFilter/Particles                                                                                                                     |

FilterDesktop/Topo4BodyBBDTSelBeauty2CharmFilter

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/TopoBBDT')                  |
| Inputs          | [ 'Phys/Topo4for4SelBeauty2CharmFilter' ]       |
| DecayDescriptor | None                                              |
| Output          | Phys/Topo4BodyBBDTSelBeauty2CharmFilter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/PseudoTopoCands

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                       |
| Inputs          | [ 'Phys/Topo2BodyBeauty2CharmFilter' , 'Phys/Topo3BodyBeauty2CharmFilter' , 'Phys/Topo4BodyBBDTSelBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                                                      |
| Output          | Phys/PseudoTopoCands/Particles                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

ConeJetProxyFilter/ConeJetFilter

|                 |                              |
|-----------------|------------------------------|
| Code            | ALL                          |
| Inputs          | [ 'Phys/PseudoTopoCands' ] |
| DecayDescriptor | None                         |
| Output          | Phys/ConeJetFilter/Particles |

CombineParticles/PseudoDoubleTopoSel

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| Inputs           | [ 'Phys/ConeJetFilter' ]                                     |
| DaughtersCuts    | { '' : 'ALL' , 'B0' : 'ALL' , 'B~0' : 'ALL' }                  |
| CombinationCut   | (COSANGLE \< 0.990000) & (COSDPHI \< 0.000000) &(AM \> 0\*MeV) |
| MotherCut        | MAXTREE(ISBASIC,PT) \> 4000\*MeV                               |
| DecayDescriptor  | B_c+ -\> B0 B0                                                 |
| DecayDescriptors | [ 'B_c+ -\> B0 B0' ]                                         |
| Output           | Phys/PseudoDoubleTopoSel/Particles                             |

TisTosParticleTagger/PseudoDoubleTopoLine

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/PseudoDoubleTopoSel' ]      |
| DecayDescriptor | None                                  |
| Output          | Phys/PseudoDoubleTopoLine/Particles   |
| TisTosSpecs     | { 'Hlt2Topo.\*BBDTDecision%TOS' : 0 } |
