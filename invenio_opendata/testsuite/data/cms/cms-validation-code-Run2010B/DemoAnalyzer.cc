// -*- C++ -*-
//
// Package:    DemoAnalyzer
// Class:      DemoAnalyzer
// 
/**\class DemoAnalyzer DemoAnalyzer.cc Demo/DemoAnalyzer/src/DemoAnalyzer.cc

 Description: [one line class summary]

 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  
//         Created:  Mon May  4 15:24:13 CEST 2015
//         Finalized: February 24, 2016  by   A. Geiser
//                    with contributions from I. Dutta, 
//                                            H. Hirvonsalo
//                                            B. Sheeran
// $Id$
// ..
//
// ***************************************************************************
// version of DEMO setup provided by CMS open data access team               *
// expanded/upgraded to contain a validation example for the                 *
// dimuon mass spectrum (MUO-10-004)                                         *
//                                                                           *
// Note that the published spectrum is reproduced approximately, but not     *
// exactly, since the data sets only partially overlap, and, for reasons of  *
// simplicity, there is no trigger selection beyond the one implicit in the  *
// Mu data set, only global muons are used, and only part of the muon        *
// quality cuts are applied                                                  *
// ***************************************************************************

// system include files
#include <memory>

// user include files, general
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//------ EXTRA HEADER FILES--------------------//
#include "math.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Common/interface/Ref.h"

// for Root histogramming
#include "TH1.h"

// for tracking information
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"

// class declaration
//

class DemoAnalyzer: public edm::EDAnalyzer {
public:
	explicit DemoAnalyzer(const edm::ParameterSet&);
	~DemoAnalyzer();

private:
	virtual void beginJob();
	virtual void analyze(const edm::Event&, const edm::EventSetup&);
	virtual void endJob();
	bool providesGoodLumisection(const edm::Event& iEvent);

	// ----------member data ---------------------------

// declare Root histograms
// for a description of their content see below
TH1D *h1;
TH1D *h2;
TH1D *h3;
TH1D *h4;

TH1D *h5;
TH1D *h6;

TH1D *h10;

TH1D *h53;
TH1D *h54;
TH1D *h55;

TH1D *h60;
TH1D *h61;

TH1D *h100;

TH1D *h200;
TH1D *h201;
TH1D *h202;
TH1D *h203;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//

DemoAnalyzer::DemoAnalyzer(const edm::ParameterSet& iConfig) {

// *****************************************************************
// This is the main analysis routine
// The goal is to approximately reproduce the dimuon mass spectrum  
// from MUO-10-004
// *****************************************************************

//now do what ever initialization is needed
edm::Service<TFileService> fs;

// ************************************
// book histograms and set axis labels
// (called once for initialization)
// ************************************

// monitoring histograms for global muons, 
// intended for muons from Mu sample

// global muon multiplicity
h10 = fs->make<TH1D>("GMmultiplicty", "GMmultiplicity", 8, 0, 8); 
h10->GetXaxis()->SetTitle("Number of Global Muons");
h10->GetYaxis()->SetTitle("Number of Events");

// global muon momentum
h1 = fs->make<TH1D>("GMmomentum", "GM_Momentum", 240, 0., 120.); 
h1->GetXaxis()->SetTitle("Global Muon Momentum (in GeV/c)");
h1->GetYaxis()->SetTitle("Number of Events");

// global muon Transverse_momentum
h2 = fs->make<TH1D>("GM_Transverse_momentum", "TransverseMomentum", 240, 0., 120.); 
h2->GetXaxis()->SetTitle("Transverse Momentum of global muons (in GeV/c)");
h2->GetYaxis()->SetTitle("Number of Events");

// global muon pseudorapity
h3 = fs->make<TH1D>("GM_eta", "GM_Eta", 140, -3.5, 3.5);
h3->GetXaxis()->SetTitle("Eta of global muons (in radians)");
h3->GetYaxis()->SetTitle("Number of Events");

// global muon azimuth angle  
h4 = fs->make<TH1D>("GM_phi", "GM_phi", 314, -3.15, 3.15);
h4->GetXaxis()->SetTitle("Phi");
h4->GetYaxis()->SetTitle("Number of Events");

// dimuon mass spectrum up to 4 GeV (low mass range, rho/omega, phi, psi)
h5 = fs->make<TH1D>("GMmass" , "GMmass" , 400, 0. , 4. );
h5->GetXaxis()->SetTitle("Invariant Mass for Nmuon>=2 (in GeV/c^2)");
h5->GetYaxis()->SetTitle("Number of Events");

// dimuon mass spectrum up to 120 GeV (high mass range: upsilon, Z)
h6 = fs->make<TH1D>("GMmass_extended" , "GMmass" , 240, 0. , 120. );
h6->GetXaxis()->SetTitle("Invariant Mass for Nmuon>=2 (in GeV/c^2)");
h6->GetYaxis()->SetTitle("Number of Events");

// global muon track chi2
h53 = fs->make<TH1D>("GM_chi2", "GM_Chi2", 300, 0, 150);
h53->GetXaxis()->SetTitle("Chi2 values");
h53->GetYaxis()->SetTitle("Number of Events");

// global muon track number of degrees of freedom
h54 = fs->make<TH1D>("GM_ndof", "GM_ndof", 100, 0, 100);
h54->GetXaxis()->SetTitle("Ndof values");
h54->GetYaxis()->SetTitle("Number of Events");

// global muon track chi2 normalized to number of degrees of freedom
h55 = fs->make<TH1D>("GM_normalizedchi2", "GM_normalizedChi2", 200, 0, 20); 
h55->GetXaxis()->SetTitle("NormalizedChi2 values");
h55->GetYaxis()->SetTitle("Number of Events");

// global muon track, number of valid hits
h60 = fs->make<TH1D>("GM_validhits", "GM_ValidHits", 100, 0., 100);
h60->GetXaxis()->SetTitle("Number of valid hits");
h60->GetYaxis()->SetTitle("Number of Events");

// global muon track, number of pixel hits
h61 = fs->make<TH1D>("GM_pixelhits", "GM_pixelhits", 14, 0., 14);
h61->GetXaxis()->SetTitle("Munber of pixel hits");
h61->GetYaxis()->SetTitle("Number of Events");

// main histogram for MUO-10-004

// unlike sign dimuon invariant mass from global muon selection, 
// binning chosen to correspond to log(0.3) - log(500), 200 bins/log10 unit
h100 = fs->make<TH1D>("GM_mass_log", "GM mass log", 644, -.52, 2.7); 
h100->GetXaxis()->SetTitle("Invariant Log10(Mass) for Nmuon>=2 (in log10(m/GeV/c^2))");
h100->GetYaxis()->SetTitle("Number of Events/GeV");

// general event histograms      and 
// histograms to check good run preselection from  JSON

// Run number for all events that have been analyzed 
h200 = fs->make<TH1D>("Run number", "Run number", 3100, 146400, 149500);

// Run number for events that have been analyzed, 
// which belong to runs considered "bad" according to JSON, Should be empty!
// If it is not empty, check JSON preselction in Python part of program
h201 = fs->make<TH1D>("Run number, JSON","Run number, JSON, should be empty!", 3100, 146400, 149500);

// Event numbers for all events that have been analyzed.
h202 = fs->make<TH1D>("Event number", "Event number", 2000, 0, 2000000000);

// Luminosity sections for all events that have been analyzed.
h203 = fs->make<TH1D>("Lumi section", "Lumi section", 300, 0, 3000);

}


DemoAnalyzer::~DemoAnalyzer() {
	// do anything here that needs to be done at destruction time
	// (e.g. close files, deallocate resources etc.)
}



//
// member functions
//

// ------------ method called for each event  ------------
void DemoAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

// **********************************************
// here each relevant event will get analyzed 
// **********************************************

using namespace edm;
using namespace reco;
using namespace std;


#ifdef THIS_IS_AN_EVENT_EXAMPLE
	Handle<ExampleData> pIn;
	iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
	ESHandle<SetupData> pSetup;
	iSetup.get<SetupRecord>().get(pSetup);
#endif


//--------------Fill basic Event-information histograms---------------------//
// debug print commented out
// LogInfo("Demo")<<"Event id: "<<iEvent.id()<<" Run number: "<<iEvent.run();

h200->Fill(iEvent.run());   // Run number which the analyzed Event belongs to
h202->Fill((iEvent.id()).event());	// Event's EventNumber
h203->Fill(iEvent.luminosityBlock());	// Luminosity Section that this 
                                        //   Event provides

//------------------Luminosity section check------------------------//
// WHAT: Checks if the Event to be analyzed provides a luminosity section 
//       that is considered to be good.
// WHY: Only Events from good Runs and those that provide good Luminosity 
//      Section should be analyzed.
// Note: Normally the good luminosity section preselection is already done 
//       via the JSON file in the Python part, so this is only a cross-check
//       whether this was doen and worked properly.
//       histogram h201 should always be empty!  
if (!providesGoodLumisection(iEvent)) {

// something went wrong with the JSON (see above)
  h201->Fill(iEvent.run());
  LogInfo("Demo") << "bad JSON Event id (" << iEvent.id() << ") --> Skipping analysis...";
}
else { // Event is to be analyzed

  LogInfo("Demo")
  << "Starting to analyze \n"
  << "Event number: " << (iEvent.id()).event()
  << ", Run number: " << iEvent.run()
  << ", Lumisection: " << iEvent.luminosityBlock();

//------------------Load (relevant) Event information------------------------//
// INFO: Getting Data From an Event
// https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookChapter4#GetData
// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDMGetDataFromEvent#get_ByLabel
// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAodDataTable
// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideRecoDataTable


// INFO: globalMuons
// NB: note that when using keyword "globalMuons" getByLabel-function returns 
//     reco::TrackCollection
  Handle<reco::TrackCollection> gmuons;
  iEvent.getByLabel("globalMuons", gmuons);

//------------------analysing Global Muons (gmuons-TrackCollection)----------//

// WHAT: declare variables used later
  double sqm1, s1, s2, s, w;

// WHAT: set square of muon mass
// WHY:  needed in later calculations
  sqm1 = (0.105658) * (0.105658);

// WHAT: Fill histogram of the number of globalMuon-Tracks 
//       in the current Event.
// WHY:  for monitoring purposes
  h10->Fill(gmuons->size());

// WHAT: Loop over all the Global Muons of current Event
// WHY:  to select good candidates to be used in invariant mass calculation
  for (reco::TrackCollection::const_iterator it = gmuons->begin(); 
    it != gmuons->end(); it++) {

// WHAT: Fill histograms for the following attributes from the current 
//       globalMuon-Track:
// - p (momentum vector magnitude)
// - pt (track transverse momentum)
// - eta (pseudorapidity of momentum vector)
// - chi-square
// - ndof (number of degrees of freedom of the fit)
// - normalizedChi2 (normalized chi-square == chi-squared divided by ndof 
//                   OR chi-squared * 1e6 if ndof is zero)
    h1->Fill(it->p());
    h2->Fill(it->pt());
    h3->Fill(it->eta());
    h4->Fill(it->phi());
    h53->Fill(it->chi2());
    h54->Fill(it->ndof());
    h55->Fill(it->normalizedChi2());

// the following can be uncommented if more log information is wished    
//   LogInfo("Demo")  <<"global  muon track pointer "<<it;
//   LogInfo("Demo")<<"global muon track p"<<it->p()<<"  global muon track pos"<<it->referencePoint()<<" global muon track vertex"<<it->vertex();

//-----------------prepare variables to determine quality cuts---------------//
// WHAT: 1) Find out the number of Hits in the current globalMuon-Track
//       2) Determine if there are enough Hits that are considered to be Valid
//       3) Determine if there are enough Hits that have been recorded in the 
//          pixel detector(s).
// WHY:  quality cuts are applied to eliminate badly reconstructed muon 
//       candidates   
    int ValidHits = 0, PixelHits = 0;

// WHAT: Get HitPattern-object for Track of current Global Muon
// WHY:  in order to count the number of hits on the track
    const reco::HitPattern& p = it->hitPattern();

// WHAT: Loop over all the Hits in the HitPattern of current Track.
// WHY:  Check if a Hit is Valid and/or whether it is a PixelHit
    for (int i = 0; i < p.numberOfHits(); i++) {

      uint32_t hit = p.getHitPattern(i);

// WHAT: Check if current Hit in the HitPattern is valid and/or in pixel
// WHY:  to increase counter if the answer is yes
// NTS:  Validity of the Hit must be asked from the HitPattern-object!
      if (p.validHitFilter(hit) && p.pixelHitFilter(hit))
          PixelHits++;
      if (p.validHitFilter(hit))
	  ValidHits++;
    } // end of loop over hits

// WHAT: Fill number of ValidHits and PixelHits in current globalMuon-Track
//       into histogram
// WHY:  to check distribution before cuts
    h60->Fill(ValidHits);
    h61->Fill(PixelHits);

// loop over globalMuon-Tracks satisfying quality cuts //

// WHAT: If current globalMuon-Track satisfies quality-cut-criteria, it is 
//       compared to other globalMuon-Tracks that come after this current one. 
//       (succeeding globalMuon-Tracks that are in the gmuons-TrackCollection)
//       need at least two candidates to calculate dimuon mass
    if (gmuons->size() >= 2
        && ValidHits >= 12
        && PixelHits >= 2
        && it->normalizedChi2() < 4.0) {

// NTS: Stores iterator for current globalMuon-Track and advances it by one.
//      In other words, the needed preparation to be able to compare all the 
//      other globalMuon-Tracks after
//      the current one to the current globalMuon-Track with iterator it.
      reco::TrackCollection::const_iterator i = it;
      i++;

// loop over 2nd global muon candidate 
      for (; i != gmuons->end(); i++) {

// initialize hit counters for 2nd muon candidate
        int ValidHits1 = 0, PixelHits1 = 0;
        const reco::HitPattern& p1 = i->hitPattern();

// loop over the hits of the track
        for (int n = 0; n < p1.numberOfHits(); n++) {
          uint32_t hit = p1.getHitPattern(n);
// if the hit is valid and/or in pixel, increase counter
          if (p1.validHitFilter(hit) && p1.pixelHitFilter(hit))
              PixelHits1++;
          if (p1.validHitFilter(hit))
              ValidHits1++;
        } // end of loop over hits

// WHAT: Compare electric charges of the current two globalMuon-Tracks 
//       (Iterators "it" and "i")
// WHY: Need to find out if the charges of the current two globalMuons-Tracks 
//      are like or unlike charge, since the decaying parents are neutral

        if (it->charge() == -(i->charge()) // unlike charges
// and cut on quality of 2nd global muon candidate
            && ValidHits1 >= 12
            && PixelHits1 >= 2
            && i->normalizedChi2() < 4.0) {

//----------Calculate invariant mass-----------------//
// WHAT: Calculate invariant mass of globalMuon-Tracks under comparison 
// (Iterators "it" and "i")
// WHY: in order to fill the mass histogram
          s1 = sqrt(((it->p())*(it->p()) + sqm1) * ((i->p())*(i->p()) + sqm1));
          s2 = it->px()*i->px() + it->py()*i->py() + it->pz()*i->pz();
          s = sqrt(2.0 * (sqm1 + (s1 - s2)));

// WHAT: Store the invariant mass of two muons with unlike sign charges in 
//       linear scale
// WHY:  in order to see the various mass peaks on linear scale
          h5->Fill(s);
          h6->Fill(s);

// WHAT: apply weight 200/(ln10*m/GeV) according to histogram binning
// WHY: to convert units to events/GeV in logarithmic mass plot
          w = 200 / log(10) / s;

// WHAT: Store the invariant mass of two muons with unlike charges in log scale
// WHY: Reproduce the "Invariant mass spectrum of dimuons in events"-plot 
//      from MUO-10-004
          h100->Fill(log10(s), w); // MUO-10-004 with MuonCollection

        } // end of unlike charge if
      }   //end of for(;i!=gmuons....)
    }   //end of if(gmuons->size >=2 .....)
  }   //end of reco ::TrackCollection loop
 }  // end of if (goodlumisection)
} //DemoAnalyzer::analyze ends


// ---- method called for each event to check good quality lumi section ---- //
bool DemoAnalyzer::providesGoodLumisection(const edm::Event& iEvent) {

// check JSON "by hand"
// This is a 'primitive' check which has the advantage that it also works 
// outside a python setup environment.
// Here it is intended as a check only, but it could replace this environment 
// if needed/wished.
 
// a JSON provides a "list of good lumi sections" 
//      from general data quality monitoring 
// 
// if badJSON is nonzero the event should not be used for analysis 
//      unless monitoring of `rejected' runs is wished

// https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCollisionsDataAnalysis#Conceptual_overview

// NTS: this code checks whether the RunNumber_t from edm::EventID is
// included in the JSON that describes runs that are consider to be good.
// Then it checks if the luminosityBlock of the event doesn't fall into the 
// luminosityBlocks defined in the same file
// e.g RunNumber "146428" has three good luminosityBlock ranges: 
//     [1, 2], [11, 52], [55, 92] and the code below
// checks if the analyzed run falls outside these ranges 
// and marks the event as "bad" if it doesn't belong to these ranges.

// NTS: A "better" (i.e. more standard) way to check LumiList info is provided 
// here:
// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGoodLumiSectionsJSONFile

// NTS: Another way (the usual one) is to configure good lumisections 
// from _cfg.py
// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePythonTips?redirectedfrom=CMS.SWGuidePythonTips#Use_a_JSON_file_of_good_lumi_sec
// The present code assumes that this has indeed been done, and gives an 
// error message if it finds inconsistencies 
	
 int badJSON = 0;

 if (iEvent.run() == 146428) {
  if ((iEvent.luminosityBlock() > 2 && iEvent.luminosityBlock() < 11) ||
      (iEvent.luminosityBlock() > 52 && iEvent.luminosityBlock() < 55) ||
      (iEvent.luminosityBlock() > 92))
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146430) {
  if ((iEvent.luminosityBlock() > 12 && iEvent.luminosityBlock() < 18) ||
      (iEvent.luminosityBlock() > 47 && iEvent.luminosityBlock() < 50) ||
      (iEvent.luminosityBlock() > 62 && iEvent.luminosityBlock() < 65) ||
      (iEvent.luminosityBlock() > 90))
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146431) {
  if (iEvent.luminosityBlock() > 23)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146436) {
  if (iEvent.luminosityBlock() > 532)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146437) {
  if (iEvent.luminosityBlock() > 798)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146510) {
  if (iEvent.luminosityBlock() > 510)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146511) {
  if (iEvent.luminosityBlock() == 64 || iEvent.luminosityBlock() > 778)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146513) {
  if (iEvent.luminosityBlock() == 2 || iEvent.luminosityBlock() > 15)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146514) {
  if (iEvent.luminosityBlock() == 546 || iEvent.luminosityBlock() == 547 || iEvent.luminosityBlock() > 871)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146589) {
  if (iEvent.luminosityBlock() < 34 || iEvent.luminosityBlock() > 248)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146644) {
   if (iEvent.luminosityBlock() < 89 || iEvent.luminosityBlock() == 118 || iEvent.luminosityBlock() == 566 || iEvent.luminosityBlock() == 868 || iEvent.luminosityBlock() == 1033 || (iEvent.luminosityBlock() > 2171 && iEvent.luminosityBlock() < 2369) || iEvent.luminosityBlock() > 2465)
   badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146698) {
   if (iEvent.luminosityBlock() < 155 || (iEvent.luminosityBlock() > 180 && iEvent.luminosityBlock() < 186) || iEvent.luminosityBlock() > 189)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146710) {
   if (iEvent.luminosityBlock() == 116 || (iEvent.luminosityBlock() > 49 && iEvent.luminosityBlock() < 114) || iEvent.luminosityBlock() > 214)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146712) {
   if (iEvent.luminosityBlock() > 69)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146713) {
   if (iEvent.luminosityBlock() == 49 || iEvent.luminosityBlock() > 256)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146715) {
   if (iEvent.luminosityBlock() > 125)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146721) {
   if (iEvent.luminosityBlock() > 6)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146724) {
   if (iEvent.luminosityBlock() == 107 || iEvent.luminosityBlock() == 108 || (iEvent.luminosityBlock() > 109 && iEvent.luminosityBlock() < 112) || iEvent.luminosityBlock() == 151 || iEvent.luminosityBlock() > 159)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146804) {
   if (iEvent.luminosityBlock() < 111 || iEvent.luminosityBlock() == 149 || iEvent.luminosityBlock() == 521 || iEvent.luminosityBlock() == 790 || iEvent.luminosityBlock() == 823 || iEvent.luminosityBlock() > 905)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146807) {
   if (iEvent.luminosityBlock() < 132 || iEvent.luminosityBlock() == 363 || iEvent.luminosityBlock() == 364 || iEvent.luminosityBlock() == 421 || iEvent.luminosityBlock() > 469)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 146944) {
   if (iEvent.luminosityBlock() < 177 || iEvent.luminosityBlock() > 669)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147043) {
   if (iEvent.luminosityBlock() < 161 || iEvent.luminosityBlock() > 500)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147048) {
   if (iEvent.luminosityBlock() < 94 || iEvent.luminosityBlock() > 484)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147114) {
   if (iEvent.luminosityBlock() < 180 || (iEvent.luminosityBlock() > 187 && iEvent.luminosityBlock() < 227) || (iEvent.luminosityBlock() > 240 && iEvent.luminosityBlock() < 247) || iEvent.luminosityBlock() > 667)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147115) {
   if (iEvent.luminosityBlock() > 546)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147116) {
   if (iEvent.luminosityBlock() > 54)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147196) {
   if (iEvent.luminosityBlock() > 90)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147214) {
   if (iEvent.luminosityBlock() > 79)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147216) {
   if (iEvent.luminosityBlock() > 63)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147217) {
   if (iEvent.luminosityBlock() > 193)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147218) {
   if (iEvent.luminosityBlock() > 45)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147219) {
   if ((iEvent.luminosityBlock() > 293 && iEvent.luminosityBlock() < 309) || iEvent.luminosityBlock() > 320)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147222) {
   if (iEvent.luminosityBlock() > 444)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147284) {
   if (iEvent.luminosityBlock() < 32 || iEvent.luminosityBlock() > 306)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147390) {
   if (iEvent.luminosityBlock() == 479 || iEvent.luminosityBlock() > 837)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147450) {
   if (iEvent.luminosityBlock() < 80 || iEvent.luminosityBlock() > 166)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147451) {
   if (iEvent.luminosityBlock() == 117 || iEvent.luminosityBlock() > 129)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147452) {
   if (iEvent.luminosityBlock() > 44)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147453) {
   if (iEvent.luminosityBlock() > 146)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147454) {
   if (iEvent.luminosityBlock() > 97)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147754) {
   if (iEvent.luminosityBlock() == 168 || iEvent.luminosityBlock() == 169 || iEvent.luminosityBlock() > 377)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147755) {
   if (iEvent.luminosityBlock() < 81 || iEvent.luminosityBlock() > 231)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147757) {
   if (iEvent.luminosityBlock() > 359)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147926) {
   if (iEvent.luminosityBlock() < 77 || iEvent.luminosityBlock() > 548)
   badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147927) {
   if (iEvent.luminosityBlock() > 152)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 147929) {
   if ((iEvent.luminosityBlock() > 266 && iEvent.luminosityBlock() < 272) || iEvent.luminosityBlock() == 619 || iEvent.luminosityBlock() > 643)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148002) {
   if (iEvent.luminosityBlock() < 92 || iEvent.luminosityBlock() > 203)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148029) {
   if (iEvent.luminosityBlock() < 50 || iEvent.luminosityBlock() == 484 || iEvent.luminosityBlock() == 570 || iEvent.luminosityBlock() > 571)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148031) {
   if ((iEvent.luminosityBlock() > 341 && iEvent.luminosityBlock() < 472) || iEvent.luminosityBlock() == 758 || iEvent.luminosityBlock() > 855)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148032) {
  if (iEvent.luminosityBlock() > 199)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148058) {
   if (iEvent.luminosityBlock() > 97)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148822) {
   if (iEvent.luminosityBlock() > 446)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148829) {
   if ((iEvent.luminosityBlock() > 240 && iEvent.luminosityBlock() < 244) || iEvent.luminosityBlock() == 74 || iEvent.luminosityBlock() > 303)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148860) {
   if (iEvent.luminosityBlock() > 39)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148862) {
   if (iEvent.luminosityBlock() == 19 || iEvent.luminosityBlock() == 109 || iEvent.luminosityBlock() == 150 || (iEvent.luminosityBlock() > 165 && iEvent.luminosityBlock() < 224) || (iEvent.luminosityBlock() > 258 && iEvent.luminosityBlock() < 262) || iEvent.luminosityBlock() == 298 || iEvent.luminosityBlock() == 367 || (iEvent.luminosityBlock() > 504 && iEvent.luminosityBlock() < 512) || iEvent.luminosityBlock() > 679)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148864) {
   if (iEvent.luminosityBlock() == 32 || (iEvent.luminosityBlock() > 141 && iEvent.luminosityBlock() < 224) || iEvent.luminosityBlock() == 237 || iEvent.luminosityBlock() == 477 || iEvent.luminosityBlock() > 680)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148952) {
   if (iEvent.luminosityBlock() < 70 || iEvent.luminosityBlock() > 257)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 148953) {
   if (iEvent.luminosityBlock() > 100)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 149003) {
   if (iEvent.luminosityBlock() < 84 || iEvent.luminosityBlock() > 238)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 149011) {
   if (iEvent.luminosityBlock() == 342 || iEvent.luminosityBlock() > 706)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 149058) {
   if (iEvent.luminosityBlock() > 65)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 149063) {
   if (iEvent.luminosityBlock() > 102)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 149181) {
   if (iEvent.luminosityBlock() < 229 || (iEvent.luminosityBlock() > 1840 && iEvent.luminosityBlock() < 1844) || iEvent.luminosityBlock() > 1920)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 149291) {
   if (iEvent.luminosityBlock() < 79 || (iEvent.luminosityBlock() > 79 && iEvent.luminosityBlock() < 82) || iEvent.luminosityBlock() == 787 || iEvent.luminosityBlock() == 789 || (iEvent.luminosityBlock() > 790 && iEvent.luminosityBlock() < 794) || iEvent.luminosityBlock() > 794)
    badJSON = iEvent.run(); 
 }
 else if (iEvent.run() == 149294) {
  if (iEvent.luminosityBlock() > 171)
    badJSON = iEvent.run(); 
 }
 else {
   badJSON = iEvent.run(); 
 }

 // signal presence of bad JSON event
 if (badJSON > 0) {
    	return false;
 }
 else
        return true;
}


// ------------ method called once each job just before starting event loop  ------------
void DemoAnalyzer::beginJob() {

}

// ------------ method called once each job just after ending the event loop  ------------
void DemoAnalyzer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(DemoAnalyzer);

