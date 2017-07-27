class MgrDrawED { // Manager intended for drawing of Electronic detector (2D) events

  constructor() {

    this._canvasesMain = [null, null];  // Array of two svg main canvases for XZ & YZ views of ED events
                                        // Each main canvas contains axes, titles, and embedded canvas with event picture

    this._canvasesEmb  = [null, null];  // Array of two svg embedded canvases

    // Fixed aspect ratio of the displayed OPERA world
    this._aspectRatio = (DetCfg.globDetBounds().xyzMax[2] -
                         DetCfg.globDetBounds().xyzMin[2])/
                        (DetCfg.globDetBounds().xyzMax[0] - 
                         DetCfg.globDetBounds().xyzMin[0]);

    // Height and width are the same for the both ED canvases!
    this._canvMainHeight = 320; // Fixed!

    this._canvMainWidth = this._canvMainHeight*this._aspectRatio;

    this._axesOffsets = {

      leftW:   50, //px
      rightW:   0, //px
      topW:    20,
      bottomW: 35  //px

    };
  
    this._canvEmbOffsets = {

      leftW:   this._axesOffsets.leftW + 10,   //px
      rightW:  10,                             //px
      topW:    10,                             //px
      bottomW: this._axesOffsets.bottomW + 10  //px

    };

    this._canvEmbHeight = this._canvMainHeight - 
                          this._canvEmbOffsets.topW -
                          this._canvEmbOffsets.bottomW;

    this._canvEmbWidth  = this._canvMainWidth - 
                          this._canvEmbOffsets.leftW -
                          this._canvEmbOffsets.rightW;

    this._zoom = 1;  // Initial zoom for the canvases (full detector view)

    this._zoomMax = 60;

    this._zoomFarViewMax = 5; // Needed to display hits and bricks in different way

    this._zoomFactor = 1.25;

    this._moveFactor = [0.2, 0.2, 0.2];

    this._zoomIsChanged = 1;

    this._viewIsChanged = 1;

    this._sm = 0;             // Needed to draw bricks only in one OPERA super-module (SM)

    // Coefficient for convertation of pixels to cm
    this._coefPixToCM = 0;

    // init value for zoom=1
    this._initCoefPixToCM = (DetCfg.globDetBounds().xyzMax[2] -
                             DetCfg.globDetBounds().xyzMin[2])/this._canvMainWidth;

    this._currViewBounds = {}; // Current view bounds of the canvases for the selected zoom

    // init value for zoom=1
    this._initViewBounds = {

      xyzMin: [

        DetCfg.globDetBounds().xyzMin[0],
        DetCfg.globDetBounds().xyzMin[1],
        DetCfg.globDetBounds().xyzMin[2]

      ],

      xyzMax: [

        DetCfg.globDetBounds().xyzMax[0],
        DetCfg.globDetBounds().xyzMax[1],
        DetCfg.globDetBounds().xyzMax[2]

      ]

    };

    // Bounds of a current event
    this._currEventBounds = {};

    // Start values to search for bounds of a current event
    this._initEventBounds = {

      xyzMin1: [

        DetCfg.globDetBounds().xyzMax[0],
        DetCfg.globDetBounds().xyzMax[1],
        DetCfg.globDetBounds().xyzMax[2]

      ],

      xyzMax1: [

        DetCfg.globDetBounds().xyzMin[0],
        DetCfg.globDetBounds().xyzMin[1],
        DetCfg.globDetBounds().xyzMin[2]

      ],

      xyzMin2: [ // Min2 and Max2 are needed to exclude from event area far distant single hits

        DetCfg.globDetBounds().xyzMax[0],
        DetCfg.globDetBounds().xyzMax[1],
        DetCfg.globDetBounds().xyzMax[2]

      ],

      xyzMax2: [

        DetCfg.globDetBounds().xyzMin[0],
        DetCfg.globDetBounds().xyzMin[1],
        DetCfg.globDetBounds().xyzMin[2]

      ]

    };

    this._scalesOfAxes = []; // Scales for the X, Y, and Z axes

    // init value for zoom=1
    this._initScalesOfAxes = [

      d3.scaleLinear()
        .domain([this._initViewBounds.xyzMin[0] +
                 this._initCoefPixToCM*this._axesOffsets.bottomW,
                 this._initViewBounds.xyzMax[0] -
                 this._initCoefPixToCM*this._axesOffsets.topW])
        .range([this._canvMainHeight - this._axesOffsets.bottomW,
                this._axesOffsets.topW]),

      d3.scaleLinear()
        .domain([this._initViewBounds.xyzMin[1] +
                 this._initCoefPixToCM*this._axesOffsets.bottomW,
                 this._initViewBounds.xyzMax[1] -
                 this._initCoefPixToCM*this._axesOffsets.topW])
        .range([this._canvMainHeight - this._axesOffsets.bottomW,
                this._axesOffsets.topW]),

      d3.scaleLinear()
        .domain([this._initViewBounds.xyzMin[2] +
                 this._initCoefPixToCM*this._axesOffsets.leftW,
                 this._initViewBounds.xyzMax[2] -
                 this._initCoefPixToCM*this._axesOffsets.rightW])
        .range([this._axesOffsets.leftW, this._canvMainWidth -
                this._axesOffsets.rightW])

    ];

    this._scalesOfCanvEmb = [];   // Scales for X, Y, and Z of the embedded canvases

    // init value for zoom=1
    this._initScalesOfCanvEmb = [

      d3.scaleLinear()
        .domain([this._initViewBounds.xyzMin[0] +
                 this._initCoefPixToCM*this._canvEmbOffsets.bottomW,
                 this._initViewBounds.xyzMax[0] -
                 this._initCoefPixToCM*this._canvEmbOffsets.topW])
        .range([this._canvEmbHeight, 0]),

      d3.scaleLinear()
        .domain([this._initViewBounds.xyzMin[1] +
                 this._initCoefPixToCM*this._canvEmbOffsets.bottomW,
                 this._initViewBounds.xyzMax[1] -
                 this._initCoefPixToCM*this._canvEmbOffsets.topW])
        .range([this._canvEmbHeight, 0]),

      d3.scaleLinear()
        .domain([this._initViewBounds.xyzMin[2] +
                 this._initCoefPixToCM*this._canvEmbOffsets.leftW,
                 this._initViewBounds.xyzMax[2] - 
                 this._initCoefPixToCM*this._canvEmbOffsets.rightW])
        .range([0, this._canvEmbWidth])

    ];

    this._groupXYAxesIDs = [

      "groupXYAxesXZ",
      "groupXYAxesYZ"

    ];

    this._groupZAxesIDs = [

      "groupZAxesXZ",
      "groupZAxesYZ"

    ];

    this._groupTTWallsIDs = [

      "groupTTWallsXZ",
      "groupTTWallsYZ"

    ];

    this._groupBrickWallsIDs = [

      "groupBrickWallsXZ",
      "groupBrickWallsYZ"

    ];

    this._groupRPCLayersIDs = [

      "groupRPCLayersXZ",
      "groupRPCLayersYZ"

    ];

    this._groupDTLayersIDs = [

      "groupDTLayersXZ",
      "groupDTLayersYZ"

    ];

    this._groupVisBricksIDs = [

      "groupVisBricksXZ",
      "groupVisBricksYZ"

    ];

    this._groupVertBrickIDs = [

      "groupVertBrickXZ",
      "groupVertBrickYZ"

    ];

    this._groupTTHitsIDs = [

      "groupTTHitsXZ",
      "groupTTHitsYZ"

    ];

    this._groupRPCHitsIDs = [

      "groupRPCHitsXZ",
      "groupRPCHitsYZ"

    ];

    this._groupDTHitsIDs = [

      "groupDTHitsXZ",
      ""      // There are no DT hits in YZ view

    ];

    this._groupNeuVertexIDs = [

      "groupNeuVertexXZ",
      "groupNeuVertexYZ"

    ];

    this._groupPartTracksIDs = [

      "groupPartTracksXZ",
      "groupPartTracksYZ"

    ];

    this._groupMuTrackIDs = [

      "groupMuTrackXZ",
      "groupMuTrackYZ"

    ];

    this._axesTitles = [

      "X (cm)",
      "Y (cm)"

    ];

    //Sizes of hits for small zoom (far distance view mode)
    this._hitTTsizeFarView   = 6; // px
    this._hitRPCsizeFarView  = 6; // px
    this._hitDTradiusFarView = 3; // px

    // X, Y, and Z sizes of hits in px!
    this._hitTTdims  = [];
    this._hitRPCdims = [];

    this._trackLinePars = [];  // Array of line parameters used for drawing of the ECC tracks

  };

  canvasesMain(ip) {

    if (ip === undefined) return this._canvasesMain;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::canvasesMain()::Error: ip is wrong: ip = " + ip + "!!!");
      return;
    }

    return this._canvasesMain[ip];

  };

  canvasesEmb(ip) {

    if (ip === undefined) return this._canvasesEmb;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::canvasesEmb()::Error: ip is wrong: ip = " + ip + "!!!");
      return;
    }

    return this._canvasesEmb[ip];

  };

  aspectRatio() { return this._aspectRatio; };

  canvMainWidth()  { return this._canvMainWidth; };
  canvMainHeight() { return this._canvMainHeight; };

  canvEmbWidth()  { return this._canvEmbWidth; };
  canvEmbHeight() { return this._canvEmbHeight; };

  zoom(zz) {

    if (zz === undefined) return this._zoom;

    if (!Utils.checkNumber(zz)) {
      alert("MgrDrawED-def::zoom()::Error: zz is not a number!!!: zz = " + zz + "!!!");
      return;
    }

    if ( (zz < 1) || (zz > 100) ) {
      alert("MgrDrawED-def::zoom()::Error: zz is strange!!!: zz = " + zz + "!!!");
      return;
    }

    this._zoom = zz;

  }; 

  zoomFactor() { return this._zoomFactor; };

  zoomMax() { return this._zoomMax; };

  zoomFarViewMax() { return this._zoomFarViewMax; };

  moveFactor(ip) {

    if (ip === undefined) return this._moveFactor;

    if (!Utils.checkIP(ip, 3)) {
      alert("MgrDrawED-def::moveFactor()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._moveFactor[ip];

  };

  zoomIsChanged(zc) {

    if (zc === undefined) return this._zoomIsChanged;

    if (!Utils.checkNumber(zc)) {
      alert("MgrDrawED-def::zoomIsChanged()::Error: zc is not a number!!!: zc = " + zc + "!!!");
      return;
    }

    if ( (zc != 0) && (zc != 1) ) {
      alert("MgrDrawED-def::zoomIsChanged()::Error: zc is strange!!!: zc = " + zc + "!!!");
      return;
    }

    this._zoomIsChanged = zc;

  };

  viewIsChanged(vc) {

    if (vc === undefined) return this._viewIsChanged;

    if (!Utils.checkNumber(vc)) {
      alert("MgrDrawED-def::viewIsChanged()::Error: vc is not a number!!!: vc = " + vc + "!!!");
      return;
    }

    if ( (vc != 0) && (vc != 1) ) {
      alert("MgrDrawED-def::viewIsChanged()::Error: vc is strange!!!: vc = " + vc + "!!!");
      return;
    }

    this._viewIsChanged = vc;

  };

  sm(mn) {

    if (mn === undefined) return this._sm;

    if (!Utils.checkNumber(mn)) {
      alert("MgrDrawED-def::sm()::Error: mn is not a number!!!: mn = " + mn + "!!!");
      return;
    }

    if ( (mn != 1) && (mn != 2) ) {
      alert("MgrDrawED-def::sm()::Error: mn is strange!!!: mn = " + mn + "!!!");
      return;
    }

    this._sm = mn;

  };

  axesOffsets() { return this._axesOffsets; };

  canvEmbOffsets() { return this._canvEmbOffsets; };

  coefPixToCM(coef) {

    if (coef === undefined) return this._coefPixToCM;

    if (!Utils.checkNumber(coef)) {
      alert("MgrDrawED-def::coefPixToCM()::Error: coef is not a number!!!: coef = " + coef + "!!!");
      return;
    }

    if ( (coef <= 0) || (coef > 300) ) {  //MMM 30
      alert("MgrDrawED-def::coefPixToCM()::Error: coef is strange!!!: coef = " + coef + "!!!");
      return;
    }

    this._coefPixToCM = coef;
  };

  initCoefPixToCM() { return this._initCoefPixToCM; };

  scalesOfAxes(scales) {

    if (scales === undefined) return this._scalesOfAxes;

    if (typeof(scales) !== "object") {
      alert("MgrDrawED-def::scalesOfAxes()::Error: scales is not an object!!!: typeof(scales) = " + typeof(scales) + "!!!");
      return;
    }

    this._scalesOfAxes = scales;

  };

  initScalesOfAxes() { return this._initScalesOfAxes; };

  scalesOfCanvEmb(scales) {

    if (scales === undefined) return this._scalesOfCanvEmb;

    if (typeof(scales) !== "object") {
      alert("MgrDrawED-def::scalesOfCanvEmb()::Error: scales is not an object!!!: typeof(scales) = " + typeof(scales) + "!!!");
      return;
    }

    this._scalesOfCanvEmb = scales;

  };

  initScalesOfCanvEmb() { return this._initScalesOfCanvEmb; };

  currViewBounds(currbounds) {

    if (currbounds === undefined) return this._currViewBounds;

    if (typeof(currbounds) !== "object") {
      alert("MgrDrawED-def::currViewBounds()::Error: currbounds is not an object!!!: currbounds = " + currbounds + "!!!");
      return;
    }

    this._currViewBounds = currbounds;
  };

  initViewBounds() { return this._initViewBounds; };

  currEventBounds(currbounds) {

    if (currbounds === undefined) return this._currEventBounds;

    if (typeof(currbounds) !== "object") {
      alert("MgrDrawED-def::currEventBounds()::Error: currbounds is not an object!!!: currbounds = " + currbounds + "!!!");
      return;
    }

    this._currEventBounds = currbounds;
  };

  initEventBounds() { return this._initEventBounds; };

  groupXYAxesIDs(ip) {

    if (ip === undefined) return this._groupXYAxesIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupXYAxesIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupXYAxesIDs[ip];

  };

  groupZAxesIDs(ip) {

    if (ip === undefined) return this._groupZAxesIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupZAxesIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupZAxesIDs[ip];

  };

  groupTTWallsIDs(ip) {

    if (ip === undefined) return this._groupTTWallsIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupTTWallsIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupTTWallsIDs[ip];

  };

  groupBrickWallsIDs(ip) {

    if (ip === undefined) return this._groupBrickWallsIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupBrickWallsIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupBrickWallsIDs[ip];

  };

  groupRPCLayersIDs(ip) {

    if (ip === undefined) return this._groupRPCLayersIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupRPCLayersIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupRPCLayersIDs[ip];

  };

  groupDTLayersIDs(ip) {

    if (ip === undefined) return this._groupDTLayersIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupDTLayersIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupDTLayersIDs[ip];

  };

  groupVisBricksIDs(ip) {

    if (ip === undefined) return this._groupVisBricksIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupVisBricksIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupVisBricksIDs[ip];

  };

  groupVertBrickIDs(ip) {

    if (ip === undefined) return this._groupVertBrickIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupVertBrickIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupVertBrickIDs[ip];

  };

  groupTTHitsIDs(ip) {

    if (ip === undefined) return this._groupTTHitsIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupTTHitsIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupTTHitsIDs[ip];

  };

  groupRPCHitsIDs(ip) {

    if (ip === undefined) return this._groupRPCHitsIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupRPCHitsIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupRPCHitsIDs[ip];

  };

  groupDTHitsIDs(ip) {

    if (ip === undefined) return this._groupDTHitsIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupDTHitsIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupDTHitsIDs[ip];

  };

  groupNeuVertexIDs(ip) {

    if (ip === undefined) return this._groupNeuVertexIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupNeuVertexIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupNeuVertexIDs[ip];

  };

  groupPartTracksIDs(ip) {

    if (ip === undefined) return this._groupPartTracksIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupPartTracksIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupPartTracksIDs[ip];

  };

  groupMuTrackIDs(ip) {

    if (ip === undefined) return this._groupMuTrackIDs;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::groupMuTrackIDs()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._groupMuTrackIDs[ip];

  };

  axesTitles(ip) {

    if (ip === undefined) return this._axesTitles;

    if (!Utils.checkIP(ip)) {
      alert("MgrDrawED-def::axesTitles()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._axesTitles[ip];

  };

  hitTTsizeFarView()   { return this._hitTTsizeFarView; };
  hitRPCsizeFarView()  { return this._hitRPCsizeFarView; };
  hitDTradiusFarView() { return this._hitDTradiusFarView; };

  hitTTdims(ip) {

    if (ip === undefined) return this._hitTTdims;

    if (!Utils.checkIP(ip, 3)) {
      alert("MgrDrawED-def::hitTTdims()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._hitTTdims[ip];

  };

  hitRPCdims(ip) {

    if (ip === undefined) return this._hitRPCdims;

    if (!Utils.checkIP(ip, 3)) {
      alert("MgrDrawED-def::hitRPCdims()::Error: ip is wrong!!!: ip = " + ip + "!!!");
      return;
    }

    return this._hitRPCdims[ip];

  };

  trackLinePars() { return this._trackLinePars; };

};
