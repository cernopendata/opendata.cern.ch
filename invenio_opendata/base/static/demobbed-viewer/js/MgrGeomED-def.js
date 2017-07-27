class MgrGeomED { // Contains parameters of the OPERA ED geometry

  constructor() {

    this._wallsTT    = [];
    this._wallsBrick = [];
    this._layersRPC  = [];
    this._layersDT   = [];


    this._bricksSM1VisXY = [[], []]; // Array of two arrays of bricks of SM1
                                     // to be displayed in XZ and YZ projections

    this._bricksSM2VisXY = [[], []]; // Array of two arrays of bricks of SM2
                                     // to be displayed in XZ and YZ projections

    this._brickVertex = []; // The array contains only 1 (vertex) brick

  };

  wallsTT(ttwalls) {

    if (ttwalls === undefined) return this._wallsTT;

    if (!Array.isArray(ttwalls)) {
      alert("MgrGeomED-def::wallsTT()::Error: ttwalls is not an Array!!!");
      return;
    }

    this._wallsTT = ttwalls;

  };

  wallsBrick(brickwalls) {

    if (brickwalls === undefined) return this._wallsBrick;

    if (!Array.isArray(brickwalls)) {
      alert("MgrGeomED-def::wallsBrick()::Error: brickwalls is not an Array!!!");
      return;
    }

    this._wallsBrick = brickwalls;

  };

  layersRPC(rpclayers) {

    if (rpclayers === undefined) return this._layersRPC;

    if (!Array.isArray(rpclayers)) {
      alert("MgrGeomED-def::layersRPC()::Error: rpclayers is not an Array!!!");
      return;
    }

    this._layersRPC = rpclayers;

  };

  layersDT(dtlayers) {

    if (dtlayers === undefined) return this._layersDT;

    if (!Array.isArray(dtlayers)) {
      alert("MgrGeomED-def::layersDT()::Error: dtlayers is not an Array!!!");
      return;
    }

    this._layersDT = dtlayers;

  };

  bricksSM1VisXY(ip) {

    if (ip === undefined) return this._bricksSM1VisXY;

    if (!Utils.checkIP(ip)) {
      alert("MgrGeomED-def::bricksSM1VisXY()::Error: ip is wrong: ip = " + ip + "!!!");
      return;
    }

    return this._bricksSM1VisXY[ip];

  };

  bricksSM2VisXY(ip) {

    if (ip === undefined) return this._bricksSM2VisXY;

    if (!Utils.checkIP(ip)) {
      alert("MgrGeomED-def::bricksSM2VisXY()::Error: ip is wrong: ip = " + ip + "!!!");
      return;
    }

    return this._bricksSM2VisXY[ip];

  };

  brickVertex(brick) {

    if (brick === undefined) return this._brickVertex;

    if (!Array.isArray(brick)) {
      alert("MgrGeomED-def::brickVertex()::Error: brick is not an Array (as it should be)!!!");
      return;
    }

    this._brickVertex = brick;

  };

};
