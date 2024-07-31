[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingDitauMXLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/DitauMXLine/Particles |
| Postscale      | 1.0000000                  |
| HLT1           | None                       |
| HLT2           | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionEW

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & ~ALG_PASSED('StrippingStreamEWBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqDitauMXLine

GaudiSequencer/SEQ:SelDitauCand_emu_os

GaudiSequencer/SeqTauIso

GaudiSequencer/SEQ:SelTauIso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

FilterDesktop/SelTauIso_mu

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_mu/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

FilterDesktop/SelTauIso_h3

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h3' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h3/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

FilterDesktop/SelTauIso_h1

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h1' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h1/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

FilterDesktop/SelTauIso_e

|                 |                            |
|-----------------|----------------------------|
| Code            | (PTFrac05C \> 0.8)         |
| Inputs          | [ 'Phys/SelTauNoiso_e' ] |
| DecayDescriptor | None                       |
| Output          | Phys/SelTauIso_e/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauIso

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                        |
| Inputs          | [ 'Phys/SelTauIso_e' , 'Phys/SelTauIso_h1' , 'Phys/SelTauIso_h3' , 'Phys/SelTauIso_mu' ] |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/TauIso/Particles                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_emu_os

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TauIso' ]                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(ALL)' , 'e-' : '(ALL)' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' } |
| CombinationCut   | (AM \> 12000.0) & (APTMAX \> 9000.0)                                                 |
| MotherCut        | (ALL)                                                                                |
| DecayDescriptor  | [ Z0 -\> e- mu+ ]cc                                                                |
| DecayDescriptors | [ '[ Z0 -\> e- mu+ ]cc' ]                                                        |
| Output           | Phys/SelDitauCand_emu_os/Particles                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDitauCand_h3mu_os

GaudiSequencer/SeqTauIso

GaudiSequencer/SEQ:SelTauIso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

FilterDesktop/SelTauIso_mu

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_mu/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

FilterDesktop/SelTauIso_h3

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h3' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h3/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

FilterDesktop/SelTauIso_h1

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h1' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h1/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

FilterDesktop/SelTauIso_e

|                 |                            |
|-----------------|----------------------------|
| Code            | (PTFrac05C \> 0.8)         |
| Inputs          | [ 'Phys/SelTauNoiso_e' ] |
| DecayDescriptor | None                       |
| Output          | Phys/SelTauIso_e/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauIso

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                        |
| Inputs          | [ 'Phys/SelTauIso_e' , 'Phys/SelTauIso_h1' , 'Phys/SelTauIso_h3' , 'Phys/SelTauIso_mu' ] |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/TauIso/Particles                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_h3mu_os

|                  |                                                                                          |
|------------------|------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TauIso' ]                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' , 'tau+' : '(ALL)' , 'tau-' : '(ALL)' } |
| CombinationCut   | (AM \> 12000.0) & (APTMAX \> 9000.0)                                                     |
| MotherCut        | (ALL)                                                                                    |
| DecayDescriptor  | [ Z0 -\> tau- mu+ ]cc                                                                  |
| DecayDescriptors | [ '[ Z0 -\> tau- mu+ ]cc' ]                                                          |
| Output           | Phys/SelDitauCand_h3mu_os/Particles                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDitauCand_mumu_os

GaudiSequencer/SeqTauIso

GaudiSequencer/SEQ:SelTauIso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

FilterDesktop/SelTauIso_mu

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_mu/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

FilterDesktop/SelTauIso_h3

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h3' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h3/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

FilterDesktop/SelTauIso_h1

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h1' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h1/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

FilterDesktop/SelTauIso_e

|                 |                            |
|-----------------|----------------------------|
| Code            | (PTFrac05C \> 0.8)         |
| Inputs          | [ 'Phys/SelTauNoiso_e' ] |
| DecayDescriptor | None                       |
| Output          | Phys/SelTauIso_e/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauIso

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                        |
| Inputs          | [ 'Phys/SelTauIso_e' , 'Phys/SelTauIso_h1' , 'Phys/SelTauIso_h3' , 'Phys/SelTauIso_mu' ] |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/TauIso/Particles                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_mumu_os

|                  |                                                    |
|------------------|----------------------------------------------------|
| Inputs           | [ 'Phys/TauIso' ]                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' } |
| CombinationCut   | (AM \> 8000.0) & (APTMAX \> 4000.0)                |
| MotherCut        | (ALL)                                              |
| DecayDescriptor  | Z0 -\> mu- mu+                                     |
| DecayDescriptors | [ ' Z0 -\> mu- mu+ ' ]                           |
| Output           | Phys/SelDitauCand_mumu_os/Particles                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDitauCand_h1mu_os

GaudiSequencer/SeqTauIso

GaudiSequencer/SEQ:SelTauIso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

FilterDesktop/SelTauIso_mu

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_mu/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

FilterDesktop/SelTauIso_h3

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h3' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h3/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

FilterDesktop/SelTauIso_h1

|                 |                             |
|-----------------|-----------------------------|
| Code            | (PTFrac05C \> 0.8)          |
| Inputs          | [ 'Phys/SelTauNoiso_h1' ] |
| DecayDescriptor | None                        |
| Output          | Phys/SelTauIso_h1/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauIso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r0p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

FilterDesktop/SelTauIso_e

|                 |                            |
|-----------------|----------------------------|
| Code            | (PTFrac05C \> 0.8)         |
| Inputs          | [ 'Phys/SelTauNoiso_e' ] |
| DecayDescriptor | None                       |
| Output          | Phys/SelTauIso_e/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauIso

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                        |
| Inputs          | [ 'Phys/SelTauIso_e' , 'Phys/SelTauIso_h1' , 'Phys/SelTauIso_h3' , 'Phys/SelTauIso_mu' ] |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/TauIso/Particles                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_h1mu_os

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TauIso' ]                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' , 'pi+' : '(ALL)' , 'pi-' : '(ALL)' } |
| CombinationCut   | (AM \> 16000.0) & (APTMAX \> 12000.0)                                                  |
| MotherCut        | (ALL)                                                                                  |
| DecayDescriptor  | [ Z0 -\> pi- mu+ ]cc                                                                 |
| DecayDescriptors | [ '[ Z0 -\> pi- mu+ ]cc' ]                                                         |
| Output           | Phys/SelDitauCand_h1mu_os/Particles                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/DitauMXLine

|                 |                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                        |
| Inputs          | [ 'Phys/SelDitauCand_emu_os' , 'Phys/SelDitauCand_h1mu_os' , 'Phys/SelDitauCand_h3mu_os' , 'Phys/SelDitauCand_mumu_os' ] |
| DecayDescriptor | None                                                                                                                       |
| Output          | Phys/DitauMXLine/Particles                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

AddRelatedInfo/RelatedInfo1_DitauMXLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/DitauMXLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo1_DitauMXLine/Particles |
