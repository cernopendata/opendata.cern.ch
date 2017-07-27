//dmED  == demobbed.mgrDrawED()  !!!
//gmED  == demobbed.mgrGeomED()  !!!
//dmECC == demobbed.mgrDrawECC() !!!
//-----------------------------------

dmED.initGraphics = function() {

  dmED.canvasesMain()[0] = d3.select("#canvas-ED-XZ")
                             .append("svg")
                               .attr("class",  "canvas-bordered")
                               .attr("id",     "canvasMain-ED-XZ")
                               .attr("width",  dmED.canvMainWidth())
                               .attr("height", dmED.canvMainHeight());

  dmED.canvasesMain()[1] = d3.select("#canvas-ED-YZ")
                             .append("svg")
                               .attr("class",  "canvas-bordered")
                               .attr("id",     "canvasMain-ED-YZ")
                               .attr("width",  dmED.canvMainWidth())
                               .attr("height", dmED.canvMainHeight());

  d3.select("#canvasMain-ED-XZ")
    .append("g")
    .attr("id",        "groupCanvasEbm-ED-XZ")
    .attr("transform", "translate(" + dmED.canvEmbOffsets().leftW + ", " +
                                      dmED.canvEmbOffsets().topW + ")");

  dmED.canvasesEmb()[0] = d3.select("#groupCanvasEbm-ED-XZ")
                            .append("svg")
                              .attr("class",  "canvas2D")
                              .attr("id",     "canvasEbm-ED-XZ")
                              .attr("width",  dmED.canvEmbWidth())
                              .attr("height", dmED.canvEmbHeight());

  //dmED.canvasesEmb()[0].on("mousedown", dmED.onMouseDown);

  d3.select("#canvasMain-ED-YZ")
    .append("g")
    .attr("id",        "groupCanvasEbm-ED-YZ")
    .attr("transform", "translate(" + dmED.canvEmbOffsets().leftW + ", " +
                                      dmED.canvEmbOffsets().topW + ")");

  dmED.canvasesEmb()[1] = d3.select("#groupCanvasEbm-ED-YZ")
                            .append("svg")
                              .attr("class",  "canvas2D")
                              .attr("id",     "canvasEbm-ED-YZ")
                              .attr("width",  dmED.canvEmbWidth())
                              .attr("height", dmED.canvEmbHeight());

  dmED.createDrawGroupsAndTitles();

  gmED.genBrickVisPars();
  gmED.findBrickVertexPars();
                            
  dmED.setInitViewParams();

  dmED.initTrackLineProperties();

};
//------------------------------------------------------------------------------

dmED.initTrackLineProperties = function() {

  dmED.trackLinePars()[1] = { // for a track of muon

    color:  TrackECC.colors(1),
    length: 10*DetCfg.brickWallToWallDistZ(),
    //width:  1

  };

  dmED.trackLinePars()[2] = { // for a track of hadron

    color:  TrackECC.colors(2),
    length: 3*DetCfg.brickWallToWallDistZ(),
    //width:  2

  };

};
//------------------------------------------------------------------------------


dmED.onMouseDown = function() {

  // JUST A TEST

  let svgX = d3.mouse(this)[0];
  let svgY = d3.mouse(this)[1];

  let detX = dmED.scalesOfCanvEmb()[0].invert(svgY);
  let detZ = dmED.scalesOfCanvEmb()[2].invert(svgX);

  //console.log("detX = invY = " + detX);

  let hit = demobbed.event().hitsTT()[0][0];

  let selectorHitElID = "#h" + hit.id();

  let hitColor = "red";

  hit.color(hitColor);

  d3.select(selectorHitElID)
    .attr("fill", hitColor);

};
//-----------------------------------------------------------------------------

dmED.createDrawGroupsAndTitles = function() {

  for (let ip = 0; ip < 2; ip++) {

    dmED.canvasesMain(ip).append("text")
                         .attr("transform",
                               "translate(" + (dmED.canvMainWidth() - 50) + ", " +
                                              (dmED.canvMainHeight() - 2) + ")")
  
                         .text("Z (cm)");
  
    dmED.canvasesMain(ip).append("text")
                         .style("text-anchor", "middle")
                         .attr("transform", "rotate(-90)")
                         .attr("x", -50)
                         .attr("y", dmED.axesOffsets().leftW/3)
                         .text(dmED.axesTitles(ip));
  
    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupTTWallsIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupBrickWallsIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupRPCLayersIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupDTLayersIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupVisBricksIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupVertBrickIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupTTHitsIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupRPCHitsIDs(ip));

    if (!ip) dmED.canvasesEmb(0).append("g")
                                .attr("id", dmED.groupDTHitsIDs(0));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupPartTracksIDs(ip));

    dmED.canvasesEmb(ip).append("g")
                        .attr("id", dmED.groupNeuVertexIDs(ip));

  }

};
//-----------------------------------------------------------------------------

dmED.setInitViewParams = function() {

  dmED.coefPixToCM(dmED.initCoefPixToCM());

  $.extend(true, dmED.currViewBounds(), dmED.initViewBounds());

  //dmED.scalesOfAxes(dmED.initScalesOfAxes());
  //dmED.scalesOfCanvEmb(dmED.initScalesOfCanvEmb());

  $.extend(true, dmED.scalesOfAxes(), dmED.initScalesOfAxes());

  $.extend(true, dmED.scalesOfCanvEmb(), dmED.initScalesOfCanvEmb());

  dmED.setFarViewHitSizes();

};
//-----------------------------------------------------------------------------

dmED.onEventChange = function() {

  if (dmED.zoom() !== 1) {

    dmED.zoom(1);

    dmED.zoomIsChanged(1);
    dmED.viewIsChanged(1);

  }

  if (dmED.canvasesMain(0) !== null) gmED.findBrickVertexPars();

  dmED.displayEventInfo();

  dmED.updateCanvases();

};
//-----------------------------------------------------------------------------

dmED.displayEventInfo = function() {

  const evId = demobbed.event().id();

  const inputEvent = document.getElementById("inputEvent");

  inputEvent.value = evId;

  const dateFormatOptions = {

    timeZone: "UTC",
    hour12:    false,

    year:     "numeric",
    month:    "short",
    day:      "2-digit",
    hour:     "2-digit",
    minute:   "2-digit"

  }

  const titleBeg = "Event: " + evId + ", " +
                           demobbed.event().date().toLocaleString("en-US", dateFormatOptions) +
                           " (UTC),";

  $("#canvas-ED-XZ-title").text(titleBeg + " Electronic detectors: TOP VIEW");
  $("#canvas-ED-YZ-title").text(titleBeg + " Electronic detectors: SIDE VIEW");

  $("#canvas-ECC-title").text(titleBeg + " Tracks reconstructed in emulsion");

};
//-----------------------------------------------------------------------------

dmED.checkSM = function() {

  if (dmED.currViewBounds().xyzMin[2] > -300) dmED.sm(2);
  else if (dmED.currViewBounds().xyzMax[2] < 100) dmED.sm(1);

};
//-----------------------------------------------------------------------------

dmED.zoomIn = function() {

  const newZoom = Math.round(1000*dmED.zoom()*dmED.zoomFactor())/1000;

  if (newZoom > dmED.zoomMax()) return;

  dmED.zoom(newZoom);

  dmED.zoomIsChanged(1);
  dmED.viewIsChanged(1);

  const xyzmin = [];
  const xyzmax = [];

  for (let ip = 0; ip < 3; ip++) {

    const DDxyz = dmED.currViewBounds().xyzMax[ip] - dmED.currViewBounds().xyzMin[ip];

    const dxyz = (DDxyz*(1 - 1/dmED.zoomFactor()))/2;

    xyzmin[ip] = dmED.currViewBounds().xyzMin[ip] + dxyz;
    xyzmax[ip] = dmED.currViewBounds().xyzMax[ip] - dxyz;

  };

  dmED.currViewBounds({

    xyzMin: [xyzmin[0], xyzmin[1], xyzmin[2] ],
    xyzMax: [xyzmax[0], xyzmax[1], xyzmax[2] ],

  });

  dmED.checkSM();

  dmED.updateCanvases();

};
//-----------------------------------------------------------------------------

dmED.zoomOut = function() {

  const newZoom = Math.round(1000*dmED.zoom()/dmED.zoomFactor())/1000;

  if (newZoom < 1) return;

  if (newZoom < dmED.zoomFactor()) {

    dmED.zoom(1);

    dmED.zoomIsChanged(1);
    dmED.viewIsChanged(1);

    dmED.updateCanvases();

    return; //!!!

  }

  dmED.zoom(newZoom);

  dmED.zoomIsChanged(1);
  dmED.viewIsChanged(1);

  const xyzmin = [];
  const xyzmax = [];

  for (let ip = 0; ip < 3; ip++) {

    const DDxyz = dmED.currViewBounds().xyzMax[ip] - dmED.currViewBounds().xyzMin[ip];

    const dxyz = (DDxyz*(dmED.zoomFactor() - 1))/2;

    xyzmin[ip] = dmED.currViewBounds().xyzMin[ip] - dxyz;
    xyzmax[ip] = dmED.currViewBounds().xyzMax[ip] + dxyz;

    let xyzShift = xyzmin[ip] - DetCfg.globDetBounds().xyzMin[ip];

    if (xyzShift < -0.1) {

      xyzmin[ip] -= xyzShift;
      xyzmax[ip] -= xyzShift;

    }

    xyzShift = DetCfg.globDetBounds().xyzMax[ip] - xyzmax[ip];

    if (xyzShift < -0.1) {

      xyzmin[ip] += xyzShift;
      xyzmax[ip] += xyzShift;

    }

  };

  dmED.currViewBounds({

    xyzMin: [xyzmin[0], xyzmin[1], xyzmin[2] ],
    xyzMax: [xyzmax[0], xyzmax[1], xyzmax[2] ],

  });

  dmED.checkSM();

  dmED.updateCanvases();

};
//-----------------------------------------------------------------------------

dmED.zoomToBrick = function() {

  const xyzmin = [];
  const xyzmax = [];

  for (let ip = 0; ip < 2; ip++) {

    xyzmin[ip] = gmED.brickVertex()[0].xyMax(ip) - 3.7*DetCfg.brickDims(0);
    xyzmax[ip] = gmED.brickVertex()[0].xyMax(ip) + 2.1*DetCfg.brickDims(0);

  }

  xyzmin[2] = gmED.brickVertex()[0].zMin() - 2.1*DetCfg.brickWallToWallDistZ();
  xyzmax[2] = xyzmin[2] + dmED.aspectRatio()*(xyzmax[0] - xyzmin[0]);

  dmED.setNewCurrViewBounds(xyzmin, xyzmax);

};
//-----------------------------------------------------------------------------

dmED.zoomToEvent = function() {

  if (!dmED.findEventBounds()) return;

  const DDxyz = [];

  for (let ip = 0; ip < 3; ip++)
    DDxyz[ip] = dmED.currEventBounds().xyzMax1[ip] - dmED.currEventBounds().xyzMin1[ip];

  const dDDxy = DDxyz[1] - DDxyz[0];

  if (dDDxy >= 0) {

    dmED.currEventBounds().xyzMin1[0] -= dDDxy/2;
    dmED.currEventBounds().xyzMax1[0] += dDDxy/2;

    DDxyz[0] += dDDxy;

  }
  else {

    dmED.currEventBounds().xyzMin1[1] += dDDxy/2;
    dmED.currEventBounds().xyzMax1[1] -= dDDxy/2;

    DDxyz[1] -= dDDxy;

  }

  const xyzmin = [];
  const xyzmax = [];

  const aspectRatioEvent = DDxyz[2]/DDxyz[0];

  if (aspectRatioEvent >= dmED.aspectRatio()) {

    xyzmin[2] = dmED.currEventBounds().xyzMin1[2];
    xyzmax[2] = dmED.currEventBounds().xyzMax1[2];

    const DDxyNew = DDxyz[2]/dmED.aspectRatio();

    for (let ip = 0; ip < 2; ip++) {

      const dxy = (DDxyNew - DDxyz[0])/2;
  
      xyzmin[ip] = dmED.currEventBounds().xyzMin1[ip] - dxy;
      xyzmax[ip] = dmED.currEventBounds().xyzMax1[ip] + dxy;
  
    }

  }
  else {

    for (let ip = 0; ip < 2; ip++) {

      xyzmin[ip] = dmED.currEventBounds().xyzMin1[ip];
      xyzmax[ip] = dmED.currEventBounds().xyzMax1[ip];

    }

    const DDzNew = DDxyz[0]*dmED.aspectRatio();

    const dz = (DDzNew - DDxyz[2])/2;

    xyzmin[2] = dmED.currEventBounds().xyzMin1[2] - dz;
    xyzmax[2] = dmED.currEventBounds().xyzMax1[2] + dz;

  }

  for (let ip = 0; ip < 3; ip++) {

    let xyzShift = xyzmin[ip] - DetCfg.globDetBounds().xyzMin[ip];

    if (xyzShift < -0.1) {

      xyzmin[ip] -= xyzShift;
      xyzmax[ip] -= xyzShift;

    }

    xyzShift = DetCfg.globDetBounds().xyzMax[ip] - xyzmax[ip];

    if (xyzShift < -0.1) {

      xyzmin[ip] += xyzShift;
      xyzmax[ip] += xyzShift;

    }

  }

  dmED.setNewCurrViewBounds(xyzmin, xyzmax);

};
//-----------------------------------------------------------------------------

dmED.setNewCurrViewBounds = function(xyzmin, xyzmax) {

  dmED.currViewBounds({

    xyzMin: [xyzmin[0], xyzmin[1], xyzmin[2] ],
    xyzMax: [xyzmax[0], xyzmax[1], xyzmax[2] ],

  });

  dmED.checkSM();

  const newZoom = (DetCfg.globDetBounds().xyzMax[2] -
                   DetCfg.globDetBounds().xyzMin[2])/(xyzmax[2] - xyzmin[2]);

  if (newZoom < 1) alert("MgrDrawED-funcAdd.js::dmED.zoomToEvent()::Error: newZoom: " + newZoom + "!!!");

  dmED.zoom(newZoom);

  dmED.zoomIsChanged(1);
  dmED.viewIsChanged(1);

  dmED.updateCanvases();

};
//-----------------------------------------------------------------------------

dmED.findEventBounds = function() {

  $.extend(true, dmED.currEventBounds(), dmED.initEventBounds());

  for (let ip = 0; ip < 2; ip++) {

    dmED.findMinMaxBoundsForHits(ip, demobbed.event().hitsTT()[ip]);

    dmED.findMinMaxBoundsForHits(ip, demobbed.event().hitsRPC()[ip]);

  }

  dmED.findMinMaxBoundsForHits(0, demobbed.event().hitsDT()[0]);

  if ( (dmED.currEventBounds().xyzMin1[0] == dmED.initEventBounds().xyzMin1[0]) ||
       (dmED.currEventBounds().xyzMin1[1] == dmED.initEventBounds().xyzMin1[1]) ||
       (dmED.currEventBounds().xyzMin1[2] == dmED.initEventBounds().xyzMin1[2]) )
    return false; //!!!

  const totalNbOfHits = [0, 0];

  totalNbOfHits[0] += demobbed.event().hitsDT()[0].length;

  for (let ip = 0; ip < 2; ip++) {

    totalNbOfHits[ip] += demobbed.event().hitsTT()[ip].length;

    totalNbOfHits[ip] += demobbed.event().hitsRPC()[ip].length;

    if (totalNbOfHits[ip] > 10) dmED.checkMin12Max12BoundsForHits(ip, 200);

  }

  if (totalNbOfHits[0] + totalNbOfHits[1] > 10) dmED.checkMin12Max12BoundsForHits(2, 400);

  for (let ip = 0; ip < 2; ip++) {

    dmED.currEventBounds().xyzMin1[ip] -= 50; // cm
    dmED.currEventBounds().xyzMax1[ip] += 50; // cm

  }

  dmED.currEventBounds().xyzMin1[2] -= 200; // cm
  dmED.currEventBounds().xyzMax1[2] += 200; // cm

  return true;

};
//-----------------------------------------------------------------------------

dmED.findMinMaxBoundsForHits = function(ip, hits) {

  const nbOfHits = hits.length;

  for (let ih = 0; ih < nbOfHits; ih++) {

    const hitXY = hits[ih].x();

    if (dmED.currEventBounds().xyzMin1[ip] >= hitXY )
      dmED.currEventBounds().xyzMin1[ip] = hitXY;
    else {

      if (dmED.currEventBounds().xyzMin2[ip] > hitXY )
        dmED.currEventBounds().xyzMin2[ip] = hitXY;

    }

    if (dmED.currEventBounds().xyzMax1[ip] <= hitXY )
      dmED.currEventBounds().xyzMax1[ip] = hitXY;
    else {

      if (dmED.currEventBounds().xyzMax2[ip] < hitXY )
        dmED.currEventBounds().xyzMax2[ip] = hitXY;

    }

    const hitZ  = hits[ih].z();

    if (dmED.currEventBounds().xyzMin1[2] >= hitZ )
      dmED.currEventBounds().xyzMin1[2] = hitZ;
    else {

      if (dmED.currEventBounds().xyzMin2[2] > hitZ )
        dmED.currEventBounds().xyzMin2[2] = hitZ;

    }

    if (dmED.currEventBounds().xyzMax1[2] <= hitZ )
      dmED.currEventBounds().xyzMax1[2] = hitZ;
    else {

      if (dmED.currEventBounds().xyzMax2[2] < hitZ )
        dmED.currEventBounds().xyzMax2[2] = hitZ;

    }

  }

};
//-----------------------------------------------------------------------------

dmED.checkMin12Max12BoundsForHits = function(ip, maxDist) {

  const xyzMin2 = dmED.currEventBounds().xyzMin2[ip];

  if (xyzMin2 < dmED.initEventBounds().xyzMin1[ip]) {

    if (xyzMin2 - dmED.currEventBounds().xyzMin1[ip] > maxDist)
      dmED.currEventBounds().xyzMin1[ip] = xyzMin2;

  }

  const xyzMax2 = dmED.currEventBounds().xyzMax2[ip];

  if (xyzMax2 > dmED.initEventBounds().xyzMax1[ip]) {

    if (dmED.currEventBounds().xyzMax1[ip] - xyzMax2 > maxDist)
      dmED.currEventBounds().xyzMax1[ip] = xyzMax2;

  }

};
//-----------------------------------------------------------------------------

dmED.moveView = function(ip, dirLRUD) {

  // ip = 0, 1, or 2 for moving along X, Y, and Z

  // dirLRUD - direction of moving (left, right, up, or down)
  // dirLRUD =  1 for moving to right or up
  // dirLRUD = -1 for moving to left or down

  // E.g.: Move the XZ camera up   (detector - down) if ip=0 and dirLRUD=1
  // E.g.: Move both XZ and YZ cameras left (detector - right) if ip=2 and dirLRUD=-1

  if (!Utils.checkIP(ip, 3)) {
    alert("MgrDrawED-funcAdd.js::dmED.onMoveVert()::Error: ip is strange!!!: ip = " + ip + "!!!");
    return;
  }

  if (dmED.zoom() < dmED.zoomFactor()) return; //!!!

  dmED.viewIsChanged(1);

  const xyzmin = [0, 0, 0];
  const xyzmax = [0, 0, 0];

  const DDxyz = dmED.currViewBounds().xyzMax[ip] - dmED.currViewBounds().xyzMin[ip];

  const dxyz = DDxyz*dmED.moveFactor(ip);

  xyzmin[ip] = dmED.currViewBounds().xyzMin[ip] + dirLRUD*dxyz;
  xyzmax[ip] = dmED.currViewBounds().xyzMax[ip] + dirLRUD*dxyz;

  const xyzShift = (dirLRUD > 0) ? (DetCfg.globDetBounds().xyzMax[ip] - xyzmax[ip])
                                 : (xyzmin[ip] - DetCfg.globDetBounds().xyzMin[ip]);

  if (xyzShift < -0.1) {

    xyzmin[ip] += dirLRUD*xyzShift;
    xyzmax[ip] += dirLRUD*xyzShift;

  }

  dmED.currViewBounds().xyzMin[ip] = xyzmin[ip];
  dmED.currViewBounds().xyzMax[ip] = xyzmax[ip];

  dmED.checkSM();

  dmED.updateCanvases();

};
//-----------------------------------------------------------------------------

dmED.updateCanvases = function() {

  if (dmED.canvasesMain(0) === null) {

    dmED.initGraphics();
    dmECC.initGraphics();

  }

  if (dmED.viewIsChanged()) {

    if (dmED.zoom() == 1) dmED.setInitViewParams();
    else {

      if (dmED.zoomIsChanged()) {

        dmED.updateCoefPixToCM();

        if (dmED.zoom() > dmED.zoomFarViewMax()) dmED.setCloseViewHitSizes();
        else dmED.setFarViewHitSizes();

        dmED.zoomIsChanged(0);

      }

      dmED.updateScalesOfAxes();

      dmED.updateScalesOfCanvEmb();

    }

    dmED.clearCanvases();

    for (let ip = 0; ip < 2; ip++) {

      dmED.drawAxes(ip);

      dmED.drawDet(ip);

      dmED.drawEvent(ip);

    }

    dmED.viewIsChanged(0);

    return; //!!!
  }

  for (let ip = 0; ip < 2; ip++) {

    dmED.clearEvent(ip);

    dmED.drawEvent(ip);

  }

};
//-----------------------------------------------------------------------------

dmED.updateCoefPixToCM = function() {

  dmED.coefPixToCM( (dmED.currViewBounds().xyzMax[2] -
                        dmED.currViewBounds().xyzMin[2])/dmED.canvMainWidth() );

};
//-----------------------------------------------------------------------------

dmED.updateScalesOfAxes = function() {

  dmED.scalesOfAxes([

    d3.scaleLinear()
      .domain([dmED.currViewBounds().xyzMin[0] +
               dmED.coefPixToCM()*dmED.axesOffsets().bottomW,
               dmED.currViewBounds().xyzMax[0] -
               dmED.coefPixToCM()*dmED.axesOffsets().topW])
      .range([dmED.canvMainHeight() - dmED.axesOffsets().bottomW,
              dmED.axesOffsets().topW]),

    d3.scaleLinear()
      .domain([dmED.currViewBounds().xyzMin[1] +
               dmED.coefPixToCM()*dmED.axesOffsets().bottomW,
               dmED.currViewBounds().xyzMax[1] -
               dmED.coefPixToCM()*dmED.axesOffsets().topW])
      .range([dmED.canvMainHeight() - dmED.axesOffsets().bottomW,
              dmED.axesOffsets().topW]),

    d3.scaleLinear()
      .domain([dmED.currViewBounds().xyzMin[2] +
               dmED.coefPixToCM()*dmED.axesOffsets().leftW,
               dmED.currViewBounds().xyzMax[2] -
               dmED.coefPixToCM()*dmED.axesOffsets().rightW])
      .range([dmED.axesOffsets().leftW, dmED.canvMainWidth() -
              dmED.axesOffsets().rightW])

  ]);

};
//-----------------------------------------------------------------------------

dmED.updateScalesOfCanvEmb = function() {

  dmED.scalesOfCanvEmb([

    d3.scaleLinear()
      .domain([dmED.currViewBounds().xyzMin[0] +
               dmED.coefPixToCM()*dmED.canvEmbOffsets().bottomW,
               dmED.currViewBounds().xyzMax[0] -
               dmED.coefPixToCM()*dmED.canvEmbOffsets().topW])
      .range([dmED.canvEmbHeight(), 0]),

    d3.scaleLinear()
      .domain([dmED.currViewBounds().xyzMin[1] +
               dmED.coefPixToCM()*dmED.canvEmbOffsets().bottomW,
               dmED.currViewBounds().xyzMax[1] -
               dmED.coefPixToCM()*dmED.canvEmbOffsets().topW])
      .range([dmED.canvEmbHeight(), 0]),

    d3.scaleLinear()
      .domain([dmED.currViewBounds().xyzMin[2] +
               dmED.coefPixToCM()*dmED.canvEmbOffsets().leftW,
               dmED.currViewBounds().xyzMax[2] - 
               dmED.coefPixToCM()*dmED.canvEmbOffsets().rightW])
      .range([0, dmED.canvEmbWidth()])

  ]);

};
//-----------------------------------------------------------------------------

dmED.clearCanvases = function() {

  for (let ip = 0; ip < 2; ip++) {

    dmED.clearAxes(ip);

    dmED.clearDet(ip);

    dmED.clearEvent(ip);

  }

};
//-----------------------------------------------------------------------------

dmED.drawAxes = function(ip) {

  dmED.canvasesMain(ip).append("g")
                       .attr("id", dmED.groupZAxesIDs(ip))
 	               .attr("class", "z axis")
		       .attr("transform", "translate(0, " + (dmED.canvMainHeight() -
                                                             dmED.axesOffsets().bottomW) + ")")
                       .call(d3.axisBottom(dmED.scalesOfAxes()[2]));

  dmED.canvasesMain(ip).append("g")
                       .attr("id", dmED.groupXYAxesIDs(ip))
		       .attr("class", "x axis")
		       .attr("transform", "translate(" + dmED.axesOffsets().leftW + ", 0)")
		       .call(d3.axisLeft(dmED.scalesOfAxes()[ip]));

};
//-----------------------------------------------------------------------------

dmED.clearAxes = function(ip) {

  d3.select("#" + dmED.groupZAxesIDs(ip))
    .remove();

  d3.select("#" + dmED.groupXYAxesIDs(ip))
    .remove();

};
//-----------------------------------------------------------------------------

dmED.drawDet = function(ip) {

  dmED.drawDetElems(ip, dmED.groupTTWallsIDs(ip),    gmED.wallsTT());
  dmED.drawDetElems(ip, dmED.groupBrickWallsIDs(ip), gmED.wallsBrick());
  dmED.drawDetElems(ip, dmED.groupRPCLayersIDs(ip),  gmED.layersRPC());
  dmED.drawDetElems(ip, dmED.groupDTLayersIDs(ip),   gmED.layersDT());

  if (dmED.zoom() > dmED.zoomFarViewMax()) {

    if (dmED.sm() == 1)      dmED.drawDetElems(ip, dmED.groupVisBricksIDs(ip), gmED.bricksSM1VisXY(ip));
    else if (dmED.sm() == 2) dmED.drawDetElems(ip, dmED.groupVisBricksIDs(ip), gmED.bricksSM2VisXY(ip));

    dmED.drawDetElems(ip, dmED.groupVertBrickIDs(ip), gmED.brickVertex());

  }

};
//-----------------------------------------------------------------------------

dmED.clearDet = function(ip) {

  d3.select("#" + dmED.groupTTWallsIDs(ip))
    .selectAll('rect')
    .remove();

  d3.select("#" + dmED.groupBrickWallsIDs(ip))
    .selectAll('rect')
    .remove();

  d3.select("#" + dmED.groupRPCLayersIDs(ip))
    .selectAll('rect')
    .remove();

  d3.select("#" + dmED.groupDTLayersIDs(ip))
    .selectAll('rect')
    .remove();

  d3.select("#" + dmED.groupVisBricksIDs(ip))
    .selectAll('rect')
    .remove();

  d3.select("#" + dmED.groupVertBrickIDs(ip))
    .selectAll('rect')
    .remove();

};
//-----------------------------------------------------------------------------

dmED.drawDetElems = function(ip, groupIDs, detElems) {

  const detElemBoxes = d3.select("#" + groupIDs)
                         .selectAll('rect')
                         .data(detElems);

  detElemBoxes
    .enter()
    .append('rect')
    .attr('x', function(d) {
      return dmED.scalesOfCanvEmb()[2](d.zMin());
    })
    .attr('y', function(d) {
      return dmED.scalesOfCanvEmb()[ip](d.xyMax(ip));
    })
    .attr('width', function(d) {
      return d.dims(2)/dmED.coefPixToCM();
    })
    .attr('height', function(d) {
      return d.dims(ip)/dmED.coefPixToCM();
    })
    .attr('fill', function(d) {
      return d.color();
    })
    .attr('stroke', function(d) {
      return d.borderColor();
    });

};
//-----------------------------------------------------------------------------

dmED.drawBricks = function(ip) {

  const brickBoxes = d3.select("#" + dmED.groupBricksIDs(ip))
                       .selectAll('rect')

};
//-----------------------------------------------------------------------------

dmED.drawEvent = function(ip) {

  dmED.drawHits(ip);

  if (dmED.zoom() > dmED.zoomFarViewMax()) {

    dmED.drawNeuVertex(ip);

    dmED.drawPartTracks(ip);

  }

};
//-----------------------------------------------------------------------------

dmED.clearEvent = function(ip) {

  dmED.clearHits(ip);

  d3.select("#" + dmED.groupNeuVertexIDs(ip))
    .selectAll('circle')
    .remove();

  d3.select("#" + dmED.groupPartTracksIDs(ip))
    .selectAll('line')
    .remove();

};
//-----------------------------------------------------------------------------

dmED.drawHits = function(ip) {

  dmED.drawTTHits(ip);

  dmED.drawRPCHits(ip);
  if (!ip) dmED.drawDTHits();

};
//-----------------------------------------------------------------------------

dmED.clearHits = function(ip) {

  d3.select("#" + dmED.groupTTHitsIDs(ip))
    .selectAll('rect')
    .remove();

  d3.select("#" + dmED.groupRPCHitsIDs(ip))
    .selectAll('rect')
    .remove();

  if (!ip) d3.select("#" + dmED.groupDTHitsIDs(0))
             .selectAll('circle')
             .remove();

};
//-----------------------------------------------------------------------------

dmED.drawTTHits = function(ip) {

  const TTHitBoxes = d3.select("#" + dmED.groupTTHitsIDs(ip))
                       .selectAll('rect')
                       .data(demobbed.event().hitsTT()[ip]);

  const w2 = dmED.hitTTdims(2)/2;
  const h2 = dmED.hitTTdims(ip)/2;

  TTHitBoxes
    .enter()
    .append('rect')
    .attr('id', function(d) {

      return "h" + d.id();

    })
    .attr('x', function(d) {

      return dmED.scalesOfCanvEmb()[2](d.z()) - w2;

    })
    .attr('y', function(d) {

      return dmED.scalesOfCanvEmb()[ip](d.x()) - h2;

    })
    .attr('width', function(d) {

      const brd2 = DetCfg.brickDims(2)/dmED.coefPixToCM();

      const ampl = d.ampl();

      if (ampl > 200) return brd2 + dmED.hitTTdims(2);
      else return 0.005*brd2*ampl + dmED.hitTTdims(2);

    })
    .attr('height', function(d) {

      return dmED.hitTTdims(ip);

    })
    .attr('fill', function(d) {

      return d.color();

    });

};
//-----------------------------------------------------------------------------

dmED.drawRPCHits = function(ip) {

  const RPCHitBoxes = d3.select("#" + dmED.groupRPCHitsIDs(ip))
                        .selectAll('rect')
                        .data(demobbed.event().hitsRPC()[ip]);

  const w2 = dmED.hitRPCdims(2)/2;
  const h2 = dmED.hitRPCdims(ip)/2;

  RPCHitBoxes
    .enter()
    .append('rect')
    .attr('id', function(d) {

      return "h" + d.id();

    })
    .attr('x', function(d) {

      return dmED.scalesOfCanvEmb()[2](d.z()) - w2;

    })
    .attr('y', function(d) {

      const y = dmED.scalesOfCanvEmb()[ip](d.x());

      if (dmED.zoom() > dmED.zoomFarViewMax())
        return y - d.clLength()/(2*dmED.coefPixToCM());
      else
        return y - h2;

    })
    .attr('width', function(d) {

      return dmED.hitRPCdims(2);

    })
    .attr('height', function(d) {

      if (dmED.zoom() > dmED.zoomFarViewMax())
        return d.clLength()/dmED.coefPixToCM();
      else
        return dmED.hitRPCdims(ip);

    })
    .attr('fill', function(d) {

      return d.color();

    });

};
//-----------------------------------------------------------------------------

dmED.drawDTHits = function() {

  const DTHitCircles = d3.select("#" + dmED.groupDTHitsIDs(0))
                         .selectAll('circle')
                         .data(demobbed.event().hitsDT()[0]);

  DTHitCircles
    .enter()
    .append('circle')
    .attr('id', function(d) {

      return "h" + d.id();

    })
    .attr('cx', function(d) {

      return dmED.scalesOfCanvEmb()[2](d.z());

    })
    .attr('cy', function(d) {

      return dmED.scalesOfCanvEmb()[0](d.x());

    })
    .attr('r', function(d) {

      if (dmED.zoom() > dmED.zoomFarViewMax())
        return d.driftDist()/dmED.coefPixToCM();
      else
        return dmED.hitDTradiusFarView();

    })
    .attr('fill', function(d) {

      return d.color();

    });

};
//-----------------------------------------------------------------------------

dmED.drawNeuVertex = function(ip) {

  const NeuVertexCircle = d3.select("#" + dmED.groupNeuVertexIDs(ip))
                            .selectAll('circle')
                            .data(demobbed.event().vertex());

  NeuVertexCircle
    .enter()
    .append('circle')
    .attr('cx', function(d) {
      return dmED.scalesOfCanvEmb()[2](d.posGlob()[2]);
    })
    .attr('cy', function(d) {
      return dmED.scalesOfCanvEmb()[ip](d.posGlob()[ip]);
    })
    .attr('r', 2)
    //.attr('fill', "#FF3300");
    .attr('fill', Vertex.color());

};
//-----------------------------------------------------------------------------

dmED.drawPartTracks = function(ip) {

  const PartTracksLines = d3.select("#" + dmED.groupPartTracksIDs(ip))
                            .selectAll('line')
                            .data(demobbed.event().tracksECC());

  const vertPosGlob = demobbed.event().vertex()[0].posGlob();

  PartTracksLines
    .enter()
    .append('line')
    .attr('x1', dmED.scalesOfCanvEmb()[2](vertPosGlob[2]))
    .attr('y1', dmED.scalesOfCanvEmb()[ip](vertPosGlob[ip]))
    .attr('x2', function(d) {                  

      const trPartId = d.partId();

      if ( (trPartId == 1) || (trPartId == 2) ) // draw only tracks of muons and hadrons!
        return dmED.scalesOfCanvEmb()[2](vertPosGlob[2] + dmED.trackLinePars()[trPartId].length);

    })
    .attr('y2', function(d) {

      const trPartId = d.partId();

      if ( (trPartId == 1) || (trPartId == 2) ) // draw only tracks of muons and hadrons!
        return dmED.scalesOfCanvEmb()[ip](vertPosGlob[ip] + d.Axy(ip)*dmED.trackLinePars()[trPartId].length);

    })
    .attr('stroke', function(d) {

      const trPartId = d.partId();

      if ( (trPartId == 1) || (trPartId == 2) ) // draw only tracks of muons and hadrons!
        return dmED.trackLinePars()[trPartId].color;

    });

};
//-----------------------------------------------------------------------------

dmED.setFarViewHitSizes = function() {

  for (let ip = 0; ip < 3; ip++) {

    dmED.hitTTdims()[ip]  = dmED.hitTTsizeFarView();
    dmED.hitRPCdims()[ip] = dmED.hitRPCsizeFarView();

  }

};
//-----------------------------------------------------------------------------

dmED.setCloseViewHitSizes = function() {

  dmED.hitTTdims()[0]  = dmED.hitTTdims()[1] =
                         DetCfg.TTstripWidth()/dmED.coefPixToCM();

  dmED.hitTTdims()[2]  = DetCfg.TTstripDepth()/dmED.coefPixToCM();

  dmED.hitRPCdims()[2] = DetCfg.RPCstripDepth()/dmED.coefPixToCM();

};
//-----------------------------------------------------------------------------
