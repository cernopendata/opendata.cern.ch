[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine/Particles                  |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingXib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

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

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21r1-commonparticles-stdallnopidsprotons)/Particles')\>0 |

FilterDesktop/PInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r1-commonparticles-stdallnopidsprotons)' ]       |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PInputsBeauty2CharmFilter/Particles                                                      |

CombineParticles/Lc2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                            |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Lambda_c+') \< 110\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (ADMASS('Lambda_c+') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                  |
| Output           | Phys/Lc2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                     |

FilterDesktop/Lc2pKPiPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/Lc2PKPiBeauty2Charm' ]                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/Lc2pKPiPIDBeauty2CharmFilter/Particles                                                                                                                             |

GaudiSequencer/SeqD2HHHBeauty2Charm

GaudiSequencer/SEQ:D+2HHHBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

CombineParticles/ProtoD+2HHHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('pi+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','K+','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D+ -\> pi+ pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD+2HHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

SubPIDMMFilter/D+2HHHSubPIDSelBeauty2Charm

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                          |
| Inputs          | [ 'Phys/ProtoD+2HHHBeauty2Charm' ]                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                         |
| Output          | Phys/D+2HHHSubPIDSelBeauty2Charm/Particles                                                                                                                                                                   |
| MaxMM           | 2068.4900                                                                                                                                                                                                    |
| MinMM           | 1769.6200                                                                                                                                                                                                    |
| PIDs            | [ [ 'pi+' , 'pi+' , 'pi-' ] , [ 'pi+' , 'pi+' , 'K-' ] , [ 'K+' , 'pi+' , 'pi-' ] , [ 'K+' , 'pi+' , 'K-' ] , [ 'pi+' , 'K+' , 'pi-' ] , [ 'pi+' , 'K+' , 'K-' ] , [ 'K+' , 'K+' , 'pi-' ] ] |

FilterDesktop/D+2HHHBeauty2CharmFilter

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | in_range(1769.62,MM,2068.49)             |
| Inputs          | [ 'Phys/D+2HHHSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/D+2HHHBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D-2HHHBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

CombineParticles/ProtoD-2HHHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('pi+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','K+','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D- -\> pi- pi- pi+' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD-2HHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

SubPIDMMFilter/D-2HHHSubPIDSelBeauty2Charm

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                          |
| Inputs          | [ 'Phys/ProtoD-2HHHBeauty2Charm' ]                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                         |
| Output          | Phys/D-2HHHSubPIDSelBeauty2Charm/Particles                                                                                                                                                                   |
| MaxMM           | 2068.4900                                                                                                                                                                                                    |
| MinMM           | 1769.6200                                                                                                                                                                                                    |
| PIDs            | [ [ 'pi-' , 'pi-' , 'pi+' ] , [ 'pi-' , 'pi-' , 'K+' ] , [ 'K-' , 'pi-' , 'pi+' ] , [ 'K-' , 'pi-' , 'K+' ] , [ 'pi-' , 'K-' , 'pi+' ] , [ 'pi-' , 'K-' , 'K+' ] , [ 'K-' , 'K-' , 'pi+' ] ] |

FilterDesktop/D-2HHHBeauty2CharmFilter

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | in_range(1769.62,MM,2068.49)             |
| Inputs          | [ 'Phys/D-2HHHSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/D-2HHHBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHHBeauty2Charm

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | ALL                                                                     |
| Inputs          | [ 'Phys/D+2HHHBeauty2CharmFilter' , 'Phys/D-2HHHBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/D2HHHBeauty2Charm/Particles                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHHPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2HHHBeauty2Charm' ]                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2HHHPIDBeauty2CharmFilter/Particles                                                                                                                               |

FilterDesktop/D2HHHPIDTIGHTBeauty2CharmFilter

|                 |                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -5),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -5), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 10), 1) == 0) |
| Inputs          | [ 'Phys/D2HHHPIDBeauty2CharmFilter' ]                                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                  |
| Output          | Phys/D2HHHPIDTIGHTBeauty2CharmFilter/Particles                                                                                                                        |

FilterDesktop/Ds2HHHPIDTIGHTBeauty2CharmFilter

|                 |                                                                                                                                                                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (((NINTREE(ID=='K-')==1) & (NINTREE(ID=='K+')==1)) \|(NINTREE(ABSID=='K+')==0) \| ((ID=='D+') & (NINTREE(ID=='K+')==1) & (NINTREE(ABSID=='K+') == 1)) \| ((ID=='D-') & (NINTREE(ID=='K-')==1) & (NINTREE(ABSID=='K+') == 1))) & (in_range(1868.49\*MeV,MM,2068.49\*MeV)) |
| Inputs          | [ 'Phys/D2HHHPIDTIGHTBeauty2CharmFilter' ]                                                                                                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                                                                     |
| Output          | Phys/Ds2HHHPIDTIGHTBeauty2CharmFilter/Particles                                                                                                                                                                                                                          |

CombineParticles/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Ds2HHHPIDTIGHTBeauty2CharmFilter' , 'Phys/KInputsBeauty2CharmFilter' , 'Phys/Lc2pKPiPIDBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>5200\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[Xi_b0 -\> Lambda_c+ D- K+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                  |

TisTosParticleTagger/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2Charm' ]                                                                                 |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmTISTOS/Particles                                                                         |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                  |
| Inputs          | [ 'Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                             |
| Output          | Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
| Code            | ALL                                                                            |
| Inputs          | [ 'Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                           |
| Output          | Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo1_Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo2_Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo3_Xib02LcDsKPiWSLc2PKPiDs2KKPiBeauty2CharmLine/Particles |
