[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCcbar2PpbarDetachedLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Ccbar2PpbarDetachedLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingCcbar2PpbarDetachedLineVOIDFilter

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600.0 ) |

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightProtons](./stripping21r1-commonparticles-stdtightprotons)/Particles')\>0 |

CombineParticles/Ccbar2PpbarDetachedLine

|                  |                                                                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdTightProtons](./stripping21r1-commonparticles-stdtightprotons)' ]                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 1000.0 \*MeV) & (P \> -2.0 \*GeV) & (TRCHI2DOF \< 5.0) & ((PIDp-PIDpi) \> 15.0) & ((PIDp-PIDK) \> 10.0) & (BPVIPCHI2()\>9)' , 'p~-' : '(PT \> 1000.0 \*MeV) & (P \> -2.0 \*GeV) & (TRCHI2DOF \< 5.0) & ((PIDp-PIDpi) \> 15.0) & ((PIDp-PIDK) \> 10.0) & (BPVIPCHI2()\>9)' } |
| CombinationCut   | (in_range( 2650.0 \*MeV, AM, 1000000.0 \*MeV))                                                                                                                                                                                                                                                            |
| MotherCut        | (VFASPF(VCHI2)\< 9.0) & (in_range( 2700.0 \*MeV, MM, 1000000.0 \*MeV)) & (BPVDLS\>5)                                                                                                                                                                                                                      |
| DecayDescriptor  | J/psi(1S) -\> p+ p~-                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'J/psi(1S) -\> p+ p~-' ]                                                                                                                                                                                                                                                                              |
| Output           | Phys/Ccbar2PpbarDetachedLine/Particles                                                                                                                                                                                                                                                                    |
