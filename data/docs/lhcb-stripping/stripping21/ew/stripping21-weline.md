[[stripping21 lines]](./stripping21-index)

# StrippingWeLine

## Properties:

|                |                       |
|----------------|-----------------------|
| OutputLocation | Phys/WeLine/Particles |
| Postscale      | 1.0000000             |
| HLT            | None                  |
| Prescale       | 1.0000000             |
| L0DU           | None                  |
| ODIN           | None                  |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsElectrons_Particles**

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsElectrons](./stripping21-stdallnopidselectrons) /Particles')\>0 |

**FilterDesktop/WeLine**

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PPINFO(LHCb.ProtoParticle.CaloPrsE,0)\>50.0) & (PPINFO(LHCb.ProtoParticle.CaloEcalE,0)\>P\*0.1) & (PPINFO(LHCb.ProtoParticle.CaloHcalE,99999) 20.0\*GeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsElectrons](./stripping21-stdallnopidselectrons) ' ]                                                                               |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/WeLine/Particles                                                                                                                                     |
