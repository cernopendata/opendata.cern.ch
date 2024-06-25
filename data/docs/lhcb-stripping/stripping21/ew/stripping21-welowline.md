[[stripping21 lines]](./stripping21-index)

# StrippingWeLowLine

## Properties:

|                |                          |
|----------------|--------------------------|
| OutputLocation | Phys/WeLowLine/Particles |
| Postscale      | 1.0000000                |
| HLT            | None                     |
| Prescale       | 0.10000000               |
| L0DU           | None                     |
| ODIN           | None                     |

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

**FilterDesktop/WeLowLine**

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PPINFO(LHCb.ProtoParticle.CaloPrsE,0)\>50.0) & (PPINFO(LHCb.ProtoParticle.CaloEcalE,0)\>P\*0.1) & (PPINFO(LHCb.ProtoParticle.CaloHcalE,99999) 15.0\*GeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsElectrons](./stripping21-stdallnopidselectrons) ' ]                                                                               |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/WeLowLine/Particles                                                                                                                                  |
