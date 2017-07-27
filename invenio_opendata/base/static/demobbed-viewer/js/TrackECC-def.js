class TrackECC {

  static checkID(jd) {

    if (!Utils.checkNumber(jd)) {
      alert("TrackECC-def::checkID()::Error: jd is not a number: jd = " + jd + "!!!");
      return false;
    }

    if ( (jd < 0) || (jd > 20) ) {
      alert("TrackECC-def::checkID()::Error: jd is strange: jd = " + jd + "!!!");
      return false;
    }

    return true;

  };

  static checkPartID(jd) {

    if (!Utils.checkNumber(jd)) {
      alert("TrackECC-def::checkPartID()::Error: jd is not a number: jd = " + jd + "!!!");
      return false;
    }

    if ( (jd < 1) || (jd > 8) ) {
      alert("TrackECC-def::checkPartID()::Error: jd is strange: jd = " + jd + "!!!");
      return false;
    }

    return true;

  };

  static checkSlope(slope, ip) {

    if (ip === undefined) ip = 2;
    else if (!Utils.checkIP(ip)) {
      alert("TrackECC-def::checkSlope()::Error: ip is wrong: ip = " + ip + "!!!");
      return false;
    }

    if (!Utils.checkNumber(slope)) {
      alert("TrackECC-def::checkSlope()::Error: slope[" + ip + "] is not a number: " + slope + "!!!");
      return false;
    }

    if ( (slope < -0.85) || (slope > 0.85) ) {
      alert("TrackECC-def::checkSlope()::Error: slope[" + ip + "] is strange: " + slope + "!!!");
      return false;
    }

    return true;

  };

  constructor(id, partId, pos, slopes) {

    if (!TrackECC.checkID(id)) return;
    if (!TrackECC.checkPartID(partId)) return;

    for (let ip = 0; ip < 3; ip++) {

      if (!Utils.checkPos(pos[ip], ip)) {
        alert("TrackECC-def::constructor()::Error: pos[" + ip + "] is not correct!");
        return;
      }

      if (ip == 2) break; //!!!

      if (!TrackECC.checkSlope(slopes[ip], ip)) return;

    }

    this._id = id;

    this._partId = partId; // particle Id

    this._pos = pos;       // [posX, posY, posZ] Position in the OPERA brick system of reference (in micrometers)

    // Equations of a track:
    // X = Z*Axy[0] + Bxy[0], Y = Z*Axy[1] + Bxy[1]

    this._Axy = slopes; // [slopeXZ, slopeYZ] --- tangents of the track angles

  };

  id() { return this._id; };

  partId() { return this._partId; };

  pos(ps) {

    if (ps === undefined) return this._pos;

    if (!Array.isArray(ps)) {
      alert("TrackECC-def::pos()::Error: ps is not an Array!!!");
      return;
    }

    if (ps.length != 3) {
      alert("TrackECC-def::pos()::Error: Length of array of ps is != 3:" + ps.length + "!!!");
      return false;
    }

    this._pos = ps;

  };

  Axy(ip) {

    if (ip === undefined) return this._Axy;

    if (!Utils.checkIP(ip)) {
      alert("TrackECC-def::Axy()::Error: ip is wrong: ip = " + ip + "!!!");
      return;
    }

    return this._Axy[ip];

  };

  static colors(partId) {

    switch (partId) {

      case 1: return "blue";    // for a track of muon
      case 2: return "red";     // for a track of hadron
      case 3: return "green";   // for a track of electron
      case 4: return "black";   // for a black track
      case 5: return "black";   // for a back black track
      case 6: return "dimgray"; // for a gray track
      case 7: return "dimgray"; // for a back gray track
      case 8: return "orange";  // for a track of tau lepton

      default: return "white";  // for other tracks

    }

  };

};
//------------------------------------------------------------------------------
