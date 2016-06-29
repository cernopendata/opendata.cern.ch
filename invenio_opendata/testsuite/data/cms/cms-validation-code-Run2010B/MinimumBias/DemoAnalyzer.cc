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
//         Finalized: June 10, 2016  by   A. Geiser
//                    with contributions from I. Dutta, 
//                                            H. Hirvonsalo
// $Id$
// ..
//
// ***************************************************************************
// version of DEMO setup provided by CMS open data access team               *
// expanded/upgraded to contain a validation example for some technical      *
// track distributions as well as minumum bias track multiplicities and      *
// pt/eta distributions (QCD-10-006)                                         *
//                                                                           *
// Note that the published spectra can not be reproduced exactly, since no   *
// MC is provided, so track acceptance corrections can not be applied.       *
// The comparison is therfore meant to be qualitative.                       *
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

// for vertex information 
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

//for beamspot information
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

// class declaration
//

class DemoAnalyzer: public edm::EDAnalyzer {
public:
	explicit DemoAnalyzer(const edm::ParameterSet&);
	~DemoAnalyzer();

	// declare variables
	double deltaz;
	double firstz;

private:
	virtual void beginJob();
	virtual void analyze(const edm::Event&, const edm::EventSetup&);
	virtual void endJob();
	bool providesGoodLumisection(const edm::Event& iEvent);

	// ----------member data ---------------------------

// declare Root histograms
// for a description of their content see below
	TH1D *h6;
	TH1D *h7;
	TH1D *h8;
	TH1D *h9;
	TH1D *h10;
	TH1D *h11;
	TH1D *h12;
	TH1D *h13;
	TH1D *h14;
	TH1D *h15;
	TH1D *h16;
	TH1D *h17;
	TH1D *h18;
	TH1D *h19;
	TH1D *h20;
	TH1D *h21;
	TH1D *h22;
	// TH1D *h23;
	// TH1D *h24;
	// TH1D *h25;
	TH1D *h26;
	TH1D *h27;
	TH1D *h28;
	TH1D *h29;
	TH1D *h30;
	TH1D *h31;
	TH1D *h32;
	TH1D *h33;
	TH1D *h34;
	TH1D *h35;
	TH1D *h36;
	TH1D *h37;
	TH1D *h38;
	TH1D *h39;
	TH1D *h40;
	TH1D *h41;
	TH1D *h42;
	TH1D *h43;
	TH1D *h44;
	TH1D *h45;
	TH1D *h46;
	TH1D *h47;
	TH1D *h48;
	TH1D *h49;
	TH1D *h50;
	TH1D *h51;
	TH1D *h52;
	TH1D *h53;
	TH1D *h54;
	TH1D *h55;
	TH1D *h56;
	TH1D *h57;
	TH1D *h58;
	TH1D *h59;
	TH1D *h60;
	TH1D *h61;
	TH1D *h62;
	TH1D *h63;
	TH1D *h64;
	TH1D *h65;
	TH1D *h66;
	TH1D *h67;
	TH1D *h68;
	TH1D *h69;
	TH1D *h70;
	TH1D *h71;
	TH1D *h72;
	TH1D *h73;
	TH1D *h74;
	TH1D *h75;
	TH1D *h76;
	TH1D *h77;
	TH1D *h78;
	TH1D *h79;
	TH1D *h80;
	TH1D *h81;
	TH1D *h82;
	TH1D *h83;
	TH1D *h84;
	TH1D *h85;
	TH1D *h86;
	TH1D *h87;
	TH1D *h88;
	TH1D *h89;
	TH1D *h90;
	TH1D *h91;
	TH1D *h92;
	TH1D *h93;
	TH1D *h94;
	TH1D *h95;

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
// The goal is to approximately reproduce the track spectra
// from QCD-10-006
// *****************************************************************

	//now do what ever initialization is needed
	edm::Service<TFileService> fs;

// ************************************
// book histograms and set axis labels
// (called once for initialization)
// ************************************

// Monitoring histograms for inclusive tracks,
// intended for tracks from minimum bias sample


        // global track multiplicity
	h6  = fs->make<TH1D>("tracks", "Tracks", 300, 0, 300); // Track Multiplicity
        // track momentum, transverse momentum, pseurapidity, azimuth angle
	h34 = fs->make<TH1D>("momentum", "Momentum", 200, 0, 20.0); // Track momentum
	h35 = fs->make<TH1D>("pt", "PT", 200, 0, 4.0); //Track pt
	h38 = fs->make<TH1D>("track_eta", "Eta", 100, -3.5, 3.5); //Track eta
	h81 = fs->make<TH1D>("track_phi", "Track_Phi", 314, -3.15, 3.15); //Track phi
	// track vertex position
	h36 = fs->make<TH1D>("posx", "Position X", 100, 0.0, .2); // Track position x
	h37 = fs->make<TH1D>("posy", "Position Y", 100, -.1, .1); // track position y
	h7  = fs->make<TH1D>("posz", "Position Z", 100, -25.0, 25.0); // Track position z
        // flag for "proper" vertices (excluding null vertices)
	h8  = fs->make<TH1D>("propvertex", "ProperVertices", 20, 0, 20); // Proper vertices, i.e.after checking the number of tracks for the vertex
        // track pt spectra for different |eta| ranges, 0-0.2, 0.2-0.4, 0.4-0.6, 0.6-0.8, 0.8-1.0,
        //                                            1.0-1.2, 1.2-1.4, 1.4-1.6, 1.6-1.8, 1.8-2.0,
        //                                            2.0-2.2, 2.2-2.4, 2.4-2.6 
	h9  = fs->make<TH1D>("0.2pt", "0.2pt", 100, 0, 4.0); // Tracks with absolute value of eta less than 0.2
	h10 = fs->make<TH1D>("0.4pt", "0.4pt", 100, 0, 4.0); //Tracks with absolute value mof eta between 0.2 and 0.4
	h11 = fs->make<TH1D>("0.6pt", "0.6pt", 100, 0, 4.0); // and so on...
	h12 = fs->make<TH1D>("0.8pt", "0.8pt", 100, 0, 4.0);
	h13 = fs->make<TH1D>("1.0pt", "1.0pt", 100, 0, 4.0);
	h14 = fs->make<TH1D>("1.2pt", "1.2pt", 100, 0, 4.0);
	h15 = fs->make<TH1D>("1.4pt", "1.4pt", 100, 0, 4.0);
	h16 = fs->make<TH1D>("1.6pt", "1.6pt", 100, 0, 4.0);
	h17 = fs->make<TH1D>("1.8pt", "1.8pt", 100, 0, 4.0);
	h18 = fs->make<TH1D>("2.0pt", "2.0pt", 100, 0, 4.0);
	h19 = fs->make<TH1D>("2.2pt", "2.2pt", 100, 0, 4.0);
	h20 = fs->make<TH1D>("2.4pt", "2.4pt", 100, 0, 4.0);
	h21 = fs->make<TH1D>("2.6pt", "2.6pt", 100, 0, 4.0);
        // z distance of vertices from primary vertex
	h22 = fs->make<TH1D>("deltaz", "DeltaZ", 300, 0, 30.0); // the absolute value of the distance in the z coordinate of all vertices from Primvertex->begin()
	//h23=fs->make<TH1D>("track_vertex_x" , "TrackVertexX" , 100 , -30.0 , 30.0 );
	//h24=fs->make<TH1D>("track_vertex_y" , "TrackVertexY" , 100 , -30.0 , 30.0 );
	//h25=fs->make<TH1D>("track_vertex_z" , "TrackVertexZ" , 100 , -30.0 , 30.0 );
        // 'raw' vertex multiplicity
	h26 = fs->make<TH1D>("vertex", "Vertices", 20, 0, 20); // Just vertex multiplicity, without any corrections
        // momentum, pt, phi for vertex tracks
	h28 = fs->make<TH1D>("VertexTrack_momentum", "VertexTrack_Momentum", 200, 0, 20.0); // Track momentum
	h27 = fs->make<TH1D>("VertexTrack_pt", "VertexTrack_Pt", 200, 0, 4.0); // Pt of tracks associated with a particular vertex
        h85= fs->make<TH1D>("VertexTrack_eta", "VertexTrack_Eta",100, -3.5,3.5); //Track eta for tracks associated to vertex
	h82 = fs->make<TH1D>("VertexTrack_phi", "VertexTrack_Phi", 100, -3.5, 3.5); //Track phi

        h86= fs->make<TH1D>("tracks_per_vertex_using_counter" , "Tracks per Vertex using counter" , 200 , 0 , 200 );// Track Multiplicity
        h87= fs->make<TH1D>("tracks_per_vertex" , "Tracks per Vertex" , 200 , 0 , 200.);// Track Multiplicity


	// set axis labels
	h6->GetXaxis()->SetTitle("Number of Tracks");
	h6->GetYaxis()->SetTitle("Number of Events");

 	h34->GetXaxis()->SetTitle("Momentum (in GeV/c)");
	h34->GetYaxis()->SetTitle("Number of Events");

	h35->GetXaxis()->SetTitle("Transverse Momentum (in GeV/c)");
	h35->GetYaxis()->SetTitle("Number of Events");

	h36->GetXaxis()->SetTitle("Position X of Vertices (in cm)");
	h36->GetYaxis()->SetTitle("Number of Events");

	h37->GetXaxis()->SetTitle("Position Y of Vertices (in cm)");
	h37->GetYaxis()->SetTitle("Number of Events");

	h7->GetXaxis()->SetTitle("Position z of Vertices (in cm)");
	h7->GetYaxis()->SetTitle("Number of Events");

	h38->GetXaxis()->SetTitle("Eta (in radians)");
	h38->GetYaxis()->SetTitle("Number of Events");

	h81->GetXaxis()->SetTitle("Phi");
	h81->GetYaxis()->SetTitle("Number of Events");

	h8->GetXaxis()->SetTitle("Number of vertices with a non zero number of tracks associated to it");
	h8->GetYaxis()->SetTitle("Number of Events");

	h9->GetXaxis()->SetTitle("Transverse Momentum for |eta|<0.2(in GeV/c)");
	h9->GetYaxis()->SetTitle("Number of Events");

	h10->GetXaxis()->SetTitle("Transverse Momentum for |eta|<0.4 and |eta|>=0.2(in GeV/c)");
	h10->GetYaxis()->SetTitle("Number of Events");

	h11->GetXaxis()->SetTitle("Transverse Momentum for |eta|<0.6 and |eta|>=0.4(in GeV/c)");
	h11->GetYaxis()->SetTitle("Number of Events");

	h12->GetXaxis()->SetTitle("Transverse Momentum for |eta|<0.8 and |eta|>=0.6(in GeV/c)");
	h12->GetYaxis()->SetTitle("Number of Events");

	h13->GetXaxis()->SetTitle("Transverse Momentum for |eta|<1.0 and |eta|>=0.8(in GeV/c)");
	h13->GetYaxis()->SetTitle("Number of Events");

	h14->GetXaxis()->SetTitle("Transverse Momentum for |eta|<1.2 and |eta|>=1.0(in Gev/c)");
	h14->GetYaxis()->SetTitle("Number of Events");

	h15->GetXaxis()->SetTitle("Transverse Momentum for |eta|<1.4 and |eta|>=1.2(in GeV/c)");
	h15->GetYaxis()->SetTitle("Number of Events");

	h16->GetXaxis()->SetTitle("Transverse Momentum for |eta|<1.6 and |eta|>=1.4(in GeV/c)");
	h16->GetYaxis()->SetTitle("Number of Events");

	h17->GetXaxis()->SetTitle("Transverse Momentum for |eta|<1.8 and |eta|>=1.6(in Gev/c)");
	h17->GetYaxis()->SetTitle("Number of Events");

	h18->GetXaxis()->SetTitle("Transverse Momentum for |eta|<2.0 and |eta|>=1.8(in GeV/c)");
	h18->GetYaxis()->SetTitle("Number of Events");

	h19->GetXaxis()->SetTitle("Transverse Momentum for |eta|<2.2 and |eta|>=2.0(in Gev/c)");
	h19->GetYaxis()->SetTitle("Number of Events");

	h20->GetXaxis()->SetTitle("Transverse Momentum for |eta|<2.4 and |eta|>=2.2(in GeV/c)");
	h20->GetYaxis()->SetTitle("Number of Events");

	h21->GetXaxis()->SetTitle("Transverse Momentum for |eta|<2.6 and |eta|>=2.4(in GeV/c)");
	h21->GetYaxis()->SetTitle("Number of Events");

	h22->GetXaxis()->SetTitle("Absolute value of the z distance of Vertices from the first primary vertex (in cm)");
	h22->GetYaxis()->SetTitle("Number of Events");

	h26->GetXaxis()->SetTitle("Vertex multiplicity");
	h26->GetYaxis()->SetTitle("Number of Events");

	h28->GetXaxis()->SetTitle("Momentum of tracks associated with a vertex (in GeV/c)");
	h28->GetYaxis()->SetTitle("Number of Events");

	h27->GetXaxis()->SetTitle("Transverse Momentum of tracks associated with a vertex (in GeV/c)");
	h27->GetYaxis()->SetTitle("Number of Events");

        h85->GetXaxis()->SetTitle("Eta of tracks associated to vertex (in radians)");
        h85->GetYaxis()->SetTitle("Number of Events"); 

	h82->GetXaxis()->SetTitle("Phi of tracks associated to a vertex");
	h82->GetYaxis()->SetTitle("Number of Events");

        h86->GetXaxis()->SetTitle("Number of Tracks");
        h86->GetYaxis()->SetTitle("Number of Vertices");
        h87->GetXaxis()->SetTitle("Number of Tracks");
        h87->GetYaxis()->SetTitle("Number of Vertices");


// general event histograms      and 
// histograms to check good run preselection from  JSON

// Run number for all events that have been analyzed 
	h200 = fs->make<TH1D>("Run number", "Run number", 3100, 146400, 149500);

// Run number for events that have been analyzed, 
// which belong to runs considered "bad" according to JSON, Should be empty!
// If it is not empty, check JSON preselection in Python part of program	
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


	//------------------Fill basic Event-information histograms------------------------//
// debug print commented out
//      LogInfo("Demo")<<"Event id: "<<iEvent.id()<<" Run number: "<<iEvent.run();

	h200->Fill(iEvent.run());		// Run number which the analyzed Event belongs to
	h202->Fill((iEvent.id()).event());	// Event's EventNumber
	h203->Fill(iEvent.luminosityBlock());	// Luminosity Section that this Event provides


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
				<< ",Run number: " << iEvent.run()
				<< ",Lumisection: " << iEvent.luminosityBlock();

		//------------------Load (relevant) Event information------------------------//
		// INFO: Getting Data From an Event
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookChapter4#GetData
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDMGetDataFromEvent#get_ByLabel
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAodDataTable
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideRecoDataTable


		//------------------Tracks of Event-------------------------//
		// INFO: Basic info about Tracks of an Event.
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideTrackReco
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideTrackingFAQ
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookPATExampleTrackBJet#ExerCise1
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookChapter4#GeT
		// Alternative fits for tracks: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookTrackAnalysis#TrackQual

		// INFO: generalTracks
		// "Collection of tracks obtained with tracker-standalone reconstruction
		// and officially supported by the Tracker DPG group. Such a collection can
		// contain tracks from different tracking algorithms"
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideDataFormatRecoTracker
		Handle<reco::TrackCollection> tracks;
		iEvent.getByLabel("generalTracks", tracks);

		//------------------BeamSpot of Event-------------------------//
		// WHAT:
		// WHY:
		// INFO: Basic info about BeamSpot
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFindingBeamSpot#Introduction
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFindingBeamSpot#Access_to_the_beam_spot_data
		Handle<reco::BeamSpot> beamSpotHandle;
		iEvent.getByLabel("offlineBeamSpot", beamSpotHandle);
		reco::BeamSpot beamSpot;
		if (beamSpotHandle.isValid()) {
			beamSpot = *beamSpotHandle;
		} else {
			edm::LogInfo("Demo") << "No beam spot available from EventSetup \n";
		}


		//------------------Primary vertices of Event-------------------------//
		// WHAT: choose primary vertices with or without BeamSpot
		// https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideDataFormatRecoVertex
		Handle<reco::VertexCollection> primaryVertices;
		// defualt is with beam spot. to change to without beam spot, comment the next line, and uncomment next-to-next
		iEvent.getByLabel("offlinePrimaryVerticesWithBS", primaryVertices);
//		iEvent.getByLabel("offlinePrimaryVertices",Primvertex);


		//------------------fill basic track information (all tracks in event)-------------------------//

		// WHAT: Store number of tracks in current Event
		h6->Fill(tracks->size());

		// WHAT: Store number of primaryVertices in current Event
		h26->Fill(primaryVertices->size());


		// WHAT: Loop over all the Tracks of current Event
		// NTS: This loop is for QCD-10-006, to get p,pt,eta,phi for a track.
		for (reco::TrackCollection::const_iterator it = tracks->begin(); it != tracks->end(); it++) {
//		    LogInfo("Demo")<<"track p"<<it->p()<< "  track reference position"<<it->referencePoint()<< "   track vertex position"<<it->vertex();

			// WHAT: Store p, pt, eta and phi of each Track.
			h34->Fill(it->p());
			h35->Fill(it->pt());
			h38->Fill(it->eta());
			h81->Fill(it->phi());

			// NTS: These histograms where commented out in the original code. Should these be removed?
//			h23->Fill(it->vx());
//			h24->Fill(it->vy());
//			h25->Fill(it->vz());

			// WHAT: Fill histograms for QCD-10-006
			if (fabs(it->eta()) <= 0.200) {
				h9->Fill(it->pt());
			}
			if (fabs(it->eta()) > 0.200 && fabs(it->eta()) < 0.400) {
				h10->Fill(it->pt());
			}
			if (fabs(it->eta()) > 0.400 && fabs(it->eta()) <= 0.600) {
				h11->Fill(it->pt());
			}
			if (fabs(it->eta()) < 0.600 && fabs(it->eta()) <= 0.800) {
				h12->Fill(it->pt());
			}
			if (fabs(it->eta()) > 0.800 && fabs(it->eta()) <= 1.00) {
				h13->Fill(it->pt());
			}
			if (fabs(it->eta()) > 1.00 && fabs(it->eta()) <= 1.20) {
				h14->Fill(it->pt());
			}
			if (fabs(it->eta()) > 1.200 && fabs(it->eta()) <= 1.40) {
				h15->Fill(it->pt());
			}
			if (fabs(it->eta()) > 1.400 && fabs(it->eta()) <= 1.60) {
				h16->Fill(it->pt());
			}
			if (fabs(it->eta()) > 1.600 && fabs(it->eta()) <= 1.80) {
				h17->Fill(it->pt());
			}
			if (fabs(it->eta()) > 1.800 && fabs(it->eta()) <= 2.00) {
				h18->Fill(it->pt());
			}
			if (fabs(it->eta()) > 2.000 && fabs(it->eta()) <= 2.20) {
				h19->Fill(it->pt());
			}
			if (fabs(it->eta()) > 2.200 && fabs(it->eta()) <= 2.40) {
				h20->Fill(it->pt());
			}
			if (fabs(it->eta()) > 2.400 && fabs(it->eta()) <= 2.60) {
				h21->Fill(it->pt());
			}

		}	// end of Tracks-collection loop


		// WHAT: Get basic Primary Vertex information of current Event
		// WHY:
		int size; // variable to store the size of vertices in current event //NTS: size of vertices --> NUMBER of vertices?
		size = primaryVertices->size();

		// NTS: This section tries to identify if there are muons (from Handle<reco::MuonCollection> muons) associated with the vertices.
		// WHAT: Loop over all of the Primary Vertices of current Event
		for (reco::VertexCollection::const_iterator ite = primaryVertices->begin(); ite != primaryVertices->end(); ite++) {

			// WHAT: Store z-position of first vertex
			if (ite == primaryVertices->begin())
				firstz = ite->z();

			// WHAT:
			// WHY:
			if (ite->tracksSize() == 0) { //This is done so that there are no vertices with zero tracks stored in the histogram.
				size = size - 1;
			}

			// WHAT: Store distance of current vertex to first vertex and fill histogram
			if (ite->z() != firstz) {
				deltaz = fabs(firstz - (ite->z()));
				h22->Fill(deltaz);
			}

			// WHAT: only store the coordinates of those vertices which are valid and have tracks
			// WHY: very first attempt in context of FWD-11-001 (from Achim)
			if (ite->tracksSize() != 0) {

				// WHAT: Store x, y, z -positions and number Tracks associated to current Primary Vertex
				// WHY:
				h36->Fill(ite->x());
				h37->Fill(ite->y());
				h7->Fill(ite->z());
				h87->Fill(ite->tracksSize());

				//-----Get track details for valid vertices-------------//

//				LogInfo("Demo")<<"Vertex position"<<ite->position()<<endl;

				// WHAT: loop over all Tracks associated to current Vertex
				// WHY: for dealing with tracks associated with a particular vertex
				int counter = 0;
				for (reco::Vertex::trackRef_iterator iTrack = ite->tracks_begin(); iTrack != ite->tracks_end(); ++iTrack) {

					// WHAT: Store pt, p, eta, phi of each Track associated to the current Primary Vertex
					// NTS: *iTrack points to an Track-object contained in vector<TrackRef> that is a member of Vertex-class
					h27->Fill((*iTrack)->pt()); // vertex.track pt
					h28->Fill((*iTrack)->p()); // vertex.track p
					h85->Fill((*iTrack)->eta());
					h82->Fill((*iTrack)->phi());

//					LogInfo("Demo")<<"Vertex track p"<<(*iTrack)->p()<<"  Vertex trackposition"<<(*iTrack)->referencePoint();

					counter++;
				}

				// WHAT: Fill number of tracks associated to this vertex (is it Ok to fill int?)
				h86->Fill(counter);

			} // end of if(ite->tracksSize()!=0 && Muflag==0)
		} //end of vertex collection loop

		//only valid vertices get stored.
		// NTS: Is it that, "valid vertices" in this context mean Vertices that have Tracks associated to them???
		h8->Fill(size);

        } // end of good lumi section

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

