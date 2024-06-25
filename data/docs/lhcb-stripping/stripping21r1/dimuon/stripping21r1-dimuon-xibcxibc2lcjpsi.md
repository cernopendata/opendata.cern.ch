[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXibcXibc2LcJpsi

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/XibcXibc2LcJpsi/Particles |
| Postscale      | 1.0000000                      |
| HLT            | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingXibcXibc2LcJpsiVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseJpsi2MuMu_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseJpsi2MuMu](./stripping21r1-commonparticles-stdloosejpsi2mumu)/Particles')\>0 |

FilterDesktop/XibcJpsiMuonFilterSelection

|                 |                                                                                                                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CHILDCUT(((PIDmu \> 0) & (TRPCHI2 \> 0.005) & (TRGHP \< 0.4) & (PT \> 650\*MeV) ),1) & CHILDCUT(((PIDmu \> 0) & (TRPCHI2 \> 0.005) & (TRGHP \< 0.4) & (PT \> 650\*MeV) ),2)) & (VFASPF(VCHI2/VDOF)\<10) & (ADMASS('J/psi(1S)') \< 50\*MeV) |
| Inputs          | [ 'Phys/[StdLooseJpsi2MuMu](./stripping21r1-commonparticles-stdloosejpsi2mumu)' ]                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                                        |
| Output          | Phys/XibcJpsiMuonFilterSelection/Particles                                                                                                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21r1-commonparticles-stdallnopidsprotons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/XibcLcSelection

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' , 'Phys/[StdAllNoPIDsProtons](./stripping21r1-commonparticles-stdallnopidsprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRPCHI2 \> 0.05) &(PROBNNk \> 0.02) & (TRGHP \< 0.4) &(P \> 0\*GeV) & (PT \> 450\*MeV)' , 'K-' : '(TRPCHI2 \> 0.05) &(PROBNNk \> 0.02) & (TRGHP \< 0.4) &(P \> 0\*GeV) & (PT \> 450\*MeV)' , 'p+' : '(TRPCHI2 \> 0.05) & (PROBNNp \> 0.05) & (TRGHP \< 0.4) & (PT \> 450\*MeV) & (P \> 0\*GeV) ' , 'pi+' : '(MIPCHI2DV(PRIMARY)\> 0.0) & (TRPCHI2 \> 0.015) & (TRGHP \< 0.4) & (PROBNNpi \> 0.2) &(PT \> 250\*MeV)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\> 0.0) & (TRPCHI2 \> 0.015) & (TRGHP \< 0.4) & (PROBNNpi \> 0.2) &(PT \> 250\*MeV)' , 'p~-' : '(TRPCHI2 \> 0.05) & (PROBNNp \> 0.05) & (TRGHP \< 0.4) & (PT \> 450\*MeV) & (P \> 0\*GeV) ' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 120\*MeV) & (APT \> 1500\*MeV) & (ADOCAMAX('') \< 0.5\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5) & (ADMASS('Lambda_c+') \< 30\*MeV) & (BPVDIRA \> 0.98) & (BPVLTIME()\>-0.0001)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [Lambda_c+ -\> p+ pi+ K-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ pi+ K-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/XibcLcSelection/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

CombineParticles/XibcXibc2LcJpsi

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcJpsiMuonFilterSelection' , 'Phys/XibcLcSelection' ]                 |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' } |
| CombinationCut   | (ADAMASS('Xi_bc+') \< 1.5\*GeV)                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<7) & (MIPDV(PRIMARY) \< 1000.0)                              |
| DecayDescriptor  | [Xi_bc+ -\> J/psi(1S) Lambda_c+]cc                                              |
| DecayDescriptors | [ '[Xi_bc+ -\> J/psi(1S) Lambda_c+]cc' ]                                      |
| Output           | Phys/XibcXibc2LcJpsi/Particles                                                    |
