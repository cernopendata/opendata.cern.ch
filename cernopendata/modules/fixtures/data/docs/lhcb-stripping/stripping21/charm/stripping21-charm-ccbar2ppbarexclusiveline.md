[[stripping21 lines]](./stripping21-index)

# StrippingCcbar2PpbarExclusiveLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/Ccbar2PpbarExclusiveLine/Particles |
| Postscale      | 1.0000000                               |
| HLT            | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingCcbar2PpbarExclusiveLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 20.0 ) |

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightProtons](./stripping21-commonparticles-stdtightprotons)/Particles')\>0 |

CombineParticles/Ccbar2PpbarExclusiveLine

|                  |                                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdTightProtons](./stripping21-commonparticles-stdtightprotons)' ]                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 550.0 \*MeV) & (P \> -2.0 \*GeV) & (TRCHI2DOF \< 5.0) & ((PIDp-PIDpi) \> 20.0) & ((PIDp-PIDK) \> 15.0)' , 'p~-' : '(PT \> 550.0 \*MeV) & (P \> -2.0 \*GeV) & (TRCHI2DOF \< 5.0) & ((PIDp-PIDpi) \> 20.0) & ((PIDp-PIDK) \> 15.0)' } |
| CombinationCut   | (in_range( 0.0 \*MeV, AM, 1000000.0 \*MeV))                                                                                                                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2)\< 9.0) & (in_range( 0.0 \*MeV, MM, 1000000.0 \*MeV))                                                                                                                                                                                               |
| DecayDescriptor  | J/psi(1S) -\> p+ p~-                                                                                                                                                                                                                                              |
| DecayDescriptors | [ 'J/psi(1S) -\> p+ p~-' ]                                                                                                                                                                                                                                      |
| Output           | Phys/Ccbar2PpbarExclusiveLine/Particles                                                                                                                                                                                                                           |
