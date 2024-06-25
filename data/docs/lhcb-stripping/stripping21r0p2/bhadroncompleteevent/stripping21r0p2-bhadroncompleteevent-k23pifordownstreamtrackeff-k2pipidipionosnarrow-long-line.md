[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingK23PiForDownstreamTrackEff_K2PiPiDipionOSNarrow_Long_Line

## Properties:

|                |                                                                          |
|----------------|--------------------------------------------------------------------------|
| OutputLocation | Phys/K23PiForDownstreamTrackEff_K2PiPiDipionOSNarrow_Long_Line/Particles |
| Postscale      | 1.0000000                                                                |
| HLT1           | None                                                                     |
| HLT2           | None                                                                     |
| Prescale       | 0.20000000                                                               |
| L0DU           | None                                                                     |
| ODIN           | None                                                                     |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/LongPi_forK23PiForDownstreamTrackEff

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 49.0)                                                    |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/LongPi_forK23PiForDownstreamTrackEff/Particles                             |

CombineParticles/K23PiForDownstreamTrackEff_K2PiPiDipionOSNarrow_Long_Line

|                  |                                                                                                                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LongPi_forK23PiForDownstreamTrackEff' ]                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P \> 1500 ) & (PT \> 125 ) & (PROBNNghost \< 0.25 ) & (PROBNNpi \> 0.6 ) & (MIPCHI2DV(PRIMARY) \> 16.0 ) & (PROBNNp \< 0.1 )' , 'pi-' : '(P \> 1500 ) & (PT \> 125 ) & (PROBNNghost \< 0.25 ) & (PROBNNpi \> 0.6 ) & (MIPCHI2DV(PRIMARY) \> 16.0 ) & (PROBNNp \< 0.1 )' } |
| CombinationCut   | AALL                                                                                                                                                                                                                                                                                               |
| MotherCut        | (M \> 275 ) & (M \< 500 ) & (VFASPF(VCHI2/VDOF) \< 2 ) & (BPVVDCHI2 \> 100 ) & (VFASPF(VZ) \> 100.0 ) & (VFASPF(VZ) \< 2200.0 ) & (PT \> 300 ) & (P \> 3000 ) & (BPVDIRA \> 0.9995 ) & ( MCORRPi \< 600 ) & (PSEUDOERR \< 30 ) & (ADMASS('KS0') \> 40)                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ 'phi(1020) -\> pi+ pi-' ]                                                                                                                                                                                                                                                                      |
| Output           | Phys/K23PiForDownstreamTrackEff_K2PiPiDipionOSNarrow_Long_Line/Particles                                                                                                                                                                                                                           |
