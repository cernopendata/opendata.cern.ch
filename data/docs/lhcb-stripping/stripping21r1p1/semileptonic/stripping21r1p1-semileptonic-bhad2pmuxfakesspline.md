[[stripping21r1p1 lines]](./stripping21r1p1-index)

# Strippingbhad2PMuXFakeSSpLine

## Properties:

|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| OutputLocation | Phys/bhad2PMuXFakeSSpLine/Particles                                                     |
| Postscale      | 1.0000000                                                                               |
| HLT1           | None                                                                                    |
| HLT2           | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision')\| HLT_PASS_RE('Hlt2TopoMu2Body.\*Decision') |
| Prescale       | 0.0050000000                                                                            |
| L0DU           | L0_CHANNEL_RE('Muon')                                                                   |
| ODIN           | None                                                                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/Strippingbhad2PMuXFakeSSpLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Mu_forbhad2PMuX

|                 |                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 16.0 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                       |
| DecayDescriptor | None                                                                                                                |
| Output          | Phys/Mu_forbhad2PMuX/Particles                                                                                      |

TisTosParticleTagger/Mu_forbhad2PMuXTOS

|                 |                                    |
|-----------------|------------------------------------|
| Inputs          | [ 'Phys/Mu_forbhad2PMuX' ]       |
| DecayDescriptor | None                               |
| Output          | Phys/Mu_forbhad2PMuXTOS/Particles  |
| TisTosSpecs     | { 'L0.\*Muon.\*Decision%TOS' : 0 } |

GaudiSequencer/SeqSelection_fakemergeddaughters

GaudiSequencer/SEQ:fakep_forbhad2PMuX

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21r1p1-commonparticles-stdallnopidsprotons)/Particles',True)\>0 |

FilterDesktop/fakep_forbhad2PMuX

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 15000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r1p1-commonparticles-stdallnopidsprotons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/fakep_forbhad2PMuX/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:fakePPbar_Lb_forbhad2PMuX

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21r1p1-commonparticles-stdallnopidsprotons)/Particles',True)\>0 |

FilterDesktop/fakep_forbhad2PMuX

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 15000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r1p1-commonparticles-stdallnopidsprotons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/fakep_forbhad2PMuX/Particles                                                                                                              |

CombineParticles/fakePPbar_Lb_forbhad2PMuX

|                  |                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/fakep_forbhad2PMuX' ]                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                                                            |
| CombinationCut   | ATRUE                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.994)& (PT \> 1500.0)& (INTREE((ABSID == 'p+')& (PIDp-PIDpi\> 10.0 )&(PIDp-PIDK\> 5.0 ))) & (BPVVDCHI2 \>150.0) |
| DecayDescriptor  | None                                                                                                                                                     |
| DecayDescriptors | [ 'J/psi(1S) -\> p+ p~-' ]                                                                                                                             |
| Output           | Phys/fakePPbar_Lb_forbhad2PMuX/Particles                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:fakePpipi_Lb_forbhad2PMuX

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21r1p1-commonparticles-stdallnopidsprotons)/Particles',True)\>0 |

FilterDesktop/fakep_forbhad2PMuX

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 15000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r1p1-commonparticles-stdallnopidsprotons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/fakep_forbhad2PMuX/Particles                                                                                                              |

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

CombineParticles/fakePpipi_Lb_forbhad2PMuX

|                  |                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/fakep_forbhad2PMuX' , 'Phys/pi_forbhad2PMuX' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                       |
| CombinationCut   | ATRUE                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2.0) & (BPVDIRA\> 0.994)& (PT \> 1500.0)& (MM \< 3000.0)& (BPVVDCHI2 \>150.0) |
| DecayDescriptor  | None                                                                                                |
| DecayDescriptors | [ '[N(1440)+ -\> p+ pi+ pi-]cc' ]                                                               |
| Output           | Phys/fakePpipi_Lb_forbhad2PMuX/Particles                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_fakemergeddaughters

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                   |
| Inputs          | [ 'Phys/fakePPbar_Lb_forbhad2PMuX' , 'Phys/fakePpipi_Lb_forbhad2PMuX' , 'Phys/fakep_forbhad2PMuX' ] |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/Selection_fakemergeddaughters/Particles                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/pMuSS_fakep_Lb_forbhad2PMuX

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Mu_forbhad2PMuXTOS' , 'Phys/Selection_fakemergeddaughters' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'N(1440)+' : 'ALL' , 'N(1440)~-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | (AM\>1000.0\*MeV)                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 20.0) & (BPVDIRA\> 0.9994)& (PT \> 1500.0)& (BPVVDCHI2 \>150.0)     |
| DecayDescriptor  | None                                                                                      |
| DecayDescriptors | [ '[Lambda_b0 -\> N(1440)+ mu+]cc' ]                                                  |
| Output           | Phys/pMuSS_fakep_Lb_forbhad2PMuX/Particles                                                |

TisTosParticleTagger/bhad2PMuXFakeSSpLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/pMuSS_fakep_Lb_forbhad2PMuX' ]                                             |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/bhad2PMuXFakeSSpLine/Particles                                                  |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 } |
