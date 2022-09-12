[[stripping21 lines]](./stripping21-index)

# StrippingLFVB2heMuLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/LFVB2heMuLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21-stdloosemuons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsKaons](./stripping21-stdnopidskaons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsProtons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsProtons](./stripping21-stdnopidsprotons) /Particles')\>0 |

**CombineParticles/LFVB2heMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' , 'Phys/ [StdNoPIDsKaons](./stripping21-stdnopidskaons) ' , 'Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) ' , 'Phys/ [StdNoPIDsProtons](./stripping21-stdnopidsprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'e+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDe \> 2)' , 'e-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDe \> 2)' , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3)' , 'p+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDp\>5) & (TRGHOSTPROB\<0.3)' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>25.)&( TRCHI2DOF \< 3 )& (TRGHOSTPROB\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>25.)&( TRCHI2DOF \< 3 )& (TRGHOSTPROB\<0.3)' , 'p\~-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDp\>5) & (TRGHOSTPROB\<0.3)' } |
| CombinationCut   | (ADAMASS('B+')\<600\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 600\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[B+ -\> K+ e+ mu-]cc' , '[B+ -\> K- e+ mu+]cc' , '[B+ -\> K+ e- mu+]cc' , '[B+ -\> pi+ e+ mu-]cc' , '[B+ -\> pi- e+ mu+]cc' , '[B+ -\> pi+ e- mu+]cc' , '[B+ -\> p+ e+ mu-]cc' , '[B- -\> p+ e- mu-]cc' , '[B+ -\> p+ e- mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/LFVB2heMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

****Tools:****

**OfflineVertexFitter**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| maxDeltaChi2 :           | 0.0010000000                                                                                              |
| applyMomMassConstraint : | False                                                                                                     |
| PropertiesPrint :        | False                                                                                                     |
| applyDauMassConstraint : | False                                                                                                     |
| AuditStart :             | False                                                                                                     |
| useResonanceVertex :     | False                                                                                                     |
| maxIter :                | 10                                                                                                        |
| includeDauVertexChi2 :   | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| RootOnTES :              | None                                                                                                      |
| PrintMyAlg :             | True                                                                                                      |
| RootInTES :              | None                                                                                                      |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| Transporter :            | ParticleTransporter:PUBLIC                                                                                |
| widthThreshold :         | 2.0000000                                                                                                 |
| ContextService :         | AlgContextSvc                                                                                             |
| AuditTools :             | False                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| ErrorsPrint :            | True                                                                                                      |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| maxDeltaZ :              | 1.0000000                                                                                                 |
| UseEfficiencyRowFormat : | True                                                                                                      |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |
