[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingDitauMXssnoisoLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/DitauMXssnoisoLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 0.10000000                        |
| L0DU           | None                              |
| ODIN           | None                              |

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

GaudiSequencer/SeqDitauMXssnoisoLine

GaudiSequencer/SEQ:SelDitauCand_h1mu_ss_noiso

GaudiSequencer/SeqTauNoiso

GaudiSequencer/SEQ:SelTauNoiso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauNoiso

|                 |                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                |
| Inputs          | [ 'Phys/SelTauNoiso_e' , 'Phys/SelTauNoiso_h1' , 'Phys/SelTauNoiso_h3' , 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                                                                                               |
| Output          | Phys/TauNoiso/Particles                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_h1mu_ss_noiso

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TauNoiso' ]                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' , 'pi+' : '(ALL)' , 'pi-' : '(ALL)' } |
| CombinationCut   | (AM \> 16000.0) & (APTMAX \> 12000.0)                                                  |
| MotherCut        | (ALL)                                                                                  |
| DecayDescriptor  | [ Z0 -\> pi- mu- ]cc                                                                 |
| DecayDescriptors | [ '[ Z0 -\> pi- mu- ]cc' ]                                                         |
| Output           | Phys/SelDitauCand_h1mu_ss_noiso/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDitauCand_mumu_ss_noiso

GaudiSequencer/SeqTauNoiso

GaudiSequencer/SEQ:SelTauNoiso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauNoiso

|                 |                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                |
| Inputs          | [ 'Phys/SelTauNoiso_e' , 'Phys/SelTauNoiso_h1' , 'Phys/SelTauNoiso_h3' , 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                                                                                               |
| Output          | Phys/TauNoiso/Particles                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_mumu_ss_noiso

|                  |                                                    |
|------------------|----------------------------------------------------|
| Inputs           | [ 'Phys/TauNoiso' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' } |
| CombinationCut   | (AM \> 8000.0) & (APTMAX \> 4000.0)                |
| MotherCut        | (ALL)                                              |
| DecayDescriptor  | [ Z0 -\> mu- mu- ]cc                             |
| DecayDescriptors | [ '[ Z0 -\> mu- mu- ]cc' ]                     |
| Output           | Phys/SelDitauCand_mumu_ss_noiso/Particles          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDitauCand_emu_ss_noiso

GaudiSequencer/SeqTauNoiso

GaudiSequencer/SEQ:SelTauNoiso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauNoiso

|                 |                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                |
| Inputs          | [ 'Phys/SelTauNoiso_e' , 'Phys/SelTauNoiso_h1' , 'Phys/SelTauNoiso_h3' , 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                                                                                               |
| Output          | Phys/TauNoiso/Particles                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_emu_ss_noiso

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TauNoiso' ]                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(ALL)' , 'e-' : '(ALL)' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' } |
| CombinationCut   | (AM \> 12000.0) & (APTMAX \> 9000.0)                                                 |
| MotherCut        | (ALL)                                                                                |
| DecayDescriptor  | [ Z0 -\> e- mu- ]cc                                                                |
| DecayDescriptors | [ '[ Z0 -\> e- mu- ]cc' ]                                                        |
| Output           | Phys/SelDitauCand_emu_ss_noiso/Particles                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDitauCand_h3mu_ss_noiso

GaudiSequencer/SeqTauNoiso

GaudiSequencer/SEQ:SelTauNoiso_mu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_mu

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 13) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISMUON) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]                 |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/SelTauNoiso_mu/Particles                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h3

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelTauNoiso_h3

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' , 'pi-' : '(ETA \> 2.0) & (PT \> 1000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (ISPIONORKAON)' } |
| CombinationCut   | (AM \> 600.0) & (AM \< 1500.0)                                                                                                                                                                                                                               |
| MotherCut        | (PT \> 5000.0) & (DRTRIOMAX \< 0.4) & (VCHI2PDOF \< 10.0)                                                                                                                                                                                                    |
| DecayDescriptor  | [ tau- -\> pi- pi- pi+ ]cc                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ tau- -\> pi- pi- pi+ ]cc' ]                                                                                                                                                                                                                         |
| Output           | Phys/SelTauNoiso_h3/Particles                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_h1

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_h1

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ETA \> 2.25) & (PT \> 5000.0) & (~ISMUONLOOSE) & (ALL) & (TRPCHI2 \> 0.01) & (HCALFrac \> 0.05) & (ETA \< 3.75) & (ISPIONORKAON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/SelTauNoiso_h1/Particles                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelTauNoiso_e

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)/Particles',True)\>0 |

FilterDesktop/SelTauNoiso_e

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CaloPrsE \> 50.0) & (ETA \> 2.0) & (PT \> 5000.0) & (ABSID == 11) & (ECALFrac \> 0.1) & (ALL) & (TRPCHI2 \> 0.01) & (ETA \< 4.5) & (~ISMUONLOOSE) |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r1p1-commonparticles-stdallnopidselectrons)' ]                                                      |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/SelTauNoiso_e/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/TauNoiso

|                 |                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                |
| Inputs          | [ 'Phys/SelTauNoiso_e' , 'Phys/SelTauNoiso_h1' , 'Phys/SelTauNoiso_h3' , 'Phys/SelTauNoiso_mu' ] |
| DecayDescriptor | None                                                                                               |
| Output          | Phys/TauNoiso/Particles                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDitauCand_h3mu_ss_noiso

|                  |                                                                                          |
|------------------|------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TauNoiso' ]                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(ALL)' , 'mu-' : '(ALL)' , 'tau+' : '(ALL)' , 'tau-' : '(ALL)' } |
| CombinationCut   | (AM \> 12000.0) & (APTMAX \> 9000.0)                                                     |
| MotherCut        | (ALL)                                                                                    |
| DecayDescriptor  | [ Z0 -\> tau- mu- ]cc                                                                  |
| DecayDescriptors | [ '[ Z0 -\> tau- mu- ]cc' ]                                                          |
| Output           | Phys/SelDitauCand_h3mu_ss_noiso/Particles                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/DitauMXssnoisoLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                |
| Inputs          | [ 'Phys/SelDitauCand_emu_ss_noiso' , 'Phys/SelDitauCand_h1mu_ss_noiso' , 'Phys/SelDitauCand_h3mu_ss_noiso' , 'Phys/SelDitauCand_mumu_ss_noiso' ] |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/DitauMXssnoisoLine/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

AddRelatedInfo/RelatedInfo1_DitauMXssnoisoLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/DitauMXssnoisoLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo1_DitauMXssnoisoLine/Particles |
