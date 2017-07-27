class DetGeomElement { // Base class for geometry description of the OPERA detector components

  static checkID(jd) {

    if (!Utils.checkNumber(jd)) {
      alert("DetElem-defs.js::DetGeomElement::checkID()::Error: jd is not a number: jd = " + jd + "!!!");
      return false;
    }

    if ( (jd < 0) || (jd > 10000) ) {
      alert("DetElem-defs.js::DetGeomElement::checkID()::Error: jd is strange: jd = " + jd + "!!!");
      return false;
    }

    return true;

  };

  static checkXYMax(xymax) {

    if (!Utils.checkNumber(xymax)) {
      alert("DetElem-defs.js::DetGeomElement::checkXYMax()::Error: xymax is not a number: xymax = " + xymax + "!!!");
      return false;
    }

    if ( (xymax < DetCfg.globDetBounds().xyzMin[0]) || (xymax > DetCfg.globDetBounds().xyzMax[0]) ) {
      alert("DetElem-defs.js::DetGeomElement::checkXYMax()::Error: xymax is strange: xymax = " + xymax + "!!!");
      return false;
    }

    return true;

  };

  static checkZMin(zmin) {

    if (!Utils.checkNumber(zmin)) {
      alert("DetElem-defs.js::DetGeomElement::checkZMin()::Error: zmin is not a number: zmin = " + zmin + "!!!");
      return false;
    }

    if ( (zmin < DetCfg.globDetBounds().xyzMin[2]) || (zmin > DetCfg.globDetBounds().xyzMax[2]) ) {
      alert("DetElem-defs.js::DetGeomElement::checkZMin()::Error: zmin is strange: zmin = " + zmin + "!!!");
      return false;
    }

    return true;

  };

  static checkDim(dim) {

    if (!Utils.checkNumber(dim)) {
      alert("DetElem-defs.js::DetGeomElement::checkDim()::Error: dim is not a number: dim = " + dim + "!!!");
      return false;
    }

    if ( (dim <= 0) || (dim > 900) ) {
      alert("DetElem-defs.js::DetGeomElement::checkDim()::Error: dim is strange: dim = " + dim + "!!!");
      return false;
    }

    return true;

  };

  constructor(id, xMax, yMax, zMin, dimX, dimY, dimZ) {

    if (!DetGeomElement.checkID(id)) return;
    if (!DetGeomElement.checkXYMax(xMax)) return;
    if (!DetGeomElement.checkXYMax(yMax)) return;
    if (!DetGeomElement.checkZMin(zMin))  return;

    if (!DetGeomElement.checkDim(dimX)) return;
    if (!DetGeomElement.checkDim(dimY)) return;
    if (!DetGeomElement.checkDim(dimZ)) return;

    this._id = id;

    this._xyMax = [xMax, yMax]; // Array of xMax and yMax coordinates (in cm)

    this._zMin  = zMin;          // zMin coordinate (in cm)

    this._dims  = [dimX, dimY, dimZ];

    this._color       = "white"; //!!!
    this._borderColor = "white"; //!!!

  };

  id() { return this._id; };

  xyMax(ip) {

    if (ip === undefined) return this._xyMax;

    if (!Utils.checkIP(ip)) {
      alert("DetElem-defs.js::DetGeomElement::xyMax()::Error: ip is wrong: ip = " + ip + "!!!");
      return;
    }

    return this._xyMax[ip];

  };

  zMin() { return this._zMin; };

  dims(ip) {

    if (ip === undefined) return this._dims;

    if (!Utils.checkIP(ip, 3)) {
      alert("DetElem-defs.js::DetGeomElement::dims()::Error: ip is wrong: ip = " + ip + "!!!");
      return;
    }

    return this._dims[ip];

  };

  color() { return this._color; };

  borderColor() { return this._borderColor; };

};
//-----------------------------------------------------------------------------

class WallTT extends DetGeomElement {

  constructor(id, xMax, yMax, zMin, dimX, dimY, dimZ) {

    super(id, xMax, yMax, zMin, dimX, dimY, dimZ);

    //this._color = "gray";
    //this._color = "dimgray";
    this._color = "darkgray";

    this._borderColor = "darkgray";

  };

};
//-----------------------------------------------------------------------------

class WallBrick extends DetGeomElement {

  constructor(id, xMax, yMax, zMin, dimX, dimY, dimZ) {

    super(id, xMax, yMax, zMin, dimX, dimY, dimZ);

    //this._color = "cadetblue";
    //this._color = "darkcyan";
    this._color = "mediumaquamarine";

    this._borderColor = "mediumaquamarine";

  };

};
//-----------------------------------------------------------------------------

class LayerRPC extends DetGeomElement {

  constructor(id, xMax, yMax, zMin, dimX, dimY, dimZ) {

    super(id, xMax, yMax, zMin, dimX, dimY, dimZ);

    //this._color = "sienna";
    //this._color = "goldenrod";
    //this._color = "indianred";
    //this._color = "darkorange";
    this._color = "chocolate";

    this._borderColor = "chocolate";

  };

};
//-----------------------------------------------------------------------------

class LayerDT extends DetGeomElement {

  constructor(id, xMax, yMax, zMin, dimX, dimY, dimZ) {

    super(id, xMax, yMax, zMin, dimX, dimY, dimZ);

    //this._color = "lightblue";
    //this._color = "skyblue";
    //this._color = "lightseagreen";
    this._color = "darkseagreen";

    this._borderColor = "darkseagreen";

  };

};
//-----------------------------------------------------------------------------

class BrickVis extends DetGeomElement {

  constructor(id, xMax, yMax, zMin, dimX, dimY, dimZ) {

    super(id, xMax, yMax, zMin, dimX, dimY, dimZ);

    //this._color = "cadetblue";
    //this._color = "darkcyan";
    this._color = "mediumaquamarine";

    this._borderColor = "dimgray";

  };

};
//-----------------------------------------------------------------------------

class BrickVertex extends DetGeomElement {

  constructor(id, xMax, yMax, zMin, dimX, dimY, dimZ) {

    super(id, xMax, yMax, zMin, dimX, dimY, dimZ);

    //this._color = "fuchsia";
    //this._color = "hotpink";
    //this._color = "magenta";
    //this._color = "orchid";
    //this._color = "plum";
    //this._color = "violet";
    //this._color = "deeppink";
    this._color = "lightpink";

    this._borderColor = "dimgray";

  };

};
//-----------------------------------------------------------------------------
