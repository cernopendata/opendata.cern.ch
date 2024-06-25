The number of events in the simulated datasets do not match the number of events we expect to observe for each process, so we need to normalize the simulation to correspond to some cross section. Cross sections evaluated at next-to-leading order (NLO) or next-to-next-to-leading order (NNLO) in perturbative QCD are preferred, because they are more accurate. However, leading-order simulation remains the default for many SM processes, so higher-order cross sections cannot be extracted from the simulation itself. This page documents cross sections commonly used in CMS for Run 1 and Run 2 datasets.

## <a name="run1">Run 1</a>

Selected SM cross section values for Run 1 datasets can be found in the following tables. More details about these cross sections are available [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/StandardModelCrossSections).<br>

Higher-order top quark cross sections are available from the LHC Physics Working Group for all LHC energies:

- Top quark pair production at [NNLO](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO)
- Single top quark production at [NLO](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec) and at [NNLO](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef)<br>

### <a name="7tev">7 TeV</a>

<table class=\"ui celled table\">
  <thead>
    <tr class="header">
      <th>Process<br></th>
      <th>Generator/Source<br></th>
      <th>Phase space cuts<br></th>
      <th>Order<br></th>
      <th>Final state<br></th>
      <th>Cross section (pb)<br></th>
      <th>Uncertainty (pb):<br>Scale unc. (PDF unc.)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>W+           </td><td>FEWZ</td><td>--                  </td><td>NNLO</td><td>W->lv, l=e,m,t</td><td>18456</td><td>±233 (±850)  </td></tr>
    <tr><td>W-           </td><td>FEWZ</td><td>--                  </td><td>NNLO</td><td>W->lv, l=e,m,t</td><td>12858</td><td> ±174 (±654) </td></tr>
    <tr><td>Total W      </td><td>FEWZ</td><td>--                  </td><td>NNLO</td><td>W->lv, l=e,m,t</td><td>31314</td><td> ±407 (±1504)</td></tr>
    <tr><td>Z/a* (20)    </td><td>FEWZ</td><td>m(ll)>20GeV         </td><td>NNLO</td><td>Z -> ll       </td><td>4998</td><td>±34 (±270) </td></tr>
    <tr><td>Z/a* (50)    </td><td>FEWZ</td><td>m(ll)>50GeV         </td><td>NNLO</td><td>Z -> ll       </td><td>3048</td><td>±34 (±128) </td></tr>
    <tr><td>Z/a* (60-120)</td><td>FEWZ</td><td>60 < m(ll) < 120 GeV</td><td>NNLO</td><td>Z -> ll       </td><td>2916</td><td>±34 (±122) </td></tr>
    <tr><td>W+cbar       </td><td>MCFM</td><td>--                  </td><td>NLO </td><td>Inclusive     </td><td>1718</td><td>±157       </td></tr>
    <tr><td>W-c          </td><td>MCFM</td><td>--                  </td><td>NLO </td><td>Inclusive     </td><td>1910</td><td>±164       </td></tr>
    <tr><td>Total Wc     </td><td>MCFM</td><td>--	           </td><td>NLO </td><td>Inclusive     </td><td>3628</td><td>±227       </td></tr>
    <tr><td>W+b bbar     </td><td>MCFM</td><td>--	           </td><td>LO  </td><td>Inclusive     </td><td>22.1</td><td>±4.4       </td></tr>
    <tr><td>W-b bbar     </td><td>MCFM</td><td>--	           </td><td>LO  </td><td>Inclusive     </td><td>13.2</td><td>±2.5       </td></tr>
    <tr><td>Total Wb bbar</td><td>MCFM</td><td>--	           </td><td>LO  </td><td>Inclusive     </td><td>35.3</td><td>±5.1       </td></tr>
    <tr><td>Z/a*b bbar   </td><td>MCFM</td><td>m(ll) > 20 GeV      </td><td>LO  </td><td>Inclusive     </td><td>67.3</td><td>±18.8      </td></tr>
    <tr><td>W+W-         </td><td>MCFM</td><td>--	           </td><td>NLO </td><td>Inclusive     </td><td>43  </td><td>±1.5       </td></tr>
    <tr><td>W+Z/a*       </td><td>MCFM</td><td>m(ll) > 40 GeV      </td><td>NLO </td><td>Inclusive     </td><td>11.8</td><td>±0.6       </td></tr>
    <tr><td>W-Z/a*       </td><td>MCFM</td><td>m(ll) > 40 GeV	   </td><td>NLO </td><td>Inclusive     </td><td>6.4 </td><td>±0.4       </td></tr>
    <tr><td>Total WZ/a*  </td><td>MCFM</td><td>m(ll) > 40 GeV	   </td><td>NLO </td><td>Inclusive     </td><td>18.2</td><td>±0.7       </td></tr>
    <tr><td>Z/a* Z/a*   </td><td>MCFM</td><td>m(ll) > 40 GeV	   </td><td>NLO </td><td>Inclusive     </td><td>5.9 </td><td>±0.15      </td></tr>
    <tr><td>ttbarW       </td><td> -- </td><td> --	           </td><td>NLO </td><td>Inclusive     </td><td>0.1473</td><td> ±0.0155 </td></tr>
    <tr><td>ttbarZ       </td><td> -- </td><td> --	           </td><td>NLO </td><td>Inclusive     </td><td>0.1369</td><td> ±0.029  </td><td>
  </tbody>
</table>

### <a name="8tev">8 TeV</a>

<table class=\"ui celled table\">
  <thead>
    <tr class="header">
      <th>Process<br></th>
      <th>Generator/Source<br></th>
      <th>Phase space cuts<br></th>
      <th>Order<br></th>
      <th>Final state<br></th>
      <th>Cross section (pb)<br></th>
      <th>Uncertainty (pb):<br>Scale unc. (PDF unc.)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>W+            </td><td>FEWZ 3.1</td><td>--                  </td><td>NNLO</td><td>W->μν      </td><td>7213.4  </td><td>+45.3 -21.3 (±241.3)</td></tr>
    <tr><td>W-            </td><td>FEWZ 3.1</td><td>--                  </td><td>NNLO</td><td>W->μν      </td><td>5074.7  </td><td>+33.8 -18.3 (±188.3)</td></tr>
    <tr><td>Total W       </td><td>FEWZ 3.1</td><td>--                  </td><td>NNLO</td><td>W->μν      </td><td>12234.4 </td><td>+79.0 -39.7 (±414.7)</td></tr>
    <tr><td>Z/a*(20)      </td><td>FEWZ 3.1</td><td>m(ll)>20 GeV        </td><td>NNLO</td><td>Z -> μμ    </td><td>1966.7  </td><td>+19.8 -13.7 (±87.7) </td></tr>
    <tr><td>Z/a* (50)     </td><td>FEWZ 3.1</td><td>m(ll)>50 GeV        </td><td>NNLO</td><td>Z -> μμ    </td><td>1177.3  </td><td>+5.9 -3.6 (±38.8)   </td></tr>
    <tr><td>Z/a* (60-120) </td><td>FEWZ 3.1</td><td>60 < m(ll) < 120 GeV</td><td>NNLO</td><td>Z -> μμ    </td><td>1129.2  </td><td>+5.5 -2.6 (±37.5)   </td></tr>
    <tr><td>W+cbar        </td><td>MCFM    </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>2423.5  </td><td>                    </td></tr>
    <tr><td>W+cbar        </td><td>MCFM    </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>2624.6  </td><td>                    </td></tr>
    <tr><td>Total Wc      </td><td>MCFM    </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>5048.1  </td><td>                    </td></tr>
    <tr><td>Total Wb bbar </td><td>aMC@NLO </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>377.4   </td><td>+19.5% -16.8%       </td></tr>
    <tr><td>Z/a*b bbar    </td><td>MCFM    </td><td>m(ll) > 50 GeV      </td><td>LO  </td><td>Inclusive  </td><td>76.75   </td><td>                    </td></tr>
    <tr><td>Total WZ/a*   </td><td>MCFM    </td><td>m(ll) > 12 GeV      </td><td>NLO </td><td>Inclusive  </td><td>33.21 (CTEQ)<br>33.85 (MSTW)<br>33.72 (NNPDF)</td></tr>
    <tr><td>ttbarW        </td><td>MCFM    </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>0.232      </td><td>±0.067 (±0.03)   </td></tr>
    <tr><td>ttbarZ        </td><td>NLO     </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>0.2057     </td><td>+0.019 -0.024    </td></tr>
    <tr><td>tqZ; q!=b     </td><td>aMC@NLO </td><td>m(ll) > 50 GeV      </td><td>NLO </td><td>Z->leptons </td><td>0.02450    </td><td>+3.3% -2.6%      </td></tr>
    <tr><td>tbZ           </td><td>aMC@NLO </td><td>m(ll) > 50 GeV      </td><td>NLO </td><td>Z->leptons </td><td>0.0114     </td><td>+3.3% -2.6%      </td></tr>
    <tr><td>WWW           </td><td>aMC@NLO </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>8.058e-02  </td><td>+4.7% -3.9%      </td></tr>
    <tr><td>WWZ           </td><td>aMC@NLO </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>5.795e-02  </td><td>+5.6% -4.6%      </td></tr>
    <tr><td>WZZ           </td><td>aMC@NLO </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>1.968e-02  </td><td>+6.0% -4.9%      </td></tr>
    <tr><td>ZZZ           </td><td>aMC@NLO </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>5.527e-03  </td><td>+2.7% -2.4%      </td></tr>
    <tr><td>tttt          </td><td>aMC@NLO </td><td>--                  </td><td>NLO </td><td>Inclusive  </td><td>9.144e-04  </td><td>+36.3%, -27.0%   </td></tr>
    <tr><td>W+ W-         </td><td>MCFM 6.6</td><td>0                   </td><td>NLO </td><td>W->eν W->eν</td><td>0.6472     </td><td>±0.0231 (±0.0266)</td></tr>
    <tr><td>W+ Z/a*       </td><td>MCFM 6.6</td><td>m(l+l-) > 12 GeV    </td><td>NLO </td><td>W->μν Z->ee</td><td>0.0748     </td><td>±0.0025 (±0.0029)</td></tr>
    <tr><td>W+ Z/a*       </td><td>MCFM 6.6</td><td>m(l+l-) > 40 GeV    </td><td>NLO </td><td>W->μν Z->ee</td><td>0.0535     </td><td>±0.0018 (±0.0028)</td></tr>
    <tr><td>W- Z/a*       </td><td>MCFM 6.6</td><td>m(l+l-) > 12 GeV    </td><td>NLO </td><td>W->μν Z->ee</td><td>0.0446     </td><td>±0.0021 (±0.0018)</td></tr>
    <tr><td>W- Z/a*       </td><td>MCFM 6.6</td><td>m(l+l-) > 40 GeV    </td><td>NLO </td><td>W->μν Z->ee</td><td>0.0305     </td><td>±0.0014 (±0.0014)</td></tr>
    <tr><td>Z/a* Z/a*     </td><td>MCFM 6.6</td><td>both dileptonic <br>m(l+l-) > 12 GeV </td><td>NLO </td><td>Z->μμ Z->ee   </td><td>0.0385 </td><td>±0.0011 (±0.0011)</td></tr>
    <tr><td>Z/a* Z/a*     </td><td>MCFM 6.6</td><td>both dileptonic <br>m(l+l-) > 40 GeV </td><td>NLO </td><td>Z->μμ Z->ee   </td><td>0.0185 </td><td>±0.0007 (±0.0007)</td></tr>
    <tr><td>Z/a* Z        </td><td>MCFM 6.6</td><td>m(l+l- from Z/a*) > 12 GeV </td><td>NLO   </td><td>Z->ee Z->νν </td><td>0.1318       </td><td>±0.0040 (±0.0067)</td></tr>
    <tr><td>Z Z           </td><td>MCFM 6.6</td><td>both dileptonic <br>m(l+l-) > 1 GeV  </td><td>NLO   </td><td>Z->ee Z->μμ </td><td>0.0173 </td><td>±0.0067 (±0.0007)</td></tr>
  </tbody>
</table>
<br>

## <a name="run2">Run 2</a>

### <a name="genxsec">Calculate cross sections using GenXSecAnalyzer</a>

For Run2, the [GenXSecAnalyzer tool](https://github.com/cms-sw/cmssw/blob/CMSSW_7_6_X/GeneratorInterface/Core/plugins/GenXSecAnalyzer.cc) is available to compute cross section from an existing MC sample in [MiniAOD format](/docs/cms-getting-started-miniaod). It retrieves information from collections called [GenLumiInfoProduct](https://github.com/cms-sw/cmssw/blob/CMSSW_7_6_X/SimDataFormats/GeneratorProducts/interface/GenLumiInfoProduct.h) and [GenFilterInfo](https://github.com/cms-sw/cmssw/blob/CMSSW_7_6_X/SimDataFormats/GeneratorProducts/interface/GenFilterInfo.h) to compute averaged cross sections over all the input luminosity blocks.

**Many SM simulations corresponding to Run 2 data have the output of this analyzer available on the record page.**

The following instructions show how to compute a cross section from a MiniAOD sample. This example is given for a 2015
MiniAOD dataset using CMSSW_7_6_7, but the commands can be adapted for later MiniAOD samples by using the corresponding
CMSSW release and updating the input file or dataset names.

Setup the CMS environment by following the [instructions for MiniAOD](/docs/cms-getting-started-miniaod).

Inside the `CMSSW_7_6_7/src` directory, fetch a configuration file for the `GenXSecAnalyzer`:
```
curl https://raw.githubusercontent.com/cms-sw/genproductions/master/Utilities/calculateXSectionAndFilterEfficiency/genXsec_cfg.py -o genXSecAnalyzer_cfg.py
```

Examine the configuration file with your preferred editor. Within the configuration file, the `maxEvents` setting
controls the maximum number of events passed to the GenXSecAnalyzer. Set it to `-1` if you would like to use all the events:
```
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
```

The `source` setting specifies the names of the root files to be used:
```
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = secFiles
)
```

You may specify `inputFiles` and `maxEvents` and run the script in command line:
```
cmsRun genXSecAnalyzer_cfg.py inputFiles="file:root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/QCDJets_flat_pythia_shifted15mmvertex/MINIAODSIM/PU25nsData2015v1_Shifted15mmCollision2015_76X_mcRun2_asymptotic_v12-v1/60000/00D4D020-59B8-E511-8D6D-A0000420FE80.root" maxEvents=10
```

Here we use a root file from 2015 QCD MC sample and set the maximum number of events to 10.
The printout should look like this:
```
------------------------------------
GenXsecAnalyzer:
------------------------------------
Before Filtrer: total cross section = 1.887e+09 +- 7.281e+07 pb
Filter efficiency (taking into account weights)= (3.38384) / (3.38384) = 1.000e+00 +- 0.000e+00
Filter efficiency (event-level)= (200) / (200) = 1.000e+00 +- 0.000e+00
After filter: final cross section = 1.887e+09 +- 7.281e+07 pb

=============================================
```

Depending on the type of simulation, the analyzer will present different information. The most common values are:
* Before matching: the cross section before jet matching and any filter.
* After matching: the cross section after jet matching BUT before any filter.
* Filter efficiency: the efficiency of any filter.
* After filter: the cross section after jet matching and additional filters are applied. This is your final cross section.

To compute the cross section of *QCDuubar_Pt-15to3000_TuneZ2star_Flat_13TeV_pythia6* for 2015 data using **all the files** in this sample, find the link to the filelist on this dataset's [record](https://opendata.cern.ch/record/18392).

In `CMSSW_7_6_7/src` (or `CMSSW_10_6_30/src` for 2016 datasets), download the filelist using its URL:
```
curl https://opendata.cern.ch/record/18392/files/CMS_mc_RunIIFall15MiniAODv2_QCDuubar_Pt-15to3000_TuneZ2star_Flat_13TeV_pythia6_MINIAODSIM_PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1_60000_file_index.txt -o filelist.txt
```

Create a python script `compute_xsec.py` with the following code that will read the file list and provide all the files
as an argument to the analyzer:
```
import os

# parameters to EDIT
inputFilelist = "filelist.txt"
maxEvents = "10" # You may increase maxEvents for a better estimation (e.g. set to -1)
outfileName = "xsec_QCDuubar_Pt-15to3000.log"

# get inputFiles
filelist = open(inputFilelist, 'r').readlines()
inputFiles = ""
for rootfile in filelist:
   if('root' in rootfile):
       inputFiles += ' inputFiles='+rootfile + ' '

# compute cross section
command = 'cmsRun genXSecAnalyzer_cfg.py {} maxEvents={} 2>&1 | tee {}'.format(inputFiles, maxEvents, outfileName)
os.system(command)
```

In the CMS environment (make sure you have executed `cmsenv` if using a VM), run:
```
python compute_xsec.py
```

### <a name="higher">13 TeV higher-order cross sections</a>

Higher order top quark cross sections are available from the LHC Physics Working Group for all LHC energies:

- Top quark pair production at [NNLO](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO)
- Single top quark production at [NLO](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec) and at [NNLO](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef)<br>

A table of further higher-order cross sections for other processes will be added when available.

