[[stripping21r1 lines]](./stripping21r1-index)

# StrippingZ02eeSSLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/Z02eeSSLine/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles**

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsElectrons](./stripping21r1-stdallnopidselectrons) /Particles')\>0 |

**CombineParticles/Z02eeSSLine**

|                  |                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllNoPIDsElectrons](./stripping21r1-stdallnopidselectrons) ' ]                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '((PT\>10.0\*GeV) & (PPINFO(LHCb.ProtoParticle.CaloPrsE,0)\>50.0) & (PPINFO(LHCb.ProtoParticle.CaloEcalE,0)\>P\*0.1) & (PPINFO(LHCb.ProtoParticle.CaloHcalE,99999) 10.0\*GeV) & (PPINFO(LHCb.ProtoParticle.CaloPrsE,0)\>50.0) & (PPINFO(LHCb.ProtoParticle.CaloEcalE,0)\>P\*0.1) & (PPINFO(LHCb.ProtoParticle.CaloHcalE,99999) |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                |
| MotherCut        | (MM\>40.0\*GeV)                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [Z0 -\> e- e-]cc                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[Z0 -\> e- e-]cc' ]                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/Z02eeSSLine/Particles                                                                                                                                                                                                                                                                                                                           |
