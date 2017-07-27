// Definitions of classes Hit, HitTT, HitRPC, and HitDT for hits of electronic detectors (ED)

class Hit { // base class for ED hits

  static checkId(jd) {

    if (!Utils.checkNumber(jd)) {
      alert("Hits-defs.js::Hit::checkId()::Error: jd = " + jd + "!!!");
      return false;
    }

    return true;

  };

  static checkX(xx) {

    if (!Utils.checkNumber(xx)) {
      alert("Hits-defs.js::Hit::checkX()::Error: xx = " + xx + "!!!");
      return false;
    }

    if ( (xx < -500) || (xx > 500) ) {
      alert("Hits-defs.js::Hit::checkX()::Error: xx = " + xx + "!!!");
      return false;
    }

    return true;

  };

  static checkZ(zz) {

    if (!Utils.checkNumber(zz)) {
      alert("Hits-defs.js::Hit::checkZ()::Error: zz = " + zz + "!!!");
      return false;
    }

    if ( (zz < -1000) || (zz > 1500) ) {
      alert("Hits-defs.js::Hit::checkZ()::Error: zz = " + zz + "!!!");
      return false;
    }

    return true;

  };

  constructor(id, x, z) {

    if (!Hit.checkId(id)) return;
    if (!Hit.checkX(x)) return;
    if (!Hit.checkZ(z)) return;

    this._id = id;

    this._x = x;   // X or Y coordinate (depending on XZ or YZ view) in the reference system of the OPERA detector 
    this._z = z;   // Z coordinate in the reference system of the OPERA detector 

    this._initColor = "black";

    this._color = this._initColor;

  };

  x() { return this._x; };

  z() { return this._z; };

  id() { return this._id; };

  color(col) {

    if (col === undefined) return this._color;

    this._color = col;

  };

};
//--------------------------------------------------------------------------

class HitTT extends Hit { // Hit of the Target Tracker (TT) detector

  static checkAmpl(ampl) {

    if (!Utils.checkNumber(ampl)) {
      alert("Hits-defs.js::HitTT::checkAmpl()::Error: ampl = " + ampl + "!!!");
      return false;
    }

    if ( (ampl < 0) || (ampl > 1500) ) {
      alert("Hits-defs.js::HitTT::checkAmpl()::Error: ampl = " + ampl + "!!!");
      return false;
    }

    return true;

  };

  constructor(id, x, z, ampl) {

    super(id, x, z);

    if (!HitTT.checkAmpl(ampl)) return;
    //if (!HitTT.checkAmpl(amplR)) return;

    this._ampl = ampl; // amplitude of the TT signal from the "left" side (in photo-electrons, p.e.) 
    //this._amplR = amplR; // amplitude of the TT signal from the "right" side (in photo-electrons, p.e.) 

    //this._colorL = "red";

  };

  ampl() { return this._ampl; };
  //amplR() { return this._amplR; };

  //colorL(col) {
    //if (col === undefined) return this._colorL;
    //this._colorL = col;
  //};

};
//--------------------------------------------------------------------------

class HitRPC extends Hit { // Hit of the RPC detector

  static checkClusterLength(length) {

    if (!Utils.checkNumber(length)) {
      alert("Hits-defs.js::HitRPC::checkClusterLength()::Error: length = " + length + "!!!");
      return false;
    }

    if ( (length < 0) || (length > 500) ) {
      alert("Hits-defs.js::HitRPC::checkClusterLength()::Error: length = " + length + "!!!");
      return false;
    }

    return true;

  }

  constructor(id, x, z, clLength) {

    super(id, x, z);

    if (!HitRPC.checkClusterLength(clLength)) return;

    this._clLength = clLength; // cluster length

  }

  clLength() { return this._clLength; }

};
//--------------------------------------------------------------------------

class HitDT extends Hit { // Hit of the HPT (drift tubes) detector

  static checkDriftDist(dist) {

    if (!Utils.checkNumber(dist)) {
      alert("Hits-defs.js::HitDT::checkDriftDist()::Error: dist = " + dist + "!!!");
      return false;
    }

    if ( (dist < 0) || (dist > 10) ) {
      alert("Hits-defs.js::HitDT::checkDriftDist()::Error: dist = " + dist + "!!!");
      return false;
    }

    return true;

  }

  constructor(id, x, z, driftDist) {

    super(id, x, z);

    if (!HitDT.checkDriftDist(driftDist)) return;

    this._driftDist = driftDist; // drift distance

  }

  driftDist() { return this._driftDist; }

};
//--------------------------------------------------------------------------

