/*
    Copyright (c) 2017, Sergey Dmitrievsky

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

class Demobbed { // Demonstrative browser-based event display

  constructor() {

    this._evList     = [];    // Array of OPERA event IDs available for open data access
    this._evIndex    = -1;    // Index of the loaded event in the array (from 0 to evList.length - 1)
    this._evIndexMax = -1;    // Max index of the loaded event in the array (=== evList.length - 1)
    this._event      = {};    // Loaded (displayed) event

    this._mgrGeomED  = {};    // Contains parameters of the OPERA ED geometry

    this._mgrDrawED  = {};    // Manager hired for drawing of Electronic detector (2D) events

    this._mgrDrawECC = {};    // Manager hired for drawing of (3D) tracks found in emulsion

    this._showECC = 0;

  };

  evList(evlist) {

    if (evlist === undefined) return this._evList;

    if (!Array.isArray(evlist)) {
      alert("Demobbed-def::evList()::Error: evlist is not an Array!!!");
      return;
    }

    if (evlist.length > 1000) {
      alert("Demobbed-def::evList()::Error: evlist.length > 1000: " + evlist.length + "!!!");
      return;
    }

    this._evList = evlist;
    this._evIndex = 0;
    this._evIndexMax = evlist.length - 1;

  };

  evIndex(evindex) {

    if (evindex === undefined) return this._evIndex;

    if (!this.checkEvIndex(evindex)) return;

    this._evIndex = evindex;

  };

  event(ev) {

    if (ev === undefined) return this._event;

    if (typeof(ev) !== "object") {
      alert("Demobbed-def::event()::Error: ev is not an object!!!: typeof(ev) = " + typeof(ev) + "!!!");
      return;
    }

    this._event = ev;

  };

  resetEvent() { this._event = new Event(); };

  loadPrevOrNextEvent(dIndex) {

    if (dIndex === undefined) dIndex = 1; // by default load next event in the event list
    else if (!Utils.checkNumber(dIndex)) {
      alert("Demobbed-def::loadPrevOrNextEvent()::Error: dIndex is not a number!!!: dIndex = " + dIndex + "!!!");
      return;
    }

    let newIndex = this._evIndex + dIndex;

    if (!this.checkEvIndex(newIndex, false)) return;

    this._evIndex = newIndex;

    let evID = this._evList[newIndex];

    changeScrLoadEvent(evID); // External function defined in the loadEvent.js file

  };

  checkEvIndex(evindex, showAlerts) {

    if (showAlerts === undefined) showAlerts = true;

    if (!Utils.checkNumber(evindex)) {
      if (showAlerts) alert("Demobbed-def::checkEvIndex()::Error: evindex is not a number!!!: evindex = " + evindex + "!!!");
      return false;
    }

    if ( (evindex < 0) || (evindex > this._evIndexMax) ) {
      if (showAlerts)  alert("Demobbed-def::checkIndex()::Error: index is out of range: evindex = " + evindex + "!!!");
      return false;
    }

    return true;

  };

  mgrGeomED(mgrgeom) {

    if (mgrgeom === undefined) return this._mgrGeomED;

    if (typeof(mgrgeom) !== "object") {
      alert("Demobbed-def::mgrGeomED()::Error: mgrgeom is not an object: mgrgeom = " + mgrgeom + "!!!");
      return;
    }

    this._mgrGeomED = mgrgeom;

  };

  mgrDrawED(mgrdraw) {

    if (mgrdraw === undefined) return this._mgrDrawED;

    if (typeof(mgrdraw) !== "object") {
      alert("Demobbed-def::mgrDrawED()::Error: mgrdraw is not an object: mgrdraw = " + mgrdraw + "!!!");
      return;
    }

    this._mgrDrawED = mgrdraw;

  };

  mgrDrawECC(mgrdraw) {

    if (mgrdraw === undefined) return this._mgrDrawECC;

    if (typeof(mgrdraw) !== "object") {
      alert("Demobbed-def::mgrDrawECC()::Error: mgrdraw is not an object: mgrdraw = " + mgrdraw + "!!!");
      return;
    }

    this._mgrDrawECC = mgrdraw;

  };

  showECC(show) {

    if (show === undefined) return this._showECC;

    if (!Utils.checkNumber(show)) {
      alert("Demobbed-def::showECC()::Error: show is not a number!!!: show = " + show + "!!!");
      return;
    }

    this._showECC = show;

  };

};
