class Vertex {

  constructor(pos, posGlob) {

    for (let ip = 0; ip < 3; ip++) {

      if (!Utils.checkPos(pos[ip], ip)) {
        alert("Vertex-def::constructor()::Error: pos[" + ip + "] is not correct!");
        return;
      }

      if (!Utils.checkPosGlob(posGlob[ip], ip)) {
        alert("Vertex-def::constructor()::Error: posGlob[" + ip + "] is not correct!");
        return;
      }

    }

    this._pos = pos;         // [posX, posY, posZ] Position in the OPERA brick system of reference (in micrometers)

    this._posGlob = posGlob; // [posGlobX, posGlobY, posGlobZ] Position in the OPERA detector system of reference (in cm)

  };

  pos(ps) {

    if (ps === undefined) return this._pos;

    if (!Array.isArray(ps)) {
      alert("Vertex-def::pos()::Error: ps is not an Array!!!");
      return;
    }

    if (ps.length != 3) {
      alert("Vertex-def::pos()::Error: Length of array of ps is != 3:" + ps.length + "!!!");
      return false;
    }

    this._pos = ps;

  };

  posGlob(ps) {

    if (ps === undefined) return this._posGlob;

    if (!Array.isArray(ps)) {
      alert("Vertex-def::posGlob()::Error: ps is not an Array!!!");
      return;
    }

    if (ps.length != 3) {
      alert("Vertex-def::posGlob()::Error: Length of array of ps is != 3:" + ps.length + "!!!");
      return false;
    }

    this._posGlob = ps;

  };

  static color() { return "darkmagenta"; };

};
