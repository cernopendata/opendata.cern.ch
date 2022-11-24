[[stripping21r1 lines]](./stripping21r1-index)

# StrippingKs2PiPiee_PiPiFromTracksLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/Ks2PiPiee_PiPiFromTracksLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles**

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdDiElectronFromTracks](./stripping21r1-stddielectronfromtracks) /Particles')\>0 |

**FilterDesktop/ElecsFromTracksForKs2PiPiee**

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE(ABSID\<14,PT) \> 100.0) &(MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 16) &(MAXTREE(ABSID\<14,TRGHOSTPROB) \< 0.5) &(MINTREE(ABSID\<14,PIDe) \> -4) |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21r1-stddielectronfromtracks) ' ]                                                                         |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/ElecsFromTracksForKs2PiPiee/Particles                                                                                                                |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsPions](./stripping21r1-stdnopidspions) /Particles')\>0 |

**FilterDesktop/PionsForKs2PiPiee**

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16) &(TRGHOSTPROB \< 0.5) &(PIDK \< 5)   |
| Inputs          | [ 'Phys/ [StdNoPIDsPions](./stripping21r1-stdnopidspions) ' ] |
| DecayDescriptor | None                                                            |
| Output          | Phys/PionsForKs2PiPiee/Particles                                |

**CombineParticles/Ks2PiPiee_PiPiFromTracksLine**

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ElecsFromTracksForKs2PiPiee' , 'Phys/PionsForKs2PiPiee' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                      |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm)                                          |
| MotherCut        | (M \< 800.0 \*MeV) &(MIPDV(PRIMARY) \< 1 \*mm) & ((BPVVDSIGN\*M/P) \> 0.8953\*2.9979e-01) |
| DecayDescriptor  | KS0 -\> pi+ pi- J/psi(1S)                                                                 |
| DecayDescriptors | [ 'KS0 -\> pi+ pi- J/psi(1S)' ]                                                         |
| Output           | Phys/Ks2PiPiee_PiPiFromTracksLine/Particles                                               |
