//dmECC == demobbed.mgrDrawECC() !!!
//gmED  == demobbed.mgrGeomED()  !!!
//---------------------------------------

dmECC.initGraphics = function() {

  const canvWidth  = dmED.canvMainWidth();
  const canvHeight = 0.618*canvWidth; //!!!

  //dmECC.camera(new THREE.PerspectiveCamera(70, canvWidth/canvHeight, 0.1, 20000));

  dmECC.camera(new THREE.OrthographicCamera(-1800, 4200, 1854, -1854, 0, 15000));
  dmECC.cameraInset(new THREE.OrthographicCamera(-1200, 1800, 1554, -300, 0, 10000));

  dmECC.scene(new THREE.Scene());
  dmECC.sceneInset(new THREE.Scene());

  dmECC.initRenderers(canvWidth, canvHeight);

  dmECC.initVertexPoint();

  dmECC.groupOfTrackLines(new THREE.Group());

  dmECC.initTrackLineProperties();

  dmECC.initGroupOfAxesAndTrackTitles();

  dmECC.drawTrackLegend();

};
//------------------------------------------------------------------------------

dmECC.initRenderers = function(canvWidth, canvHeight) {

  const canvasECC = document.getElementById("canvas-ECC");
  const canvasAxesECC = document.getElementById("canvas-axes-ECC");

  dmECC.renderer(new THREE.WebGLRenderer( { canvas: canvasECC, antialias: true, alpha: true } ));
  dmECC.rendererInset(new THREE.WebGLRenderer( { canvas: canvasAxesECC, antialias: true, alpha: true } ));

  dmECC.renderer().setPixelRatio(window.devicePixelRatio);
  dmECC.rendererInset().setPixelRatio(window.devicePixelRatio);

  dmECC.renderer().setSize(canvWidth, canvHeight);
  dmECC.rendererInset().setSize(canvWidth/2, canvHeight/2);

  dmECC.renderer().setClearColor(0xFAFAFA, 1);
  dmECC.rendererInset().setClearColor(0xFAFAFA, 0);

  dmECC.renderer().gammaInput  = true;
  dmECC.renderer().gammaOutput = true;

  dmECC.rendererInset().gammaInput  = true;
  dmECC.rendererInset().gammaOutput = true;

};
//------------------------------------------------------------------------------

dmECC.initVertexPoint = function() {

  const vertexGeometry = new THREE.SphereGeometry(20, 32, 32);

  //let vertexMaterial = new THREE.MeshBasicMaterial( {color: 0xFF3300} );
  const vertexMaterial = new THREE.MeshBasicMaterial({ color: Vertex.color() });

  dmECC.vertexPoint(new THREE.Mesh(vertexGeometry, vertexMaterial));

};
//------------------------------------------------------------------------------

dmECC.initGroupOfAxesAndTrackTitles = function() {

  dmECC.groupOfAxes(new THREE.Group());

  const colorX = "seagreen";
  const colorY = "magenta";
  const colorZ = "maroon";

  const rx = new three3DExtras.tubeLine([0, 0, 0], [1000, 0, 0], 8, colorX);
  const gy = new three3DExtras.tubeLine([0, 0, 0], [0, 1000, 0], 8, colorY);
  const bz = new three3DExtras.tubeLine([0, 0, 0], [0, 0, 1000], 8, colorZ);

  dmECC.groupOfAxes().add(rx.getObject3D());
  dmECC.groupOfAxes().add(gy.getObject3D());
  dmECC.groupOfAxes().add(bz.getObject3D());

  const font_loader = new THREE.FontLoader();
  font_loader.load('./fonts/helvetiker_regular.typeface.json', function(font) {

    // init axes titles

    const tps = { size:110, height:10, font:font };

    const x_geo = new THREE.TextGeometry('X', tps);
    const y_geo = new THREE.TextGeometry('Y', tps);
    const z_geo = new THREE.TextGeometry('Z', tps);

    const un_geo = new THREE.TextGeometry('1mm', tps);

    const x_material = new THREE.MeshBasicMaterial({ color: colorX });
    const x_text = new THREE.Mesh(x_geo, x_material);
    x_text.position.x = 980;
    x_text.position.y =  50;
    x_text.position.z =  50;
    x_text.rotation.y = -1.57;

    const y_material = new THREE.MeshBasicMaterial({ color: colorY });
    const y_text = new THREE.Mesh(y_geo, y_material);
    y_text.position.y = 900;
    y_text.position.z =  50;
    y_text.rotation.y = -1.57;

    const z_material = new THREE.MeshBasicMaterial({ color: colorZ });
    const z_text = new THREE.Mesh(z_geo, z_material);
    z_text.position.y =  50;
    z_text.position.z = 920;
    z_text.rotation.y = -1.57;

    const un_material = new THREE.MeshBasicMaterial({ color: colorY });
    const un_text = new THREE.Mesh(un_geo, un_material);
    un_text.position.y =  450;
    un_text.position.z =  50;
    un_text.rotation.y = -1.57;

    dmECC.groupOfAxes().add(x_text);
    dmECC.groupOfAxes().add(y_text);
    dmECC.groupOfAxes().add(z_text);
    dmECC.groupOfAxes().add(un_text);

    // init track titles

    const trMu_geo = new THREE.TextGeometry('mu', tps);
    const trMu_material = new THREE.MeshBasicMaterial({ color: TrackECC.colors(1) });

    dmECC.trackTitles()[1] = new THREE.Mesh(trMu_geo, trMu_material);
    dmECC.trackTitles()[1].rotation.y = -1.57;

    const trEl_geo = new THREE.TextGeometry('e', tps);
    const trEl_material = new THREE.MeshBasicMaterial({ color: TrackECC.colors(3) });

    dmECC.trackTitles()[3] = new THREE.Mesh(trEl_geo, trEl_material);
    dmECC.trackTitles()[3].rotation.y = -1.57;

    dmECC.trackTitles()[2] = dmECC.trackTitles()[4] = dmECC.trackTitles()[5]
                           = dmECC.trackTitles()[6] = dmECC.trackTitles()[7]
                           = dmECC.trackTitles()[8] = null; //!!!

  });

};
//------------------------------------------------------------------------------

dmECC.initTrackLineProperties = function() {

  dmECC.trackLinePars()[1] = { // for a track of muon

    color:  TrackECC.colors(1),
    length: 10*DetCfg.plateToPlateDistECC(),
    //width:  5
    width:  12

  };

  dmECC.trackLinePars()[2] = { // for a track of hadron

    color:  TrackECC.colors(2),
    length: 10*DetCfg.plateToPlateDistECC(),
    //width:  5
    width:  12

  };

  dmECC.trackLinePars()[3] = { // for a track of electron

    color:  TrackECC.colors(3),
    length: 3*DetCfg.plateToPlateDistECC(),
    //width:  5
    width:  12

  };

  dmECC.trackLinePars()[4] = { // for a black track

    color:  TrackECC.colors(4),
    length: 1*DetCfg.plateToPlateDistECC(),
    //width:  7
    width:  17

  };

  dmECC.trackLinePars()[5] = { // for a back black track

    color:  TrackECC.colors(5),
    length: 1*DetCfg.plateToPlateDistECC(),
    //width:  7
    width:  17

  };

  dmECC.trackLinePars()[6] = { // for a gray track

    color:  TrackECC.colors(6),
    length: 1.5*DetCfg.plateToPlateDistECC(),
    //width:  7
    width:  17

  };

  dmECC.trackLinePars()[7] = { // for a back gray track

    color:  TrackECC.colors(7),
    length: 1.5*DetCfg.plateToPlateDistECC(),
    //width:  7
    width:  17

  };

  dmECC.trackLinePars()[8] = { // for a track of tau lepton

    color:  TrackECC.colors(8),
    length: 0.7*DetCfg.plateToPlateDistECC(),
    //width:  7
    width:  17

  };

};
//------------------------------------------------------------------------------

dmECC.drawEvent = function() {

  dmECC.scene().add(dmECC.vertexPoint());

  dmECC.drawTracks();

  dmECC.sceneInset().add(dmECC.groupOfAxes())

  //dmECC.camera().position.set(-3000, 0, 1000);          // for perspective camera
  //dmECC.camera().lookAt(new THREE.Vector3(0, 0, 1000)); // for perspective camera

  dmECC.camera().position.set(-2000, 200, 200);
  dmECC.cameraInset().position.set(-2000, 200, 200);

  dmECC.camera().lookAt(dmECC.vecOrigin());
  dmECC.cameraInset().lookAt(dmECC.vecOrigin());

  dmECC.renderer().render(dmECC.scene(), dmECC.camera());
  dmECC.rendererInset().render(dmECC.sceneInset(), dmECC.cameraInset());

};
//------------------------------------------------------------------------------

dmECC.accelerateAnimation = function() {

  dmECC.animationFrameID(requestAnimationFrame(dmECC.accelerateAnimation));

  dmECC.groupOfTrackLines().rotation.y += 0.004;

  dmECC.groupOfAxes().rotation.y += 0.004;

  dmECC.renderer().render(dmECC.scene(), dmECC.camera());
  dmECC.rendererInset().render(dmECC.sceneInset(), dmECC.cameraInset());

};
//------------------------------------------------------------------------------

dmECC.decelerateAnimation = function() {

  cancelAnimationFrame(dmECC.animationFrameID());

};
//------------------------------------------------------------------------------

dmECC.drawTracks = function() {

  const evTracks = demobbed.event().tracksECC();

  const vertPos = demobbed.event().vertex()[0].pos();

  const nbOfTracks = evTracks.length;

  for (let it = 0; it < nbOfTracks; it++) {

    const trPartId = evTracks[it].partId();

    const trAxy = evTracks[it].Axy();

    const trackPartTitle = dmECC.trackTitles()[trPartId];

    const trPars = dmECC.trackLinePars()[trPartId];

    //const zPlate = evTracks[it].pos()[2] - vertPos[2];

    const trBeg = [0, 0, 0];
    const trEnd = [0, 0, 0];

    const trTitlePos = [0, 0, 0];

    if ( (trPartId == 5) || (trPartId == 7) ) { // back track

      trEnd[2] = -30;
      trBeg[2] = trEnd[2] - trPars.length;

    }
    else {

      trBeg[2] = (trPartId === 3) ? 900 : 30; // an electron comes not from the vertex itself
      trEnd[2] = trBeg[2] + trPars.length;

      if (trackPartTitle) trTitlePos[2] = trBeg[2] + 1500;

    }

    for (let ip = 0; ip < 2; ip++) {

      trBeg[ip] = trBeg[2]*trAxy[ip];
      trEnd[ip] = trEnd[2]*trAxy[ip];

      if (trackPartTitle) trTitlePos[ip] = trTitlePos[2]*trAxy[ip];

    }

    const trackLine = new three3DExtras.tubeLine(trBeg, trEnd, trPars.width, trPars.color); 

    dmECC.groupOfTrackLines().add(trackLine.getObject3D());

    if (trackPartTitle) {

      const trackTitle = trackPartTitle.clone(); //!!!

      trackTitle.position.x = trTitlePos[0];
      trackTitle.position.y = trTitlePos[1] + 100;
      trackTitle.position.z = trTitlePos[2];

      dmECC.groupOfTrackLines().add(trackTitle);

    }

  }

  dmECC.scene().add(dmECC.groupOfTrackLines());

};
//------------------------------------------------------------------------------

dmECC.onEventChange = function() {

  const divECC = document.getElementById("div-ECC");

  if (!demobbed.showECC()) {

    if (dmECC.camera() !== null) {

      cancelAnimationFrame(dmECC.animationFrameID());

      dmECC.clearCanvas();

      dmECC.eraseEventInfo();

    }

    divECC.style.display = "none";

    return; //!!!

  }

  divECC.style.display = "block";

  dmECC.updateCanvas();

  dmECC.displayEventInfo();

};
//------------------------------------------------------------------------------

dmECC.displayEventInfo = function() {
};
//------------------------------------------------------------------------------

dmECC.eraseEventInfo = function() {
};
//------------------------------------------------------------------------------

dmECC.updateCanvas = function() {

  //if (dmECC.camera() === null) dmECC.initGraphics(); // the initialisation is called in MgrDrawED-addMethods.js!

  dmECC.clearCanvas();

  const rotY = dmECC.groupOfTrackLines().rotation.y;

  if (rotY >= 0) {

    dmECC.groupOfTrackLines().rotation.y = 0;
    dmECC.groupOfAxes().rotation.y = 0;
  }

  dmECC.drawEvent();

};
//------------------------------------------------------------------------------

dmECC.clearCanvas = function() {

  dmECC.clearGroupOfTrackLines();

  dmECC.scene().remove(dmECC.vertexPoint());

  dmECC.sceneInset().remove(dmECC.groupOfAxes());

  dmECC.renderer().render(dmECC.scene(), dmECC.camera());
  dmECC.rendererInset().render(dmECC.sceneInset(), dmECC.cameraInset());

};
//------------------------------------------------------------------------------

dmECC.drawECC = function(showECC) {

  demobbed.showECC(showECC);

  dmECC.onEventChange();  

};
//------------------------------------------------------------------------------

dmECC.drawTrackLegend = function() {

  const canvasLegendECC = document.getElementById("canvas-legend-ECC");

  dmECC.trackLegendContext(canvasLegendECC.getContext("2d"));

  dmECC.trackLegendLineBeg(120);
  dmECC.trackLegendLineEnd(canvasLegendECC.width - 10);

  dmECC.trackLegendContext().font = "16px serif";

  dmECC.trackLegendContext().fillText("Track types", 50, 15);

  dmECC.trackLegendContext().beginPath();
  dmECC.trackLegendContext().moveTo(0, 20);
  dmECC.trackLegendContext().lineTo(canvasLegendECC.width, 20);
  dmECC.trackLegendContext().stroke();

  dmECC.addLegendEntry("muon:",             38, TrackECC.colors(1));
  dmECC.addLegendEntry("hadron:",           56, TrackECC.colors(2));
  dmECC.addLegendEntry("electron:",         74, TrackECC.colors(3));
  dmECC.addLegendEntry("highly ionizing:",  92, TrackECC.colors(4));
  dmECC.addLegendEntry("ionizing:",        110, TrackECC.colors(6));

};
//-----------------------------------------------------------------------------

dmECC.addLegendEntry = function(trTypeName, topDist, trColor) {

  dmECC.trackLegendContext().fillStyle = trColor;
  dmECC.trackLegendContext().fillText(trTypeName, 8, topDist + 3);

  dmECC.trackLegendContext().beginPath();
  dmECC.trackLegendContext().moveTo(dmECC.trackLegendLineBeg(), topDist);
  dmECC.trackLegendContext().lineTo(dmECC.trackLegendLineEnd(), topDist);
  dmECC.trackLegendContext().lineWidth = 3;
  dmECC.trackLegendContext().strokeStyle = trColor;
  dmECC.trackLegendContext().stroke();

};
//-----------------------------------------------------------------------------
