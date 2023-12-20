[[stripping21r1p1 lines]](./stripping21r1p1-index)

# Strippingbhad2PMuXFakemuLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/bhad2PMuXFakemuLine/Particles      |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | HLT_PASS_RE('Hlt2Topo2Body.\*Decision') |
| Prescale       | 0.020000000                             |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/Strippingbhad2PMuXFakemuLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsMuons](./stripping21r1p1-commonparticles-stdallnopidsmuons)/Particles',True)\>0 |

FilterDesktop/fakeMu_forbhad2PMuX

|                 |                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (~ISMUON) & (INMUON)& (MIPCHI2DV(PRIMARY)\> 16.0 ) |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r1p1-commonparticles-stdallnopidsmuons)' ]                                                     |
| DecayDescriptor | None                                                                                                                                      |
| Output          | Phys/fakeMu_forbhad2PMuX/Particles                                                                                                        |

GaudiSequencer/SeqSelection_mergeddaughters

GaudiSequencer/SEQ:p_forbhad2PMuX

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/p_forbhad2PMuX

|                 |                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 15000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (PIDp-PIDpi\> 10.0 )& (PIDp-PIDK\> 5.0 ) & (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                      |
| Output          | Phys/p_forbhad2PMuX/Particles                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:PPbar_Lb_forbhad2PMuX

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/p_forbhad2PMuX

|                 |                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 15000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (PIDp-PIDpi\> 10.0 )& (PIDp-PIDK\> 5.0 ) & (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                      |
| Output          | Phys/p_forbhad2PMuX/Particles                                                                                                                                                             |

CombineParticles/PPbar_Lb_forbhad2PMuX

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/p_forbhad2PMuX' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                       |
| CombinationCut   | ATRUE                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.994)& (PT \> 1500.0)& (BPVVDCHI2 \>150.0) |
| DecayDescriptor  | None                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> p+ p~-' ]                                                        |
| Output           | Phys/PPbar_Lb_forbhad2PMuX/Particles                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Ppipi_Lb_forbhad2PMuX

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/p_forbhad2PMuX

|                 |                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 15000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (PIDp-PIDpi\> 10.0 )& (PIDp-PIDK\> 5.0 ) & (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                      |
| Output          | Phys/p_forbhad2PMuX/Particles                                                                                                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/pi_forbhad2PMuX

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1)                       |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/pi_forbhad2PMuX/Particles                                                |

CombineParticles/Ppipi_Lb_forbhad2PMuX

|                  |                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/p_forbhad2PMuX' , 'Phys/pi_forbhad2PMuX' ]                                                |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                       |
| CombinationCut   | ATRUE                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2.0) & (BPVDIRA\> 0.994)& (PT \> 1500.0)& (MM \< 3000.0)& (BPVVDCHI2 \>150.0) |
| DecayDescriptor  | None                                                                                                |
| DecayDescriptors | [ '[N(1440)+ -\> p+ pi+ pi-]cc' ]                                                               |
| Output           | Phys/Ppipi_Lb_forbhad2PMuX/Particles                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_mergeddaughters

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                       |
| Inputs          | [ 'Phys/PPbar_Lb_forbhad2PMuX' , 'Phys/Ppipi_Lb_forbhad2PMuX' , 'Phys/p_forbhad2PMuX' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_mergeddaughters/Particles                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/pMu_fakemu_Lb_forbhad2PMuX

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_mergeddaughters' , 'Phys/fakeMu_forbhad2PMuX' ]                                             |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'N(1440)+' : 'ALL' , 'N(1440)~-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | (AM\>1000.0\*MeV)                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 20.0) & (BPVDIRA\> 0.9994)& (PT \> 1500.0)& (BPVVDCHI2 \>150.0)                           |
| DecayDescriptor  | None                                                                                                            |
| DecayDescriptors | [ '[Lambda_b0 -\> J/psi(1S) mu-]cc' , '[Lambda_b0 -\> N(1440)+ mu-]cc' ]                                  |
| Output           | Phys/pMu_fakemu_Lb_forbhad2PMuX/Particles                                                                       |

TisTosParticleTagger/bhad2PMuXFakemuLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/pMu_fakemu_Lb_forbhad2PMuX' ]   |
| DecayDescriptor | None                                      |
| Output          | Phys/bhad2PMuXFakemuLine/Particles        |
| TisTosSpecs     | { 'Hlt2.\*Topo2Body.\*Decision%TOS' : 0 } |
