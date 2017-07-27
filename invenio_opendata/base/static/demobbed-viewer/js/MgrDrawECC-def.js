class MgrDrawECC { // Manager intended for drawing of (3D) tracks found in emulsion

  constructor() {

    this._camera      = null;
    this._cameraInset = null;   // Inset objects are needed for axes

    this._scene      = null;
    this._sceneInset = null;

    this._renderer      = null;
    this._rendererInset = null;

    //---

    this._vertexPoint = {};       // three.js sphere

    this._trackLinePars = [];     // Array of line parameters used for drawing of the ECC tracks

    this._trackTitles = [];       // Array of THREE.Mesh objects with titles of tracks

    this._groupOfTrackLines = {}; // three.js group of track lines

    this._groupOfAxes = {};       // three.js group of 3 arrows with titles: "X", "Y", and "Z"

    this._animationFrameID = 0;

    this._vecOrigin = new THREE.Vector3(0, 0, 0);

    this._trackLegendContext = {}; // Context of a track legend canvas

    this._trackLegendLineBeg = 0;
    this._trackLegendLineEnd = 0;

  };

  camera(cam) {

    if (cam === undefined) return this._camera;

    if (typeof(cam) !== "object") {
      alert("MgrDrawECC-def::camera()::Error: cam is not an object!!!: typeof(cam) = " + typeof(cam) + "!!!");
      return;
    }

    this._camera = cam;

  };

  cameraInset(cam) {

    if (cam === undefined) return this._cameraInset;

    if (typeof(cam) !== "object") {
      alert("MgrDrawECC-def::cameraInset()::Error: cam is not an object!!!: typeof(cam) = " + typeof(cam) + "!!!");
      return;
    }

    this._cameraInset = cam;

  };

  scene(sc) {

    if (sc === undefined) return this._scene;

    if (typeof(sc) !== "object") {
      alert("MgrDrawECC-def::scene()::Error: sc is not an object!!!: typeof(sc) = " + typeof(sc) + "!!!");
      return;
    }

    this._scene = sc;

  };

  sceneInset(sc) {

    if (sc === undefined) return this._sceneInset;

    if (typeof(sc) !== "object") {
      alert("MgrDrawECC-def::sceneInset()::Error: sc is not an object!!!: typeof(sc) = " + typeof(sc) + "!!!");
      return;
    }

    this._sceneInset = sc;

  };

  renderer(rend) {

    if (rend === undefined) return this._renderer;

    if (typeof(rend) !== "object") {
      alert("MgrDrawECC-def::renderer()::Error: rend is not an object!!!: typeof(rend) = " + typeof(rend) + "!!!");
      return;
    }

    this._renderer = rend;

  };

  rendererInset(rend) {

    if (rend === undefined) return this._rendererInset;

    if (typeof(rend) !== "object") {
      alert("MgrDrawECC-def::rendererInset()::Error: rend is not an object!!!: typeof(rend) = " + typeof(rend) + "!!!");
      return;
    }

    this._rendererInset = rend;

  };

  vertexPoint(vp) {

    if (vp === undefined) return this._vertexPoint;

    if (typeof(vp) !== "object") {
      alert("MgrDrawECC-def::vertexPoint()::Error: vp is not an object!!!: typeof(vp) = " + typeof(vp) + "!!!");
      return;
    }

    this._vertexPoint = vp;

  };

  trackLinePars() { return this._trackLinePars; };

  trackTitles() { return this._trackTitles; };

  groupOfTrackLines(group) {

    if (group === undefined) return this._groupOfTrackLines;

    if (typeof(group) !== "object") {
      alert("MgrDrawECC-def::groupOfTrackLines()::Error: group is not an object!!!: typeof(group) = " + typeof(group) + "!!!");
      return;
    }

    this._groupOfTrackLines = group;

  };

  groupOfAxes(group) {

    if (group === undefined) return this._groupOfAxes;

    if (typeof(group) !== "object") {
      alert("MgrDrawECC-def::groupOfAxes()::Error: group is not an object!!!: typeof(group) = " + typeof(group) + "!!!");
      return;
    }

    this._groupOfAxes = group;

  };

  clearGroupOfTrackLines() {

    if (!this._groupOfTrackLines) return;

    let children = this._groupOfTrackLines.children;

    for (let ic = children.length - 1; ic >= 0; ic--) {
      this._groupOfTrackLines.remove(children[ic]);
    }

  };

  animationFrameID(jd) {

    if (jd === undefined) return this._animationFrameID;

    this._animationFrameID = jd;

  };

  vecOrigin() { return this._vecOrigin; };

  trackLegendContext(ctx) {

    if (ctx === undefined) return this._trackLegendContext;

    if (typeof(ctx) !== "object") {
      alert("MgrDrawECC-def::trackLegendContext()::Error: ctx is not an object!!!: typeof(ctx) = " + typeof(ctx) + "!!!");
      return;
    }

    this._trackLegendContext = ctx;

  };

  trackLegendLineBeg(lineBeg) {

    if (lineBeg === undefined) return this._trackLegendLineBeg;

    if (!Utils.checkNumber(lineBeg)) {
      alert("MgrDrawECC-def::trackLegendLineBeg()::Error: lineBeg is not a number: " + lineBeg + "!!!");
      return;
    }

    this._trackLegendLineBeg = lineBeg;

  };

  trackLegendLineEnd(lineEnd) {

    if (lineEnd === undefined) return this._trackLegendLineEnd;

    if (!Utils.checkNumber(lineEnd)) {
      alert("MgrDrawECC-def::trackLegendLineEnd()::Error: lineEnd is not a number: " + lineEnd + "!!!");
      return;
    }

    this._trackLegendLineEnd = lineEnd;

  };

};
