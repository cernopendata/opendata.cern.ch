[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDstarD02Kpipi0RS

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/DstarD02Kpipi0RS/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 0.083000000                     |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

GaudiSequencer/SeqPi0ForDstarD02Kpipi0

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/Pi0ForDstarD02Kpipi0

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                     |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/Pi0ForDstarD02Kpipi0/Particles                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02Kpipi0ForDstarD02Kpipi0

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0ForDstarD02Kpipi0' , 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (MIPCHI2DV(PRIMARY)\>4) & (TRCHI2DOF\<5) & ((PPINFO(LHCb.ProtoParticle.RichDLLk,-1000))\>0)' , 'K-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (MIPCHI2DV(PRIMARY)\>4) & (TRCHI2DOF\<5) & ((PPINFO(LHCb.ProtoParticle.RichDLLk,-1000))\>0)' , 'pi+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (MIPCHI2DV(PRIMARY)\>4) & (TRCHI2DOF\<5) & ((PPINFO(LHCb.ProtoParticle.RichDLLk,-1000))\<0)' , 'pi-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (MIPCHI2DV(PRIMARY)\>4) & (TRCHI2DOF\<5) & ((PPINFO(LHCb.ProtoParticle.RichDLLk,-1000))\<0)' , 'pi0' : '(PT\>800\*MeV) & (P\>5\*GeV)' } |
| CombinationCut   | (ADAMASS('D0')\<200\*MeV) & (ADOCA(1,2) \< 1.5) & (AHASCHILD(((ABSID == 'K+') \| (ABSID == 'pi+')) & (MIPCHI2DV(PRIMARY)\>40)))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | (BPVDIRA\>0.9) & (PT\>2.5\*GeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [D0 -\> K- pi+ pi0]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi0]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/D02Kpipi0ForDstarD02Kpipi0/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

CombineParticles/DstarD02Kpipi0RS

|                  |                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02Kpipi0ForDstarD02Kpipi0' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : '(ALL)' , 'D~0' : '(ALL)' , 'pi+' : '(PT\>170\*MeV) & (BPVIP()\<0.5\*mm)' , 'pi-' : '(PT\>170\*MeV) & (BPVIP()\<0.5\*mm)' } |
| CombinationCut   | (ADAMASS('D\*(2010)+')\<200\*MeV)                                                                                                                 |
| MotherCut        | (PT\>3\*GeV) & ((M-M2)\>(145.5-10)\*MeV) & ((M-M2)\<(145.5+20)\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVIPCHI2()\<100)                              |
| DecayDescriptor  | [D\*(2010)+ -\> pi+ D0]cc                                                                                                                       |
| DecayDescriptors | [ '[D\*(2010)+ -\> pi+ D0]cc' ]                                                                                                               |
| Output           | Phys/DstarD02Kpipi0RS/Particles                                                                                                                   |
