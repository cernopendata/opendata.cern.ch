[[stripping21 lines]](./stripping21-index)

# StrippingKs2PiPiee_PiPiLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/Ks2PiPiee_PiPiLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsElectrons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsElectrons](./stripping21-stdnopidselectrons) /Particles')\>0 |

**FilterDesktop/ElecsForKs2PiPiee**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16) &(TRGHOSTPROB \< 0.5) &(PIDe \> -4)        |
| Inputs          | [ 'Phys/ [StdNoPIDsElectrons](./stripping21-stdnopidselectrons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/ElecsForKs2PiPiee/Particles                                      |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) /Particles')\>0 |

**FilterDesktop/PionsForKs2PiPiee**

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16) &(TRGHOSTPROB \< 0.5) &(PIDK \< 5) |
| Inputs          | [ 'Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) ' ] |
| DecayDescriptor | None                                                          |
| Output          | Phys/PionsForKs2PiPiee/Particles                              |

**CombineParticles/Ks2PiPiee_PiPiLine**

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ElecsForKs2PiPiee' , 'Phys/PionsForKs2PiPiee' ]                                 |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }              |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm)                                          |
| MotherCut        | (M \< 800.0 \*MeV) &(MIPDV(PRIMARY) \< 1 \*mm) & ((BPVVDSIGN\*M/P) \> 0.8953\*2.9979e-01) |
| DecayDescriptor  | KS0 -\> pi+ pi- e+ e-                                                                     |
| DecayDescriptors | [ 'KS0 -\> pi+ pi- e+ e-' ]                                                             |
| Output           | Phys/Ks2PiPiee_PiPiLine/Particles                                                         |
