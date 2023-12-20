[[stripping21 lines]](./stripping21-index)

# StrippingCcbar2PpbarLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/Ccbar2PpbarLine/Particles |
| Postscale      | 1.0000000                      |
| HLT            | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingCcbar2PpbarLineVOIDFilter

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 300.0 ) |

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightProtons](./stripping21-commonparticles-stdtightprotons)/Particles')\>0 |

CombineParticles/Ccbar2PpbarLine

|                  |                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdTightProtons](./stripping21-commonparticles-stdtightprotons)' ]                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 1950.0 \*MeV) & (P \> 10.0 \*GeV) & (TRCHI2DOF \< 4.0) & ((PIDp-PIDpi) \> 20.0) & ((PIDp-PIDK) \> 15.0)' , 'p~-' : '(PT \> 1950.0 \*MeV) & (P \> 10.0 \*GeV) & (TRCHI2DOF \< 4.0) & ((PIDp-PIDpi) \> 20.0) & ((PIDp-PIDK) \> 15.0)' } |
| CombinationCut   | (in_range( 2750.0 \*MeV, AM, 4100.0 \*MeV))                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2)\< 9.0) & (in_range( 2800.0 \*MeV, MM, 4000.0 \*MeV)) & (PT\>6\*GeV)                                                                                                                                                                                  |
| DecayDescriptor  | J/psi(1S) -\> p+ p~-                                                                                                                                                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> p+ p~-' ]                                                                                                                                                                                                                                        |
| Output           | Phys/Ccbar2PpbarLine/Particles                                                                                                                                                                                                                                      |
