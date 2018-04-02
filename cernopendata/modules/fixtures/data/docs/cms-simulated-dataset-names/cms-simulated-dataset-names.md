### What is the “simulated dataset” name?

It’s the part of the dataset name before the second 'slash', i.e. for the dataset

`/GluGluToHToZZTo4L_M-550_7TeV-minloHJJ-pythia6-tauola/Summer11LegDR-PU_S13_START53_LV6-v1/AODSIM`

the dataset name is

`GluGluToHToZZTo4L_M-550_7TeV-minloHJJ-pythia6-tauola`.

### Convention

CMS uses the following convention for this name:

`PROCESS_RANGETYPE-RANGELOWtoRANGEHIGH_FILTER_TUNE_COMMENT_COMENERGY-GENERATOR`,

where

*   `PROCESS` is the physics process in the sample, e.g. `QCD`, `TT`, `W`, `DY`
*   `RANGETYPE` is the variable the sample is binned in, e.g. `PT`, `M`
*   `RANGELOW` is the lower bound of that range in GeV, e.g. `0`, `10`, `200`
*   `RANGEHIGH` is the upper bound
*   `FILTER` denotes information on additional filters applied
*   `TUNE` is the underlying-event tune (e.g. `TuneZ2Star`)
*   `COMMENT` for additional comments
*   `COMENERGY` is the centre-of-mass collision energy, e.g. `7TeV`, `10TeV`
*   `GENERATOR` is the generator used, e.g. `pythia6`, `herwigpp`, `sherpa`

Some details on all these parts are below.

#### PROCESS

To unify this part CMS uses the following conventions:

*   all ‘particles’ start with capital letters, followed by minor letters, e.g. `W`, `Z`, `Mu`, `Tau`, `E`, `Nu`, `Wplus`, `H`, `Jets`, `Tbar`, `B`, `Bbar`
*   if a specific decay is simulated, this is specified using the keyword `To`, e.g. `WToENu`, `HToWWTo2L2Nu`
*   initial-state particles are only specified if needed to distinguish between other processes, e.g. `GluGluToWW` with respect to `WW`
*   charge for a particle is only specified if relevant, i.e. `Wplus` is used if only W<sup>+</sup> is in the sample, and `Tbar` if an anti-top is present; `WplusWminus` **is not** used for W-pair production and a top-antitop pair is represented with `TT`
*   if there is (a) more then one particle of the same kind and (b) more then two particles in total, say, `2E2Nu` is used rather then `EENuNu`

The following conventions are applied for the most common particles:

<table class="table table-condensed">

<thead>

<tr class="header">

<th align="left">Particle</th>

<th align="left">Keyword</th>

<th align="left">modifications if needed</th>

</tr>

</thead>

<tbody>

<tr class="odd">

<td align="left">electron/positron</td>

<td align="left">`E`</td>

<td align="left">`Eminus`, `Eplus`</td>

</tr>

<tr class="even">

<td align="left">muon</td>

<td align="left">`Mu`</td>

<td align="left">`Muplus`, `Muminus`</td>

</tr>

<tr class="odd">

<td align="left">tau</td>

<td align="left">`Tau`</td>

<td align="left">`Tauplus`, `Tauminus`</td>

</tr>

<tr class="even">

<td align="left">charged lepton</td>

<td align="left">`L`</td>

</tr>

<tr class="odd">

<td align="left">neutrino</td>

<td align="left">`Nu`</td>

<td align="left">`Nue`, `Numu`, `Nutau`, `Nuebar`,…</td>

</tr>

<tr class="even">

<td align="left">W</td>

<td align="left">`W`</td>

<td align="left">`Wplus`, `Wminus`, `Wprime`</td>

</tr>

<tr class="odd">

<td align="left">Z (no photon)</td>

<td align="left">`Z`</td>

<td align="left">`Zprime`</td>

</tr>

<tr class="even">

<td align="left">Z/photon (Drell-Yan)</td>

<td align="left">`DY`</td>

</tr>

<tr class="odd">

<td align="left">photon</td>

<td align="left">`G`</td>

</tr>

<tr class="even">

<td align="left">gluon</td>

<td align="left">`Glu`</td>

</tr>

<tr class="odd">

<td align="left">top</td>

<td align="left">`T`</td>

<td align="left">`Tbar`, `Tprime`</td>

</tr>

<tr class="even">

<td align="left">bottom</td>

<td align="left">`B`</td>

<td align="left">`Bbar`, `Bprime`</td>

</tr>

<tr class="odd">

<td align="left">quark</td>

<td align="left">`Q`</td>

<td align="left">`Qbar`</td>

</tr>

<tr class="even">

<td align="left">jet</td>

<td align="left">`Jet`</td>

<td align="left">`Jets` for more than one (inclusive); `1Jet`, `2Jets`, … for exclusive</td>

</tr>

<tr class="odd">

<td align="left">jet</td>

<td align="left">`J`</td>

<td align="left">for decay products, if both quarks and gluons are produced</td>

</tr>

</tbody>

</table>

#### RANGETYPE, RANGELOW, RANGEHIGH

This part denotes the variable (if at all) in which the sample is binned. Typical possibilities are `Pt` (pthat), `M` (inv. mass), as well as the range for this variable. This part of the name may also be used togther with `M` to specify the mass of a particle that is used as a parameter (e.g. Higgs mass, Z′ mass, …). Examples are

*   `Pt-100To200` for binning in pthat from 100 GeV to 200 GeV
*   `Pt-50` if there is only a lower cut on pthat
*   `M-30` as a lower inv. mass cut (e.g. in Drell-Yan)
*   `M-160` for Higgs mass of 160 GeV

If needed, the variable may be accompanied by specification of the particle in the process on which the cut is applied:

*   `PtW-300` if there is a lower cut on the W pthat

This part of the dataset name may be dropped if there is no binning, inv. mass cuts etc.

#### FILTER

This part specifies a GEN-level filter for the production, if present. The part is however not standardised; here a few examples:

*   `EMEnriched`: some filter — enriching the sample with electrons/photons — is applied
*   `MuEnriched`: GEN-level filter on Muons
*   `MuEnrichedPt5`: cut on GEN-level muons of 5 GeV

#### COMMENT

Used only if necessary information could not be put in any of the other fields. e.g. only QCD or only EWK production, special selections etc.

#### COMENERGY and GENERATOR

Units are added to integers in `COMENERGY`, i.e. `7TeV`, `10TeV`, `900GeV`, `2360GeV` and so on.

The generators used are:

<table class="table table-condensed">

<thead>

<tr class="header">

<th align="left">Generator</th>

<th align="left">Keyword</th>

</tr>

</thead>

<tbody>

<tr class="odd">

<td align="left">Pythia6</td>

<td align="left">`pythia6`</td>

</tr>

<tr class="even">

<td align="left">Pythia8</td>

<td align="left">`pythia8`</td>

</tr>

<tr class="odd">

<td align="left">Herwig6</td>

<td align="left">`herwig6`</td>

</tr>

<tr class="even">

<td align="left">Herwig++</td>

<td align="left">`herwigpp`</td>

</tr>

<tr class="odd">

<td align="left">Sherpa</td>

<td align="left">`sherpa`</td>

</tr>

<tr class="even">

<td align="left">MadGraph</td>

<td align="left">`madgraph`</td>

</tr>

<tr class="odd">

<td align="left">MadGraph **not showered with Pythia6**</td>

<td align="left">`madgraph-herwigpp`, …</td>

</tr>

<tr class="even">

<td align="left">Alpgen</td>

<td align="left">`alpgen`</td>

</tr>

<tr class="odd">

<td align="left">Alpgen **not showered with Pythia6**</td>

<td align="left">`alpgen-herwig6`, …</td>

</tr>

<tr class="even">

<td align="left">MC@NLO</td>

<td align="left">`mcatnlo`</td>

</tr>

<tr class="odd">

<td align="left">MC@NLO **not showered with Herwig6**</td>

<td align="left">`mcatnlo-pythia6`, …``</td>

</tr>

<tr class="even">

<td align="left">POWHEG</td>

<td align="left">`powheg`</td>

</tr>

<tr class="odd">

<td align="left">POWHEG **not showered with Pythia6**</td>

<td align="left">`powheg-pythia8`, …</td>

</tr>

<tr class="even">

<td align="left">HARDCOL</td>

<td align="left">`hardcol`</td>

</tr>

<tr class="odd">

<td align="left">BCVEGPY 2</td>

<td align="left">`bcvegpy2`</td>

</tr>

<tr class="even">

<td align="left">…</td>

<td align="left">…</td>

</tr>

</tbody>

</table>

If a specialised decay tool was used, it was appended to the name, e.g. if EvtGen was used after Pythia6, the keyword would be `…-pythia6-evtgen`.
