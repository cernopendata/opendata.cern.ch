# /cdaq/physics/Run2011HI/2760GeV/v1.1/HLT/V4 (CMSSW_3_11_0_HLT18)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string( '/cdaq/physics/Run2011HI/2760GeV/v1.1/HLT/V4' )
)

process.streams = cms.PSet(
  A = cms.vstring( 'AllPhysics2760',
    'Commissioning',
    'Cosmics',
    'HcalHPDNoise',
    'HcalNZS' ),
  ALCAP0 = cms.vstring( 'AlCaP0' ),
  ALCAPHISYM = cms.vstring( 'AlCaPhiSym' ),
  Calibration = cms.vstring( 'TestEnables' ),
  DQM = cms.vstring( 'OnlineMonitor' ),
  EcalCalibration = cms.vstring( 'EcalLaser' ),
  Express = cms.vstring( 'ExpressPhysics2760' ),
  HLTDQM = cms.vstring( 'OnlineHltMonitor' ),
  HLTDQMResults = cms.vstring( 'OnlineHltResults' ),
  HLTMON = cms.vstring( 'OfflineMonitor' ),
  NanoDST = cms.vstring( 'L1Accept' ),
  OnlineErrors = cms.vstring( 'FEDMonitor',
    'LogMonitor' ),
  RPCMON = cms.vstring( 'RPCMonitor' )
)

process.datasets = cms.PSet(
  AlCaP0 = cms.vstring( 'AlCa_EcalEta_v3',
    'AlCa_EcalPi0_v4' ),
  AlCaPhiSym = cms.vstring( 'AlCa_EcalPhiSym_v2' ),
  AllPhysics2760 = cms.vstring( 'HLT_DoubleMu3_v3',
    'HLT_Ele8_v2',
    'HLT_Jet20_v1',
    'HLT_Jet40_v1',
    'HLT_Jet60_v1',
    'HLT_L1BscMinBiasORBptxPlusANDMinus_v1',
    'HLT_L1DoubleForJet32_EtaOpp_v1',
    'HLT_L1DoubleForJet8_EtaOpp_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_Mu0_v3',
    'HLT_Mu3_v3',
    'HLT_Mu5_v3',
    'HLT_Photon10_CaloIdVL_v1',
    'HLT_Photon15_CaloIdVL_v1',
    'HLT_PixelTracks_Multiplicity50_Loose',
    'HLT_PixelTracks_Multiplicity60_Loose',
    'HLT_PixelTracks_Multiplicity70_Loose',
    'HLT_Random_v1',
    'HLT_ZeroBiasPixel_SingleTrack_v1',
    'HLT_ZeroBias_v1' ),
  Commissioning = cms.vstring( 'HLT_BeamGas_BSC_v2',
    'HLT_BeamGas_HF_v2',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_L1SingleEG12_v1',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1' ),
  Cosmics = cms.vstring( 'HLT_BeamHalo_v2',
    'HLT_L1SingleMuOpen_AntiBPTX_v1',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_RegionalCosmicTracking_v1' ),
  EcalLaser = cms.vstring( 'HLT_EcalCalibration_v1' ),
  ExpressPhysics2760 = cms.vstring( 'HLT_Ele8_v2',
    'HLT_Jet60_v1',
    'HLT_Mu5_v3',
    'HLT_Photon15_CaloIdVL_v1',
    'HLT_ZeroBias_v1' ),
  FEDMonitor = cms.vstring( 'HLT_DTErrors_v1' ),
  HcalHPDNoise = cms.vstring( 'HLT_GlobalRunHPDNoise_v2',
    'HLT_L1Tech_HBHEHO_totalOR_v1' ),
  HcalNZS = cms.vstring( 'HLT_HcalNZS_v3',
    'HLT_HcalPhiSym_v3' ),
  L1Accept = cms.vstring( 'HLT_Physics_NanoDST_v1' ),
  LogMonitor = cms.vstring( 'HLT_LogMonitor_v1' ),
  OfflineMonitor = cms.vstring( 'AlCa_EcalEta_v3',
    'AlCa_EcalPhiSym_v2',
    'AlCa_EcalPi0_v4',
    'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2',
    'HLT_BeamGas_BSC_v2',
    'HLT_BeamGas_HF_v2',
    'HLT_BeamHalo_v2',
    'HLT_DTErrors_v1',
    'HLT_DoubleMu3_v3',
    'HLT_Ele8_v2',
    'HLT_GlobalRunHPDNoise_v2',
    'HLT_HcalNZS_v3',
    'HLT_HcalPhiSym_v3',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_Jet20_v1',
    'HLT_Jet40_v1',
    'HLT_Jet60_v1',
    'HLT_L1BscMinBiasORBptxPlusANDMinus_v1',
    'HLT_L1DoubleForJet32_EtaOpp_v1',
    'HLT_L1DoubleForJet8_EtaOpp_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L1SingleEG12_v1',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMuOpen_AntiBPTX_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1Tech_HBHEHO_totalOR_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_LogMonitor_v1',
    'HLT_Mu0_v3',
    'HLT_Mu3_v3',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1',
    'HLT_Mu5_v3',
    'HLT_Photon10_CaloIdVL_v1',
    'HLT_Photon15_CaloIdVL_v1',
    'HLT_PixelTracks_Multiplicity50_Loose',
    'HLT_PixelTracks_Multiplicity60_Loose',
    'HLT_PixelTracks_Multiplicity70_Loose',
    'HLT_Random_v1',
    'HLT_RegionalCosmicTracking_v1',
    'HLT_ZeroBiasPixel_SingleTrack_v1',
    'HLT_ZeroBias_v1' ),
  OnlineHltMonitor = cms.vstring( 'AlCa_EcalEta_v3',
    'AlCa_EcalPhiSym_v2',
    'AlCa_EcalPi0_v4',
    'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2',
    'HLT_BeamGas_BSC_v2',
    'HLT_BeamGas_HF_v2',
    'HLT_BeamHalo_v2',
    'HLT_DTErrors_v1',
    'HLT_DoubleMu3_v3',
    'HLT_Ele8_v2',
    'HLT_GlobalRunHPDNoise_v2',
    'HLT_HcalNZS_v3',
    'HLT_HcalPhiSym_v3',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_Jet20_v1',
    'HLT_Jet40_v1',
    'HLT_Jet60_v1',
    'HLT_L1BscMinBiasORBptxPlusANDMinus_v1',
    'HLT_L1DoubleForJet32_EtaOpp_v1',
    'HLT_L1DoubleForJet8_EtaOpp_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L1SingleEG12_v1',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMuOpen_AntiBPTX_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1Tech_HBHEHO_totalOR_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_LogMonitor_v1',
    'HLT_Mu0_v3',
    'HLT_Mu3_v3',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1',
    'HLT_Mu5_v3',
    'HLT_Photon10_CaloIdVL_v1',
    'HLT_Photon15_CaloIdVL_v1',
    'HLT_PixelTracks_Multiplicity50_Loose',
    'HLT_PixelTracks_Multiplicity60_Loose',
    'HLT_PixelTracks_Multiplicity70_Loose',
    'HLT_Random_v1',
    'HLT_RegionalCosmicTracking_v1',
    'HLT_ZeroBiasPixel_SingleTrack_v1',
    'HLT_ZeroBias_v1' ),
  OnlineHltResults = cms.vstring( 'HLTriggerFinalPath' ),
  OnlineMonitor = cms.vstring( 'HLT_BeamGas_BSC_v2',
    'HLT_BeamGas_HF_v2',
    'HLT_BeamHalo_v2',
    'HLT_Calibration_v1',
    'HLT_DTErrors_v1',
    'HLT_DoubleMu3_v3',
    'HLT_EcalCalibration_v1',
    'HLT_Ele8_v2',
    'HLT_GlobalRunHPDNoise_v2',
    'HLT_HcalCalibration_v1',
    'HLT_HcalNZS_v3',
    'HLT_HcalPhiSym_v3',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_Jet20_v1',
    'HLT_Jet40_v1',
    'HLT_Jet60_v1',
    'HLT_L1BscMinBiasORBptxPlusANDMinus_v1',
    'HLT_L1DoubleForJet32_EtaOpp_v1',
    'HLT_L1DoubleForJet8_EtaOpp_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L1SingleEG12_v1',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMuOpen_AntiBPTX_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1Tech_HBHEHO_totalOR_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_LogMonitor_v1',
    'HLT_Mu0_v3',
    'HLT_Mu3_v3',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1',
    'HLT_Mu5_v3',
    'HLT_Photon10_CaloIdVL_v1',
    'HLT_Photon15_CaloIdVL_v1',
    'HLT_PixelTracks_Multiplicity50_Loose',
    'HLT_PixelTracks_Multiplicity60_Loose',
    'HLT_PixelTracks_Multiplicity70_Loose',
    'HLT_Random_v1',
    'HLT_RegionalCosmicTracking_v1',
    'HLT_TrackerCalibration_v1',
    'HLT_ZeroBiasPixel_SingleTrack_v1',
    'HLT_ZeroBias_v1' ),
  RPCMonitor = cms.vstring( 'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2' ),
  TestEnables = cms.vstring( 'HLT_Calibration_v1',
    'HLT_HcalCalibration_v1',
    'HLT_TrackerCalibration_v1' )
)

process.source = cms.Source( "DaqSource",
  evtsPerLS = cms.untracked.uint32( 0 ),
  writeStatusFile = cms.untracked.bool( False ),
  processingMode = cms.untracked.string( "defaultMode" ),
  readerPluginName = cms.untracked.string( "FUShmReader" ),
  readerPset = cms.untracked.PSet(

  )
)

process.GlobalTag = cms.ESSource( "PoolDBESSource",
  appendToDataLabel = cms.string( "" ),
  timetype = cms.string( "runnumber" ),
  authenticationMethod = cms.untracked.uint32( 0 ),
  siteLocalConfig = cms.untracked.bool( False ),
  messagelevel = cms.untracked.uint32( 0 ),
  connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG" ),
  label = cms.untracked.string( "" ),
  DumpStat = cms.untracked.bool( False ),
  BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
  globaltag = cms.string( "GR_H_V16::All" ),
  DBParameters = cms.PSet(
    authenticationPath = cms.untracked.string( "." ),
    connectionRetrialTimeOut = cms.untracked.int32( 60 ),
    idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
    messageLevel = cms.untracked.int32( 0 ),
    enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
    enableConnectionSharing = cms.untracked.bool( True ),
    enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
    connectionTimeOut = cms.untracked.int32( 0 ),
    connectionRetrialPeriod = cms.untracked.int32( 10 )
  ),
  toGet = cms.VPSet(

  ),
  RefreshEachRun = cms.untracked.bool( True )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
  pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" ),
  appendToDataLabel = cms.string( "" )
)
process.eegeom = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "EcalMappingRcd" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
  H2Mode = cms.untracked.bool( False ),
  toGet = cms.untracked.vstring( "GainWidths" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESSAK5CaloL2L3 = cms.ESSource( "JetCorrectionServiceChain",
  appendToDataLabel = cms.string( "" ),
  correctors = cms.vstring( "hltESSL2RelativeCorrectionService", "hltESSL3AbsoluteCorrectionService" ),
  label = cms.string( "hltESSAK5CaloL2L3" )
)
process.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "JetTagComputerRecord" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
process.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
process.hltESSL2RelativeCorrectionService = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L2Relative" ),
  algorithm = cms.string( "AK5Calo" ),
  section = cms.string( "" ),
  era = cms.string( "" ),
  useCondDB = cms.untracked.bool( True )
)
process.hltESSL3AbsoluteCorrectionService = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L3Absolute" ),
  algorithm = cms.string( "AK5Calo" ),
  section = cms.string( "" ),
  era = cms.string( "" ),
  useCondDB = cms.untracked.bool( True )
)
process.magfield = cms.ESSource( "XMLIdealGeometryESSource",
  rootNodeName = cms.string( "cmsMagneticField:MAGF" ),
  userControlledNamespace = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" ),
  geomXMLFiles = cms.vstring( "Geometry/CMSCommonData/data/normal/cmsextent.xml", "Geometry/CMSCommonData/data/cms.xml", "Geometry/CMSCommonData/data/cmsMagneticField.xml", "MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml", "MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml" )
)

process.hcal_db_producer = cms.ESProducer( "HcalDbProducer",
  file = cms.untracked.string( "" ),
  appendToDataLabel = cms.string( "" ),
  dump = cms.untracked.vstring(  )
)
process.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPChi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "hltESPChi2EstimatorForRefit" ),
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPChi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator" ),
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPCkf3HitTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPCkf3HitTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPCkf3HitTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( True ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPCkf3HitTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPCkf3HitTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 3 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  )
)
process.hltESPCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPCkfTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( True ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPCkfTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  )
)
process.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPESUnpackerWorker = cms.ESProducer( "ESUnpackerWorkerESProducer",
  ComponentName = cms.string( "hltESPESUnpackerWorker" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet(
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
  ),
  RHAlgo = cms.PSet(
    ESRecoAlgo = cms.int32( 0 ),
    Type = cms.string( "ESRecHitWorker" )
  )
)
process.hltESPEcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  appendToDataLabel = cms.string( "" ),
  esMapping = cms.PSet(
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
  )
)
process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "anyDirection" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer",
  appendToDataLabel = cms.string( "" )
)
process.hltESPHIPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPHIPixelLayerPairs" ),
  layerList = cms.vstring( "BPix1+BPix2", "BPix1+BPix3", "BPix2+BPix3", "BPix1+FPix1_pos", "BPix1+FPix1_neg", "BPix1+FPix2_pos", "BPix1+FPix2_neg", "BPix2+FPix1_pos", "BPix2+FPix1_neg", "BPix2+FPix2_pos", "BPix2+FPix2_neg", "FPix1_pos+FPix2_pos", "FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    hitErrorRZ = cms.double( 0.006 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet(
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(

  )
)
process.hltESPHIPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPHIPixelLayerTriplets" ),
  layerList = cms.vstring( "BPix1+BPix2+BPix3", "BPix1+BPix2+FPix1_pos", "BPix1+BPix2+FPix1_neg", "BPix1+FPix1_pos+FPix2_pos", "BPix1+FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    hitErrorRZ = cms.double( 0.006 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet(
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(

  )
)
process.hltESPHITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPHITTRHBuilderWithoutRefit" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "Fake" ),
  Matcher = cms.string( "Fake" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  HitMatcher = cms.string( "StandardMatcher" ),
  Regional = cms.bool( True ),
  OnDemand = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripModuleQualityDB = cms.bool( True ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  stripClusterProducer = cms.string( "hltSiStripClusters" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  appendToDataLabel = cms.string( "" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  inactiveStripDetectorLabels = cms.VInputTag(  ),
  badStripCuts = cms.PSet(
    TID = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  )
)
process.hltESPMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPMixedLayerPairs" ),
  layerList = cms.vstring( "BPix1+BPix2", "BPix1+BPix3", "BPix2+BPix3", "BPix1+FPix1_pos", "BPix1+FPix1_neg", "BPix1+FPix2_pos", "BPix1+FPix2_neg", "BPix2+FPix1_pos", "BPix2+FPix1_neg", "BPix2+FPix2_pos", "BPix2+FPix2_neg", "FPix1_pos+FPix2_pos", "FPix1_neg+FPix2_neg", "FPix2_pos+TEC1_pos", "FPix2_pos+TEC2_pos", "TEC1_pos+TEC2_pos", "TEC2_pos+TEC3_pos", "FPix2_neg+TEC1_neg", "FPix2_neg+TEC2_neg", "TEC1_neg+TEC2_neg", "TEC2_neg+TEC3_neg" ),
  BPix = cms.PSet(
    hitErrorRZ = cms.double( 0.006 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet(
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  )
)
process.hltESPMuTrackJpsiTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPMuTrackJpsiTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  )
)
process.hltESPMuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  useSeedLayer = cms.bool( False ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  appendToDataLabel = cms.string( "" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( False ),
  alwaysUseInvalidHits = cms.bool( True )
)
process.hltESPMuonCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minimumNumberOfHits = cms.int32( 5 )
  )
)
process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer",
  appendToDataLabel = cms.string( "" )
)
process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  size_cutX = cms.double( 3.0 ),
  size_cutY = cms.double( 3.0 ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  inflate_errors = cms.bool( False ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  IrradiationBiasCorrection = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  TanLorentzAnglePerTesla = cms.double( 0.106 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 )
)
process.hltESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerPairs" ),
  layerList = cms.vstring( "BPix1+BPix2", "BPix1+BPix3", "BPix2+BPix3", "BPix1+FPix1_pos", "BPix1+FPix1_neg", "BPix1+FPix2_pos", "BPix1+FPix2_neg", "BPix2+FPix1_pos", "BPix2+FPix1_neg", "BPix2+FPix2_pos", "BPix2+FPix2_neg", "FPix1_pos+FPix2_pos", "FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    hitErrorRZ = cms.double( 0.006 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet(
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(

  )
)
process.hltESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerTriplets" ),
  layerList = cms.vstring( "BPix1+BPix2+BPix3", "BPix1+BPix2+FPix1_pos", "BPix1+BPix2+FPix1_neg", "BPix1+FPix1_pos+FPix2_pos", "BPix1+FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    hitErrorRZ = cms.double( 0.006 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet(
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(

  )
)
process.hltESPPixelLayerTripletsHITHB = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHB" ),
  layerList = cms.vstring( "BPix1+BPix2+BPix3" ),
  BPix = cms.PSet(
    hitErrorRZ = cms.double( 0.006 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet(
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(

  )
)
process.hltESPPixelLayerTripletsHITHE = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltESPPixelLayerTripletsHITHE" ),
  layerList = cms.vstring( "BPix1+BPix2+FPix1_pos", "BPix1+BPix2+FPix1_neg", "BPix1+FPix1_pos+FPix2_pos", "BPix1+FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    hitErrorRZ = cms.double( 0.006 ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  FPix = cms.PSet(
    hitErrorRZ = cms.double( 0.0036 ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    useErrorsFromParam = cms.bool( True )
  ),
  TEC = cms.PSet(

  )
)
process.hltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  appendToDataLabel = cms.string( "" ),
  impactParameterType = cms.int32( 0 ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  maxImpactParameterSig = cms.double( 999999.0 ),
  trackQualityClass = cms.string( "any" ),
  nthTrack = cms.int32( -1 )
)
process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPSiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
process.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPSmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "hltESPSmartPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  appendToDataLabel = cms.string( "" ),
  distance = cms.double( 0.5 )
)
process.hltESPSoftLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  appendToDataLabel = cms.string( "" ),
  ipSign = cms.string( "any" )
)
process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPStraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
  ComponentName = cms.string( "hltESPStraightLinePropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPTrackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  appendToDataLabel = cms.string( "" ),
  nthTrack = cms.int32( 2 ),
  impactParameterType = cms.int32( 0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  trackQualityClass = cms.string( "any" )
)
process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  trackerGeometryLabel = cms.untracked.string( "" ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPTrajectoryBuilderL3 = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPTrajectoryBuilderL3" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPTrajectoryFilterL3" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  appendToDataLabel = cms.string( "" ),
  fractionShared = cms.double( 0.5 ),
  allowSharedFirstHit = cms.bool( False )
)
process.hltESPTrajectoryFilterL3 = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPTrajectoryFilterL3" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minPt = cms.double( 0.9 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 7 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  )
)
process.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPbJetRegionalTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
  updator = cms.string( "hltESPKFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPbJetRegionalTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minPt = cms.double( 1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    chargeSignificance = cms.double( -1.0 )
  )
)
process.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  appendToDataLabel = cms.string( "" )
)
process.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
process.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer",
  appendToDataLabel = cms.string( "" )
)
process.sistripconn = cms.ESProducer( "SiStripConnectivity" )
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
process.AutoMagneticFieldESProducer = cms.ESProducer( "AutoMagneticFieldESProducer",
  label = cms.untracked.string( "" ),
  valueOverride = cms.int32( -1 ),
  appendToDataLabel = cms.string( "" ),
  nominalCurrents = cms.untracked.vint32( -1, 0, 9558, 14416, 16819, 18268, 19262 ),
  mapLabels = cms.untracked.vstring( "090322_3_8t", "0t", "071212_2t", "071212_3t", "071212_3_5t", "090322_3_8t", "071212_4t" )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  useRealWireGeometry = cms.bool( True ),
  useOnlyWiresInME1a = cms.bool( False ),
  useGangedStripsInME1a = cms.bool( True ),
  useCentreTIOffsets = cms.bool( False ),
  debugV = cms.untracked.bool( False ),
  useDDD = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  appendToDataLabel = cms.string( "" ),
  SelectedCalos = cms.vstring( "HCAL", "ZDC", "EcalBarrel", "EcalEndcap", "EcalPreshower", "TOWER" )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder",
  appendToDataLabel = cms.string( "" )
)
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" ),
  appendToDataLabel = cms.string( "" )
)
process.CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder",
  appendToDataLabel = cms.string( "" )
)
process.EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService",
  appendToDataLabel = cms.string( "" )
)
process.EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
process.EcalUnpackerWorkerESProducer = cms.ESProducer( "EcalUnpackerWorkerESProducer",
  ComponentName = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet(
    tccUnpacking = cms.bool( False ),
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    srpUnpacking = cms.bool( False ),
    syncCheck = cms.bool( False ),
    feIdCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    feUnpacking = cms.bool( True ),
    forceKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
  ),
  ElectronicsMapper = cms.PSet(
    numbXtalTSamples = cms.uint32( 10 ),
    numbTriggerTSamples = cms.uint32( 1 )
  ),
  UncalibRHAlgo = cms.PSet(
    Type = cms.string( "EcalUncalibRecHitWorkerWeights" )
  ),
  CalibRHAlgo = cms.PSet(
    flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 6, 6, 6, 7, 8 ),
    Type = cms.string( "EcalRecHitWorkerSimple" ),
    killDeadChannels = cms.bool( True ),
    ChannelStatusToBeExcluded = cms.vint32( 10, 11, 12, 13, 14, 78, 142 ),
    laserCorrection = cms.bool( False )
  )
)
process.HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP",
  Exclude = cms.untracked.string( "" ),
  H2Mode = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.MuonNumberingInitialization = cms.ESProducer( "MuonNumberingInitialization",
  appendToDataLabel = cms.string( "" )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  compatibiltyWith11 = cms.untracked.bool( True ),
  useDDD = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  AutomaticNormalization = cms.bool( False ),
  NormalizationFactor = cms.double( 1.0 ),
  printDebug = cms.untracked.bool( False ),
  APVGain = cms.VPSet(
    cms.PSet(
      Record = cms.string( "SiStripApvGainRcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    ),
    cms.PSet(
      Record = cms.string( "SiStripApvGain2Rcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    )
  )
)
process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
  appendToDataLabel = cms.string( "" ),
  PrintDebugOutput = cms.bool( False ),
  ThresholdForReducedGranularity = cms.double( 0.3 ),
  UseEmptyRunInfo = cms.bool( False ),
  ReduceGranularity = cms.bool( False ),
  ListOfRecordToMerge = cms.VPSet(
    cms.PSet(
      record = cms.string( "SiStripDetVOffRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripDetCablingRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripBadChannelRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripBadFiberRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripBadModuleRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "RunInfoRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SlaveField0 = cms.ESProducer( "UniformMagneticFieldESProducer",
  ZFieldInTesla = cms.double( 0.0 ),
  label = cms.untracked.string( "slave_0" ),
  appendToDataLabel = cms.string( "" )
)
process.SlaveField20 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_20" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "2_0T" )
  )
)
process.SlaveField30 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_30" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "3_0T" )
  )
)
process.SlaveField35 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_35" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "3_5T" )
  )
)
process.SlaveField38 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_38" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "3_8T" )
  )
)
process.SlaveField40 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_40" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "4_0T" )
  )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "anyDirection" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.StripCPEfromTrackAngleESProducer = cms.ESProducer( "StripCPEESProducer",
  ComponentName = cms.string( "StripCPEfromTrackAngle" ),
  appendToDataLabel = cms.string( "" ),
  TanDiffusionAngle = cms.double( 0.01 ),
  ThicknessRelativeUncertainty = cms.double( 0.02 ),
  NoiseThreshold = cms.double( 2.3 ),
  MaybeNoiseThreshold = cms.double( 3.5 ),
  UncertaintyScaling = cms.double( 1.42 ),
  MinimumUncertainty = cms.double( 0.01 )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True ),
  fromDDD = cms.bool( False )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  fromDDD = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" ),
  appendToDataLabel = cms.string( "" )
)
process.VBF0 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "0t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_2t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_0" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF20 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_2t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_20" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF30 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_3t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_3t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_30" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF35 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_3_5t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_3_5t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_35" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF38 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "090322_3_8t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_090322_3_8t" ),
  overrideMasterSector = cms.bool( False ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_38" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32( 14100, 14200, 17600, 17800, 17900, 18100, 18300, 18400, 18600, 23100, 23300, 23400, 23600, 23800, 23900, 24100, 28600, 28800, 28900, 29100, 29300, 29400, 29600, 28609, 28809, 28909, 29109, 29309, 29409, 29609, 28610, 28810, 28910, 29110, 29310, 29410, 29610, 28611, 28811, 28911, 29111, 29311, 29411, 29611 ),
  scalingFactors = cms.vdouble( 1.0, 1.0, 0.994, 1.004, 1.004, 1.005, 1.004, 1.004, 0.994, 0.965, 0.958, 0.958, 0.953, 0.958, 0.958, 0.965, 0.918, 0.924, 0.924, 0.906, 0.924, 0.924, 0.918, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991 ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF40 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_4t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_4t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_40" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.XMLFromDBSource = cms.ESProducer( "XMLIdealGeometryESProducer",
  rootDDName = cms.string( "cms:OCMS" ),
  label = cms.string( "Extended" ),
  appendToDataLabel = cms.string( "" )
)
process.ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" ),
  appendToDataLabel = cms.string( "" )
)
process.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
process.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  SeverityLevels = cms.VPSet(
    cms.PSet(
      RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(
      RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( "HcalCellCaloTowerProb" ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(
      RecHitFlags = cms.vstring( "HSCP_R1R2", "HSCP_FracLeader", "HSCP_OuterEnergy", "HSCP_ExpFit", "ADCSaturationBit" ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(
      RecHitFlags = cms.vstring( "HBHEHpdHitMultiplicity", "HBHEPulseShape", "HOBit", "HFDigiTime", "HFInTimeWindow", "HFS8S1Ratio", "ZDCBit", "CalibrationBit", "TimingErrorBit" ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(
      RecHitFlags = cms.vstring( "HFLongShort" ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(
      RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( "HcalCellCaloTowerMask" ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(
      RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( "HcalCellHot" ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(
      RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( "HcalCellOff", "HcalCellDead" ),
      Level = cms.int32( 20 )
    )
  ),
  RecoveredRecHitBits = cms.vstring( "TimingAddedBit", "TimingSubtractedBit" ),
  appendToDataLabel = cms.string( "" ),
  DropChannelStatusBits = cms.vstring( "HcalCellMask", "HcalCellOff", "HcalCellDead" )
)

process.DQM = cms.Service( "DQM" )
process.DQMStore = cms.Service( "DQMStore",
  verbose = cms.untracked.int32( 0 ),
  verboseQT = cms.untracked.int32( 0 ),
  collateHistograms = cms.untracked.bool( False ),
  referenceFileName = cms.untracked.string( "" )
)
process.DTDataIntegrityTask = cms.Service( "DTDataIntegrityTask",
  getSCInfo = cms.untracked.bool( True ),
  fedIntegrityFolder = cms.untracked.string( "DT/FEDIntegrity_EvF" ),
  processingMode = cms.untracked.string( "HLT" )
)
process.FUShmDQMOutputService = cms.Service( "FUShmDQMOutputService",
  initialMessageBufferSize = cms.untracked.int32( 1000000 ),
  lumiSectionsPerUpdate = cms.double( 1.0 ),
  useCompression = cms.bool( True ),
  compressionLevel = cms.int32( 1 ),
  lumiSectionInterval = cms.untracked.int32( 0 )
)
process.MessageLogger = cms.Service( "MessageLogger",
  destinations = cms.untracked.vstring( "warnings", "errors", "infos", "debugs", "cout", "cerr" ),
  categories = cms.untracked.vstring( "FwkJob", "FwkReport", "FwkSummary", "Root_NoDictionary" ),
  statistics = cms.untracked.vstring( "cerr" ),
  cerr = cms.untracked.PSet(
    INFO = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    noTimeStamps = cms.untracked.bool( False ),
    FwkReport = cms.untracked.PSet(
      reportEvery = cms.untracked.int32( 1 ),
      limit = cms.untracked.int32( 0 )
    ),
    default = cms.untracked.PSet(
      limit = cms.untracked.int32( 10000000 )
    ),
    Root_NoDictionary = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    FwkJob = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    FwkSummary = cms.untracked.PSet(
      reportEvery = cms.untracked.int32( 1 ),
      limit = cms.untracked.int32( 10000000 )
    ),
    threshold = cms.untracked.string( "INFO" )
  ),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string( "ERROR" )
  ),
  errors = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True )
  ),
  warnings = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True )
  ),
  infos = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    Root_NoDictionary = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    placeholder = cms.untracked.bool( True )
  ),
  debugs = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True )
  ),
  default = cms.untracked.PSet(

  ),
  fwkJobReports = cms.untracked.vstring( "FrameworkJobReport" ),
  FrameworkJobReport = cms.untracked.PSet(
    default = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    FwkJob = cms.untracked.PSet(
      limit = cms.untracked.int32( 10000000 )
    )
  ),
  debugModules = cms.untracked.vstring(  ),
  suppressDebug = cms.untracked.vstring(  ),
  suppressInfo = cms.untracked.vstring(  ),
  suppressWarning = cms.untracked.vstring( "hltOnlineBeamSpot", "hltPixelTracksForMinBias", "hltPixelTracksForHighMult", "hltHITPixelTracksHE", "hltHITPixelTracksHB", "hltSiPixelClusters", "hltPixelTracks" ),
  threshold = cms.untracked.string( "INFO" )
)
process.MicroStateService = cms.Service( "MicroStateService" )
process.ModuleWebRegistry = cms.Service( "ModuleWebRegistry" )
process.PrescaleService = cms.Service( "PrescaleService",
  lvl1DefaultLabel = cms.untracked.string( "7E31" ),
  lvl1Labels = cms.vstring( "8E30", "4E30", "2E30", "1E30", "5E29" ),
  prescaleTable = cms.VPSet(
    cms.PSet(
      pathName = cms.string( "HLTDQMResultsOutput" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLTMONOutput" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 100 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_GlobalRunHPDNoise_v2" ),
      prescales = cms.vuint32( 120, 60, 30, 15, 8 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Jet20_v1" ),
      prescales = cms.vuint32( 10, 5, 2, 1, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Jet40_v1" ),
      prescales = cms.vuint32( 5, 2, 1, 1, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleEG12_v1" ),
      prescales = cms.vuint32( 200, 100, 50, 25, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleEG5_v1" ),
      prescales = cms.vuint32( 2400, 1200, 600, 300, 150 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleJet36_v1" ),
      prescales = cms.vuint32( 400, 200, 100, 50, 25 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleMuOpen_AntiBPTX_v1" ),
      prescales = cms.vuint32( 6, 12, 25, 50, 50 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleMuOpen_DT_v1" ),
      prescales = cms.vuint32( 16, 8, 4, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleMuOpen_v1" ),
      prescales = cms.vuint32( 160, 80, 40, 20, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_BSC_halo_v1" ),
      prescales = cms.vuint32( 10, 4, 2, 1, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L3MuonsCosmicTracking_v1" ),
      prescales = cms.vuint32( 0, 0, 0, 0, 0 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu0_v3" ),
      prescales = cms.vuint32( 6, 2, 1, 1, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu3_v3" ),
      prescales = cms.vuint32( 3, 1, 1, 1, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Photon10_CaloIdVL_v1" ),
      prescales = cms.vuint32( 12, 6, 3, 1, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Physics_NanoDST_v1" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_PixelTracks_Multiplicity50_Loose" ),
      prescales = cms.vuint32( 50, 20, 10, 5, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_PixelTracks_Multiplicity60_Loose" ),
      prescales = cms.vuint32( 5, 2, 1, 1, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Random_v1" ),
      prescales = cms.vuint32( 6000, 6000, 6000, 6000, 6000 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_RegionalCosmicTracking_v1" ),
      prescales = cms.vuint32( 0, 0, 0, 0, 0 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_ZeroBias_v1" ),
      prescales = cms.vuint32( 4, 4, 4, 4, 4 )
    )
  )
)
process.UpdaterService = cms.Service( "UpdaterService" )

process.hlt1HighMult50 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
  vertexCollection = cms.InputTag( "hltPixelVerticesForHighMultLoose" ),
  trackCollection = cms.InputTag( "hltPixelCandsForHighMultLoose" ),
  MinPt = cms.double( 0.4 ),
  MaxPt = cms.double( 10000.0 ),
  MaxEta = cms.double( 2.4 ),
  MaxVz = cms.double( 15.0 ),
  MinTrks = cms.int32( 50 ),
  MinSep = cms.double( 0.12 )
)
process.hlt1HighMult60 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
  vertexCollection = cms.InputTag( "hltPixelVerticesForHighMultLoose" ),
  trackCollection = cms.InputTag( "hltPixelCandsForHighMultLoose" ),
  MinPt = cms.double( 0.4 ),
  MaxPt = cms.double( 10000.0 ),
  MaxEta = cms.double( 2.4 ),
  MaxVz = cms.double( 15.0 ),
  MinTrks = cms.int32( 60 ),
  MinSep = cms.double( 0.12 )
)
process.hlt1HighMult70 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
  vertexCollection = cms.InputTag( "hltPixelVerticesForHighMultLoose" ),
  trackCollection = cms.InputTag( "hltPixelCandsForHighMultLoose" ),
  MinPt = cms.double( 0.4 ),
  MaxPt = cms.double( 10000.0 ),
  MaxEta = cms.double( 2.4 ),
  MaxVz = cms.double( 15.0 ),
  MinTrks = cms.int32( 70 ),
  MinSep = cms.double( 0.12 )
)
process.hltAlCaEtaRecHitsFilter = cms.HLTFilter( "HLTEcalResonanceFilter",
  barrelHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEB" ),
  barrelClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersBarrel" ),
  endcapHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEE" ),
  endcapClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersEndcap" ),
  doSelBarrel = cms.bool( True ),
  doSelEndcap = cms.bool( True ),
  useRecoFlag = cms.bool( False ),
  flagLevelRecHitsToUse = cms.int32( 1 ),
  useDBStatus = cms.bool( True ),
  statusLevelRecHitsToUse = cms.int32( 1 ),
  preshRecHitProducer = cms.InputTag( "hltESRegionalPi0EtaRecHit:EcalRecHitsES" ),
  storeRecHitES = cms.bool( True ),
  debugLevel = cms.int32( 0 ),
  barrelSelection = cms.PSet(
    massLowPi0Cand = cms.double( 0.084 ),
    seleIso = cms.double( 0.5 ),
    seleMinvMaxBarrel = cms.double( 0.8 ),
    selePtPair = cms.double( 4.0 ),
    seleMinvMinBarrel = cms.double( 0.3 ),
    seleS4S9Gamma = cms.double( 0.87 ),
    seleS9S25Gamma = cms.double( 0.8 ),
    selePtGamma = cms.double( 1.2 ),
    seleBeltDR = cms.double( 0.3 ),
    ptMinForIsolation = cms.double( 0.5 ),
    store5x5RecHitEB = cms.bool( True ),
    seleBeltDeta = cms.double( 0.1 ),
    removePi0CandidatesForEta = cms.bool( True ),
    barrelHitCollection = cms.string( "etaEcalRecHitsEB" ),
    massHighPi0Cand = cms.double( 0.156 )
  ),
  endcapSelection = cms.PSet(
    selePtGammaEndCap_region1 = cms.double( 1.0 ),
    selePtGammaEndCap_region3 = cms.double( 0.7 ),
    selePtGammaEndCap_region2 = cms.double( 1.0 ),
    region1_EndCap = cms.double( 2.0 ),
    seleS9S25GammaEndCap = cms.double( 0.85 ),
    selePtPairMaxEndCap_region3 = cms.double( 9999.0 ),
    seleMinvMinEndCap = cms.double( 0.2 ),
    seleS4S9GammaEndCap = cms.double( 0.9 ),
    seleMinvMaxEndCap = cms.double( 0.9 ),
    selePtPairEndCap_region1 = cms.double( 3.0 ),
    seleBeltDREndCap = cms.double( 0.3 ),
    selePtPairEndCap_region3 = cms.double( 3.0 ),
    selePtPairEndCap_region2 = cms.double( 3.0 ),
    seleIsoEndCap = cms.double( 0.5 ),
    ptMinForIsolationEndCap = cms.double( 0.5 ),
    endcapHitCollection = cms.string( "etaEcalRecHitsEE" ),
    region2_EndCap = cms.double( 2.5 ),
    seleBeltDetaEndCap = cms.double( 0.1 ),
    store5x5RecHitEE = cms.bool( True )
  ),
  preshowerSelection = cms.PSet(
    preshCalibGamma = cms.double( 0.024 ),
    preshStripEnergyCut = cms.double( 0.0 ),
    debugLevelES = cms.string( "" ),
    preshCalibPlaneY = cms.double( 0.7 ),
    preshCalibPlaneX = cms.double( 1.0 ),
    preshCalibMIP = cms.double( 9.0e-05 ),
    ESCollection = cms.string( "etaEcalRecHitsES" ),
    preshNclust = cms.int32( 4 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 )
  )
)
process.hltAlCaPhiSymStream = cms.HLTFilter( "HLTEcalPhiSymFilter",
  barrelHitCollection = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEB" ),
  endcapHitCollection = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEE" ),
  phiSymBarrelHitCollection = cms.string( "phiSymEcalRecHitsEB" ),
  phiSymEndcapHitCollection = cms.string( "phiSymEcalRecHitsEE" ),
  eCut_barrel = cms.double( 0.15 ),
  eCut_endcap = cms.double( 0.75 ),
  eCut_barrel_high = cms.double( 999999.0 ),
  eCut_endcap_high = cms.double( 999999.0 ),
  statusThreshold = cms.uint32( 3 ),
  useRecoFlag = cms.bool( False )
)
process.hltAlCaPi0RecHitsFilter = cms.HLTFilter( "HLTEcalResonanceFilter",
  barrelHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEB" ),
  barrelClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersBarrel" ),
  endcapHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEE" ),
  endcapClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersEndcap" ),
  doSelBarrel = cms.bool( True ),
  doSelEndcap = cms.bool( True ),
  useRecoFlag = cms.bool( False ),
  flagLevelRecHitsToUse = cms.int32( 1 ),
  useDBStatus = cms.bool( True ),
  statusLevelRecHitsToUse = cms.int32( 1 ),
  preshRecHitProducer = cms.InputTag( "hltESRegionalPi0EtaRecHit:EcalRecHitsES" ),
  storeRecHitES = cms.bool( True ),
  debugLevel = cms.int32( 0 ),
  barrelSelection = cms.PSet(
    massLowPi0Cand = cms.double( 0.084 ),
    seleIso = cms.double( 0.5 ),
    seleMinvMaxBarrel = cms.double( 0.23 ),
    selePtPair = cms.double( 2.6 ),
    seleMinvMinBarrel = cms.double( 0.04 ),
    seleS4S9Gamma = cms.double( 0.83 ),
    seleS9S25Gamma = cms.double( 0.0 ),
    selePtGamma = cms.double( 1.3 ),
    seleBeltDR = cms.double( 0.2 ),
    ptMinForIsolation = cms.double( 0.5 ),
    store5x5RecHitEB = cms.bool( False ),
    seleBeltDeta = cms.double( 0.05 ),
    removePi0CandidatesForEta = cms.bool( False ),
    barrelHitCollection = cms.string( "pi0EcalRecHitsEB" ),
    massHighPi0Cand = cms.double( 0.156 )
  ),
  endcapSelection = cms.PSet(
    selePtGammaEndCap_region1 = cms.double( 0.6 ),
    selePtGammaEndCap_region3 = cms.double( 0.5 ),
    selePtGammaEndCap_region2 = cms.double( 0.6 ),
    region1_EndCap = cms.double( 2.0 ),
    seleS9S25GammaEndCap = cms.double( 0.0 ),
    selePtPairMaxEndCap_region3 = cms.double( 2.5 ),
    seleMinvMinEndCap = cms.double( 0.05 ),
    seleS4S9GammaEndCap = cms.double( 0.9 ),
    seleMinvMaxEndCap = cms.double( 0.3 ),
    selePtPairEndCap_region1 = cms.double( 2.5 ),
    seleBeltDREndCap = cms.double( 0.2 ),
    selePtPairEndCap_region3 = cms.double( 1.0 ),
    selePtPairEndCap_region2 = cms.double( 2.5 ),
    seleIsoEndCap = cms.double( 0.5 ),
    ptMinForIsolationEndCap = cms.double( 0.5 ),
    endcapHitCollection = cms.string( "pi0EcalRecHitsEE" ),
    region2_EndCap = cms.double( 2.5 ),
    seleBeltDetaEndCap = cms.double( 0.05 ),
    store5x5RecHitEE = cms.bool( False )
  ),
  preshowerSelection = cms.PSet(
    preshCalibGamma = cms.double( 0.024 ),
    preshStripEnergyCut = cms.double( 0.0 ),
    debugLevelES = cms.string( "" ),
    preshCalibPlaneY = cms.double( 0.7 ),
    preshCalibPlaneX = cms.double( 1.0 ),
    preshCalibMIP = cms.double( 9.0e-05 ),
    ESCollection = cms.string( "pi0EcalRecHitsES" ),
    preshNclust = cms.int32( 4 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 )
  )
)
process.hltAntiKT5CaloJets = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "AntiKt" ),
  rParam = cms.double( 0.5 ),
  src = cms.InputTag( "hltTowerMakerForAll" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" ),
  sumRecHits = cms.bool( False )
)
process.hltAntiKT5CaloJetsRegional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "AntiKt" ),
  rParam = cms.double( 0.5 ),
  src = cms.InputTag( "hltTowerMakerForJets" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" ),
  sumRecHits = cms.bool( False )
)
process.hltAntiKT5L2L3CorrCaloJets = cms.EDProducer( "CaloJetCorrectionProducer",
  src = cms.InputTag( "hltAntiKT5CaloJets" ),
  verbose = cms.untracked.bool( False ),
  alias = cms.untracked.string( "JetCorJetAntiKT5" ),
  correctors = cms.vstring( "hltESSAK5CaloL2L3" )
)
process.hltAntiKT5L2L3CorrCaloJetsRegional = cms.EDProducer( "CaloJetCorrectionProducer",
  src = cms.InputTag( "hltAntiKT5CaloJetsRegional" ),
  verbose = cms.untracked.bool( False ),
  alias = cms.untracked.string( "JetCorJetAntiKT5" ),
  correctors = cms.vstring( "hltESSAK5CaloL2L3" )
)
process.hltBPTXAntiCoincidence = cms.HLTFilter( "HLTLevel1Activity",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  daqPartitions = cms.uint32( 1 ),
  ignoreL1Mask = cms.bool( True ),
  invert = cms.bool( True ),
  physicsLoBits = cms.uint64( 0x0000000000000001 ),
  physicsHiBits = cms.uint64( 0x0000000000000000 ),
  technicalBits = cms.uint64( 0x0000000000000011 ),
  bunchCrossings = cms.vint32( 0, 1, -1 )
)
process.hltBPTXCoincidence = cms.HLTFilter( "HLTLevel1Activity",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  daqPartitions = cms.uint32( 1 ),
  ignoreL1Mask = cms.bool( True ),
  invert = cms.bool( False ),
  physicsLoBits = cms.uint64( 0x0000000000000001 ),
  physicsHiBits = cms.uint64( 0x0000000000000000 ),
  technicalBits = cms.uint64( 0x000000000000007f ),
  bunchCrossings = cms.vint32( 0, -1, 1 )
)
process.hltBoolEnd = cms.HLTFilter( "HLTBool",
  result = cms.bool( True )
)
process.hltBoolTrue = cms.HLTFilter( "HLTBool",
  result = cms.bool( True )
)
process.hltCalibrationEventsFilter = cms.HLTFilter( "HLTTriggerTypeFilter",
  SelectedTriggerType = cms.int32( 2 )
)
process.hltCorrectedHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1Isolated" ),
  superClusterAlgo = cms.string( "Hybrid" ),
  applyEnergyCorrection = cms.bool( True ),
  applyCrackCorrection = cms.bool( False ),
  sigmaElectronicNoise = cms.double( 0.03 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 1.1 ),
    fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -0.0005735, 1.343 ),
    brLinearHighThr = cms.double( 8.0 ),
    fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 )
  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(

  )
)
process.hltCorrectedHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
  L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolatedTemp" ),
  L1IsoSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
  L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedHybridSuperClustersL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1NonIsolated" ),
  superClusterAlgo = cms.string( "Hybrid" ),
  applyEnergyCorrection = cms.bool( True ),
  applyCrackCorrection = cms.bool( False ),
  sigmaElectronicNoise = cms.double( 0.03 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 1.1 ),
    fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -0.0005735, 1.343 ),
    brLinearHighThr = cms.double( 8.0 ),
    fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 )
  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(

  )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  superClusterAlgo = cms.string( "Multi5x5" ),
  applyEnergyCorrection = cms.bool( True ),
  applyCrackCorrection = cms.bool( False ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(

  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 0.6 ),
    fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 ),
    brLinearHighThr = cms.double( 6.0 ),
    fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 )
  )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
  L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp" ),
  L1IsoSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
  superClusterAlgo = cms.string( "Multi5x5" ),
  applyEnergyCorrection = cms.bool( True ),
  applyCrackCorrection = cms.bool( False ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(

  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 0.6 ),
    fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 ),
    brLinearHighThr = cms.double( 6.0 ),
    fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 )
  )
)
process.hltCosmicTrackSelector = cms.EDProducer( "CosmicTrackSelector",
  src = cms.InputTag( "hltRegionalCosmicTracks" ),
  beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
  copyExtras = cms.untracked.bool( False ),
  copyTrajectories = cms.untracked.bool( False ),
  keepAllTracks = cms.bool( False ),
  chi2n_par = cms.double( 10.0 ),
  max_d0 = cms.double( 999.0 ),
  max_z0 = cms.double( 999.0 ),
  min_pt = cms.double( 5.0 ),
  max_eta = cms.double( 2.0 ),
  min_nHit = cms.uint32( 6 ),
  min_nPixelHit = cms.uint32( 0 ),
  minNumberLayers = cms.uint32( 0 ),
  minNumber3DLayers = cms.uint32( 0 ),
  maxNumberLostLayers = cms.uint32( 999 ),
  qualityBit = cms.string( "" )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
  CSCUseCalibrations = cms.bool( True ),
  CSCUseStaticPedestals = cms.bool( False ),
  CSCUseTimingCorrections = cms.bool( True ),
  stripDigiTag = cms.InputTag( "hltMuonCSCDigis:MuonCSCStripDigi" ),
  wireDigiTag = cms.InputTag( "hltMuonCSCDigis:MuonCSCWireDigi" ),
  CSCstripWireDeltaTime = cms.int32( 8 ),
  CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
  CSCStripPeakThreshold = cms.double( 10.0 ),
  CSCStripClusterChargeCut = cms.double( 25.0 ),
  CSCWireClusterDeltaT = cms.int32( 1 ),
  CSCStripxtalksOffset = cms.double( 0.03 ),
  NoiseLevel_ME1a = cms.double( 7.0 ),
  XTasymmetry_ME1a = cms.double( 0.0 ),
  ConstSyst_ME1a = cms.double( 0.022 ),
  NoiseLevel_ME1b = cms.double( 8.0 ),
  XTasymmetry_ME1b = cms.double( 0.0 ),
  ConstSyst_ME1b = cms.double( 0.007 ),
  NoiseLevel_ME12 = cms.double( 9.0 ),
  XTasymmetry_ME12 = cms.double( 0.0 ),
  ConstSyst_ME12 = cms.double( 0.0 ),
  NoiseLevel_ME13 = cms.double( 8.0 ),
  XTasymmetry_ME13 = cms.double( 0.0 ),
  ConstSyst_ME13 = cms.double( 0.0 ),
  NoiseLevel_ME21 = cms.double( 9.0 ),
  XTasymmetry_ME21 = cms.double( 0.0 ),
  ConstSyst_ME21 = cms.double( 0.0 ),
  NoiseLevel_ME22 = cms.double( 9.0 ),
  XTasymmetry_ME22 = cms.double( 0.0 ),
  ConstSyst_ME22 = cms.double( 0.0 ),
  NoiseLevel_ME31 = cms.double( 9.0 ),
  XTasymmetry_ME31 = cms.double( 0.0 ),
  ConstSyst_ME31 = cms.double( 0.0 ),
  NoiseLevel_ME32 = cms.double( 9.0 ),
  XTasymmetry_ME32 = cms.double( 0.0 ),
  ConstSyst_ME32 = cms.double( 0.0 ),
  NoiseLevel_ME41 = cms.double( 9.0 ),
  XTasymmetry_ME41 = cms.double( 0.0 ),
  ConstSyst_ME41 = cms.double( 0.0 ),
  readBadChannels = cms.bool( True ),
  readBadChambers = cms.bool( True ),
  UseAverageTime = cms.bool( False ),
  UseParabolaFit = cms.bool( False ),
  UseFivePoleFit = cms.bool( True )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
  inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
  algo_type = cms.int32( 1 ),
  algo_psets = cms.VPSet(
    cms.PSet(
      chamber_types = cms.vstring( "ME1/a", "ME1/b", "ME1/2", "ME1/3", "ME2/1", "ME2/2", "ME3/1", "ME3/2", "ME4/1", "ME4/2" ),
      algo_name = cms.string( "CSCSegAlgoST" ),
      parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
      algo_psets = cms.VPSet(
        cms.PSet(
          maxRatioResidualPrune = cms.double( 3.0 ),
          yweightPenalty = cms.double( 1.5 ),
          maxRecHitsInCluster = cms.int32( 20 ),
          dPhiFineMax = cms.double( 0.025 ),
          preClusteringUseChaining = cms.bool( True ),
          ForceCovariance = cms.bool( False ),
          hitDropLimit6Hits = cms.double( 0.3333 ),
          NormChi2Cut2D = cms.double( 20.0 ),
          BPMinImprovement = cms.double( 10000.0 ),
          Covariance = cms.double( 0.0 ),
          tanPhiMax = cms.double( 0.5 ),
          SeedBig = cms.double( 0.0015 ),
          onlyBestSegment = cms.bool( False ),
          dRPhiFineMax = cms.double( 8.0 ),
          SeedSmall = cms.double( 0.0002 ),
          curvePenalty = cms.double( 2.0 ),
          dXclusBoxMax = cms.double( 4.0 ),
          BrutePruning = cms.bool( True ),
          curvePenaltyThreshold = cms.double( 0.85 ),
          CorrectTheErrors = cms.bool( True ),
          hitDropLimit4Hits = cms.double( 0.6 ),
          useShowering = cms.bool( False ),
          CSCDebug = cms.untracked.bool( False ),
          tanThetaMax = cms.double( 1.2 ),
          NormChi2Cut3D = cms.double( 10.0 ),
          minHitsPerSegment = cms.int32( 3 ),
          ForceCovarianceAll = cms.bool( False ),
          yweightPenaltyThreshold = cms.double( 1.0 ),
          prePrunLimit = cms.double( 3.17 ),
          hitDropLimit5Hits = cms.double( 0.8 ),
          preClustering = cms.bool( True ),
          prePrun = cms.bool( True ),
          maxDPhi = cms.double( 999.0 ),
          maxDTheta = cms.double( 999.0 ),
          Pruning = cms.bool( True ),
          dYclusBoxMax = cms.double( 8.0 )
        ),
        cms.PSet(
          maxRatioResidualPrune = cms.double( 3.0 ),
          yweightPenalty = cms.double( 1.5 ),
          maxRecHitsInCluster = cms.int32( 24 ),
          dPhiFineMax = cms.double( 0.025 ),
          preClusteringUseChaining = cms.bool( True ),
          ForceCovariance = cms.bool( False ),
          hitDropLimit6Hits = cms.double( 0.3333 ),
          NormChi2Cut2D = cms.double( 20.0 ),
          BPMinImprovement = cms.double( 10000.0 ),
          Covariance = cms.double( 0.0 ),
          tanPhiMax = cms.double( 0.5 ),
          SeedBig = cms.double( 0.0015 ),
          onlyBestSegment = cms.bool( False ),
          dRPhiFineMax = cms.double( 8.0 ),
          SeedSmall = cms.double( 0.0002 ),
          curvePenalty = cms.double( 2.0 ),
          dXclusBoxMax = cms.double( 4.0 ),
          BrutePruning = cms.bool( True ),
          curvePenaltyThreshold = cms.double( 0.85 ),
          CorrectTheErrors = cms.bool( True ),
          hitDropLimit4Hits = cms.double( 0.6 ),
          useShowering = cms.bool( False ),
          CSCDebug = cms.untracked.bool( False ),
          tanThetaMax = cms.double( 1.2 ),
          NormChi2Cut3D = cms.double( 10.0 ),
          minHitsPerSegment = cms.int32( 3 ),
          ForceCovarianceAll = cms.bool( False ),
          yweightPenaltyThreshold = cms.double( 1.0 ),
          prePrunLimit = cms.double( 3.17 ),
          hitDropLimit5Hits = cms.double( 0.8 ),
          preClustering = cms.bool( True ),
          prePrun = cms.bool( True ),
          maxDPhi = cms.double( 999.0 ),
          maxDTheta = cms.double( 999.0 ),
          Pruning = cms.bool( True ),
          dYclusBoxMax = cms.double( 8.0 )
        )
      )
    )
  )
)
process.hltDQMHLTScalers = cms.EDAnalyzer( "HLTScalers",
  dqmFolder = cms.untracked.string( "HLT/HLTScalers_EvF" ),
  triggerResults = cms.InputTag( "TriggerResults::HLT" ),
  MonitorDaemon = cms.untracked.bool( False )
)
process.hltDQML1Scalers = cms.EDAnalyzer( "L1Scalers",
  verbose = cms.untracked.bool( False ),
  l1GtData = cms.InputTag( "hltGtDigis" ),
  denomIsTech = cms.untracked.bool( True ),
  denomBit = cms.untracked.uint32( 40 ),
  tfIsTech = cms.untracked.bool( True ),
  tfBit = cms.untracked.uint32( 41 ),
  dqmFolder = cms.untracked.string( "L1T/L1Scalers_EvF" ),
  firstFED = cms.untracked.uint32( 0 ),
  lastFED = cms.untracked.uint32( 931 ),
  fedRawData = cms.InputTag( "source" ),
  HFRecHitCollection = cms.InputTag( "hltHfreco" ),
  algoMonitorBits = cms.untracked.vuint32(  ),
  techMonitorBits = cms.untracked.vuint32(  ),
  maskedChannels = cms.untracked.vint32( 8137, 8141, 8146, 8149, 8150, 8153 )
)
process.hltDQML1SeedLogicScalers = cms.EDAnalyzer( "HLTSeedL1LogicScalers",
  l1BeforeMask = cms.bool( False ),
  processname = cms.string( "HLT" ),
  L1GtDaqReadoutRecordInputTag = cms.InputTag( "hltGtDigis" ),
  L1GtRecordInputTag = cms.InputTag( "unused" ),
  DQMFolder = cms.untracked.string( "HLT/HLTSeedL1LogicScalers_EvF" ),
  monitorPaths = cms.untracked.vstring( "HLT_L1MuOpen", "HLT_L1Mu", "HLT_Mu3", "HLT_L1SingleForJet", "HLT_SingleLooseIsoTau20", "HLT_MinBiasEcal" )
)
process.hltDTROMonitorFilter = cms.HLTFilter( "HLTDTROMonitorFilter",
  inputLabel = cms.InputTag( "source" )
)
process.hltDiMuonL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 2 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltDiMuonL2PreFiltered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 2 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
  MinN = cms.int32( 2 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
  debug = cms.untracked.bool( False ),
  dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
  recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
  recAlgoConfig = cms.PSet(
    minTime = cms.double( -3.0 ),
    debug = cms.untracked.bool( False ),
    tTrigModeConfig = cms.PSet(
      vPropWire = cms.double( 24.4 ),
      doTOFCorrection = cms.bool( True ),
      tofCorrType = cms.int32( 0 ),
      wirePropCorrType = cms.int32( 0 ),
      tTrigLabel = cms.string( "" ),
      doWirePropCorrection = cms.bool( True ),
      doT0Correction = cms.bool( True ),
      debug = cms.untracked.bool( False )
    ),
    maxTime = cms.double( 420.0 ),
    tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
    stepTwoFromDigi = cms.bool( False ),
    doVdriftCorr = cms.bool( False )
  )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
  debug = cms.untracked.bool( False ),
  recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
  recHits2DLabel = cms.InputTag( "dt2DSegments" ),
  Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
  Reco4DAlgoConfig = cms.PSet(
    segmCleanerMode = cms.int32( 2 ),
    Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
    recAlgoConfig = cms.PSet(
      minTime = cms.double( -3.0 ),
      debug = cms.untracked.bool( False ),
      tTrigModeConfig = cms.PSet(
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False )
      ),
      maxTime = cms.double( 420.0 ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( False )
    ),
    nSharedHitsMax = cms.int32( 2 ),
    hit_afterT0_resolution = cms.double( 0.03 ),
    Reco2DAlgoConfig = cms.PSet(
      segmCleanerMode = cms.int32( 2 ),
      recAlgoConfig = cms.PSet(
        minTime = cms.double( -3.0 ),
        debug = cms.untracked.bool( False ),
        tTrigModeConfig = cms.PSet(
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False )
        ),
        maxTime = cms.double( 420.0 ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( False )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      AlphaMaxPhi = cms.double( 1.0 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      MaxAllowedHits = cms.uint32( 50 ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      AlphaMaxTheta = cms.double( 0.9 ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      performT0SegCorrection = cms.bool( False )
    ),
    performT0_vdriftSegCorrection = cms.bool( False ),
    debug = cms.untracked.bool( False ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
    nUnSharedHitsMin = cms.int32( 2 ),
    AllDTRecHits = cms.bool( True ),
    performT0SegCorrection = cms.bool( False )
  )
)
process.hltDynAlCaDTErrors = cms.HLTFilter( "HLTDynamicPrescaler" )
process.hltEG10EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEGRegionalL1SingleEG5" ),
  etcutEB = cms.double( 10.0 ),
  etcutEE = cms.double( 10.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltEG15EtFilterFromEG5 = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEGRegionalL1SingleEG5" ),
  etcutEB = cms.double( 15.0 ),
  etcutEE = cms.double( 15.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltEG8EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEGRegionalL1SingleEG5" ),
  etcutEB = cms.double( 8.0 ),
  etcutEE = cms.double( 8.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltEGRegionalL1SingleEG5 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG5" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltESRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
  sourceTag = cms.InputTag( "source" ),
  workerName = cms.string( "hltESPESUnpackerWorker" )
)
process.hltESRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalEgammaFEDs:es" ),
  splitOutput = cms.bool( False ),
  EBrechitCollection = cms.string( "" ),
  EErechitCollection = cms.string( "" ),
  rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltESRegionalPi0EtaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalPi0EtaFEDs:es" ),
  splitOutput = cms.bool( False ),
  EBrechitCollection = cms.string( "" ),
  EErechitCollection = cms.string( "" ),
  rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltEcalCalibrationRaw = cms.EDProducer( "EvFFEDSelector",
  inputTag = cms.InputTag( "source" ),
  fedList = cms.vuint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 )
)
process.hltEcalRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
  sourceTag = cms.InputTag( "source" ),
  workerName = cms.string( "" )
)
process.hltEcalRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalRestFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalEgammaFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "egamma" ),
  doES = cms.bool( True ),
  sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(
    cms.PSet(
      regionEtaMargin = cms.double( 0.25 ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 5.0 ),
      Source = cms.InputTag( "hltL1extraParticles:Isolated" )
    ),
    cms.PSet(
      regionEtaMargin = cms.double( 0.25 ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 5.0 ),
      Source = cms.InputTag( "hltL1extraParticles:NonIsolated" )
    )
  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalEgammaFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalJetsFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "jet" ),
  doES = cms.bool( False ),
  sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(
    cms.PSet(
      regionEtaMargin = cms.double( 1.0 ),
      regionPhiMargin = cms.double( 1.0 ),
      Ptmin = cms.double( 14.0 ),
      Source = cms.InputTag( "hltL1extraParticles:Central" )
    ),
    cms.PSet(
      regionEtaMargin = cms.double( 1.0 ),
      regionPhiMargin = cms.double( 1.0 ),
      Ptmin = cms.double( 20.0 ),
      Source = cms.InputTag( "hltL1extraParticles:Forward" )
    ),
    cms.PSet(
      regionEtaMargin = cms.double( 1.0 ),
      regionPhiMargin = cms.double( 1.0 ),
      Ptmin = cms.double( 14.0 ),
      Source = cms.InputTag( "hltL1extraParticles:Tau" )
    )
  ),
  EmJobPSet = cms.VPSet(

  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalJetsRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalJetsFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalPi0EtaFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "egamma" ),
  doES = cms.bool( True ),
  sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(
    cms.PSet(
      regionEtaMargin = cms.double( 0.25 ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 2.0 ),
      Source = cms.InputTag( "hltL1extraParticles:Isolated" )
    ),
    cms.PSet(
      regionEtaMargin = cms.double( 0.25 ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 2.0 ),
      Source = cms.InputTag( "hltL1extraParticles:NonIsolated" )
    )
  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalPi0EtaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalPi0EtaFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "" )
)
process.hltEcalRegionalRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "all" ),
  doES = cms.bool( False ),
  sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(

  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEle8HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltEle8R9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltEle8PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltEle8HEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltEle8R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltEG8EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
  inputTag = cms.InputTag( "source" ),
  fedList = cms.vuint32( 1023 )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
  inputLabel = cms.InputTag( "source" ),
  gctFedId = cms.untracked.int32( 745 ),
  hltMode = cms.bool( True ),
  numberOfGctSamplesToUnpack = cms.uint32( 1 ),
  numberOfRctSamplesToUnpack = cms.uint32( 1 ),
  unpackSharedRegions = cms.bool( False ),
  unpackerVersion = cms.uint32( 0 ),
  checkHeaders = cms.untracked.bool( False ),
  verbose = cms.untracked.bool( False )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
  DaqGtInputTag = cms.InputTag( "source" ),
  DaqGtFedId = cms.untracked.int32( 813 ),
  ActiveBoardsMask = cms.uint32( 0x0000ffff ),
  UnpackBxInEvent = cms.int32( 5 ),
  Verbosity = cms.untracked.int32( 0 )
)
process.hltHFAsymmetryFilter = cms.HLTFilter( "HLTHFAsymmetryFilter",
  HFHitCollection = cms.InputTag( "hltHfreco" ),
  ECut_HF = cms.double( 3.0 ),
  OS_Asym_max = cms.double( 0.2 ),
  SS_Asym_min = cms.double( 0.8 )
)
process.hltHITCkfTrackCandidatesHB = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltHITPixelTripletSeedGeneratorHB" ),
  TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltHITCkfTrackCandidatesHE = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltHITPixelTripletSeedGeneratorHE" ),
  TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltHITCtfWithMaterialTracksHB = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltHITCtfWithMaterialTracksHB8E29" ),
  Fitter = cms.string( "hltESPKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltHITCkfTrackCandidatesHB" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltHITCtfWithMaterialTracksHE = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltHITCtfWithMaterialTracksHE8E29" ),
  Fitter = cms.string( "hltESPKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltHITCkfTrackCandidatesHE" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltHITIPTCorrectorHB = cms.EDProducer( "IPTCorrector",
  corTracksLabel = cms.InputTag( "hltHITCtfWithMaterialTracksHB" ),
  filterLabel = cms.InputTag( "hltIsolPixelTrackL2FilterHB" ),
  associationCone = cms.double( 0.2 )
)
process.hltHITIPTCorrectorHE = cms.EDProducer( "IPTCorrector",
  corTracksLabel = cms.InputTag( "hltHITCtfWithMaterialTracksHE" ),
  filterLabel = cms.InputTag( "hltIsolPixelTrackL2FilterHE" ),
  associationCone = cms.double( 0.2 )
)
process.hltHITPixelTracksHB = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originRadius = cms.double( 0.0015 ),
      nSigmaZ = cms.double( 3.0 ),
      ptMin = cms.double( 0.7 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltESPPixelLayerTripletsHITHB" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      maxElement = cms.uint32( 10000 ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 )
    )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByConformalMappingAndLine" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    fixImpactParameter = cms.double( 0.0 )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.7 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltHITPixelTracksHE = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originRadius = cms.double( 0.0015 ),
      nSigmaZ = cms.double( 3.0 ),
      ptMin = cms.double( 0.35 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltESPPixelLayerTripletsHITHE" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      maxElement = cms.uint32( 10000 ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 )
    )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByConformalMappingAndLine" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    fixImpactParameter = cms.double( 0.0 )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.35 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltHITPixelTripletSeedGeneratorHB = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    doClusterCheck = cms.bool( False ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 )
  ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "HITRegionalPixelSeedGenerator" ),
    RegionPSet = cms.PSet(
      deltaEtaTrackRegion = cms.double( 0.05 ),
      useL1Jets = cms.bool( False ),
      deltaPhiTrackRegion = cms.double( 0.05 ),
      originHalfLength = cms.double( 15.0 ),
      precise = cms.bool( True ),
      deltaEtaL1JetRegion = cms.double( 0.3 ),
      useTracks = cms.bool( False ),
      originRadius = cms.double( 0.6 ),
      isoTrackSrc = cms.InputTag( "hltIsolPixelTrackL2FilterHB" ),
      trackSrc = cms.InputTag( "hltHITPixelTracksHB" ),
      useIsoTracks = cms.bool( True ),
      l1tjetSrc = cms.InputTag( "hltL1extraParticles:Tau" ),
      deltaPhiL1JetRegion = cms.double( 0.3 ),
      ptMin = cms.double( 1.0 ),
      fixedReg = cms.bool( False ),
      etaCenter = cms.double( 0.0 ),
      phiCenter = cms.double( 0.0 ),
      originZPos = cms.double( 0.0 ),
      vertexSrc = cms.string( "hltHITPixelVerticesHB" )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      maxElement = cms.uint32( 10000 ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRZtolerance = cms.double( 0.06 )
    )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltHITPixelTripletSeedGeneratorHE = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    doClusterCheck = cms.bool( False ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 )
  ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "HITRegionalPixelSeedGenerator" ),
    RegionPSet = cms.PSet(
      deltaEtaTrackRegion = cms.double( 0.05 ),
      useL1Jets = cms.bool( False ),
      deltaPhiTrackRegion = cms.double( 0.05 ),
      originHalfLength = cms.double( 15.0 ),
      precise = cms.bool( True ),
      deltaEtaL1JetRegion = cms.double( 0.3 ),
      useTracks = cms.bool( False ),
      originRadius = cms.double( 0.6 ),
      isoTrackSrc = cms.InputTag( "hltIsolPixelTrackL2FilterHE" ),
      trackSrc = cms.InputTag( "hltHITPixelTracksHE" ),
      useIsoTracks = cms.bool( True ),
      l1tjetSrc = cms.InputTag( "hltL1extraParticles:Tau" ),
      deltaPhiL1JetRegion = cms.double( 0.3 ),
      ptMin = cms.double( 0.5 ),
      fixedReg = cms.bool( False ),
      etaCenter = cms.double( 0.0 ),
      phiCenter = cms.double( 0.0 ),
      originZPos = cms.double( 0.0 ),
      vertexSrc = cms.string( "hltHITPixelVerticesHE" )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      maxElement = cms.uint32( 10000 ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRZtolerance = cms.double( 0.06 )
    )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltHITPixelVerticesHB = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.05 ),
  NTrkMin = cms.int32( 2 ),
  PtMin = cms.double( 1.0 ),
  TrackCollection = cms.InputTag( "hltHITPixelTracksHB" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltHITPixelVerticesHE = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.05 ),
  NTrkMin = cms.int32( 2 ),
  PtMin = cms.double( 1.0 ),
  TrackCollection = cms.InputTag( "hltHITPixelTracksHE" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
  firstSample = cms.int32( 4 ),
  samplesToAdd = cms.int32( 4 ),
  correctForTimeslew = cms.bool( True ),
  correctForPhaseContainment = cms.bool( True ),
  correctionPhaseNS = cms.double( 13.0 ),
  digiLabel = cms.InputTag( "hltHcalDigis" ),
  correctTiming = cms.bool( False ),
  setNoiseFlags = cms.bool( False ),
  setHSCPFlags = cms.bool( False ),
  setSaturationFlags = cms.bool( False ),
  setTimingTrustFlags = cms.bool( False ),
  setPulseShapeFlags = cms.bool( False ),
  dropZSmarkedPassed = cms.bool( True ),
  Subdetector = cms.string( "HBHE" ),
  setTimingShapedCutsFlags = cms.bool( False ),
  digistat = cms.PSet(

  ),
  HFInWindowStat = cms.PSet(

  ),
  S8S1stat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
    flagsToSkip = cms.int32( 16 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
    longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
    long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
    isS8S1 = cms.bool( True )
  ),
  PETstat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_R_29 = cms.vdouble( 0.8 ),
    shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
    flagsToSkip = cms.int32( 0 ),
    short_R = cms.vdouble( 0.8 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    long_R_29 = cms.vdouble( 0.8 ),
    longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
    long_R = cms.vdouble( 0.98 )
  ),
  saturationParameters = cms.PSet(
    maxADCvalue = cms.int32( 127 )
  ),
  timingshapedcutsParameters = cms.PSet(
    ignorelowest = cms.bool( True ),
    win_offset = cms.double( 0.0 ),
    ignorehighest = cms.bool( False ),
    win_gain = cms.double( 1.0 ),
    tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
  ),
  flagParameters = cms.PSet(
    nominalPedestal = cms.double( 3.0 ),
    hitMultiplicityThreshold = cms.int32( 17 ),
    hitEnergyMinimum = cms.double( 1.0 ),
    pulseShapeParameterSets = cms.VPSet(
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )
      )
    )
  ),
  hscpParameters = cms.PSet(
    slopeMax = cms.double( -0.6 ),
    r1Max = cms.double( 1.0 ),
    r1Min = cms.double( 0.15 ),
    TimingEnergyThreshold = cms.double( 30.0 ),
    slopeMin = cms.double( -1.5 ),
    outerMin = cms.double( 0.0 ),
    outerMax = cms.double( 0.1 ),
    fracLeaderMin = cms.double( 0.4 ),
    r2Min = cms.double( 0.1 ),
    r2Max = cms.double( 0.5 ),
    fracLeaderMax = cms.double( 0.7 )
  ),
  pulseShapeParameters = cms.PSet(

  ),
  hfTimingTrustParameters = cms.PSet(
    hfTimingTrustLevel2 = cms.int32( 4 ),
    hfTimingTrustLevel1 = cms.int32( 1 )
  ),
  S9S1stat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
    flagsToSkip = cms.int32( 24 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
    longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
    long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
    isS8S1 = cms.bool( False )
  ),
  firstAuxOffset = cms.int32( 0 ),
  firstAuxTS = cms.int32( 4 ),
  tsFromDB = cms.bool( True )
)
process.hltHcalCalibTypeFilter = cms.HLTFilter( "HLTHcalCalibTypeFilter",
  InputTag = cms.InputTag( "source" ),
  FilterSummary = cms.untracked.bool( False ),
  CalibTypes = cms.vint32( 1, 2, 3, 4, 5, 6 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
  InputLabel = cms.InputTag( "source" ),
  HcalFirstFED = cms.untracked.int32( 0 ),
  UnpackCalib = cms.untracked.bool( True ),
  UnpackZDC = cms.untracked.bool( True ),
  UnpackTTP = cms.untracked.bool( False ),
  silent = cms.untracked.bool( True ),
  ComplainEmptyData = cms.untracked.bool( False ),
  ExpectedOrbitMessageTime = cms.untracked.int32( 0 ),
  FEDs = cms.untracked.vint32(  ),
  firstSample = cms.int32( 0 ),
  lastSample = cms.int32( 9 ),
  FilterDataQuality = cms.bool( True )
)
process.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
  firstSample = cms.int32( 4 ),
  samplesToAdd = cms.int32( 2 ),
  correctForTimeslew = cms.bool( False ),
  correctForPhaseContainment = cms.bool( False ),
  correctionPhaseNS = cms.double( 0.0 ),
  digiLabel = cms.InputTag( "hltHcalDigis" ),
  correctTiming = cms.bool( False ),
  setNoiseFlags = cms.bool( False ),
  setHSCPFlags = cms.bool( False ),
  setSaturationFlags = cms.bool( False ),
  setTimingTrustFlags = cms.bool( False ),
  setPulseShapeFlags = cms.bool( False ),
  dropZSmarkedPassed = cms.bool( True ),
  Subdetector = cms.string( "HF" ),
  setTimingShapedCutsFlags = cms.bool( False ),
  digistat = cms.PSet(
    HFdigiflagFirstSample = cms.int32( 3 ),
    HFdigiflagMinEthreshold = cms.double( 40.0 ),
    HFdigiflagSamplesToAdd = cms.int32( 4 ),
    HFdigiflagCoef0 = cms.double( 0.93 ),
    HFdigiflagCoef2 = cms.double( -0.012667 ),
    HFdigiflagCoef1 = cms.double( -0.38275 ),
    HFdigiflagExpectedPeak = cms.int32( 4 )
  ),
  HFInWindowStat = cms.PSet(
    hflongEthresh = cms.double( 40.0 ),
    hflongMinWindowTime = cms.vdouble( -10.0 ),
    hfshortEthresh = cms.double( 40.0 ),
    hflongMaxWindowTime = cms.vdouble( 10.0 ),
    hfshortMaxWindowTime = cms.vdouble( 10.0 ),
    hfshortMinWindowTime = cms.vdouble( -12.0 )
  ),
  S8S1stat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
    flagsToSkip = cms.int32( 16 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
    longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
    long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
    isS8S1 = cms.bool( True )
  ),
  PETstat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_R_29 = cms.vdouble( 0.8 ),
    shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
    flagsToSkip = cms.int32( 0 ),
    short_R = cms.vdouble( 0.8 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    long_R_29 = cms.vdouble( 0.8 ),
    longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
    long_R = cms.vdouble( 0.98 )
  ),
  saturationParameters = cms.PSet(
    maxADCvalue = cms.int32( 127 )
  ),
  timingshapedcutsParameters = cms.PSet(
    ignorelowest = cms.bool( True ),
    win_offset = cms.double( 0.0 ),
    ignorehighest = cms.bool( False ),
    win_gain = cms.double( 1.0 ),
    tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
  ),
  flagParameters = cms.PSet(
    nominalPedestal = cms.double( 3.0 ),
    hitMultiplicityThreshold = cms.int32( 17 ),
    hitEnergyMinimum = cms.double( 1.0 ),
    pulseShapeParameterSets = cms.VPSet(
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )
      )
    )
  ),
  hscpParameters = cms.PSet(
    slopeMax = cms.double( -0.6 ),
    r1Max = cms.double( 1.0 ),
    r1Min = cms.double( 0.15 ),
    TimingEnergyThreshold = cms.double( 30.0 ),
    slopeMin = cms.double( -1.5 ),
    outerMin = cms.double( 0.0 ),
    outerMax = cms.double( 0.1 ),
    fracLeaderMin = cms.double( 0.4 ),
    r2Min = cms.double( 0.1 ),
    r2Max = cms.double( 0.5 ),
    fracLeaderMax = cms.double( 0.7 )
  ),
  pulseShapeParameters = cms.PSet(

  ),
  hfTimingTrustParameters = cms.PSet(
    hfTimingTrustLevel2 = cms.int32( 4 ),
    hfTimingTrustLevel1 = cms.int32( 1 )
  ),
  S9S1stat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
    flagsToSkip = cms.int32( 24 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
    longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
    long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
    isS8S1 = cms.bool( False )
  ),
  firstAuxOffset = cms.int32( 0 ),
  firstAuxTS = cms.int32( 4 ),
  tsFromDB = cms.bool( True )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
  firstSample = cms.int32( 4 ),
  samplesToAdd = cms.int32( 4 ),
  correctForTimeslew = cms.bool( True ),
  correctForPhaseContainment = cms.bool( True ),
  correctionPhaseNS = cms.double( 13.0 ),
  digiLabel = cms.InputTag( "hltHcalDigis" ),
  correctTiming = cms.bool( False ),
  setNoiseFlags = cms.bool( False ),
  setHSCPFlags = cms.bool( False ),
  setSaturationFlags = cms.bool( False ),
  setTimingTrustFlags = cms.bool( False ),
  setPulseShapeFlags = cms.bool( False ),
  dropZSmarkedPassed = cms.bool( True ),
  Subdetector = cms.string( "HO" ),
  setTimingShapedCutsFlags = cms.bool( False ),
  digistat = cms.PSet(

  ),
  HFInWindowStat = cms.PSet(

  ),
  S8S1stat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
    flagsToSkip = cms.int32( 16 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
    longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
    long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
    isS8S1 = cms.bool( True )
  ),
  PETstat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_R_29 = cms.vdouble( 0.8 ),
    shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
    flagsToSkip = cms.int32( 0 ),
    short_R = cms.vdouble( 0.8 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    long_R_29 = cms.vdouble( 0.8 ),
    longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
    long_R = cms.vdouble( 0.98 )
  ),
  saturationParameters = cms.PSet(
    maxADCvalue = cms.int32( 127 )
  ),
  timingshapedcutsParameters = cms.PSet(
    ignorelowest = cms.bool( True ),
    win_offset = cms.double( 0.0 ),
    ignorehighest = cms.bool( False ),
    win_gain = cms.double( 1.0 ),
    tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
  ),
  flagParameters = cms.PSet(
    nominalPedestal = cms.double( 3.0 ),
    hitMultiplicityThreshold = cms.int32( 17 ),
    hitEnergyMinimum = cms.double( 1.0 ),
    pulseShapeParameterSets = cms.VPSet(
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )
      ),
      cms.PSet(
        pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )
      )
    )
  ),
  hscpParameters = cms.PSet(
    slopeMax = cms.double( -0.6 ),
    r1Max = cms.double( 1.0 ),
    r1Min = cms.double( 0.15 ),
    TimingEnergyThreshold = cms.double( 30.0 ),
    slopeMin = cms.double( -1.5 ),
    outerMin = cms.double( 0.0 ),
    outerMax = cms.double( 0.1 ),
    fracLeaderMin = cms.double( 0.4 ),
    r2Min = cms.double( 0.1 ),
    r2Max = cms.double( 0.5 ),
    fracLeaderMax = cms.double( 0.7 )
  ),
  pulseShapeParameters = cms.PSet(

  ),
  hfTimingTrustParameters = cms.PSet(
    hfTimingTrustLevel2 = cms.int32( 4 ),
    hfTimingTrustLevel1 = cms.int32( 1 )
  ),
  S9S1stat = cms.PSet(
    longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
    flagsToSkip = cms.int32( 24 ),
    shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
    short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
    longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
    long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
    isS8S1 = cms.bool( False )
  ),
  firstAuxOffset = cms.int32( 0 ),
  firstAuxTS = cms.int32( 4 ),
  tsFromDB = cms.bool( True )
)
process.hltHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
  debugLevel = cms.string( "INFO" ),
  basicclusterCollection = cms.string( "" ),
  superclusterCollection = cms.string( "" ),
  ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalhitcollection = cms.string( "EcalRecHitsEB" ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  doIsolated = cms.bool( True ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.14 ),
  regionPhiMargin = cms.double( 0.4 ),
  HybridBarrelSeedThr = cms.double( 1.5 ),
  step = cms.int32( 17 ),
  ethresh = cms.double( 0.1 ),
  eseed = cms.double( 0.35 ),
  ewing = cms.double( 0.0 ),
  dynamicEThresh = cms.bool( False ),
  eThreshA = cms.double( 0.003 ),
  eThreshB = cms.double( 0.1 ),
  severityRecHitThreshold = cms.double( 4.0 ),
  severitySpikeId = cms.int32( 2 ),
  severitySpikeThreshold = cms.double( 0.95 ),
  excludeFlagged = cms.bool( False ),
  dynamicPhiRoad = cms.bool( False ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  RecHitSeverityToBeExcluded = cms.vint32( 999 ),
  posCalcParameters = cms.PSet(
    T0_barl = cms.double( 7.4 ),
    LogWeighted = cms.bool( True ),
    T0_endc = cms.double( 3.1 ),
    T0_endcPresh = cms.double( 1.2 ),
    W0 = cms.double( 4.2 ),
    X0 = cms.double( 0.89 )
  ),
  bremRecoveryPset = cms.PSet(

  )
)
process.hltHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
  debugLevel = cms.string( "INFO" ),
  basicclusterCollection = cms.string( "" ),
  superclusterCollection = cms.string( "" ),
  ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalhitcollection = cms.string( "EcalRecHitsEB" ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  doIsolated = cms.bool( False ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.14 ),
  regionPhiMargin = cms.double( 0.4 ),
  HybridBarrelSeedThr = cms.double( 1.5 ),
  step = cms.int32( 17 ),
  ethresh = cms.double( 0.1 ),
  eseed = cms.double( 0.35 ),
  ewing = cms.double( 0.0 ),
  dynamicEThresh = cms.bool( False ),
  eThreshA = cms.double( 0.003 ),
  eThreshB = cms.double( 0.1 ),
  severityRecHitThreshold = cms.double( 4.0 ),
  severitySpikeId = cms.int32( 2 ),
  severitySpikeThreshold = cms.double( 0.95 ),
  excludeFlagged = cms.bool( False ),
  dynamicPhiRoad = cms.bool( False ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  RecHitSeverityToBeExcluded = cms.vint32( 999 ),
  posCalcParameters = cms.PSet(
    T0_barl = cms.double( 7.4 ),
    LogWeighted = cms.bool( True ),
    T0_endc = cms.double( 3.1 ),
    T0_endcPresh = cms.double( 1.2 ),
    W0 = cms.double( 4.2 ),
    X0 = cms.double( 0.89 )
  ),
  bremRecoveryPset = cms.PSet(

  )
)
process.hltIsolPixelTrackL2FilterHB = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltIsolPixelTrackProdHB" ),
  L1GTSeedLabel = cms.InputTag( "hltL1sL1SingleJet52" ),
  MinDeltaPtL1Jet = cms.double( -40000.0 ),
  MinPtTrack = cms.double( 3.5 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 1.15 ),
  MinEtaTrack = cms.double( 0.0 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 8.0 ),
  NMaxTrackCandidates = cms.int32( 10 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL2FilterHE = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltIsolPixelTrackProdHE" ),
  L1GTSeedLabel = cms.InputTag( "hltL1sL1SingleJet52" ),
  MinDeltaPtL1Jet = cms.double( -40000.0 ),
  MinPtTrack = cms.double( 3.5 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 2.2 ),
  MinEtaTrack = cms.double( 1.1 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 12.0 ),
  NMaxTrackCandidates = cms.int32( 5 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL3FilterHB = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltHITIPTCorrectorHB" ),
  L1GTSeedLabel = cms.InputTag( "hltL1sL1SingleJet52" ),
  MinDeltaPtL1Jet = cms.double( 4.0 ),
  MinPtTrack = cms.double( 20.0 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 1.15 ),
  MinEtaTrack = cms.double( 0.0 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 38.0 ),
  NMaxTrackCandidates = cms.int32( 999 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL3FilterHE = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltHITIPTCorrectorHE" ),
  L1GTSeedLabel = cms.InputTag( "hltL1sL1SingleJet52" ),
  MinDeltaPtL1Jet = cms.double( 4.0 ),
  MinPtTrack = cms.double( 20.0 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 2.2 ),
  MinEtaTrack = cms.double( 1.1 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 38.0 ),
  NMaxTrackCandidates = cms.int32( 999 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackProdHB = cms.EDProducer( "IsolatedPixelTrackCandidateProducer",
  L1eTauJetsSource = cms.InputTag( "hltL1extraParticles:Tau" ),
  tauAssociationCone = cms.double( 0.0 ),
  tauUnbiasCone = cms.double( 1.2 ),
  ExtrapolationConeSize = cms.double( 1.0 ),
  PixelIsolationConeSizeAtEC = cms.double( 40.0 ),
  L1GTSeedLabel = cms.InputTag( "hltL1sL1SingleJet52" ),
  MaxVtxDXYSeed = cms.double( 101.0 ),
  MaxVtxDXYIsol = cms.double( 101.0 ),
  VertexLabel = cms.InputTag( "hltHITPixelVerticesHB" ),
  MagFieldRecordName = cms.string( "VolumeBasedMagneticField" ),
  minPTrack = cms.double( 5.0 ),
  maxPTrackForIsolation = cms.double( 3.0 ),
  EBEtaBoundary = cms.double( 1.479 ),
  PixelTracksSources = cms.VInputTag( "hltHITPixelTracksHB" )
)
process.hltIsolPixelTrackProdHE = cms.EDProducer( "IsolatedPixelTrackCandidateProducer",
  L1eTauJetsSource = cms.InputTag( "hltL1extraParticles:Tau" ),
  tauAssociationCone = cms.double( 0.0 ),
  tauUnbiasCone = cms.double( 1.2 ),
  ExtrapolationConeSize = cms.double( 1.0 ),
  PixelIsolationConeSizeAtEC = cms.double( 40.0 ),
  L1GTSeedLabel = cms.InputTag( "hltL1sL1SingleJet52" ),
  MaxVtxDXYSeed = cms.double( 101.0 ),
  MaxVtxDXYIsol = cms.double( 101.0 ),
  VertexLabel = cms.InputTag( "hltHITPixelVerticesHE" ),
  MagFieldRecordName = cms.string( "VolumeBasedMagneticField" ),
  minPTrack = cms.double( 5.0 ),
  maxPTrackForIsolation = cms.double( 3.0 ),
  EBEtaBoundary = cms.double( 1.479 ),
  PixelTracksSources = cms.VInputTag( "hltHITPixelTracksHB", "hltHITPixelTracksHE" )
)
process.hltJetIDPassedCorrJets = cms.EDProducer( "HLTJetIDProducer",
  jetsInput = cms.InputTag( "hltAntiKT5L2L3CorrCaloJets" ),
  min_EMF = cms.double( 1.0e-06 ),
  max_EMF = cms.double( 999.0 ),
  min_N90 = cms.int32( 2 )
)
process.hltJetIDPassedJetsRegional = cms.EDProducer( "HLTJetIDProducer",
  jetsInput = cms.InputTag( "hltL1MatchedJetsRegional" ),
  min_EMF = cms.double( 1.0e-06 ),
  max_EMF = cms.double( 999.0 ),
  min_N90 = cms.int32( 2 )
)
process.hltL1EventNumberNZS = cms.HLTFilter( "HLTL1NumberFilter",
  rawInput = cms.InputTag( "source" ),
  period = cms.uint32( 4096 ),
  invert = cms.bool( False )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
  GmtInputTag = cms.InputTag( "hltGtDigis" ),
  GctInputTag = cms.InputTag( "hltGctDigis" ),
  CastorInputTag = cms.InputTag( "castorL1Digis" ),
  ProduceL1GtDaqRecord = cms.bool( False ),
  ProduceL1GtEvmRecord = cms.bool( False ),
  ProduceL1GtObjectMapRecord = cms.bool( True ),
  WritePsbL1GtDaqRecord = cms.bool( False ),
  ReadTechnicalTriggerRecords = cms.bool( True ),
  EmulateBxInEvent = cms.int32( 1 ),
  AlternativeNrBxBoardDaq = cms.uint32( 0 ),
  AlternativeNrBxBoardEvm = cms.uint32( 0 ),
  BstLengthBytes = cms.int32( -1 ),
  Verbosity = cms.untracked.int32( 0 ),
  TechnicalTriggersInputTags = cms.VInputTag( "simBscDigis" ),
  RecordLength = cms.vint32( 3, 0 )
)
process.hltL1IsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltL1IsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
  scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
  scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1IsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
  barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
  endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  SeedConfiguration = cms.PSet(
    searchInTIDTEC = cms.bool( True ),
    HighPtThreshold = cms.double( 35.0 ),
    r2MinF = cms.double( -0.15 ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
      useOnDemandTracker = cms.untracked.int32( 0 )
    ),
    DeltaPhi1Low = cms.double( 0.23 ),
    DeltaPhi1High = cms.double( 0.08 ),
    ePhiMin1 = cms.double( -0.08 ),
    PhiMin2 = cms.double( -0.004 ),
    LowPtThreshold = cms.double( 3.0 ),
    RegionPSet = cms.PSet(
      deltaPhiRegion = cms.double( 0.4 ),
      originHalfLength = cms.double( 15.0 ),
      useZInVertex = cms.bool( True ),
      deltaEtaRegion = cms.double( 0.1 ),
      ptMin = cms.double( 1.5 ),
      originRadius = cms.double( 0.2 ),
      VertexProducer = cms.InputTag( "dummyVertices" )
    ),
    maxHOverE = cms.double( 999999.0 ),
    dynamicPhiRoad = cms.bool( False ),
    ePhiMax1 = cms.double( 0.04 ),
    DeltaPhi2 = cms.double( 0.004 ),
    measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    SizeWindowENeg = cms.double( 0.675 ),
    nSigmasDeltaZ1 = cms.double( 5.0 ),
    rMaxI = cms.double( 0.2 ),
    PhiMax2 = cms.double( 0.004 ),
    preFilteredSeeds = cms.bool( True ),
    r2MaxF = cms.double( 0.15 ),
    pPhiMin1 = cms.double( -0.04 ),
    initialSeeds = cms.InputTag( "noSeedsHere" ),
    pPhiMax1 = cms.double( 0.08 ),
    hbheModule = cms.string( "hbhereco" ),
    SCEtCut = cms.double( 3.0 ),
    z2MaxB = cms.double( 0.09 ),
    fromTrackerSeeds = cms.bool( True ),
    hcalRecHits = cms.InputTag( "hltHbhereco" ),
    z2MinB = cms.double( -0.09 ),
    hbheInstance = cms.string( "" ),
    rMinI = cms.double( -0.2 ),
    hOverEConeSize = cms.double( 0.0 ),
    hOverEHBMinE = cms.double( 999999.0 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    applyHOverECut = cms.bool( False ),
    hOverEHFMinE = cms.double( 999999.0 )
  )
)
process.hltL1IsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.7 ),
  eMinHE = cms.double( 0.8 ),
  etMinHB = cms.double( -1.0 ),
  etMinHE = cms.double( -1.0 ),
  innerCone = cms.double( 0.0 ),
  outerCone = cms.double( 0.14 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( False )
)
process.hltL1MatchedJetsRegional = cms.EDProducer( "HLTJetL1MatchProducer",
  jetsInput = cms.InputTag( "hltAntiKT5L2L3CorrCaloJetsRegional" ),
  L1TauJets = cms.InputTag( "hltL1extraParticles:Tau" ),
  L1CenJets = cms.InputTag( "hltL1extraParticles:Central" ),
  L1ForJets = cms.InputTag( "hltL1extraParticles:Forward" ),
  DeltaR = cms.double( 0.5 )
)
process.hltL1MuORL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenCandidate" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltL1MuOpenL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpen" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltL1MuOpenL1FilteredDT = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpen" ),
  MaxEta = cms.double( 1.25 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltL1NonIsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltL1NonIsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
  scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolated" ),
  scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
  recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1NonIsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
  barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolated" ),
  endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
  SeedConfiguration = cms.PSet(
    searchInTIDTEC = cms.bool( True ),
    HighPtThreshold = cms.double( 35.0 ),
    r2MinF = cms.double( -0.15 ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
      useOnDemandTracker = cms.untracked.int32( 0 )
    ),
    DeltaPhi1Low = cms.double( 0.23 ),
    DeltaPhi1High = cms.double( 0.08 ),
    ePhiMin1 = cms.double( -0.08 ),
    PhiMin2 = cms.double( -0.004 ),
    LowPtThreshold = cms.double( 3.0 ),
    RegionPSet = cms.PSet(
      deltaPhiRegion = cms.double( 0.4 ),
      originHalfLength = cms.double( 15.0 ),
      useZInVertex = cms.bool( True ),
      deltaEtaRegion = cms.double( 0.1 ),
      ptMin = cms.double( 1.5 ),
      originRadius = cms.double( 0.2 ),
      VertexProducer = cms.InputTag( "dummyVertices" )
    ),
    maxHOverE = cms.double( 999999.0 ),
    dynamicPhiRoad = cms.bool( False ),
    ePhiMax1 = cms.double( 0.04 ),
    DeltaPhi2 = cms.double( 0.004 ),
    measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    SizeWindowENeg = cms.double( 0.675 ),
    nSigmasDeltaZ1 = cms.double( 5.0 ),
    rMaxI = cms.double( 0.2 ),
    PhiMax2 = cms.double( 0.004 ),
    preFilteredSeeds = cms.bool( True ),
    r2MaxF = cms.double( 0.15 ),
    pPhiMin1 = cms.double( -0.04 ),
    initialSeeds = cms.InputTag( "noSeedsHere" ),
    pPhiMax1 = cms.double( 0.08 ),
    hbheModule = cms.string( "hbhereco" ),
    SCEtCut = cms.double( 3.0 ),
    z2MaxB = cms.double( 0.09 ),
    fromTrackerSeeds = cms.bool( True ),
    hcalRecHits = cms.InputTag( "hltHbhereco" ),
    z2MinB = cms.double( -0.09 ),
    hbheInstance = cms.string( "" ),
    rMinI = cms.double( -0.2 ),
    hOverEConeSize = cms.double( 0.0 ),
    hOverEHBMinE = cms.double( 999999.0 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    applyHOverECut = cms.bool( False ),
    hOverEHFMinE = cms.double( 999999.0 )
  )
)
process.hltL1NonIsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.7 ),
  eMinHE = cms.double( 0.8 ),
  etMinHB = cms.double( -1.0 ),
  etMinHE = cms.double( -1.0 ),
  innerCone = cms.double( 0.0 ),
  outerCone = cms.double( 0.14 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( False )
)
process.hltL1SingleMu3L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu3" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltL1TechBSChalo = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "L1Tech_BSC_halo_beam2_inner", "L1Tech_BSC_halo_beam2_outer", "L1Tech_BSC_halo_beam1_inner", "L1Tech_BSC_halo_beam1_outer" ),
  hltResults = cms.InputTag( "" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( True )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
  produceMuonParticles = cms.bool( True ),
  muonSource = cms.InputTag( "hltGtDigis" ),
  produceCaloParticles = cms.bool( True ),
  isolatedEmSource = cms.InputTag( "hltGctDigis:isoEm" ),
  nonIsolatedEmSource = cms.InputTag( "hltGctDigis:nonIsoEm" ),
  centralJetSource = cms.InputTag( "hltGctDigis:cenJets" ),
  forwardJetSource = cms.InputTag( "hltGctDigis:forJets" ),
  tauJetSource = cms.InputTag( "hltGctDigis:tauJets" ),
  etTotalSource = cms.InputTag( "hltGctDigis" ),
  etHadSource = cms.InputTag( "hltGctDigis" ),
  etMissSource = cms.InputTag( "hltGctDigis" ),
  htMissSource = cms.InputTag( "hltGctDigis" ),
  hfRingEtSumsSource = cms.InputTag( "hltGctDigis" ),
  hfRingBitCountsSource = cms.InputTag( "hltGctDigis" ),
  centralBxOnly = cms.bool( True ),
  ignoreHtMiss = cms.bool( False )
)
process.hltL1sAlCaEcalPi0Eta = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleEG10 OR L1_DoubleEG2_FwdVeto OR L1_DoubleEG3 OR L1_DoubleEG5 OR L1_DoubleEG5_HTT50 OR L1_DoubleEG5_HTT75 OR L1_DoubleEG8 OR L1_DoubleEG_12_5 OR L1_DoubleForJet32_EtaOpp OR L1_DoubleForJet44_EtaOpp OR L1_DoubleIsoEG10 OR L1_DoubleJet36_Central OR L1_DoubleJet52 OR L1_EG5_HTT100 OR L1_EG5_HTT125 OR L1_EG5_HTT75 OR L1_SingleEG12 OR L1_SingleEG12_Eta2p17 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleEG30 OR L1_SingleEG5 OR L1_SingleIsoEG12 OR L1_SingleIsoEG12_Eta2p17 OR L1_SingleJet92 OR L1_SingleJet16 OR L1_SingleJet36 OR L1_SingleJet36_FwdVeto OR L1_SingleJet52 OR L1_SingleJet68 OR L1_SingleJet80_Central  OR L1_TripleEG5 OR L1_TripleEG7 OR L1_TripleJet28_Central" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sAlCaRPC = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu7 OR L1_SingleMu10 OR L1_SingleMu12 OR L1_SingleMu16 OR L1_SingleMu20" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sETT50 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETT20" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sETT60 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETT20" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sETT70 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETT20" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sGlobalRunHPDNoise = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet20_NotBptxOR_NotMuBeamHalo" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sHcalNZS = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet16 OR L1_SingleJet36 OR L1_SingleJet52 OR L1_SingleJet68 OR L1_SingleJet92  OR L1_SingleTauJet52 OR L1_SingleTauJet68 OR L1_SingleMu3 OR L1_SingleMu7 OR L1_SingleMu10 OR L1_SingleMu12 OR L1_SingleMu16 OR L1_SingleMu20 OR L1_SingleIsoEG12 OR L1_SingleEG5 OR L1_SingleEG12 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleEG30 OR L1_ZeroBias" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sHcalPhiSym = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleEG10 OR L1_DoubleEG2_FwdVeto OR L1_DoubleEG3 OR L1_DoubleEG5 OR L1_DoubleEG8 OR L1_DoubleEG_12_5 OR L1_DoubleIsoEG10 OR L1_SingleEG12 OR L1_SingleEG12_Eta2p17 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleEG30 OR L1_SingleEG5 OR L1_SingleIsoEG12 OR L1_SingleIsoEG12_Eta2p17 OR L1_SingleMu7 OR L1_SingleMu10 OR L1_SingleMu12 OR L1_SingleMu16 OR L1_SingleMu20 OR L1_SingleMu3 OR L1_SingleMu25 OR L1_DoubleMu0 OR L1_DoubleMu3 OR L1_DoubleMu5" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BeamGasBsc = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BeamGas_Bsc" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BeamGasHf = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BeamGas_Hf" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BeamHalo = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BeamHalo" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BscMinBiasORBptxPlusANDMinus = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BscMinBiasOR_BptxPlusANDMinus" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleForJet32EtaOpp = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleForJet32_EtaOpp" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleForJet8EtaOpp = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleForJet8_EtaOpp" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleMu0 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1InterbunchBsc = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_InterBunch_Bsc" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1PreCollisions = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_PreCollisions" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG12 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleEG12" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet16 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet16" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet36 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet36" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet52 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet52" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet8 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet8" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu3 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu3" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu5BQ7 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu5_Eta1p5_Q80" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMuOpen = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMuOpenCandidate = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( False ),
  L1NrBxInEvent = cms.int32( 1 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sTechTrigHCALNoise = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "11 OR 12" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sTrackerCosmics = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "25" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sZeroBias = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "4" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sZeroBiasPixel = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "4" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL2Muons:UpdatedAtVtx" )
)
process.hltL2MuonCandidatesNoVtx = cms.EDProducer( "L2MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL2Muons" )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
  InputObjects = cms.InputTag( "hltL1extraParticles" ),
  GMTReadoutCollection = cms.InputTag( "hltGtDigis" ),
  Propagator = cms.string( "SteppingHelixPropagatorAny" ),
  L1MinPt = cms.double( 0.0 ),
  L1MaxEta = cms.double( 2.5 ),
  L1MinQuality = cms.uint32( 1 ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
  InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
  L2TrajBuilderParameters = cms.PSet(
    DoRefit = cms.bool( False ),
    SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
    FilterParameters = cms.PSet(
      NumberOfSigma = cms.double( 3.0 ),
      FitDirection = cms.string( "insideOut" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      MaxChi2 = cms.double( 1000.0 ),
      MuonTrajectoryUpdatorParameters = cms.PSet(
        MaxChi2 = cms.double( 25.0 ),
        RescaleErrorFactor = cms.double( 100.0 ),
        Granularity = cms.int32( 0 ),
        ExcludeRPCFromFit = cms.bool( False ),
        UseInvalidHits = cms.bool( True ),
        RescaleError = cms.bool( False )
      ),
      EnableRPCMeasurement = cms.bool( True ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      EnableDTMeasurement = cms.bool( True ),
      RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      EnableCSCMeasurement = cms.bool( True )
    ),
    NavigationType = cms.string( "Standard" ),
    SeedTransformerParameters = cms.PSet(
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      NMinRecHits = cms.uint32( 2 ),
      UseSubRecHits = cms.bool( False ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      RescaleError = cms.double( 100.0 )
    ),
    DoBackwardFilter = cms.bool( True ),
    SeedPosition = cms.string( "in" ),
    BWFilterParameters = cms.PSet(
      NumberOfSigma = cms.double( 3.0 ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      FitDirection = cms.string( "outsideIn" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      MaxChi2 = cms.double( 100.0 ),
      MuonTrajectoryUpdatorParameters = cms.PSet(
        MaxChi2 = cms.double( 25.0 ),
        RescaleErrorFactor = cms.double( 100.0 ),
        Granularity = cms.int32( 2 ),
        ExcludeRPCFromFit = cms.bool( False ),
        UseInvalidHits = cms.bool( True ),
        RescaleError = cms.bool( False )
      ),
      EnableRPCMeasurement = cms.bool( True ),
      BWSeedType = cms.string( "fromGenerator" ),
      EnableDTMeasurement = cms.bool( True ),
      RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      EnableCSCMeasurement = cms.bool( True )
    ),
    DoSeedRefit = cms.bool( False )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "hltESPFastSteppingHelixPropagatorAny", "hltESPFastSteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
    DoSmoothing = cms.bool( False ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( True )
  )
)
process.hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL3Muons" )
)
process.hltL3MuonCandidatesNoVtx = cms.EDProducer( "L3MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL3MuonsNoVtx" )
)
process.hltL3Muons = cms.EDProducer( "L3TrackCombiner",
  labels = cms.VInputTag( "hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit" )
)
process.hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  L3TrajBuilderParameters = cms.PSet(
    ScaleTECyFactor = cms.double( -1.0 ),
    GlbRefitterParameters = cms.PSet(
      TrackerSkipSection = cms.int32( -1 ),
      DoPredictionsOnly = cms.bool( False ),
      PropDirForCosmics = cms.bool( False ),
      HitThreshold = cms.int32( 1 ),
      MuonHitsOption = cms.int32( 1 ),
      Chi2CutRPC = cms.double( 1.0 ),
      Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      Chi2CutCSC = cms.double( 150.0 ),
      Chi2CutDT = cms.double( 10.0 ),
      RefitRPCHits = cms.bool( True ),
      SkipStation = cms.int32( -1 ),
      Propagator = cms.string( "hltESPSmartPropagatorAny" ),
      TrackerSkipSystem = cms.int32( -1 )
    ),
    ScaleTECxFactor = cms.double( -1.0 ),
    TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      Eta_min = cms.double( 0.05 ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.05 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    RefitRPCHits = cms.bool( True ),
    PCut = cms.double( 2.5 ),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      RefitRPCHits = cms.bool( True ),
      Propagator = cms.string( "hltESPSmartPropagatorAny" )
    ),
    GlobalMuonTrackMatcher = cms.PSet(
      Pt_threshold1 = cms.double( 0.0 ),
      DeltaDCut_3 = cms.double( 15.0 ),
      MinP = cms.double( 2.5 ),
      MinPt = cms.double( 1.0 ),
      Chi2Cut_1 = cms.double( 50.0 ),
      Pt_threshold2 = cms.double( 999999999.0 ),
      LocChi2Cut = cms.double( 0.001 ),
      Eta_threshold = cms.double( 1.2 ),
      Quality_3 = cms.double( 7.0 ),
      Quality_2 = cms.double( 15.0 ),
      Chi2Cut_2 = cms.double( 50.0 ),
      Chi2Cut_3 = cms.double( 200.0 ),
      DeltaDCut_1 = cms.double( 40.0 ),
      DeltaRCut_2 = cms.double( 0.2 ),
      DeltaRCut_3 = cms.double( 1.0 ),
      DeltaDCut_2 = cms.double( 10.0 ),
      DeltaRCut_1 = cms.double( 0.1 ),
      Propagator = cms.string( "hltESPSmartPropagator" ),
      Quality_1 = cms.double( 20.0 )
    ),
    PtCut = cms.double( 1.0 ),
    TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "hltESPSmartPropagatorAny", "SteppingHelixPropagatorAny", "hltESPSmartPropagator", "hltESPSteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    PutTkTrackIntoEvent = cms.untracked.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    SmoothTkTrack = cms.untracked.bool( False ),
    MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
    Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( False ),
    DoSmoothing = cms.bool( True )
  )
)
process.hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
  labels = cms.VInputTag( "hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit" )
)
process.hltL3MuonsNoVtx = cms.EDProducer( "L3TkMuonProducer",
  InputObjects = cms.InputTag( "hltL3TkTracksFromL2NoVtx" )
)
process.hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  L3TrajBuilderParameters = cms.PSet(
    ScaleTECyFactor = cms.double( -1.0 ),
    GlbRefitterParameters = cms.PSet(
      TrackerSkipSection = cms.int32( -1 ),
      DoPredictionsOnly = cms.bool( False ),
      PropDirForCosmics = cms.bool( False ),
      HitThreshold = cms.int32( 1 ),
      MuonHitsOption = cms.int32( 1 ),
      Chi2CutRPC = cms.double( 1.0 ),
      Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      Chi2CutCSC = cms.double( 150.0 ),
      Chi2CutDT = cms.double( 10.0 ),
      RefitRPCHits = cms.bool( True ),
      SkipStation = cms.int32( -1 ),
      Propagator = cms.string( "hltESPSmartPropagatorAny" ),
      TrackerSkipSystem = cms.int32( -1 )
    ),
    ScaleTECxFactor = cms.double( -1.0 ),
    TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      Eta_min = cms.double( 0.05 ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.05 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    RefitRPCHits = cms.bool( True ),
    PCut = cms.double( 2.5 ),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      RefitRPCHits = cms.bool( True ),
      Propagator = cms.string( "hltESPSmartPropagatorAny" )
    ),
    GlobalMuonTrackMatcher = cms.PSet(
      Pt_threshold1 = cms.double( 0.0 ),
      DeltaDCut_3 = cms.double( 15.0 ),
      MinP = cms.double( 2.5 ),
      MinPt = cms.double( 1.0 ),
      Chi2Cut_1 = cms.double( 50.0 ),
      Pt_threshold2 = cms.double( 999999999.0 ),
      LocChi2Cut = cms.double( 0.001 ),
      Eta_threshold = cms.double( 1.2 ),
      Quality_3 = cms.double( 7.0 ),
      Quality_2 = cms.double( 15.0 ),
      Chi2Cut_2 = cms.double( 50.0 ),
      Chi2Cut_3 = cms.double( 200.0 ),
      DeltaDCut_1 = cms.double( 40.0 ),
      DeltaRCut_2 = cms.double( 0.2 ),
      DeltaRCut_3 = cms.double( 1.0 ),
      DeltaDCut_2 = cms.double( 10.0 ),
      DeltaRCut_1 = cms.double( 0.1 ),
      Propagator = cms.string( "hltESPSmartPropagator" ),
      Quality_1 = cms.double( 20.0 )
    ),
    PtCut = cms.double( 1.0 ),
    TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "hltESPSmartPropagatorAny", "SteppingHelixPropagatorAny", "hltESPSmartPropagator", "hltESPSteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    PutTkTrackIntoEvent = cms.untracked.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    SmoothTkTrack = cms.untracked.bool( False ),
    MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
    Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( False ),
    DoSmoothing = cms.bool( True )
  )
)
process.hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  L3TrajBuilderParameters = cms.PSet(
    ScaleTECyFactor = cms.double( -1.0 ),
    GlbRefitterParameters = cms.PSet(
      TrackerSkipSection = cms.int32( -1 ),
      DoPredictionsOnly = cms.bool( False ),
      PropDirForCosmics = cms.bool( False ),
      HitThreshold = cms.int32( 1 ),
      MuonHitsOption = cms.int32( 1 ),
      Chi2CutRPC = cms.double( 1.0 ),
      Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      Chi2CutCSC = cms.double( 150.0 ),
      Chi2CutDT = cms.double( 10.0 ),
      RefitRPCHits = cms.bool( True ),
      SkipStation = cms.int32( -1 ),
      Propagator = cms.string( "hltESPSmartPropagatorAny" ),
      TrackerSkipSystem = cms.int32( -1 )
    ),
    ScaleTECxFactor = cms.double( -1.0 ),
    TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      Eta_min = cms.double( 0.05 ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.05 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    RefitRPCHits = cms.bool( True ),
    PCut = cms.double( 2.5 ),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      RefitRPCHits = cms.bool( True ),
      Propagator = cms.string( "hltESPSmartPropagatorAny" )
    ),
    GlobalMuonTrackMatcher = cms.PSet(
      Pt_threshold1 = cms.double( 0.0 ),
      DeltaDCut_3 = cms.double( 15.0 ),
      MinP = cms.double( 2.5 ),
      MinPt = cms.double( 1.0 ),
      Chi2Cut_1 = cms.double( 50.0 ),
      Pt_threshold2 = cms.double( 999999999.0 ),
      LocChi2Cut = cms.double( 0.001 ),
      Eta_threshold = cms.double( 1.2 ),
      Quality_3 = cms.double( 7.0 ),
      Quality_2 = cms.double( 15.0 ),
      Chi2Cut_2 = cms.double( 50.0 ),
      Chi2Cut_3 = cms.double( 200.0 ),
      DeltaDCut_1 = cms.double( 40.0 ),
      DeltaRCut_2 = cms.double( 0.2 ),
      DeltaRCut_3 = cms.double( 1.0 ),
      DeltaDCut_2 = cms.double( 10.0 ),
      DeltaRCut_1 = cms.double( 0.1 ),
      Propagator = cms.string( "hltESPSmartPropagator" ),
      Quality_1 = cms.double( 20.0 )
    ),
    PtCut = cms.double( 1.0 ),
    TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "hltESPSmartPropagatorAny", "SteppingHelixPropagatorAny", "hltESPSmartPropagator", "hltESPSteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    PutTkTrackIntoEvent = cms.untracked.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    SmoothTkTrack = cms.untracked.bool( False ),
    MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
    Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( False ),
    DoSmoothing = cms.bool( True )
  )
)
process.hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
  labels = cms.VInputTag( "hltL3MuonsOIState", "hltL3MuonsOIHit" )
)
process.hltL3TkTracksFromL2 = cms.EDProducer( "L3TrackCombiner",
  labels = cms.VInputTag( "hltL3TkTracksFromL2IOHit", "hltL3TkTracksFromL2OIHit", "hltL3TkTracksFromL2OIState" )
)
process.hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltESPKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2NoVtx = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltESPKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2NoVtx" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltESPKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltESPKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
  labels = cms.VInputTag( "hltL3TrackCandidateFromL2IOHit", "hltL3TrackCandidateFromL2OIHit", "hltL3TrackCandidateFromL2OIState" )
)
process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajSeedIOHit" ),
  TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2NoVtx = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajectorySeedNoVtx" ),
  TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "CosmicNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajSeedOIHit" ),
  TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajSeedOIState" ),
  TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "PropagatorWithMaterial" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  MuonTrackingRegionBuilder = cms.PSet(
    EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
    EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
    OnDemand = cms.double( -1.0 ),
    Rescale_Dz = cms.double( 3.0 ),
    Eta_min = cms.double( 0.1 ),
    Rescale_phi = cms.double( 3.0 ),
    Eta_fixed = cms.double( 0.2 ),
    DeltaZ_Region = cms.double( 15.9 ),
    MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
    vertexCollection = cms.InputTag( "pixelVertices" ),
    Phi_fixed = cms.double( 0.2 ),
    DeltaR = cms.double( 0.2 ),
    EscapePt = cms.double( 1.5 ),
    UseFixedRegion = cms.bool( False ),
    PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
    Rescale_eta = cms.double( 3.0 ),
    Phi_min = cms.double( 0.1 ),
    UseVertex = cms.bool( False ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
  ),
  TkSeedGenerator = cms.PSet(
    PSetNames = cms.vstring( "skipTSG", "iterativeTSG" ),
    L3TkCollectionA = cms.InputTag( "hltL3TkFromL2OICombination" ),
    iterativeTSG = cms.PSet(
      firstTSG = cms.PSet(
        ComponentName = cms.string( "TSGFromOrderedHits" ),
        OrderedHitsFactoryPSet = cms.PSet(
          ComponentName = cms.string( "StandardHitTripletGenerator" ),
          GeneratorPSet = cms.PSet(
            useBending = cms.bool( True ),
            useFixedPreFiltering = cms.bool( False ),
            maxElement = cms.uint32( 10000 ),
            phiPreFiltering = cms.double( 0.3 ),
            extraHitRPhitolerance = cms.double( 0.06 ),
            useMultScattering = cms.bool( True ),
            ComponentName = cms.string( "PixelTripletHLTGenerator" ),
            extraHitRZtolerance = cms.double( 0.06 )
          ),
          SeedingLayers = cms.string( "hltESPPixelLayerTriplets" )
        ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
      ),
      PSetNames = cms.vstring( "firstTSG", "secondTSG" ),
      ComponentName = cms.string( "CombinedTSG" ),
      thirdTSG = cms.PSet(
        PSetNames = cms.vstring( "endcapTSG", "barrelTSG" ),
        barrelTSG = cms.PSet(

        ),
        endcapTSG = cms.PSet(
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet(
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
            useOnDemandTracker = cms.untracked.int32( 0 )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        ),
        etaSeparation = cms.double( 2.0 ),
        ComponentName = cms.string( "DualByEtaTSG" )
      ),
      secondTSG = cms.PSet(
        ComponentName = cms.string( "TSGFromOrderedHits" ),
        OrderedHitsFactoryPSet = cms.PSet(
          maxElement = cms.uint32( 0 ),
          ComponentName = cms.string( "StandardHitPairGenerator" ),
          SeedingLayers = cms.string( "hltESPPixelLayerPairs" ),
          useOnDemandTracker = cms.untracked.int32( 0 )
        ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
      )
    ),
    skipTSG = cms.PSet(

    ),
    ComponentName = cms.string( "DualByL2TSG" )
  ),
  TrackerSeedCleaner = cms.PSet(
    cleanerFromSharedHits = cms.bool( True ),
    ptCleaner = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    directionCleaner = cms.bool( True )
  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "PropagatorWithMaterial", "hltESPSmartPropagatorAnyOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  MuonTrackingRegionBuilder = cms.PSet(

  ),
  TkSeedGenerator = cms.PSet(
    PSetNames = cms.vstring( "skipTSG", "iterativeTSG" ),
    L3TkCollectionA = cms.InputTag( "hltL3MuonsOIState" ),
    iterativeTSG = cms.PSet(
      ErrorRescaling = cms.double( 3.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      MaxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet(
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet(
          pf3_V12 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V34 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V33 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V45 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V44 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V23 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V22 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V55 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V35 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      UpdateState = cms.bool( True ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SelectState = cms.bool( False ),
      SigmaZ = cms.double( 25.0 ),
      ResetMethod = cms.string( "matrix" ),
      ComponentName = cms.string( "TSGFromPropagation" ),
      UseVertexState = cms.bool( True ),
      Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" )
    ),
    skipTSG = cms.PSet(

    ),
    ComponentName = cms.string( "DualByL2TSG" )
  ),
  TrackerSeedCleaner = cms.PSet(
    cleanerFromSharedHits = cms.bool( True ),
    ptCleaner = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    directionCleaner = cms.bool( True )
  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "hltESPSteppingHelixPropagatorOpposite", "hltESPSteppingHelixPropagatorAlong" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  MuonTrackingRegionBuilder = cms.PSet(

  ),
  TkSeedGenerator = cms.PSet(
    propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
    option = cms.uint32( 3 ),
    maxChi2 = cms.double( 40.0 ),
    errorMatrixPset = cms.PSet(
      atIP = cms.bool( True ),
      action = cms.string( "use" ),
      errorMatrixValuesPSet = cms.PSet(
        pf3_V12 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V13 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V11 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V14 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V15 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V34 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
        pf3_V33 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V45 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V44 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
        pf3_V23 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V22 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V55 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        zAxis = cms.vdouble( -3.14159, 3.14159 ),
        pf3_V35 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V25 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V24 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        )
      )
    ),
    propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
    manySeeds = cms.bool( False ),
    copyMuonRecHit = cms.bool( False ),
    ComponentName = cms.string( "TSGForRoadSearch" )
  ),
  TrackerSeedCleaner = cms.PSet(

  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
  labels = cms.VInputTag( "hltL3TrajSeedIOHit", "hltL3TrajSeedOIState", "hltL3TrajSeedOIHit" )
)
process.hltL3TrajectorySeedNoVtx = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons" ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "hltESPSteppingHelixPropagatorOpposite", "hltESPSteppingHelixPropagatorAlong" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  MuonTrackingRegionBuilder = cms.PSet(

  ),
  TkSeedGenerator = cms.PSet(
    propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
    option = cms.uint32( 3 ),
    maxChi2 = cms.double( 40.0 ),
    errorMatrixPset = cms.PSet(
      atIP = cms.bool( True ),
      action = cms.string( "use" ),
      errorMatrixValuesPSet = cms.PSet(
        pf3_V12 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V13 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V11 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V14 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
        pf3_V34 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V15 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V33 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V45 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V44 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
        pf3_V23 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V22 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V55 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        zAxis = cms.vdouble( -3.14159, 3.14159 ),
        pf3_V35 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V25 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V24 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        )
      )
    ),
    propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
    manySeeds = cms.bool( False ),
    copyMuonRecHit = cms.bool( False ),
    ComponentName = cms.string( "TSGForRoadSearch" )
  ),
  TrackerSeedCleaner = cms.PSet(

  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltLaserAlignmentEventFilter = cms.EDFilter( "LaserAlignmentEventFilter",
  FedInputTag = cms.InputTag( "source" ),
  SIGNAL_Filter = cms.bool( True ),
  SINGLE_CHANNEL_THRESH = cms.uint32( 11 ),
  CHANNEL_COUNT_THRESH = cms.uint32( 8 ),
  FED_IDs = cms.vint32( 260, 261, 262, 263, 264, 265, 266, 267, 269, 270, 273, 274, 277, 278, 281, 282, 284, 285, 288, 289, 292, 293, 294, 295, 300, 301, 304, 305, 308, 309, 310, 311, 316, 317, 324, 325, 329, 330, 331, 332, 339, 340, 341, 342, 349, 350, 351, 352, 164, 165, 172, 173, 177, 178, 179, 180, 187, 188, 189, 190, 197, 198, 199, 200, 204, 205, 208, 209, 212, 213, 214, 215, 220, 221, 224, 225, 228, 229, 230, 231, 236, 237, 238, 239, 240, 241, 242, 243, 245, 246, 249, 250, 253, 254, 257, 258, 478, 476, 477, 482, 484, 480, 481, 474, 459, 460, 461, 463, 485, 487, 488, 489, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 288, 289, 292, 293, 300, 301, 304, 305, 310, 311, 316, 317, 329, 330, 339, 340, 341, 342, 349, 350, 164, 165, 177, 178, 179, 180, 189, 190, 197, 198, 204, 205, 212, 213, 220, 221, 224, 225, 230, 231 ),
  SIGNAL_IDs = cms.vint32( 470389128, 470389384, 470389640, 470389896, 470390152, 470390408, 470390664, 470390920, 470389192, 470389448, 470389704, 470389960, 470390216, 470390472, 470390728, 470390984, 470126984, 470127240, 470127496, 470127752, 470128008, 470128264, 470128520, 470128776, 470127048, 470127304, 470127560, 470127816, 470128072, 470128328, 470128584, 470128840, 436232506, 436232826, 436233146, 436233466, 369174604, 369174812, 369175068, 369175292, 470307468, 470307716, 470308236, 470308748, 470308996, 470045316, 470045580, 470046084, 470046596, 470046860 )
)
process.hltLogMonitorFilter = cms.HLTFilter( "HLTLogMonitorFilter",
  default_threshold = cms.uint32( 10 ),
  categories = cms.VPSet(

  )
)
process.hltMinBiasPixelFilter1 = cms.HLTFilter( "HLTPixlMBFilt",
  pixlTag = cms.InputTag( "hltPixelCandsForMinBias" ),
  MinPt = cms.double( 0.0 ),
  MinTrks = cms.uint32( 1 ),
  MinSep = cms.double( 1.0 )
)
process.hltMu5NoVertexL3PreFiltered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidatesNoVtx" ),
  PreviousCandTag = cms.InputTag( "hltSingleL2MuORL2PreFilteredNoVtx" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 6 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu5TkMuJpsiTkMuMassFilteredTight = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTkMuJpsiTrackerMuonCands" ),
  PreviousCandTag = cms.InputTag( "hltMu5TkMuJpsiTrackMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( True ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu5TkMuJpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiCtfTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiPixelMassFilteredEta15" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu5TrackJpsiL1Filtered0Eta15 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu5BQ7" ),
  MaxEta = cms.double( 1.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltMu5TrackJpsiL2Filtered5Eta15 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiL1Filtered0Eta15" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 1.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltMu5TrackJpsiL3Filtered5Eta15 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiL2Filtered5Eta15" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 1.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu5TrackJpsiPixelMassFilteredEta15 = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiPixelTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiL3Filtered5Eta15" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( False ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.5 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 3 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 999.0 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.0 ),
  MaxMasses = cms.vdouble( 4.6 )
)
process.hltMuTkMuJpsiTrackerMuonCands = cms.EDProducer( "L3MuonCandidateProducerFromMuons",
  InputObjects = cms.InputTag( "hltMuTkMuJpsiTrackerMuons" )
)
process.hltMuTkMuJpsiTrackerMuons = cms.EDProducer( "MuonIdProducer",
  minPt = cms.double( 0.0 ),
  minP = cms.double( 2.7 ),
  minPCaloMuon = cms.double( 1.0 ),
  minNumberOfMatches = cms.int32( 1 ),
  addExtraSoftMuons = cms.bool( False ),
  maxAbsEta = cms.double( 999.0 ),
  maxAbsDx = cms.double( 3.0 ),
  maxAbsPullX = cms.double( 3.0 ),
  maxAbsDy = cms.double( 3.0 ),
  maxAbsPullY = cms.double( 3.0 ),
  fillCaloCompatibility = cms.bool( False ),
  fillEnergy = cms.bool( False ),
  fillMatching = cms.bool( True ),
  fillIsolation = cms.bool( False ),
  writeIsoDeposits = cms.bool( False ),
  fillGlobalTrackQuality = cms.bool( False ),
  ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
  sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
  minCaloCompatibility = cms.double( 0.6 ),
  runArbitrationCleaner = cms.bool( False ),
  trackDepositName = cms.string( "tracker" ),
  ecalDepositName = cms.string( "ecal" ),
  hcalDepositName = cms.string( "hcal" ),
  hoDepositName = cms.string( "ho" ),
  jetDepositName = cms.string( "jets" ),
  debugWithTruthMatching = cms.bool( False ),
  globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
  inputCollectionLabels = cms.VInputTag( "hltMuTrackJpsiCtfTracks" ),
  inputCollectionTypes = cms.vstring( "inner tracks" ),
  arbitrationCleanerOptions = cms.PSet(
    Clustering = cms.bool( True ),
    ME1a = cms.bool( True ),
    ClusterDPhi = cms.double( 0.6 ),
    OverlapDTheta = cms.double( 0.02 ),
    Overlap = cms.bool( True ),
    OverlapDPhi = cms.double( 0.0786 ),
    ClusterDTheta = cms.double( 0.02 )
  ),
  TrackAssociatorParameters = cms.PSet(
    muonMaxDistanceSigmaX = cms.double( 0.0 ),
    muonMaxDistanceSigmaY = cms.double( 0.0 ),
    CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
    dRHcal = cms.double( 9999.0 ),
    dRPreshowerPreselection = cms.double( 0.2 ),
    CaloTowerCollectionLabel = cms.InputTag( "towerMaker" ),
    useEcal = cms.bool( False ),
    dREcal = cms.double( 9999.0 ),
    dREcalPreselection = cms.double( 0.05 ),
    HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
    dRMuon = cms.double( 9999.0 ),
    propagateAllDirections = cms.bool( True ),
    muonMaxDistanceX = cms.double( 5.0 ),
    muonMaxDistanceY = cms.double( 5.0 ),
    useHO = cms.bool( False ),
    trajectoryUncertaintyTolerance = cms.double( -1.0 ),
    usePreshower = cms.bool( False ),
    DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
    EERecHitCollectionLabel = cms.InputTag( "ecalRecHit:EcalRecHitsEE" ),
    dRHcalPreselection = cms.double( 0.2 ),
    useMuon = cms.bool( True ),
    useCalo = cms.bool( False ),
    accountForTrajectoryChangeCalo = cms.bool( False ),
    EBRecHitCollectionLabel = cms.InputTag( "ecalRecHit:EcalRecHitsEB" ),
    dRMuonPreselection = cms.double( 0.2 ),
    truthMatch = cms.bool( False ),
    HBHERecHitCollectionLabel = cms.InputTag( "hbhereco" ),
    useHcal = cms.bool( False )
  ),
  TimingFillerParameters = cms.PSet(
    UseDT = cms.bool( True ),
    ErrorDT = cms.double( 3.1 ),
    EcalEnergyCut = cms.double( 0.4 ),
    ErrorEB = cms.double( 2.085 ),
    ErrorCSC = cms.double( 7.0 ),
    CSCTimingParameters = cms.PSet(
      CSCsegments = cms.InputTag( "hltCscSegments" ),
      CSCTimeOffset = cms.double( 213.0 ),
      MatchParameters = cms.PSet(
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        DTsegments = cms.InputTag( "hltDthlt4DSegments" ),
        TightMatchDT = cms.bool( False ),
        TightMatchCSC = cms.bool( True ),
        DTradius = cms.double( 0.01 )
      ),
      ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny", "PropagatorWithMaterial", "PropagatorWithMaterialOpposite" ),
        RPCLayers = cms.bool( True )
      ),
      debug = cms.bool( False ),
      PruneCut = cms.double( 100.0 ),
      CSCStripTimeOffset = cms.double( 0.0 ),
      CSCStripError = cms.double( 7.0 ),
      UseStripTime = cms.bool( True ),
      CSCWireError = cms.double( 8.6 ),
      CSCWireTimeOffset = cms.double( 0.0 ),
      UseWireTime = cms.bool( True )
    ),
    DTTimingParameters = cms.PSet(
      DoWireCorr = cms.bool( False ),
      PruneCut = cms.double( 1000.0 ),
      DTsegments = cms.InputTag( "hltDthlt4DSegments" ),
      ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny", "PropagatorWithMaterial", "PropagatorWithMaterialOpposite" ),
        RPCLayers = cms.bool( True )
      ),
      RequireBothProjections = cms.bool( False ),
      HitsMin = cms.int32( 3 ),
      DTTimeOffset = cms.double( 2.7 ),
      debug = cms.bool( False ),
      UseSegmentT0 = cms.bool( False ),
      MatchParameters = cms.PSet(
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        DTsegments = cms.InputTag( "hltDthlt4DSegments" ),
        TightMatchDT = cms.bool( False ),
        TightMatchCSC = cms.bool( True ),
        DTradius = cms.double( 0.01 )
      ),
      HitError = cms.double( 6.0 ),
      DropTheta = cms.bool( True )
    ),
    ErrorEE = cms.double( 6.95 ),
    UseCSC = cms.bool( True ),
    UseECAL = cms.bool( False )
  ),
  JetExtractorPSet = cms.PSet(

  ),
  TrackExtractorPSet = cms.PSet(

  ),
  MuonCaloCompatibility = cms.PSet(

  ),
  CaloExtractorPSet = cms.PSet(

  )
)
process.hltMuTrackJpsiCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltMuTrackJpsiTrackSeeds" ),
  TrajectoryBuilder = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltMuTrackJpsiCtfTrackCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltMuTrackJpsiCtfTracks" ),
  particleType = cms.string( "mu-" )
)
process.hltMuTrackJpsiCtfTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltMuTrackJpsiCtfTracks" ),
  Fitter = cms.string( "hltESPFittingSmootherRK" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  src = cms.InputTag( "hltMuTrackJpsiCkfTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltMuTrackJpsiPixelTrackCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltMuTrackJpsiPixelTrackSelector" ),
  particleType = cms.string( "mu-" )
)
process.hltMuTrackJpsiPixelTrackSelector = cms.EDProducer( "QuarkoniaTrackSelector",
  muonCandidates = cms.InputTag( "hltL3MuonCandidates" ),
  tracks = cms.InputTag( "hltPixelTracks" ),
  checkCharge = cms.bool( False ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.5 ),
  MaxTrackEta = cms.double( 999.0 ),
  MinMasses = cms.vdouble( 2.0 ),
  MaxMasses = cms.vdouble( 4.6 )
)
process.hltMuTrackJpsiTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
  InputCollection = cms.InputTag( "hltMuTrackJpsiPixelTrackSelector" ),
  useProtoTrackKinematics = cms.bool( False ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltMulti5x5BasicClustersL1Isolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  doIsolated = cms.bool( True ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  barrelHitCollection = cms.string( "EcalRecHitsEB" ),
  endcapHitCollection = cms.string( "EcalRecHitsEE" ),
  barrelClusterCollection = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  Multi5x5BarrelSeedThr = cms.double( 0.5 ),
  Multi5x5EndcapSeedThr = cms.double( 0.18 ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.3 ),
  regionPhiMargin = cms.double( 0.4 ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  posCalcParameters = cms.PSet(
    T0_barl = cms.double( 7.4 ),
    LogWeighted = cms.bool( True ),
    T0_endc = cms.double( 3.1 ),
    T0_endcPresh = cms.double( 1.2 ),
    W0 = cms.double( 4.2 ),
    X0 = cms.double( 0.89 )
  )
)
process.hltMulti5x5BasicClustersL1NonIsolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  doIsolated = cms.bool( False ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  barrelHitCollection = cms.string( "EcalRecHitsEB" ),
  endcapHitCollection = cms.string( "EcalRecHitsEE" ),
  barrelClusterCollection = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  Multi5x5BarrelSeedThr = cms.double( 0.5 ),
  Multi5x5EndcapSeedThr = cms.double( 0.18 ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.3 ),
  regionPhiMargin = cms.double( 0.4 ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  posCalcParameters = cms.PSet(
    T0_barl = cms.double( 7.4 ),
    LogWeighted = cms.bool( True ),
    T0_endc = cms.double( 3.1 ),
    T0_endcPresh = cms.double( 1.2 ),
    W0 = cms.double( 4.2 ),
    X0 = cms.double( 0.89 )
  )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "PreshowerClusterProducer",
  preshRecHitProducer = cms.InputTag( "hltESRegionalEgammaRecHit:EcalRecHitsES" ),
  endcapSClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersL1Isolated:multi5x5EndcapSuperClusters" ),
  preshClusterCollectionX = cms.string( "preshowerXClusters" ),
  preshClusterCollectionY = cms.string( "preshowerYClusters" ),
  preshNclust = cms.int32( 4 ),
  etThresh = cms.double( 5.0 ),
  assocSClusterCollection = cms.string( "" ),
  preshStripEnergyCut = cms.double( 0.0 ),
  preshSeededNstrip = cms.int32( 15 ),
  preshClusterEnergyCut = cms.double( 0.0 ),
  debugLevel = cms.string( "" )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "PreshowerClusterProducer",
  preshRecHitProducer = cms.InputTag( "hltESRegionalEgammaRecHit:EcalRecHitsES" ),
  endcapSClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersL1NonIsolated:multi5x5EndcapSuperClusters" ),
  preshClusterCollectionX = cms.string( "preshowerXClusters" ),
  preshClusterCollectionY = cms.string( "preshowerYClusters" ),
  preshNclust = cms.int32( 4 ),
  etThresh = cms.double( 5.0 ),
  assocSClusterCollection = cms.string( "" ),
  preshStripEnergyCut = cms.double( 0.0 ),
  preshSeededNstrip = cms.int32( 15 ),
  preshClusterEnergyCut = cms.double( 0.0 ),
  debugLevel = cms.string( "" )
)
process.hltMulti5x5SuperClustersL1Isolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1Isolated" ),
  barrelClusterProducer = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
  barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  barrelEtaSearchRoad = cms.double( 0.06 ),
  barrelPhiSearchRoad = cms.double( 0.8 ),
  endcapEtaSearchRoad = cms.double( 0.14 ),
  endcapPhiSearchRoad = cms.double( 0.6 ),
  seedTransverseEnergyThreshold = cms.double( 1.0 ),
  dynamicPhiRoad = cms.bool( False ),
  bremRecoveryPset = cms.PSet(
    barrel = cms.PSet(

    ),
    endcap = cms.PSet(
      a = cms.double( 47.85 ),
      c = cms.double( 0.1201 ),
      b = cms.double( 108.8 )
    ),
    doEndcaps = cms.bool( True ),
    doBarrel = cms.bool( False )
  )
)
process.hltMulti5x5SuperClustersL1NonIsolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1NonIsolated" ),
  barrelClusterProducer = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
  barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  barrelEtaSearchRoad = cms.double( 0.06 ),
  barrelPhiSearchRoad = cms.double( 0.8 ),
  endcapEtaSearchRoad = cms.double( 0.14 ),
  endcapPhiSearchRoad = cms.double( 0.6 ),
  seedTransverseEnergyThreshold = cms.double( 1.0 ),
  dynamicPhiRoad = cms.bool( False ),
  bremRecoveryPset = cms.PSet(
    barrel = cms.PSet(

    ),
    endcap = cms.PSet(
      a = cms.double( 47.85 ),
      c = cms.double( 0.1201 ),
      b = cms.double( 108.8 )
    ),
    doEndcaps = cms.bool( True ),
    doBarrel = cms.bool( False )
  )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
  InputObjects = cms.InputTag( "source" ),
  UseExaminer = cms.bool( True ),
  ExaminerMask = cms.uint32( 0x1febf3f6 ),
  UseSelectiveUnpacking = cms.bool( True ),
  ErrorMask = cms.uint32( 0x00000000 ),
  UnpackStatusDigis = cms.bool( False ),
  UseFormatStatus = cms.bool( True ),
  PrintEventNumber = cms.untracked.bool( False ),
  Debug = cms.untracked.bool( False ),
  runDQM = cms.untracked.bool( False ),
  VisualFEDInspect = cms.untracked.bool( False ),
  VisualFEDShort = cms.untracked.bool( False ),
  FormatedEventDump = cms.untracked.bool( False ),
  SuppressZeroLCT = cms.untracked.bool( True )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
  dataType = cms.string( "DDU" ),
  fedbyType = cms.bool( False ),
  inputLabel = cms.InputTag( "source" ),
  useStandardFEDid = cms.bool( True ),
  minFEDid = cms.untracked.int32( 770 ),
  maxFEDid = cms.untracked.int32( 779 ),
  dqmOnly = cms.bool( False ),
  rosParameters = cms.PSet(

  ),
  readOutParameters = cms.PSet(
    debug = cms.untracked.bool( False ),
    rosParameters = cms.PSet(
      writeSC = cms.untracked.bool( True ),
      readingDDU = cms.untracked.bool( True ),
      performDataIntegrityMonitor = cms.untracked.bool( False ),
      readDDUIDfromDDU = cms.untracked.bool( True ),
      debug = cms.untracked.bool( False ),
      localDAQ = cms.untracked.bool( False )
    ),
    localDAQ = cms.untracked.bool( False ),
    performDataIntegrityMonitor = cms.untracked.bool( False )
  )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
  InputLabel = cms.InputTag( "source" ),
  doSynchro = cms.bool( False )
)
process.hltOfflineBeamSpot = cms.EDProducer( "BeamSpotProducer" )
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
  label = cms.InputTag( "hltScalersRawToDigi" ),
  changeToCMSCoordinates = cms.bool( False ),
  maxRadius = cms.double( 2.0 ),
  maxZ = cms.double( 40.0 ),
  setSigmaZ = cms.double( 10.0 ),
  gtEvmLabel = cms.InputTag( "" )
)
process.hltPixelActivityFilter = cms.HLTFilter( "HLTPixelActivityFilter",
  inputTag = cms.InputTag( "hltSiPixelClusters" ),
  saveTag = cms.untracked.bool( False ),
  minClusters = cms.uint32( 3 ),
  maxClusters = cms.uint32( 0 )
)
process.hltPixelActivityFilterForHalo = cms.HLTFilter( "HLTPixelActivityFilter",
  inputTag = cms.InputTag( "hltSiPixelClusters" ),
  saveTag = cms.untracked.bool( False ),
  minClusters = cms.uint32( 0 ),
  maxClusters = cms.uint32( 10 )
)
process.hltPixelAsymmetryFilter = cms.HLTFilter( "HLTPixelAsymmetryFilter",
  inputTag = cms.InputTag( "hltSiPixelClusters" ),
  saveTag = cms.untracked.bool( False ),
  MinAsym = cms.double( 0.0 ),
  MaxAsym = cms.double( 1.0 ),
  MinCharge = cms.double( 4000.0 ),
  MinBarrel = cms.double( 10000.0 )
)
process.hltPixelCandsForHighMultLoose = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltPixelTracksForHighMultLoose" ),
  particleType = cms.string( "pi+" )
)
process.hltPixelCandsForMinBias = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltPixelTracksForMinBias" ),
  particleType = cms.string( "pi+" )
)
process.hltPixelTracks = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      ptMin = cms.double( 0.9 ),
      originRadius = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      originHalfLength = cms.double( 15.9 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      maxElement = cms.uint32( 10000 ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 )
    )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByHelixProjections" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltPixelTracksForHighMultLoose = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originHalfLength = cms.double( 15.0 ),
      originRadius = cms.double( 0.0015 ),
      ptMin = cms.double( 0.4 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByHelixProjections" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.4 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltPixelTracksForMinBias = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originHalfLength = cms.double( 30.0 ),
      originRadius = cms.double( 0.5 ),
      ptMin = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByHelixProjections" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltPixelVerticesForHighMultLoose = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.05 ),
  NTrkMin = cms.int32( 3 ),
  PtMin = cms.double( 0.4 ),
  TrackCollection = cms.InputTag( "hltPixelTracksForHighMultLoose" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltPreALCAP0Output = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreALCAPHISYMOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaDTErrors = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaEcalEta = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaEcalPhiSym = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaEcalPi0 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreCalibration = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreCalibrationOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDQMOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDQMOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "HLT_BeamGas_BSC_v2", "HLT_BeamGas_HF_v2", "HLT_BeamHalo_v2", "HLT_Calibration_v1 / 10", "HLT_DTErrors_v1", "HLT_DoubleMu3_v3", "HLT_EcalCalibration_v1 / 10", "HLT_Ele8_v2", "HLT_GlobalRunHPDNoise_v2", "HLT_HcalCalibration_v1", "HLT_HcalNZS_v3", "HLT_HcalPhiSym_v3", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v3", "HLT_Jet20_v1", "HLT_Jet40_v1", "HLT_Jet60_v1", "HLT_L1DoubleForJet32_EtaOpp_v1", "HLT_L1DoubleForJet8_EtaOpp_v1", "HLT_L1DoubleMu0_v1", "HLT_L1SingleEG12_v1", "HLT_L1SingleEG5_v1", "HLT_L1SingleJet36_v1", "HLT_L1SingleMuOpen_AntiBPTX_v1", "HLT_L1SingleMuOpen_DT_v1", "HLT_L1SingleMuOpen_v1", "HLT_L1Tech_BSC_halo_v1", "HLT_L1Tech_HBHEHO_totalOR_v1", "HLT_L1TrackerCosmics_v2", "HLT_L1_Interbunch_BSC_v1", "HLT_L1_PreCollisions_v1", "HLT_L2DoubleMu0_v2", "HLT_L3MuonsCosmicTracking_v1", "HLT_LogMonitor_v1", "HLT_L1BscMinBiasORBptxPlusANDMinus_v1", "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1", "HLT_Mu0_v3", "HLT_Mu3_v3", "HLT_Mu5_v3", "HLT_Photon10_CaloIdVL_v1", "HLT_Photon15_CaloIdVL_v1", "HLT_PixelTracks_Multiplicity50_Loose", "HLT_PixelTracks_Multiplicity60_Loose", "HLT_PixelTracks_Multiplicity70_Loose", "HLT_Random_v1", "HLT_RegionalCosmicTracking_v1", "HLT_TrackerCalibration_v1 / 10", "HLT_ZeroBiasPixel_SingleTrack_v1", "HLT_ZeroBias_v1" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreDoubleMu3 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEcalCalibration = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEcalCalibrationOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle8 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreExpressOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreExpressOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "HLT_Ele8_v2", "HLT_Jet60_v1", "HLT_Mu5_v3", "HLT_Photon15_CaloIdVL_v1", "HLT_ZeroBias_v1 / 8" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreGlobalRunHPDNoise = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTDQMOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTDQMOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "AlCa_EcalEta_v3 / 100", "AlCa_EcalPhiSym_v2 / 100", "AlCa_EcalPi0_v4 / 100", "AlCa_RPCMuonNoHits_v2 / 100", "AlCa_RPCMuonNoTriggers_v2 / 100", "AlCa_RPCMuonNormalisation_v2 / 100", "HLT_BeamGas_BSC_v2", "HLT_BeamGas_HF_v2", "HLT_BeamHalo_v2", "HLT_DTErrors_v1", "HLT_DoubleMu3_v3", "HLT_Ele8_v2", "HLT_GlobalRunHPDNoise_v2", "HLT_HcalNZS_v3", "HLT_HcalPhiSym_v3", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v3", "HLT_Jet20_v1", "HLT_Jet40_v1", "HLT_Jet60_v1", "HLT_L1DoubleForJet32_EtaOpp_v1", "HLT_L1DoubleForJet8_EtaOpp_v1", "HLT_L1DoubleMu0_v1", "HLT_L1SingleEG12_v1", "HLT_L1SingleEG5_v1", "HLT_L1SingleJet36_v1", "HLT_L1SingleMuOpen_AntiBPTX_v1", "HLT_L1SingleMuOpen_DT_v1", "HLT_L1SingleMuOpen_v1", "HLT_L1Tech_BSC_halo_v1", "HLT_L1Tech_HBHEHO_totalOR_v1", "HLT_L1TrackerCosmics_v2", "HLT_L1_Interbunch_BSC_v1", "HLT_L1_PreCollisions_v1", "HLT_L2DoubleMu0_v2", "HLT_L3MuonsCosmicTracking_v1", "HLT_LogMonitor_v1", "HLT_L1BscMinBiasORBptxPlusANDMinus_v1", "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1", "HLT_Mu0_v3", "HLT_Mu3_v3", "HLT_Mu5_v3", "HLT_Photon10_CaloIdVL_v1", "HLT_Photon15_CaloIdVL_v1", "HLT_PixelTracks_Multiplicity50_Loose", "HLT_PixelTracks_Multiplicity60_Loose", "HLT_PixelTracks_Multiplicity70_Loose", "HLT_Random_v1", "HLT_RegionalCosmicTracking_v1", "HLT_ZeroBiasPixel_SingleTrack_v1", "HLT_ZeroBias_v1" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreHLTDQMResultsOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTMONOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTMONOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "AlCa_EcalEta_v3 / 100", "AlCa_EcalPhiSym_v2 / 100", "AlCa_EcalPi0_v4 / 100", "AlCa_RPCMuonNoHits_v2 / 100", "AlCa_RPCMuonNoTriggers_v2 / 100", "AlCa_RPCMuonNormalisation_v2 / 100", "HLT_BeamGas_BSC_v2", "HLT_BeamGas_HF_v2", "HLT_BeamHalo_v2", "HLT_DTErrors_v1", "HLT_DoubleMu3_v3", "HLT_Ele8_v2", "HLT_GlobalRunHPDNoise_v2", "HLT_HcalNZS_v3", "HLT_HcalPhiSym_v3", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v3", "HLT_Jet20_v1", "HLT_Jet40_v1", "HLT_Jet60_v1", "HLT_L1DoubleForJet32_EtaOpp_v1", "HLT_L1DoubleForJet8_EtaOpp_v1", "HLT_L1DoubleMu0_v1", "HLT_L1SingleEG12_v1", "HLT_L1SingleEG5_v1", "HLT_L1SingleJet36_v1", "HLT_L1SingleMuOpen_AntiBPTX_v1", "HLT_L1SingleMuOpen_DT_v1", "HLT_L1SingleMuOpen_v1", "HLT_L1Tech_BSC_halo_v1", "HLT_L1Tech_HBHEHO_totalOR_v1", "HLT_L1TrackerCosmics_v2", "HLT_L1_Interbunch_BSC_v1", "HLT_L1_PreCollisions_v1", "HLT_L2DoubleMu0_v2", "HLT_L3MuonsCosmicTracking_v1", "HLT_LogMonitor_v1", "HLT_L1BscMinBiasORBptxPlusANDMinus_v1", "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1", "HLT_Mu0_v3", "HLT_Mu3_v3", "HLT_Mu5_v3", "HLT_Photon10_CaloIdVL_v1", "HLT_Photon15_CaloIdVL_v1", "HLT_PixelTracks_Multiplicity50_Loose", "HLT_PixelTracks_Multiplicity60_Loose", "HLT_PixelTracks_Multiplicity70_Loose", "HLT_Random_v1", "HLT_RegionalCosmicTracking_v1", "HLT_ZeroBiasPixel_SingleTrack_v1", "HLT_ZeroBias_v1" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreHcalCalibration = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHcalNZS = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHcalPhiSym = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreIsoTrackHB = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreIsoTrackHE = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet20 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet40 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet60 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BeamGasBsc = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BeamGasHf = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BeamHalo = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BscMinBiasORBptxPlusANDMinus = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1DoubleForJet32EtaOpp = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1DoubleForJet8EtaOpp = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1DoubleMu0 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1Interbunch1 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1MuOpenAntiBPTX = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1PreCollisions = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1SingleEG12 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1SingleEG5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1SingleJet36 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1SingleMuOpen = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1SingleMuOpenDT = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1TechBSChalo = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL2DoubleMu0 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL3MuonsCosmicTracking = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreLogMonitor = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu0 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu3 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5TkMu0JpsiTightB5Q7 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreNanoDSTOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreOnlineErrorsOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton10CaloIdVL = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton15CaloIdVL = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhysicsNanoDST = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePixelTracksMultiplicity50 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePixelTracksMultiplicity60 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePixelTracksMultiplicity70 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCMONOutput = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCMuonNoHits = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCMuonNoTriggers = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCMuonNorma = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRandom = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRegionalCosmicTracking = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreTechTrigHCALNoise = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreTrackerCalibration = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreTrackerCosmics = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreZeroBias = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreZeroBiasPixelSingleTrack = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltRPCFilter = cms.HLTFilter( "HLTRPCFilter",
  rangestrips = cms.untracked.double( 1.0 ),
  rpcRecHits = cms.InputTag( "hltRpcRecHits" ),
  rpcDTPoints = cms.InputTag( "hltRPCPointProducer:RPCDTExtrapolatedPoints" ),
  rpcCSCPoints = cms.InputTag( "hltRPCPointProducer:RPCCSCExtrapolatedPoints" )
)
process.hltRPCMuonNoTriggersL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sAlCaRPC" ),
  MaxEta = cms.double( 1.6 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32( 6 )
)
process.hltRPCMuonNormaL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sAlCaRPC" ),
  MaxEta = cms.double( 1.6 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltRPCPointProducer = cms.EDProducer( "RPCPointProducer",
  cscSegments = cms.InputTag( "hltCscSegments" ),
  dt4DSegments = cms.InputTag( "hltDt4DSegments" ),
  tracks = cms.InputTag( "NotUsed" ),
  debug = cms.untracked.bool( False ),
  incldt = cms.untracked.bool( True ),
  inclcsc = cms.untracked.bool( True ),
  incltrack = cms.untracked.bool( False ),
  MinCosAng = cms.untracked.double( 0.95 ),
  MaxD = cms.untracked.double( 80.0 ),
  MaxDrb4 = cms.untracked.double( 150.0 ),
  ExtrapolatedRegion = cms.untracked.double( 0.5 ),
  TrackTransformer = cms.PSet(

  )
)
process.hltRandomEventsFilter = cms.HLTFilter( "HLTTriggerTypeFilter",
  SelectedTriggerType = cms.int32( 3 )
)
process.hltRegionalCosmicCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltRegionalCosmicTrackerSeeds" ),
  TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "CosmicNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 200 )
)
process.hltRegionalCosmicTrackerSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    MaxNumberOfPixelClusters = cms.uint32( 300000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfCosmicClusters = cms.uint32( 300000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    doClusterCheck = cms.bool( False )
  ),
  RegionFactoryPSet = cms.PSet(
    CollectionsPSet = cms.PSet(
      recoMuonsCollection = cms.InputTag( "muons" ),
      recoTrackMuonsCollection = cms.InputTag( "cosmicMuons" ),
      recoL2MuonsCollection = cms.InputTag( "hltL2MuonCandidatesNoVtx" )
    ),
    ComponentName = cms.string( "CosmicRegionalSeedGenerator" ),
    RegionInJetsCheckPSet = cms.PSet(
      recoCaloJetsCollection = cms.InputTag( "hltIterativeCone5CaloJets" ),
      deltaRExclusionSize = cms.double( 0.3 ),
      jetsPtMin = cms.double( 5.0 ),
      doJetsExclusionCheck = cms.bool( False )
    ),
    ToolsPSet = cms.PSet(
      regionBase = cms.string( "seedOnL2Muon" ),
      thePropagatorName = cms.string( "hltESPAnalyticalPropagator" )
    ),
    RegionPSet = cms.PSet(
      precise = cms.bool( False ),
      deltaPhiRegion = cms.double( 0.3 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      zVertex = cms.double( 5.0 ),
      deltaEtaRegion = cms.double( 0.3 ),
      ptMin = cms.double( 5.0 ),
      rVertex = cms.double( 5.0 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GenericPairGenerator" ),
    LayerPSet = cms.PSet(
      TOB = cms.PSet(
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
      ),
      layerList = cms.vstring( "TOB6+TOB5", "TOB6+TOB4", "TOB6+TOB3", "TOB5+TOB4", "TOB5+TOB3", "TOB4+TOB3" )
    )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "CosmicSeedCreator" ),
    maxseeds = cms.int32( 100000 ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltRegionalCosmicTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltRegionalCosmicTracks" ),
  Fitter = cms.string( "hltESPKFFittingSmoother" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  src = cms.InputTag( "hltRegionalCosmicCkfTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
  rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
  recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
  maskSource = cms.string( "File" ),
  maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
  deadSource = cms.string( "File" ),
  deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
  recAlgoConfig = cms.PSet(

  )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
  scalersInputTag = cms.InputTag( "source" )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
  src = cms.InputTag( "hltSiPixelDigis" ),
  maxNumberOfClusters = cms.int32( 10000 ),
  payloadType = cms.string( "HLT" ),
  ClusterMode = cms.untracked.string( "PixelThresholdClusterizer" ),
  ChannelThreshold = cms.int32( 1000 ),
  SeedThreshold = cms.int32( 1000 ),
  ClusterThreshold = cms.double( 4000.0 ),
  VCaltoElectronGain = cms.int32( 65 ),
  VCaltoElectronOffset = cms.int32( -414 ),
  MissCalibrate = cms.untracked.bool( True ),
  SplitClusters = cms.bool( False )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
  IncludeErrors = cms.bool( False ),
  UseQualityInfo = cms.bool( False ),
  UseCablingTree = cms.untracked.bool( True ),
  Timing = cms.untracked.bool( False ),
  InputLabel = cms.InputTag( "source" )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
  src = cms.InputTag( "hltSiPixelClusters" ),
  VerboseLevel = cms.untracked.int32( 0 ),
  CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerSiStripRefGetterProducer",
  InputModuleLabel = cms.InputTag( "hltSiStripRawToClustersFacility" ),
  measurementTrackerName = cms.string( "hltESPMeasurementTracker" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripRawToClusters",
  ProductLabel = cms.InputTag( "source" ),
  Clusterizer = cms.PSet(
    ChannelThreshold = cms.double( 2.0 ),
    MaxSequentialBad = cms.uint32( 1 ),
    MaxSequentialHoles = cms.uint32( 0 ),
    Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
    MaxAdjacentBad = cms.uint32( 0 ),
    QualityLabel = cms.string( "" ),
    SeedThreshold = cms.double( 3.0 ),
    ClusterThreshold = cms.double( 5.0 )
  ),
  Algorithms = cms.PSet(
    SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
    CommonModeNoiseSubtractionMode = cms.string( "Median" ),
    PedestalSubtractionFedMode = cms.bool( True ),
    TruncateInSuppressor = cms.bool( True )
  )
)
process.hltSimple3x3Clusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
  doBarrel = cms.bool( True ),
  doEndcaps = cms.bool( True ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEB" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEE" ),
  clusEtaSize = cms.int32( 3 ),
  clusPhiSize = cms.int32( 3 ),
  barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
  endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
  clusSeedThr = cms.double( 0.5 ),
  clusSeedThrEndCap = cms.double( 1.0 ),
  useRecoFlag = cms.bool( False ),
  flagLevelRecHitsToUse = cms.int32( 1 ),
  useDBStatus = cms.bool( True ),
  statusLevelRecHitsToUse = cms.int32( 1 ),
  maxNumberofSeeds = cms.int32( 200 ),
  maxNumberofClusters = cms.int32( 30 ),
  debugLevel = cms.int32( 0 ),
  posCalcParameters = cms.PSet(
    T0_barl = cms.double( 7.4 ),
    LogWeighted = cms.bool( True ),
    T0_endc = cms.double( 3.1 ),
    T0_endcPresh = cms.double( 1.2 ),
    W0 = cms.double( 4.2 ),
    X0 = cms.double( 0.89 )
  )
)
process.hltSingleJet20 = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltJetIDPassedCorrJets" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltSingleJet40 = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltJetIDPassedCorrJets" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 40.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltSingleJet60Regional = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltJetIDPassedJetsRegional" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 60.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltSingleL2MuORL2PreFilteredNoVtx = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidatesNoVtx" ),
  PreviousCandTag = cms.InputTag( "hltL1MuORL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu0L2Filtered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMuOpenL1Filtered" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu0L3Filtered0 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu0L2Filtered0" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu3L2Filtered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMuOpenL1Filtered" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu3L3Filtered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu3L2Filtered0" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu5L2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu3L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltSingleMu5L3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu5L2Filtered3" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMuOpenL1Filtered = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpen" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0 ),
  EEWeight = cms.double( 1.0 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "hltHbhereco" ),
  hoInput = cms.InputTag( "hltHoreco" ),
  hfInput = cms.InputTag( "hltHfreco" ),
  AllowMissingInputs = cms.bool( False ),
  HcalAcceptSeverityLevel = cms.uint32( 11 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( False ),
  UseEcalRecoveredHits = cms.bool( False ),
  UseRejectedHitsOnly = cms.bool( False ),
  HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
  EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
  UseRejectedRecoveredHcalHits = cms.bool( False ),
  UseRejectedRecoveredEcalHits = cms.bool( False ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag( "hltEcalRecHitAll:EcalRecHitsEB", "hltEcalRecHitAll:EcalRecHitsEE" )
)
process.hltTowerMakerForJets = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0 ),
  EEWeight = cms.double( 1.0 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "hltHbhereco" ),
  hoInput = cms.InputTag( "hltHoreco" ),
  hfInput = cms.InputTag( "hltHfreco" ),
  AllowMissingInputs = cms.bool( False ),
  HcalAcceptSeverityLevel = cms.uint32( 11 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( False ),
  UseEcalRecoveredHits = cms.bool( False ),
  UseRejectedHitsOnly = cms.bool( False ),
  HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
  EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
  UseRejectedRecoveredHcalHits = cms.bool( False ),
  UseRejectedRecoveredEcalHits = cms.bool( False ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag( "hltEcalRegionalJetsRecHit:EcalRecHitsEB", "hltEcalRegionalJetsRecHit:EcalRecHitsEE" )
)
process.hltTrackerCosmicsPattern = cms.HLTFilter( "HLTLevel1Pattern",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  triggerBit = cms.string( "L1Tech_RPC_TTU_pointing_Cosmics.v0" ),
  daqPartitions = cms.uint32( 1 ),
  ignoreL1Mask = cms.bool( False ),
  invert = cms.bool( False ),
  throw = cms.bool( True ),
  bunchCrossings = cms.vint32( -2, -1, 0, 1, 2 ),
  triggerPattern = cms.vint32( 1, 1, 1, 0, 0 )
)
process.hltTrackerHaloFilter = cms.HLTFilter( "HLTTrackerHaloFilter",
  inputTag = cms.InputTag( "hltSiStripClusters" ),
  saveTag = cms.untracked.bool( False ),
  MaxClustersTECp = cms.int32( 50 ),
  MaxClustersTECm = cms.int32( 50 ),
  SignalAccumulation = cms.int32( 5 ),
  MaxClustersTEC = cms.int32( 60 ),
  MaxAccus = cms.int32( 4 ),
  FastProcessing = cms.int32( 1 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
  processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
  processName = cms.string( "@" )
)
process.hltTriggerType = cms.HLTFilter( "HLTTriggerTypeFilter",
  SelectedTriggerType = cms.int32( 1 )
)

process.hltOutputA = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_BeamGas_BSC_v2", "HLT_BeamGas_HF_v2", "HLT_BeamHalo_v2", "HLT_DoubleMu3_v3", "HLT_Ele8_v2", "HLT_GlobalRunHPDNoise_v2", "HLT_HcalNZS_v3", "HLT_HcalPhiSym_v3", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v3", "HLT_Jet20_v1", "HLT_Jet40_v1", "HLT_Jet60_v1", "HLT_L1BscMinBiasORBptxPlusANDMinus_v1", "HLT_L1DoubleForJet32_EtaOpp_v1", "HLT_L1DoubleForJet8_EtaOpp_v1", "HLT_L1DoubleMu0_v1", "HLT_L1SingleEG12_v1", "HLT_L1SingleEG5_v1", "HLT_L1SingleJet36_v1", "HLT_L1SingleMuOpen_AntiBPTX_v1", "HLT_L1SingleMuOpen_DT_v1", "HLT_L1SingleMuOpen_v1", "HLT_L1Tech_BSC_halo_v1", "HLT_L1Tech_HBHEHO_totalOR_v1", "HLT_L1TrackerCosmics_v2", "HLT_L1_Interbunch_BSC_v1", "HLT_L1_PreCollisions_v1", "HLT_L2DoubleMu0_v2", "HLT_L3MuonsCosmicTracking_v1", "HLT_Mu0_v3", "HLT_Mu3_v3", "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1", "HLT_Mu5_v3", "HLT_Photon10_CaloIdVL_v1", "HLT_Photon15_CaloIdVL_v1", "HLT_PixelTracks_Multiplicity50_Loose", "HLT_PixelTracks_Multiplicity60_Loose", "HLT_PixelTracks_Multiplicity70_Loose", "HLT_Random_v1", "HLT_RegionalCosmicTracking_v1", "HLT_ZeroBiasPixel_SingleTrack_v1", "HLT_ZeroBias_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltL1GtObjectMap_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputExpress = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_Ele8_v2", "HLT_Jet60_v1", "HLT_Mu5_v3", "HLT_Photon15_CaloIdVL_v1", "HLT_ZeroBias_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltL1GtObjectMap_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputCalibration = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_Calibration_v1", "HLT_HcalCalibration_v1", "HLT_TrackerCalibration_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputEcalCalibration = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_EcalCalibration_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltEcalCalibrationRaw_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputDQM = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_BeamGas_BSC_v2", "HLT_BeamGas_HF_v2", "HLT_BeamHalo_v2", "HLT_Calibration_v1", "HLT_DTErrors_v1", "HLT_DoubleMu3_v3", "HLT_EcalCalibration_v1", "HLT_Ele8_v2", "HLT_GlobalRunHPDNoise_v2", "HLT_HcalCalibration_v1", "HLT_HcalNZS_v3", "HLT_HcalPhiSym_v3", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v3", "HLT_Jet20_v1", "HLT_Jet40_v1", "HLT_Jet60_v1", "HLT_L1BscMinBiasORBptxPlusANDMinus_v1", "HLT_L1DoubleForJet32_EtaOpp_v1", "HLT_L1DoubleForJet8_EtaOpp_v1", "HLT_L1DoubleMu0_v1", "HLT_L1SingleEG12_v1", "HLT_L1SingleEG5_v1", "HLT_L1SingleJet36_v1", "HLT_L1SingleMuOpen_AntiBPTX_v1", "HLT_L1SingleMuOpen_DT_v1", "HLT_L1SingleMuOpen_v1", "HLT_L1Tech_BSC_halo_v1", "HLT_L1Tech_HBHEHO_totalOR_v1", "HLT_L1TrackerCosmics_v2", "HLT_L1_Interbunch_BSC_v1", "HLT_L1_PreCollisions_v1", "HLT_L2DoubleMu0_v2", "HLT_L3MuonsCosmicTracking_v1", "HLT_LogMonitor_v1", "HLT_Mu0_v3", "HLT_Mu3_v3", "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1", "HLT_Mu5_v3", "HLT_Photon10_CaloIdVL_v1", "HLT_Photon15_CaloIdVL_v1", "HLT_PixelTracks_Multiplicity50_Loose", "HLT_PixelTracks_Multiplicity60_Loose", "HLT_PixelTracks_Multiplicity70_Loose", "HLT_Random_v1", "HLT_RegionalCosmicTracking_v1", "HLT_TrackerCalibration_v1", "HLT_ZeroBiasPixel_SingleTrack_v1", "HLT_ZeroBias_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltDt4DSegments_*_*", "keep *_hltL1GtObjectMap_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEventWithRefs_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputHLTDQM = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_EcalEta_v3", "AlCa_EcalPhiSym_v2", "AlCa_EcalPi0_v4", "AlCa_RPCMuonNoHits_v2", "AlCa_RPCMuonNoTriggers_v2", "AlCa_RPCMuonNormalisation_v2", "HLT_BeamGas_BSC_v2", "HLT_BeamGas_HF_v2", "HLT_BeamHalo_v2", "HLT_DTErrors_v1", "HLT_DoubleMu3_v3", "HLT_Ele8_v2", "HLT_GlobalRunHPDNoise_v2", "HLT_HcalNZS_v3", "HLT_HcalPhiSym_v3", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v3", "HLT_Jet20_v1", "HLT_Jet40_v1", "HLT_Jet60_v1", "HLT_L1BscMinBiasORBptxPlusANDMinus_v1", "HLT_L1DoubleForJet32_EtaOpp_v1", "HLT_L1DoubleForJet8_EtaOpp_v1", "HLT_L1DoubleMu0_v1", "HLT_L1SingleEG12_v1", "HLT_L1SingleEG5_v1", "HLT_L1SingleJet36_v1", "HLT_L1SingleMuOpen_AntiBPTX_v1", "HLT_L1SingleMuOpen_DT_v1", "HLT_L1SingleMuOpen_v1", "HLT_L1Tech_BSC_halo_v1", "HLT_L1Tech_HBHEHO_totalOR_v1", "HLT_L1TrackerCosmics_v2", "HLT_L1_Interbunch_BSC_v1", "HLT_L1_PreCollisions_v1", "HLT_L2DoubleMu0_v2", "HLT_L3MuonsCosmicTracking_v1", "HLT_LogMonitor_v1", "HLT_Mu0_v3", "HLT_Mu3_v3", "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1", "HLT_Mu5_v3", "HLT_Photon10_CaloIdVL_v1", "HLT_Photon15_CaloIdVL_v1", "HLT_PixelTracks_Multiplicity50_Loose", "HLT_PixelTracks_Multiplicity60_Loose", "HLT_PixelTracks_Multiplicity70_Loose", "HLT_Random_v1", "HLT_RegionalCosmicTracking_v1", "HLT_ZeroBiasPixel_SingleTrack_v1", "HLT_ZeroBias_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltAlCaEtaRecHitsFilter_*_*", "keep *_hltAlCaPhiSymStream_*_*", "keep *_hltAlCaPi0RecHitsFilter_*_*", "keep *_hltBLifetimeL25AssociatorStartupU_*_*", "keep *_hltBLifetimeL25BJetTagsStartupU_*_*", "keep *_hltBLifetimeL25JetsStartupU_*_*", "keep *_hltBLifetimeL25TagInfosStartupU_*_*", "keep *_hltBLifetimeL3AssociatorStartupU_*_*", "keep *_hltBLifetimeL3BJetTagsStartupU_*_*", "keep *_hltBLifetimeL3JetsStartupU_*_*", "keep *_hltBLifetimeL3TagInfosStartupU_*_*", "keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*", "keep *_hltBSoftMuonL25BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL25JetsU_*_*", "keep *_hltBSoftMuonL25TagInfosU_*_*", "keep *_hltBSoftMuonL3BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL3TagInfosU_*_*", "keep *_hltCsc2DRecHits_*_*", "keep *_hltCscSegments_*_*", "keep *_hltDt4DSegments_*_*", "keep *_hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EcalIsolationDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationSingleLooseIsoTau20_*_*", "keep *_hltFilterL2EtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EtCutDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EtCutSingleLooseIsoTau20_*_*", "keep *_hltFilterL3TrackIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltGtDigis_*_*", "keep *_hltHITCtfWithMaterialTracksHB8E29_*_*", "keep *_hltHITCtfWithMaterialTracksHE8E29_*_*", "keep *_hltHITIPTCorrectorHB8E29_*_*", "keep *_hltHITIPTCorrectorHE8E29_*_*", "keep *_hltHcalDigis_*_*", "keep *_hltIconeCentral1Regional_*_*", "keep *_hltIconeCentral2Regional_*_*", "keep *_hltIconeCentral3Regional_*_*", "keep *_hltIconeCentral4Regional_*_*", "keep *_hltIconeTau1Regional_*_*", "keep *_hltIconeTau2Regional_*_*", "keep *_hltIconeTau3Regional_*_*", "keep *_hltIconeTau4Regional_*_*", "keep *_hltIsolPixelTrackProdHB8E29_*_*", "keep *_hltIsolPixelTrackProdHE8E29_*_*", "keep *_hltIterativeCone5CaloJets_*_*", "keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1IsoRecoEcalCandidate_*_*", "keep *_hltL1IsoSiStripElectronPixelSeeds_*_*", "keep *_hltL1IsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1IsolatedElectronHcalIsol_*_*", "keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1NonIsoRecoEcalCandidate_*_*", "keep *_hltL1NonIsoSiStripElectronPixelSeeds_*_*", "keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1NonIsolatedElectronHcalIsol_*_*", "keep *_hltL1extraParticles_*_*", "keep *_hltL1sDoubleLooseIsoTau15_*_*", "keep *_hltL1sSingleLooseIsoTau20_*_*", "keep *_hltL25TauConeIsolation_*_*", "keep *_hltL25TauCtfWithMaterialTracks_*_*", "keep *_hltL25TauJetTracksAssociator_*_*", "keep *_hltL25TauLeadingTrackPtCutSelector_*_*", "keep *_hltL2MuonCandidates_*_*", "keep *_hltL2MuonIsolations_*_*", "keep *_hltL2MuonSeeds_*_*", "keep *_hltL2Muons_*_*", "keep *_hltL2TauJets_*_*", "keep *_hltL2TauNarrowConeIsolationProducer_*_*", "keep *_hltL2TauRelaxingIsolationSelector_*_*", "keep *_hltL3MuonCandidates_*_*", "keep *_hltL3MuonIsolations_*_*", "keep *_hltL3MuonsIOHit_*_*", "keep *_hltL3MuonsLinksCombination_*_*", "keep *_hltL3MuonsOIHit_*_*", "keep *_hltL3MuonsOIState_*_*", "keep *_hltL3Muons_*_*", "keep *_hltL3TauConeIsolation_*_*", "keep *_hltL3TauCtfWithMaterialTracks_*_*", "keep *_hltL3TauIsolationSelector_*_*", "keep *_hltL3TauJetTracksAssociator_*_*", "keep *_hltL3TkFromL2OICombination_*_*", "keep *_hltL3TkTracksFromL2IOHit_*_*", "keep *_hltL3TkTracksFromL2OIHit_*_*", "keep *_hltL3TkTracksFromL2OIState_*_*", "keep *_hltL3TrackCandidateFromL2IOHit_*_*", "keep *_hltL3TrackCandidateFromL2OIHit_*_*", "keep *_hltL3TrackCandidateFromL2OIState_*_*", "keep *_hltL3TrajSeedIOHit_*_*", "keep *_hltL3TrajSeedOIHit_*_*", "keep *_hltL3TrajSeedOIState_*_*", "keep *_hltL3TrajectorySeed_*_*", "keep *_hltMCJetCorJetIcone5HF07_*_*", "keep *_hltMet_*_*", "keep *_hltMuTrackJpsiCtfTrackCands_*_*", "keep *_hltMuTrackJpsiPixelTrackCands_*_*", "keep *_hltMuonCSCDigis_*_*", "keep *_hltMuonRPCDigis_*_*", "keep *_hltOfflineBeamSpot_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*", "keep *_hltPixelTracks_*_*", "keep *_hltRpcRecHits_*_*", "keep *_hltSiPixelClusters_*_*", "keep *_hltSiStripRawToClustersFacility_*_*", "keep *_hltTowerMakerForMuons_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEventWithRefs_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputHLTDQMResults = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLTriggerFinalPath" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep LumiScalerss_*_*_*", "keep edmTriggerResults_*_*_*" )
)
process.hltOutputHLTMON = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_EcalEta_v3", "AlCa_EcalPhiSym_v2", "AlCa_EcalPi0_v4", "AlCa_RPCMuonNoHits_v2", "AlCa_RPCMuonNoTriggers_v2", "AlCa_RPCMuonNormalisation_v2", "HLT_BeamGas_BSC_v2", "HLT_BeamGas_HF_v2", "HLT_BeamHalo_v2", "HLT_DTErrors_v1", "HLT_DoubleMu3_v3", "HLT_Ele8_v2", "HLT_GlobalRunHPDNoise_v2", "HLT_HcalNZS_v3", "HLT_HcalPhiSym_v3", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v3", "HLT_Jet20_v1", "HLT_Jet40_v1", "HLT_Jet60_v1", "HLT_L1BscMinBiasORBptxPlusANDMinus_v1", "HLT_L1DoubleForJet32_EtaOpp_v1", "HLT_L1DoubleForJet8_EtaOpp_v1", "HLT_L1DoubleMu0_v1", "HLT_L1SingleEG12_v1", "HLT_L1SingleEG5_v1", "HLT_L1SingleJet36_v1", "HLT_L1SingleMuOpen_AntiBPTX_v1", "HLT_L1SingleMuOpen_DT_v1", "HLT_L1SingleMuOpen_v1", "HLT_L1Tech_BSC_halo_v1", "HLT_L1Tech_HBHEHO_totalOR_v1", "HLT_L1TrackerCosmics_v2", "HLT_L1_Interbunch_BSC_v1", "HLT_L1_PreCollisions_v1", "HLT_L2DoubleMu0_v2", "HLT_L3MuonsCosmicTracking_v1", "HLT_LogMonitor_v1", "HLT_Mu0_v3", "HLT_Mu3_v3", "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1", "HLT_Mu5_v3", "HLT_Photon10_CaloIdVL_v1", "HLT_Photon15_CaloIdVL_v1", "HLT_PixelTracks_Multiplicity50_Loose", "HLT_PixelTracks_Multiplicity60_Loose", "HLT_PixelTracks_Multiplicity70_Loose", "HLT_Random_v1", "HLT_RegionalCosmicTracking_v1", "HLT_ZeroBiasPixel_SingleTrack_v1", "HLT_ZeroBias_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltAlCaEtaRecHitsFilter_*_*", "keep *_hltAlCaPi0RecHitsFilter_*_*", "keep *_hltBLifetimeL25AssociatorStartupU_*_*", "keep *_hltBLifetimeL25BJetTagsStartupU_*_*", "keep *_hltBLifetimeL25JetsStartupU_*_*", "keep *_hltBLifetimeL25TagInfosStartupU_*_*", "keep *_hltBLifetimeL3AssociatorStartupU_*_*", "keep *_hltBLifetimeL3BJetTagsStartupU_*_*", "keep *_hltBLifetimeL3JetsStartupU_*_*", "keep *_hltBLifetimeL3TagInfosStartupU_*_*", "keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*", "keep *_hltBSoftMuonL25BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL25JetsU_*_*", "keep *_hltBSoftMuonL25TagInfosU_*_*", "keep *_hltBSoftMuonL3BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL3BJetTagsUByPt_*_*", "keep *_hltBSoftMuonL3TagInfosU_*_*", "keep *_hltCkfL1IsoLargeWindowTrackCandidates_*_*", "keep *_hltCkfL1NonIsoLargeWindowTrackCandidates_*_*", "keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*", "keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*", "keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*", "keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*", "keep *_hltCscSegments_*_*", "keep *_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*", "keep *_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*", "keep *_hltDt1DRecHits_*_*", "keep *_hltDt4DSegments_*_*", "keep *_hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EcalIsolationDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationSingleLooseIsoTau20_*_*", "keep *_hltFilterL2EtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EtCutDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EtCutSingleLooseIsoTau20_*_*", "keep *_hltFilterL3TrackIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltGctDigis_*_*", "keep *_hltGtDigis_*_*", "keep *_hltHoreco_*_*", "keep *_hltIconeCentral1Regional_*_*", "keep *_hltIconeCentral2Regional_*_*", "keep *_hltIconeCentral3Regional_*_*", "keep *_hltIconeCentral4Regional_*_*", "keep *_hltIconeTau1Regional_*_*", "keep *_hltIconeTau2Regional_*_*", "keep *_hltIconeTau3Regional_*_*", "keep *_hltIconeTau4Regional_*_*", "keep *_hltL1GtObjectMap_*_*", "keep *_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*", "keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*", "keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*", "keep *_hltL1IsoHLTClusterShape_*_*", "keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1IsoPhotonHollowTrackIsol_*_*", "keep *_hltL1IsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1IsolatedPhotonEcalIsol_*_*", "keep *_hltL1IsolatedPhotonHcalIsol_*_*", "keep *_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*", "keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*", "keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*", "keep *_hltL1NonIsoHLTClusterShape_*_*", "keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1NonIsoPhotonHollowTrackIsol_*_*", "keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1NonIsolatedPhotonEcalIsol_*_*", "keep *_hltL1NonIsolatedPhotonHcalIsol_*_*", "keep *_hltL1extraParticles_*_*", "keep *_hltL1sDoubleLooseIsoTau15_*_*", "keep *_hltL1sSingleLooseIsoTau20_*_*", "keep *_hltL25TauConeIsolation_*_*", "keep *_hltL25TauCtfWithMaterialTracks_*_*", "keep *_hltL25TauJetTracksAssociator_*_*", "keep *_hltL25TauLeadingTrackPtCutSelector_*_*", "keep *_hltL2MuonCandidatesNoVtx_*_*", "keep *_hltL2MuonCandidates_*_*", "keep *_hltL2MuonIsolations_*_*", "keep *_hltL2MuonSeeds_*_*", "keep *_hltL2Muons_*_*", "keep *_hltL2TauJets_*_*", "keep *_hltL2TauNarrowConeIsolationProducer_*_*", "keep *_hltL2TauRelaxingIsolationSelector_*_*", "keep *_hltL3MuonCandidatesNoVtx_*_*", "keep *_hltL3MuonCandidates_*_*", "keep *_hltL3MuonIsolations_*_*", "keep *_hltL3MuonsIOHit_*_*", "keep *_hltL3MuonsLinksCombination_*_*", "keep *_hltL3MuonsNoVtx_*_*", "keep *_hltL3MuonsOIHit_*_*", "keep *_hltL3MuonsOIState_*_*", "keep *_hltL3Muons_*_*", "keep *_hltL3TauConeIsolation_*_*", "keep *_hltL3TauCtfWithMaterialTracks_*_*", "keep *_hltL3TauIsolationSelector_*_*", "keep *_hltL3TauJetTracksAssociator_*_*", "keep *_hltL3TkFromL2OICombination_*_*", "keep *_hltL3TkTracksFromL2IOHit_*_*", "keep *_hltL3TkTracksFromL2OIHit_*_*", "keep *_hltL3TkTracksFromL2OIState_*_*", "keep *_hltL3TkTracksFromL2_*_*", "keep *_hltL3TrackCandidateFromL2IOHit_*_*", "keep *_hltL3TrackCandidateFromL2OIHit_*_*", "keep *_hltL3TrackCandidateFromL2OIState_*_*", "keep *_hltL3TrackCandidateFromL2_*_*", "keep *_hltL3TrajSeedIOHit_*_*", "keep *_hltL3TrajSeedOIHit_*_*", "keep *_hltL3TrajSeedOIState_*_*", "keep *_hltL3TrajectorySeedNoVtx_*_*", "keep *_hltL3TrajectorySeed_*_*", "keep *_hltMet_*_*", "keep *_hltMuTrackJpsiCtfTrackCands_*_*", "keep *_hltMuTrackJpsiCtfTracks_*_*", "keep *_hltMuTrackJpsiPixelTrackCands_*_*", "keep *_hltMuTrackJpsiPixelTrackSelector_*_*", "keep *_hltMuTrackJpsiTrackSeeds_*_*", "keep *_hltMuonRPCDigis_*_*", "keep *_hltOfflineBeamSpot_*_*", "keep *_hltPixelMatchElectronsL1Iso_*_*", "keep *_hltPixelMatchElectronsL1NonIso_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*", "keep *_hltPixelTracks_*_*", "keep *_hltPixelVertices_*_*", "keep *_hltRpcRecHits_*_*", "keep *_hltSiPixelRecHits_*_*", "keep *_hltSiStripClusters_*_*", "keep *_hltSiStripRawToClustersFacility_*_*", "keep *_hltTowerMakerForAll_*_*", "keep *_hltTowerMakerForMuons_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEventWithRefs_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputALCAP0 = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_EcalEta_v3", "AlCa_EcalPi0_v4" )
  ),
  outputCommands = cms.untracked.vstring( "drop *", "keep *_hltAlCaEtaRecHitsFilter_*_*", "keep *_hltAlCaPi0RecHitsFilter_*_*", "keep *_hltESRegionalPi0EtaRecHit_*_*", "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputALCAPHISYM = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_EcalPhiSym_v2" )
  ),
  outputCommands = cms.untracked.vstring( "drop *", "keep *_hltAlCaPhiSymStream_*_*", "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputNanoDST = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_Physics_NanoDST_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltFEDSelector_*_*", "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*", "keep L1MuGMTReadoutCollection_hltGtDigis_*_*", "keep edmTriggerResults_*_*_*" )
)
process.hltOutputOnlineErrors = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_DTErrors_v1", "HLT_LogMonitor_v1" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltL1GtObjectMap_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputRPCMON = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_RPCMuonNoHits_v2", "AlCa_RPCMuonNoTriggers_v2", "AlCa_RPCMuonNormalisation_v2" )
  ),
  outputCommands = cms.untracked.vstring( "drop *", "keep *_hltCscSegments_*_*", "keep *_hltDt4DSegments_*_*", "keep *_hltMuonCSCDigis_*_*", "keep *_hltMuonDTDigis_*_*", "keep *_hltMuonRPCDigis_*_*", "keep *_hltRpcRecHits_*_*", "keep L1GlobalTriggerReadoutRecord_*_*_*", "keep L1MuGMTCands_hltGtDigis_*_*", "keep L1MuGMTReadoutCollection_hltGtDigis_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot + process.hltOfflineBeamSpot )
process.HLTBeginSequenceBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.hltBPTXCoincidence + process.HLTBeamSpot )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTDoRegionalPi0EtaSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalPi0EtaFEDs + process.hltESRegionalPi0EtaRecHit + process.hltEcalRegionalPi0EtaRecHit )
process.HLTmuonlocalrecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoLocalPixelLight = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )
process.HLTBeginSequenceCalibration = cms.Sequence( process.hltCalibrationEventsFilter + process.hltGtDigis )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.HLTmuonlocalrecoSequence + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTL2muonrecoSequence = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidates )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelRecHits )
process.HLTL3muonTkCandidateSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrajSeedOIState + process.hltL3TrackCandidateFromL2OIState + process.hltL3TkTracksFromL2OIState + process.hltL3MuonsOIState + process.hltL3TrajSeedOIHit + process.hltL3TrackCandidateFromL2OIHit + process.hltL3TkTracksFromL2OIHit + process.hltL3MuonsOIHit + process.hltL3TkFromL2OICombination + process.hltL3TrajSeedIOHit + process.hltL3TrackCandidateFromL2IOHit + process.hltL3TkTracksFromL2IOHit + process.hltL3MuonsIOHit + process.hltL3TrajectorySeed + process.hltL3TrackCandidateFromL2 )
process.HLTL3muonrecoNocandSequence = cms.Sequence( process.HLTL3muonTkCandidateSequence + process.hltL3TkTracksFromL2 + process.hltL3MuonsLinksCombination + process.hltL3Muons )
process.HLTL3muonrecoSequence = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltL3MuonCandidates )
process.HLTDoRegionalEgammaEcalSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalEgammaFEDs + process.hltEcalRegionalEgammaRecHit + process.hltESRegionalEgammaRecHit )
process.HLTMulti5x5SuperClusterL1Isolated = cms.Sequence( process.hltMulti5x5BasicClustersL1Isolated + process.hltMulti5x5SuperClustersL1Isolated + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated )
process.HLTL1IsolatedEcalClustersSequence = cms.Sequence( process.hltHybridSuperClustersL1Isolated + process.hltCorrectedHybridSuperClustersL1Isolated + process.HLTMulti5x5SuperClusterL1Isolated )
process.HLTMulti5x5SuperClusterL1NonIsolated = cms.Sequence( process.hltMulti5x5BasicClustersL1NonIsolated + process.hltMulti5x5SuperClustersL1NonIsolated + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated )
process.HLTL1NonIsolatedEcalClustersSequence = cms.Sequence( process.hltHybridSuperClustersL1NonIsolated + process.hltCorrectedHybridSuperClustersL1NonIsolatedTemp + process.hltCorrectedHybridSuperClustersL1NonIsolated + process.HLTMulti5x5SuperClusterL1NonIsolated )
process.HLTEgammaR9ShapeSequence = cms.Sequence( process.hltL1IsoR9shape + process.hltL1NonIsoR9shape )
process.HLTDoLocalHcalWithoutHOSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco )
process.HLTEle8Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltEGRegionalL1SingleEG5 + process.hltEG8EtFilter + process.HLTEgammaR9ShapeSequence + process.hltEle8R9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltEle8HEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltEle8PixelMatchFilter )
process.HLTBeginSequenceNZS = cms.Sequence( process.hltTriggerType + process.hltL1EventNumberNZS + process.HLTL1UnpackerSequence + process.hltBPTXCoincidence + process.HLTBeamSpot )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTRecoJetSequenceAK5Uncorrected = cms.Sequence( process.HLTDoCaloSequence + process.hltAntiKT5CaloJets )
process.HLTRecoJetSequenceAK5Corrected = cms.Sequence( process.HLTRecoJetSequenceAK5Uncorrected + process.hltAntiKT5L2L3CorrCaloJets + process.hltJetIDPassedCorrJets )
process.HLTDoRegionalJetEcalSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalJetsFEDs + process.hltEcalRegionalJetsRecHit )
process.HLTRegionalTowerMakerForJetsSequence = cms.Sequence( process.HLTDoRegionalJetEcalSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForJets )
process.HLTRegionalRecoJetSequenceAK5Corrected = cms.Sequence( process.HLTRegionalTowerMakerForJetsSequence + process.hltAntiKT5CaloJetsRegional + process.hltAntiKT5L2L3CorrCaloJetsRegional + process.hltL1MatchedJetsRegional + process.hltJetIDPassedJetsRegional )
process.HLTBeginSequenceAntiBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.hltBPTXAntiCoincidence + process.HLTBeamSpot )
process.HLTL2muonrecoSequenceNoVtx = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidatesNoVtx )
process.HLTMuTrackJpsiPixelRecoSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.hltPixelTracks + process.hltMuTrackJpsiPixelTrackSelector + process.hltMuTrackJpsiPixelTrackCands )
process.HLTMuTrackJpsiTrackRecoSequence = cms.Sequence( process.HLTDoLocalStripSequence + process.hltMuTrackJpsiTrackSeeds + process.hltMuTrackJpsiCkfTrackCandidates + process.hltMuTrackJpsiCtfTracks + process.hltMuTrackJpsiCtfTrackCands )
process.HLTMuTkMuJpsiTkMuRecoSequence = cms.Sequence( process.hltMuTkMuJpsiTrackerMuons + process.hltMuTkMuJpsiTrackerMuonCands )
process.HLTPhoton10CaloIdVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltEGRegionalL1SingleEG5 + process.hltEG10EtFilter )
process.HLTPhoton15CaloIdVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltEGRegionalL1SingleEG5 + process.hltEG15EtFilterFromEG5 )
process.HLTRecopixelvertexingForHighMultLooseSequence = cms.Sequence( process.hltPixelTracksForHighMultLoose + process.hltPixelVerticesForHighMultLoose )
process.HLTBeginSequenceRandom = cms.Sequence( process.hltRandomEventsFilter + process.hltGtDigis )
process.HLTPixelTrackingForMinBiasSequence = cms.Sequence( process.hltPixelTracksForMinBias )

process.AlCa_EcalPhiSym_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreAlCaEcalPhiSym + process.hltEcalRawToRecHitFacility + process.hltESRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.hltAlCaPhiSymStream + process.HLTEndSequence )
process.AlCa_EcalEta_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaEcalPi0Eta + process.hltPreAlCaEcalEta + process.HLTDoRegionalPi0EtaSequence + process.hltSimple3x3Clusters + process.hltAlCaEtaRecHitsFilter + process.HLTEndSequence )
process.AlCa_EcalPi0_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaEcalPi0Eta + process.hltPreAlCaEcalPi0 + process.HLTDoRegionalPi0EtaSequence + process.hltSimple3x3Clusters + process.hltAlCaPi0RecHitsFilter + process.HLTEndSequence )
process.AlCa_RPCMuonNoHits_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNoHits + process.HLTmuonlocalrecoSequence + process.hltRPCPointProducer + process.hltRPCFilter + process.HLTEndSequence )
process.AlCa_RPCMuonNoTriggers_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNoTriggers + process.hltRPCMuonNoTriggersL1Filtered0 + process.HLTmuonlocalrecoSequence + process.HLTEndSequence )
process.AlCa_RPCMuonNormalisation_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNorma + process.hltRPCMuonNormaL1Filtered0 + process.HLTmuonlocalrecoSequence + process.HLTEndSequence )
process.HLT_BeamGas_BSC_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1BeamGasBsc + process.hltPreL1BeamGasBsc + process.HLTDoLocalPixelLight + process.hltPixelActivityFilter + process.hltPixelAsymmetryFilter + process.HLTEndSequence )
process.HLT_BeamGas_HF_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1BeamGasHf + process.hltPreL1BeamGasHf + process.hltHcalDigis + process.hltHfreco + process.hltHFAsymmetryFilter + process.HLTEndSequence )
process.HLT_BeamHalo_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1BeamHalo + process.hltPreL1BeamHalo + process.HLTDoLocalPixelLight + process.hltPixelActivityFilterForHalo + process.HLTDoLocalStripSequence + process.hltTrackerHaloFilter + process.HLTEndSequence )
process.HLT_Calibration_v1 = cms.Path( process.HLTBeginSequenceCalibration + process.hltPreCalibration + process.HLTEndSequence )
process.HLT_DTErrors_v1 = cms.Path( process.hltGtDigis + process.hltPreAlCaDTErrors + process.hltDTROMonitorFilter + process.hltDynAlCaDTErrors + process.HLTEndSequence )
process.HLT_DoubleMu3_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreDoubleMu3 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDiMuonL3PreFiltered3 + process.HLTEndSequence )
process.HLT_EcalCalibration_v1 = cms.Path( process.hltCalibrationEventsFilter + process.hltGtDigis + process.hltPreEcalCalibration + process.hltEcalCalibrationRaw + process.HLTEndSequence )
process.HLT_Ele8_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG5 + process.hltPreEle8 + process.HLTEle8Sequence + process.HLTEndSequence )
process.HLT_GlobalRunHPDNoise_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sGlobalRunHPDNoise + process.hltPreGlobalRunHPDNoise + process.HLTEndSequence )
process.HLT_HcalCalibration_v1 = cms.Path( process.hltCalibrationEventsFilter + process.hltGtDigis + process.hltPreHcalCalibration + process.hltHcalCalibTypeFilter + process.HLTEndSequence )
process.HLT_HcalNZS_v3 = cms.Path( process.HLTBeginSequenceNZS + process.hltL1sHcalNZS + process.hltPreHcalNZS + process.HLTEndSequence )
process.HLT_HcalPhiSym_v3 = cms.Path( process.HLTBeginSequenceNZS + process.hltL1sHcalPhiSym + process.hltPreHcalPhiSym + process.HLTEndSequence )
process.HLT_IsoTrackHB_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet52 + process.hltPreIsoTrackHB + process.HLTDoLocalPixelSequence + process.hltHITPixelTracksHB + process.hltHITPixelVerticesHB + process.hltIsolPixelTrackProdHB + process.hltIsolPixelTrackL2FilterHB + process.HLTDoLocalStripSequence + process.hltHITPixelTripletSeedGeneratorHB + process.hltHITCkfTrackCandidatesHB + process.hltHITCtfWithMaterialTracksHB + process.hltHITIPTCorrectorHB + process.hltIsolPixelTrackL3FilterHB + process.HLTEndSequence )
process.HLT_IsoTrackHE_v3 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet52 + process.hltPreIsoTrackHE + process.HLTDoLocalPixelSequence + process.hltHITPixelTracksHB + process.hltHITPixelTracksHE + process.hltHITPixelVerticesHE + process.hltIsolPixelTrackProdHE + process.hltIsolPixelTrackL2FilterHE + process.HLTDoLocalStripSequence + process.hltHITPixelTripletSeedGeneratorHE + process.hltHITCkfTrackCandidatesHE + process.hltHITCtfWithMaterialTracksHE + process.hltHITIPTCorrectorHE + process.hltIsolPixelTrackL3FilterHE + process.HLTEndSequence )
process.HLT_Jet20_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet8 + process.hltPreJet20 + process.HLTRecoJetSequenceAK5Corrected + process.hltSingleJet20 + process.HLTEndSequence )
process.HLT_Jet40_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet16 + process.hltPreJet40 + process.HLTRecoJetSequenceAK5Corrected + process.hltSingleJet40 + process.HLTEndSequence )
process.HLT_Jet60_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36 + process.hltPreJet60 + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltSingleJet60Regional + process.HLTEndSequence )
process.HLT_L1DoubleForJet32_EtaOpp_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet32EtaOpp + process.hltPreL1DoubleForJet32EtaOpp + process.HLTEndSequence )
process.HLT_L1DoubleForJet8_EtaOpp_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet8EtaOpp + process.hltPreL1DoubleForJet8EtaOpp + process.HLTEndSequence )
process.HLT_L1DoubleMu0_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreL1DoubleMu0 + process.hltDiMuonL1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleEG12_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG12 + process.hltPreL1SingleEG12 + process.HLTEndSequence )
process.HLT_L1SingleEG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG5 + process.hltPreL1SingleEG5 + process.HLTEndSequence )
process.HLT_L1SingleJet36_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36 + process.hltPreL1SingleJet36 + process.HLTEndSequence )
process.HLT_L1SingleMuOpen_AntiBPTX_v1 = cms.Path( process.HLTBeginSequenceAntiBPTX + process.hltL1sL1SingleMuOpen + process.hltPreL1MuOpenAntiBPTX + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleMuOpen_DT_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpen + process.hltPreL1SingleMuOpenDT + process.hltL1MuOpenL1FilteredDT + process.HLTEndSequence )
process.HLT_L1SingleMuOpen_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpen + process.hltPreL1SingleMuOpen + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_L1Tech_BSC_halo_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sZeroBias + process.hltPreL1TechBSChalo + process.hltL1TechBSChalo + process.HLTEndSequence )
process.HLT_L1Tech_HBHEHO_totalOR_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sTechTrigHCALNoise + process.hltPreTechTrigHCALNoise + process.HLTEndSequence )
process.HLT_L1TrackerCosmics_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sTrackerCosmics + process.hltPreTrackerCosmics + process.hltTrackerCosmicsPattern + process.HLTEndSequence )
process.HLT_L1_Interbunch_BSC_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1InterbunchBsc + process.hltPreL1Interbunch1 + process.HLTEndSequence )
process.HLT_L1_PreCollisions_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1PreCollisions + process.hltPreL1PreCollisions + process.HLTEndSequence )
process.HLT_L2DoubleMu0_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreL2DoubleMu0 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTEndSequence )
process.HLT_L3MuonsCosmicTracking_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sTrackerCosmics + process.hltPreL3MuonsCosmicTracking + process.hltTrackerCosmicsPattern + process.hltL1sL1SingleMuOpenCandidate + process.hltL1MuORL1Filtered0 + process.HLTL2muonrecoSequenceNoVtx + process.hltSingleL2MuORL2PreFilteredNoVtx + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrajectorySeedNoVtx + process.hltL3TrackCandidateFromL2NoVtx + process.hltL3TkTracksFromL2NoVtx + process.hltL3MuonsNoVtx + process.hltL3MuonCandidatesNoVtx + process.hltMu5NoVertexL3PreFiltered5 + process.HLTEndSequence )
process.HLT_LogMonitor_v1 = cms.Path( process.hltGtDigis + process.hltPreLogMonitor + process.hltLogMonitorFilter + process.HLTEndSequence )
process.HLT_L1BscMinBiasORBptxPlusANDMinus_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreL1BscMinBiasORBptxPlusANDMinus + process.HLTEndSequence )
process.HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu5BQ7 + process.hltPreMu5TkMu0JpsiTightB5Q7 + process.hltMu5TrackJpsiL1Filtered0Eta15 + process.HLTL2muonrecoSequence + process.hltMu5TrackJpsiL2Filtered5Eta15 + process.HLTL3muonrecoSequence + process.hltMu5TrackJpsiL3Filtered5Eta15 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu5TrackJpsiPixelMassFilteredEta15 + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu5TkMuJpsiTrackMassFiltered + process.HLTMuTkMuJpsiTkMuRecoSequence + process.hltMu5TkMuJpsiTkMuMassFilteredTight + process.HLTEndSequence )
process.HLT_Mu0_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpen + process.hltPreMu0 + process.hltSingleMuOpenL1Filtered + process.HLTL2muonrecoSequence + process.hltSingleMu0L2Filtered0 + process.HLTL3muonrecoSequence + process.hltSingleMu0L3Filtered0 + process.HLTEndSequence )
process.HLT_Mu3_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpen + process.hltPreMu3 + process.hltSingleMuOpenL1Filtered + process.HLTL2muonrecoSequence + process.hltSingleMu3L2Filtered0 + process.HLTL3muonrecoSequence + process.hltSingleMu3L3Filtered3 + process.HLTEndSequence )
process.HLT_Mu5_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltPreMu5 + process.hltL1SingleMu3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu5L2Filtered3 + process.HLTL3muonrecoSequence + process.hltSingleMu5L3Filtered5 + process.HLTEndSequence )
process.HLT_Photon10_CaloIdVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG5 + process.hltPrePhoton10CaloIdVL + process.HLTPhoton10CaloIdVLSequence + process.HLTEndSequence )
process.HLT_Photon15_CaloIdVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG5 + process.hltPrePhoton15CaloIdVL + process.HLTPhoton15CaloIdVLSequence + process.HLTEndSequence )
process.HLT_Physics_NanoDST_v1 = cms.Path( process.HLTBeginSequence + process.hltPrePhysicsNanoDST + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity50_Loose = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT50 + process.hltPrePixelTracksMultiplicity50 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForHighMultLooseSequence + process.hltPixelCandsForHighMultLoose + process.hlt1HighMult50 + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity60_Loose = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT60 + process.hltPrePixelTracksMultiplicity60 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForHighMultLooseSequence + process.hltPixelCandsForHighMultLoose + process.hlt1HighMult60 + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity70_Loose = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT70 + process.hltPrePixelTracksMultiplicity70 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForHighMultLooseSequence + process.hltPixelCandsForHighMultLoose + process.hlt1HighMult70 + process.HLTEndSequence )
process.HLT_Random_v1 = cms.Path( process.HLTBeginSequenceRandom + process.hltPreRandom + process.HLTEndSequence )
process.HLT_RegionalCosmicTracking_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sTrackerCosmics + process.hltPreRegionalCosmicTracking + process.hltTrackerCosmicsPattern + process.hltL1sL1SingleMuOpenCandidate + process.hltL1MuORL1Filtered0 + process.HLTL2muonrecoSequenceNoVtx + process.hltSingleL2MuORL2PreFilteredNoVtx + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltRegionalCosmicTrackerSeeds + process.hltRegionalCosmicCkfTrackCandidates + process.hltRegionalCosmicTracks + process.hltCosmicTrackSelector + process.HLTEndSequence )
process.HLT_TrackerCalibration_v1 = cms.Path( process.HLTBeginSequenceCalibration + process.hltPreTrackerCalibration + process.hltLaserAlignmentEventFilter + process.HLTEndSequence )
process.HLT_ZeroBiasPixel_SingleTrack_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBiasPixel + process.hltPreZeroBiasPixelSingleTrack + process.HLTDoLocalPixelSequence + process.HLTPixelTrackingForMinBiasSequence + process.hltPixelCandsForMinBias + process.hltMinBiasPixelFilter1 + process.HLTEndSequence )
process.HLT_ZeroBias_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreZeroBias + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolTrue )

process.AOutput = cms.EndPath( process.hltOutputA )
process.ExpressOutput = cms.EndPath( process.hltPreExpressOutput + process.hltPreExpressOutputSmart + process.hltOutputExpress )
process.CalibrationOutput = cms.EndPath( process.hltPreCalibrationOutput + process.hltOutputCalibration )
process.EcalCalibrationOutput = cms.EndPath( process.hltPreEcalCalibrationOutput + process.hltOutputEcalCalibration )
process.DQMOutput = cms.EndPath( process.hltDQML1Scalers + process.hltDQML1SeedLogicScalers + process.hltDQMHLTScalers + process.hltPreDQMOutput + process.hltPreDQMOutputSmart + process.hltOutputDQM )
process.HLTDQMOutput = cms.EndPath( process.hltPreHLTDQMOutput + process.hltPreHLTDQMOutputSmart + process.hltOutputHLTDQM )
process.HLTDQMResultsOutput = cms.EndPath( process.hltPreHLTDQMResultsOutput + process.hltOutputHLTDQMResults )
process.HLTMONOutput = cms.EndPath( process.hltPreHLTMONOutput + process.hltPreHLTMONOutputSmart + process.hltOutputHLTMON )
process.ALCAP0Output = cms.EndPath( process.hltPreALCAP0Output + process.hltOutputALCAP0 )
process.ALCAPHISYMOutput = cms.EndPath( process.hltPreALCAPHISYMOutput + process.hltOutputALCAPHISYM )
process.NanoDSTOutput = cms.EndPath( process.hltPreNanoDSTOutput + process.hltOutputNanoDST )
process.OnlineErrorsOutput = cms.EndPath( process.hltPreOnlineErrorsOutput + process.hltOutputOnlineErrors )
process.RPCMONOutput = cms.EndPath( process.hltPreRPCMONOutput + process.hltOutputRPCMON )

process.HLTSchedule = cms.Schedule( process.AlCa_EcalPhiSym_v2, process.AlCa_EcalEta_v3, process.AlCa_EcalPi0_v4, process.AlCa_RPCMuonNoHits_v2, process.AlCa_RPCMuonNoTriggers_v2, process.AlCa_RPCMuonNormalisation_v2, process.HLT_BeamGas_BSC_v2, process.HLT_BeamGas_HF_v2, process.HLT_BeamHalo_v2, process.HLT_Calibration_v1, process.HLT_DTErrors_v1, process.HLT_DoubleMu3_v3, process.HLT_EcalCalibration_v1, process.HLT_Ele8_v2, process.HLT_GlobalRunHPDNoise_v2, process.HLT_HcalCalibration_v1, process.HLT_HcalNZS_v3, process.HLT_HcalPhiSym_v3, process.HLT_IsoTrackHB_v2, process.HLT_IsoTrackHE_v3, process.HLT_Jet20_v1, process.HLT_Jet40_v1, process.HLT_Jet60_v1, process.HLT_L1DoubleForJet32_EtaOpp_v1, process.HLT_L1DoubleForJet8_EtaOpp_v1, process.HLT_L1DoubleMu0_v1, process.HLT_L1SingleEG12_v1, process.HLT_L1SingleEG5_v1, process.HLT_L1SingleJet36_v1, process.HLT_L1SingleMuOpen_AntiBPTX_v1, process.HLT_L1SingleMuOpen_DT_v1, process.HLT_L1SingleMuOpen_v1, process.HLT_L1Tech_BSC_halo_v1, process.HLT_L1Tech_HBHEHO_totalOR_v1, process.HLT_L1TrackerCosmics_v2, process.HLT_L1_Interbunch_BSC_v1, process.HLT_L1_PreCollisions_v1, process.HLT_L2DoubleMu0_v2, process.HLT_L3MuonsCosmicTracking_v1, process.HLT_LogMonitor_v1, process.HLT_L1BscMinBiasORBptxPlusANDMinus_v1, process.HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1, process.HLT_Mu0_v3, process.HLT_Mu3_v3, process.HLT_Mu5_v3, process.HLT_Photon10_CaloIdVL_v1, process.HLT_Photon15_CaloIdVL_v1, process.HLT_Physics_NanoDST_v1, process.HLT_PixelTracks_Multiplicity50_Loose, process.HLT_PixelTracks_Multiplicity60_Loose, process.HLT_PixelTracks_Multiplicity70_Loose, process.HLT_Random_v1, process.HLT_RegionalCosmicTracking_v1, process.HLT_TrackerCalibration_v1, process.HLT_ZeroBiasPixel_SingleTrack_v1, process.HLT_ZeroBias_v1, process.HLTriggerFinalPath, process.AOutput, process.ExpressOutput, process.CalibrationOutput, process.EcalCalibrationOutput, process.DQMOutput, process.HLTDQMOutput, process.HLTDQMResultsOutput, process.HLTMONOutput, process.ALCAP0Output, process.ALCAPHISYMOutput, process.NanoDSTOutput, process.OnlineErrorsOutput, process.RPCMONOutput )
