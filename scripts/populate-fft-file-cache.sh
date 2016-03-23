#!/bin/sh
#
# A helper script to download (mostly from CMS DocDB) files that are
# used for FFT uploads when building opendata.cern.ch site.
#
# NOTE: the FFT file cache directory is by default located in
# "$HOME/Local/opendata.cern.ch-fft-file-cache".  The script also
# makes symlink to this place from "/tmp" so that files can be
# uploaded regardless of $HOME.
#
# NOTE: if a file is already present in the destinated directory, then
# the script does not download it again, even without checking whether
# the remote file has changed or not.
#
# NOTE: The total amount of files to transfer is about 8 GB and may
# take significant time.  It is therefore better to run this script
# once in your development environment and to store the files locally
# on your laptop and use this cache for further builds.

# config section:
WGET="wget -nc -nv --no-check-certificate"
DOCDB="https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/RetrieveFile"
OUTDIR="$HOME/Local/opendata.cern.ch-fft-file-cache"

# quit on errors and potentially unbound symbols:
#set -o errexit # because of wget
set -o nounset

# make sure the output directory exists:
mkdir -p $OUTDIR

# mirror EOS files existing in the repository:
rsync -a invenio_opendata/testsuite/data/cms/eos-file-indexes/ $OUTDIR/cms-eos-file-indexes/
rsync -a invenio_opendata/testsuite/data/alice/eos-file-indexes/ $OUTDIR/alice-eos-file-indexes/
rsync -a invenio_opendata/testsuite/data/lhcb/eos-file-indexes/ $OUTDIR/lhcb-eos-file-indexes/
rsync -a invenio_opendata/testsuite/data/atlas/eos-file-indexes/ $OUTDIR/atlas-eos-file-indexes/

# download CMS DocDB files: (if not already existing)
mkdir -p $OUTDIR/cms-docdb-files
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_0.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_0.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_1.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_1.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_2.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_2.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_3.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_3.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_4.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_4.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_5.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_5.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_6.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_6.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_7.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_7.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_8.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_8.csv"
$WGET -O $OUTDIR/cms-docdb-files/Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_9.csv "$DOCDB?docid=12450&amp;filename=Run2010B_Mu_AOD_Apr21ReReco-v1-dimuon_9.csv"
$WGET -O $OUTDIR/cms-docdb-files/BTau.ig "$DOCDB?docid=12376&amp;filename=BTau.ig"
$WGET -O $OUTDIR/cms-docdb-files/EGMonitor.ig "$DOCDB?docid=12376&amp;filename=EGMonitor.ig"
$WGET -O $OUTDIR/cms-docdb-files/Electron.ig "$DOCDB?docid=12376&amp;filename=Electron.ig"
$WGET -O $OUTDIR/cms-docdb-files/Jet.ig "$DOCDB?docid=12376&amp;filename=Jet.ig"
$WGET -O $OUTDIR/cms-docdb-files/JetMETTauMonitor.ig "$DOCDB?docid=12376&amp;filename=JetMETTauMonitor.ig"
$WGET -O $OUTDIR/cms-docdb-files/METFwd.ig "$DOCDB?docid=12376&amp;filename=METFwd.ig"
$WGET -O $OUTDIR/cms-docdb-files/Mu.ig "$DOCDB?docid=12376&amp;filename=Mu.ig"
$WGET -O $OUTDIR/cms-docdb-files/MuMonitor.ig "$DOCDB?docid=12376&amp;filename=MuMonitor.ig"
$WGET -O $OUTDIR/cms-docdb-files/MuOnia.ig "$DOCDB?docid=12376&amp;filename=MuOnia.ig"
$WGET -O $OUTDIR/cms-docdb-files/MultiJet.ig "$DOCDB?docid=12376&amp;filename=MultiJet.ig"
$WGET -O $OUTDIR/cms-docdb-files/Photon.ig "$DOCDB?docid=12376&amp;filename=Photon.ig"
$WGET -O $OUTDIR/cms-docdb-files/Commissioning.ig "$DOCDB?docid=12376&amp;filename=Commissioning.ig"
$WGET -O $OUTDIR/cms-docdb-files/MinimumBias.ig "$DOCDB?docid=12376&amp;filename=MinimumBias.ig"
$WGET -O $OUTDIR/cms-docdb-files/ZeroBias.ig "$DOCDB?docid=12376&amp;filename=ZeroBias.ig"
$WGET -O $OUTDIR/cms-docdb-files/4lepton.csv "$DOCDB?docid=11976&amp;filename=4lepton.csv"
$WGET -O $OUTDIR/cms-docdb-files/4lepton.ig "$DOCDB?docid=11976&amp;filename=4lepton.ig"
$WGET -O $OUTDIR/cms-docdb-files/4lepton.json "$DOCDB?docid=11976&amp;filename=4lepton.json"
$WGET -O $OUTDIR/cms-docdb-files/diphoton.csv "$DOCDB?docid=11976&amp;filename=diphoton.csv"
$WGET -O $OUTDIR/cms-docdb-files/diphoton.ig "$DOCDB?docid=11976&amp;filename=diphoton.ig"
$WGET -O $OUTDIR/cms-docdb-files/diphoton.json "$DOCDB?docid=11976&amp;filename=diphoton.json"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi.csv "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi.csv"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_7.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_8.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_9.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_10.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_10.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_11.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_11.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_12.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_12.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_13.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_13.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_14.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_14.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_15.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_15.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_16.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_16.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi.json "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi.json"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_17.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_17.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_18.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_18.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_19.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_19.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_0.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_1.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_2.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_3.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_4.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_5.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon-Jpsi_6.ig "$DOCDB?docid=11580&amp;filename=dimuon-Jpsi_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_0.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_17.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_17.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_18.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_18.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_19.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_19.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_2.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_3.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_4.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_5.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_6.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_7.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_8.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_1.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_9.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_10.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_10.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_11.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_11.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_12.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_12.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_13.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_13.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_14.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_14.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_15.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_15.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi_16.ig "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi_16.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi.csv "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi.csv"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Jpsi.json "$DOCDB?docid=12064&amp;filename=dielectron-Jpsi.json"
$WGET -O $OUTDIR/cms-docdb-files/dimuon100k.json "$DOCDB?docid=11583&amp;filename=dimuon100k.json"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_7.ig "$DOCDB?docid=11583&amp;filename=dimuon_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_8.ig "$DOCDB?docid=11583&amp;filename=dimuon_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_9.ig "$DOCDB?docid=11583&amp;filename=dimuon_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon100k.csv "$DOCDB?docid=11583&amp;filename=dimuon100k.csv"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_0.ig "$DOCDB?docid=11583&amp;filename=dimuon_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_1.ig "$DOCDB?docid=11583&amp;filename=dimuon_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_2.ig "$DOCDB?docid=11583&amp;filename=dimuon_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_3.ig "$DOCDB?docid=11583&amp;filename=dimuon_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_4.ig "$DOCDB?docid=11583&amp;filename=dimuon_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_5.ig "$DOCDB?docid=11583&amp;filename=dimuon_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/dimuon_6.ig "$DOCDB?docid=11583&amp;filename=dimuon_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_0.ig "$DOCDB?docid=12037&amp;filename=dielectron_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron100k.csv "$DOCDB?docid=12037&amp;filename=dielectron100k.csv"
$WGET -O $OUTDIR/cms-docdb-files/dielectron100k.json "$DOCDB?docid=12037&amp;filename=dielectron100k.json"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_1.ig "$DOCDB?docid=12037&amp;filename=dielectron_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_2.ig "$DOCDB?docid=12037&amp;filename=dielectron_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_3.ig "$DOCDB?docid=12037&amp;filename=dielectron_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_4.ig "$DOCDB?docid=12037&amp;filename=dielectron_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_5.ig "$DOCDB?docid=12037&amp;filename=dielectron_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_6.ig "$DOCDB?docid=12037&amp;filename=dielectron_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_7.ig "$DOCDB?docid=12037&amp;filename=dielectron_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_8.ig "$DOCDB?docid=12037&amp;filename=dielectron_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron_9.ig "$DOCDB?docid=12037&amp;filename=dielectron_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_0.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_17.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_17.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_18.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_18.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_19.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_19.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_2.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_3.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_4.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_5.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_6.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_7.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_8.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_1.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_9.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_10.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_10.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_11.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_11.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_12.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_12.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_13.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_13.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_14.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_14.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_15.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_15.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon_16.ig "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon_16.ig"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon.csv "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon.csv"
$WGET -O $OUTDIR/cms-docdb-files/dielectron-Upsilon.json "$DOCDB?docid=12065&amp;filename=dielectron-Upsilon.json"
$WGET -O $OUTDIR/cms-docdb-files/Zee.csv "$DOCDB?docid=11581&amp;filename=Zee.csv"
$WGET -O $OUTDIR/cms-docdb-files/Zee.json "$DOCDB?docid=11581&amp;filename=Zee.json"
$WGET -O $OUTDIR/cms-docdb-files/Zee_0.ig "$DOCDB?docid=11581&amp;filename=Zee_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zee_1.ig "$DOCDB?docid=11581&amp;filename=Zee_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zee_2.ig "$DOCDB?docid=11581&amp;filename=Zee_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zee_3.ig "$DOCDB?docid=11581&amp;filename=Zee_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zee_4.ig "$DOCDB?docid=11581&amp;filename=Zee_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zmumu_0.ig "$DOCDB?docid=11582&amp;filename=Zmumu_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zmumu_1.ig "$DOCDB?docid=11582&amp;filename=Zmumu_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zmumu_2.ig "$DOCDB?docid=11582&amp;filename=Zmumu_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zmumu_3.ig "$DOCDB?docid=11582&amp;filename=Zmumu_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zmumu_4.ig "$DOCDB?docid=11582&amp;filename=Zmumu_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/Zmumu.csv "$DOCDB?docid=11582&amp;filename=Zmumu.csv"
$WGET -O $OUTDIR/cms-docdb-files/Zmumu.json "$DOCDB?docid=11582&amp;filename=Zmumu.json"
$WGET -O $OUTDIR/cms-docdb-files/Wenu.csv "$DOCDB?docid=4673&amp;filename=Wenu.csv"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_7.ig "$DOCDB?docid=4673&amp;filename=Wenu_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_8.ig "$DOCDB?docid=4673&amp;filename=Wenu_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_9.ig "$DOCDB?docid=4673&amp;filename=Wenu_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu.json "$DOCDB?docid=4673&amp;filename=Wenu.json"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_0.ig "$DOCDB?docid=4673&amp;filename=Wenu_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_1.ig "$DOCDB?docid=4673&amp;filename=Wenu_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_2.ig "$DOCDB?docid=4673&amp;filename=Wenu_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_3.ig "$DOCDB?docid=4673&amp;filename=Wenu_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_4.ig "$DOCDB?docid=4673&amp;filename=Wenu_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_5.ig "$DOCDB?docid=4673&amp;filename=Wenu_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wenu_6.ig "$DOCDB?docid=4673&amp;filename=Wenu_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu.csv "$DOCDB?docid=4655&amp;filename=Wmunu.csv"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_7.ig "$DOCDB?docid=4655&amp;filename=Wmunu_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_8.ig "$DOCDB?docid=4655&amp;filename=Wmunu_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_9.ig "$DOCDB?docid=4655&amp;filename=Wmunu_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu.json "$DOCDB?docid=4655&amp;filename=Wmunu.json"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_0.ig "$DOCDB?docid=4655&amp;filename=Wmunu_0.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_1.ig "$DOCDB?docid=4655&amp;filename=Wmunu_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_2.ig "$DOCDB?docid=4655&amp;filename=Wmunu_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_3.ig "$DOCDB?docid=4655&amp;filename=Wmunu_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_4.ig "$DOCDB?docid=4655&amp;filename=Wmunu_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_5.ig "$DOCDB?docid=4655&amp;filename=Wmunu_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/Wmunu_6.ig "$DOCDB?docid=4655&amp;filename=Wmunu_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_1-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_1-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_11-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_11-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_11-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_11-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_11.ig "$DOCDB?docid=12154&amp;filename=masterclass_11.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_12-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_12-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_12-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_12-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_12-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_12-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_12.ig "$DOCDB?docid=12154&amp;filename=masterclass_12.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_13-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_13-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_13-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_13-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_13-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_13-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_1-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_1-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_13.ig "$DOCDB?docid=12154&amp;filename=masterclass_13.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_14-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_14-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_14-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_14-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_14-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_14-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_14.ig "$DOCDB?docid=12154&amp;filename=masterclass_14.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_15-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_15-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_15-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_15-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_15-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_15-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_15.ig "$DOCDB?docid=12154&amp;filename=masterclass_15.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_16-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_16-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_1-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_1-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_16-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_16-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_16-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_16-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_16.ig "$DOCDB?docid=12154&amp;filename=masterclass_16.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_17-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_17-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_17-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_17-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_17-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_17-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_17.ig "$DOCDB?docid=12154&amp;filename=masterclass_17.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_18-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_18-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_18-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_18-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_18-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_18-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_1.ig "$DOCDB?docid=12154&amp;filename=masterclass_1.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_18.ig "$DOCDB?docid=12154&amp;filename=masterclass_18.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_19-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_19-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_19-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_19-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_19-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_19-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_19.ig "$DOCDB?docid=12154&amp;filename=masterclass_19.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_2-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_2-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_2-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_2-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_2-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_2-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_2.ig "$DOCDB?docid=12154&amp;filename=masterclass_2.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_3-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_3-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_10-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_10-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_3-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_3-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_3-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_3-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_3.ig "$DOCDB?docid=12154&amp;filename=masterclass_3.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_4-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_4-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_4-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_4-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_4-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_4-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_4.ig "$DOCDB?docid=12154&amp;filename=masterclass_4.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_5-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_5-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_5-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_5-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_5-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_5-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_10-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_10-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_5.ig "$DOCDB?docid=12154&amp;filename=masterclass_5.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_6-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_6-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_6-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_6-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_6-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_6-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_6.ig "$DOCDB?docid=12154&amp;filename=masterclass_6.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_7-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_7-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_7-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_7-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_7-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_7-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_7.ig "$DOCDB?docid=12154&amp;filename=masterclass_7.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_8-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_8-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_10-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_10-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_8-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_8-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_8-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_8-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_8.ig "$DOCDB?docid=12154&amp;filename=masterclass_8.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_9-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_9-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_9-lnu.csv "$DOCDB?docid=12154&amp;filename=masterclass_9-lnu.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_9-photon.csv "$DOCDB?docid=12154&amp;filename=masterclass_9-photon.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_9.ig "$DOCDB?docid=12154&amp;filename=masterclass_9.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_10.ig "$DOCDB?docid=12154&amp;filename=masterclass_10.ig"
$WGET -O $OUTDIR/cms-docdb-files/masterclass_11-leptons.csv "$DOCDB?docid=12154&amp;filename=masterclass_11-leptons.csv"
$WGET -O $OUTDIR/cms-docdb-files/masterclass-2014.xls "$DOCDB?docid=12154&amp;filename=masterclass-2014.xls"
$WGET -O $OUTDIR/cms-docdb-files/BTag_Run2011A.ig "$DOCDB?docid=12752&amp;filename=BTag_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/DoubleElectron_Run2011A.ig "$DOCDB?docid=12752&amp;filename=DoubleElectron_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/DoubleMu_Run2011A.ig "$DOCDB?docid=12752&amp;filename=DoubleMu_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/ElectronHad_Run2011A.ig "$DOCDB?docid=12752&amp;filename=ElectronHad_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/HT_Run2011A.ig "$DOCDB?docid=12752&amp;filename=HT_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/Jet_Run2011A.ig "$DOCDB?docid=12752&amp;filename=Jet_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/METBTag_Run2011A.ig "$DOCDB?docid=12752&amp;filename=METBTag_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/MET_Run2011A.ig "$DOCDB?docid=12752&amp;filename=MET_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/MinimumBias_Run2011A.ig "$DOCDB?docid=12752&amp;filename=MinimumBias_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/MuEG_Run2011A.ig "$DOCDB?docid=12752&amp;filename=MuEG_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/MuHad_Run2011A.ig "$DOCDB?docid=12752&amp;filename=MuHad_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/MuOnia_Run2011A.ig "$DOCDB?docid=12752&amp;filename=MuOnia_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/MultiJet_Run2011A.ig "$DOCDB?docid=12752&amp;filename=MultiJet_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/PhotonHad_Run2011A.ig "$DOCDB?docid=12752&amp;filename=PhotonHad_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/Photon_Run2011A.ig "$DOCDB?docid=12752&amp;filename=Photon_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/SingleElectron_Run2011A.ig "$DOCDB?docid=12752&amp;filename=SingleElectron_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/SingleMu_Run2011A.ig "$DOCDB?docid=12752&amp;filename=SingleMu_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/TauPlusX_Run2011A.ig "$DOCDB?docid=12752&amp;filename=TauPlusX_Run2011A.ig"
$WGET -O $OUTDIR/cms-docdb-files/Tau_Run2011A.ig "$DOCDB?docid=12752&amp;filename=Tau_Run2011A.ig"


# cernvm files:
mkdir -p $OUTDIR/cernvm-files
$WGET -O $OUTDIR/cernvm-files/CMS-OpenData-1.0.0-rc4.ova "http://cernvm.cern.ch/releases/CMS-OpenData-1.0.0-rc4.ova"
$WGET -O $OUTDIR/cernvm-files/CMS-OpenData-1.0.0-rc6.ova "http://cernvm.cern.ch/releases/CMS-OpenData-1.0.0-rc6.ova"
$WGET -O $OUTDIR/cernvm-files/CMS-OpenData-1.0.0-rc7.ova "http://cernvm.cern.ch/releases/CMS-OpenData-1.0.0-rc7.ova"

# github files
mkdir -p $OUTDIR/github-files
$WGET -O $OUTDIR/github-files/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt "https://raw.githubusercontent.com/ayrodrig/pattuples2010/master/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt"
$WGET -O $OUTDIR/github-files/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt "https://raw.githubusercontent.com/cms-outreach/ispy-analyzers/Run2011A/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt"
$WGET -O $OUTDIR/github-files/pattuples2012-1.0.0.tar.gz https://github.com/ayrodrig/pattuples2010/archive/v1.0.0.tar.gz
$WGET -O $OUTDIR/github-files/pattuples2012-1.0.2.tar.gz https://github.com/ayrodrig/pattuples2010/archive/v1.0.2.tar.gz
$WGET -O $OUTDIR/github-files/OutreachExercise2010-1.0.0.tar.gz https://github.com/ayrodrig/OutreachExercise2010/archive/v1.0.0.tar.gz
$WGET -O $OUTDIR/github-files/dimuon-filter-1.0.0.tar.gz https://github.com/tpmccauley/dimuon-filter/archive/1.0.0.tar.gz
$WGET -O $OUTDIR/github-files/HiggsML2014-1.0.tar.gz https://github.com/ATLAS-outreach/HiggsML2014/archive/v1.0.tar.gz
$WGET -O $OUTDIR/github-files/SUSYBSMAnalysis-RazorFilter-1.0.0.tar.gz https://github.com/jmduarte/SUSYBSMAnalysis-RazorFilter/archive/1.0.0.tar.gz

# CMS Hamburg files:
mkdir -p $OUTDIR/cms-hamburg-files
$WGET -O $OUTDIR/cms-hamburg-files/HEPTutorial_0.tar http://ippog.web.cern.ch/sites/ippog.web.cern.ch/files/HEPTutorial_0.tar
(cd $OUTDIR/cms-hamburg-files && tar xf HEPTutorial_0.tar HEPTutorial/files/)

# experiment data policies:
mkdir -p $OUTDIR/data-policies
$WGET -O $OUTDIR/data-policies/CMS-Data-Policy.pdf "$DOCDB?docid=6032&amp;version=1&amp;filename=CMSDataPolicy.pdf"
$WGET -O $OUTDIR/data-policies/ATLAS-Data-Policy.pdf https://twiki.cern.ch/twiki/pub/AtlasPublic/AtlasPolicyDocuments/A78_ATLAS_Data_Access_Policy.pdf
$WGET -O $OUTDIR/data-policies/LHCb-Data-Policy.pdf http://cds.cern.ch/record/1543410/files/LHCb-PUB-2013-003.pdf

# Ana's video:
mkdir -p $OUTDIR/cms-open-data-instructions
$WGET -O $OUTDIR/cms-open-data-instructions/OutreachExercise2010.m4v http://193.146.75.147/Outreach%20Exercise%202010.m4v

# ALICE data policy:
rsync -a invenio_opendata/testsuite/data/alice/alice-data-policy/ $OUTDIR/alice-data-policy/

# ATLAS Higgs Challenge 2014:
rsync -a invenio_opendata/testsuite/data/atlas/atlas-higgs-challenge-2014/ $OUTDIR/atlas-higgs-challenge-2014/

# CMS VM contextualisation scripts:
rsync -a invenio_opendata/testsuite/data/cms/cms-vm-contextualisation-scripts/ $OUTDIR/cms-vm-contextualisation-scripts/

# CMS CSV files:
rsync -a invenio_opendata/testsuite/data/cms/cms-csv-files/ $OUTDIR/cms-csv-files/

# CMS configuration files:
rsync -a invenio_opendata/testsuite/data/cms/cms-configuration-files/ $OUTDIR/cms-configuration-files/

# CMS HLT 2011 configuration files:
rsync -a invenio_opendata/testsuite/data/cms/cms-hlt-2011-configuration-files/ $OUTDIR/cms-hlt-2011-configuration-files/

# CMS pileup configuration files:
rsync -a invenio_opendata/testsuite/data/cms/cms-pileup-configuration-files/ $OUTDIR/cms-pileup-configuration-files/

# CMS dimuon spectrum 2010 files:
rsync -a invenio_opendata/testsuite/data/cms/cms-tools-dimuon-spectrum-2010/ $OUTDIR/cms-tools-dimuon-spectrum-2010/

# CMS VM image files:
rsync -a invenio_opendata/testsuite/data/cms/cms-vm-images/ $OUTDIR/cms-vm-images/

# CMS validation code Run2011B
rsync -a invenio_opendata/testsuite/data/cms/cms-validation-code-Run2010B/ $OUTDIR/cms-validation-code-Run2010B/

# finally, make symlink to FFT cache from tmp:
if [ ! -L "/tmp/$(basename $OUTDIR)" ]; then
    ln -s $OUTDIR /tmp
fi

# end of file
