The OPERA experiment was designed to conclusively prove the oscillation of muon neutrinos to tau neutrinos in appearance mode, i.e. through the observation of the appearance of tau neutrinos in a muon neutrino beam. Tau neutrinos are identified by the presence of the tau lepton in the final state.

The detector was located at the Gran Sasso Underground laboratory in Italy, 730 km away from the high-intensity and high-energy CNGS (Cern Neutrino to Gran Sasso) beam.

The detector was a hybrid apparatus consisting of an emulsion/lead target complemented by electronic detectors. The neutrino target consisted of nuclear emulsion films, acting as tracking devices with micrometric resolution for the detection of the short-lived tau lepton, alternated with lead plates, providing the kton mass scale of the apparatus. The electronic detectors provided the time stamp of the neutrino interaction, preselected the interaction region, identified muons and measured their charge and momentum.

The detector was made up of two identical super-modules (SM) aligned along the CNGS beam direction, each made of a target section and a muon spectrometer. In front of the first SM there was a veto plane made of two planes of resistive plate chambers (RPC). Each super-module was composed of a target section followed by a muon spectrometer. The target consisted of a multi-layer array of 31 target walls interleaved with 31 Target Trackers (TT), made of a double layered plane of long scintillator strips. A target wall was an assembly of horizontal trays each loaded with Emulsion Cloud Chamber target units, called bricks. In the whole apparatus there were more than 150000 bricks, each consisting of 57 emulsion films, 300 micron thick, interleaved with 56 lead plates, 1 mm thick, for a mass of 8.3 kg. The total mass of the target amounted to about 1250 tons. The muon spectrometer was composed of a magnet equipped with resistive plate chambers and drift tubes. Interface emulsion detectors, called Changeable Sheets, were attached to the downstream face of each brick and were meant to confirm the prediction of the electronic detector before analysing the full brick for the neutrino interaction location.

Nuclear emulsions are a particular type of photographic emulsions used for elementary particle studies. Techniques for their production and application have been developed in the first half of 1900. Their micrometric spatial resolution made them one of the first particle detectors, largely employed in the High Energy Physics field. A vigorous R&D on fully automated optical microscopes was conducted over the last decades which made the use of nuclear emulsions possible for large-scale applications like OPERA where more than 110000 m2 of films were produced by the Fuji Film Company.

The OPERA emulsion film had a pair of 44 micron emulsion layers coated on both sides of a 205 micron transparent cellulose triacetate base. The emulsion layer consisted of silver bromide (AgBr) crystals dispersed in a gelatin binder. The size of the grains was about 0.2 micron.

<center>
<img src="/static/docs/opera-event-reconstruction/opera-event-reconstruction-emu-electronic.png" width="80%">
<br/>
<div style="width: 80%">
<em>An emulsion film with 44 micron emulsion layers coated on both sides of a 205 micron plastic base; (b) Electron microscope view of AgBr crystals in the emulsion; (c) OPERA emulsion film; (d) examples of minimum ionising particle (mip) tracks and Compton electrons in nuclear emulsions.</em>
</div>
</center>

When a charged particle passes through the emulsion medium, the energy released frees silver atoms creating metallic silver on the surface of a bromide crystal, called latent image, not visible yet, made of a few silver atoms on crystals, each of them made of billions of atoms. The “contrail” of charged particles in nuclear emulsion are then seen after a chemical amplification of the latent image, with a gain factor up to several billions. Under this chemical development procedure, silver atoms with a diameter of about 0.6 micron are created, visible as "grains" at an optical microscope.

In the OPERA scanning laboratories in Europe and Japan the emulsion films were analysed by automatic scanning systems. During the scanning, the emulsion was placed on a glass plate equipped with a vacuum system. Moving the focal plane of the objective through the emulsion thickness, a sequence of 16 tomographic images of each field of view was obtained, where the images are taken at equally spaced depth levels. The acquired images were then converted into a grey scale of 256 levels, sent to a vision processor board, hosted in the control workstation, and analysed to search for sequences of aligned grains.

<center>
<img src="/static/docs/opera-event-reconstruction/opera-event-reconstruction-animated-gif.gif" width="80%">
<br/>
<div style="width: 80%">
<em>One nuclear emulsion layer as seen at an OPERA fully automated microscope while moving the focal plane of the objective.</em>
</div>
</center>

Grains produced by the particle, indeed, are recognized as a cluster of pixels and form the so called micro-track in one emulsion layer. Micro-tracks on the top and bottom emulsion layers are then connected across the plastic base to form a base-track. A sequence of base-tracks from different emulsion plates defines the particle track inside the ECC.

<center>
<img src="/static/docs/opera-event-reconstruction/opera-event-reconstruction-micro-reco.png" width="80%">
<br/>
<div style="width: 80%">
<em>Schematic visualization of the image grabbing and "micro-track" reconstruction by combining clusters at different levels.</em>
</div>
</center>

All tracks were digitised, allowing a fully-automatic offline analysis, which included the alignment of sequential nuclear emulsion films with a micrometric precision and the reconstruction of all tracks. Discarding passing-through tracks, it was possible to reconstruct interaction and decay vertices, to search for downstream particle decays, to measure particle momentum by Multiple Coulomb Scattering and to identify electrons by detecting the induced shower.

<center>
<img src="/static/docs/opera-event-reconstruction/opera-event-reconstruction-event-reco.png" width="80%">
<br/>
<div style="width: 80%">
<em>Different steps of the emulsion data processing. (Left) All base-tracks in 11 films of the volume under study are reconstructed; they participate in the alignment process from which tracks are reconstructed (middle); passing-through tracks are discarded and the interaction vertex is reconstructed (right).</em>
</div>
</center>
