//gmED == demobbed.mgrGeomED() !!!
//---------------------------------

gmED.genBrickVisPars = function() {

  const nbOfBrickWalls = [DetCfg.nbOfBrickWallsInSM1(), DetCfg.nbOfBrickWallsInSM2()];

  const nbOfBricks = [DetCfg.nbOfBrickColumns(), DetCfg.nbOfBrickRows()];

  const brDimX = DetCfg.brickDims(0);
  const brDimY = DetCfg.brickDims(1);
  const brDimZ = DetCfg.brickDims(2);

  const brVis = [

    [[], []],
    [[], []]

  ];

  for (let sm = 0; sm < 2; sm++) {

    let brID = 0;

    for (let ip = 0; ip < 2; ip++) {
  
      brID = 0;
  
      for (let iw = 0; iw < nbOfBrickWalls[sm]; iw++) {

        const wn = sm*nbOfBrickWalls[0] + iw;
    
        let   brXmax = gmED.wallsBrick()[wn].xyMax(0);
        let   brYmax = gmED.wallsBrick()[wn].xyMax(1);
        const brZmin = gmED.wallsBrick()[wn].zMin(0);
    
        for (let ic = 0; ic < nbOfBricks[ip]; ic++) {
    
          brVis[sm][ip][brID] = new BrickVis(brID, brXmax, brYmax, brZmin, brDimX, brDimY, brDimZ),
    
          brID++;
    
          if (ip) brYmax -= brDimY;
          else    brXmax -= brDimX;
    
        }
    
      }
  
    }

  }

  gmED.bricksSM1VisXY()[0] = brVis[0][0];
  gmED.bricksSM1VisXY()[1] = brVis[0][1];

  gmED.bricksSM2VisXY()[0] = brVis[1][0];
  gmED.bricksSM2VisXY()[1] = brVis[1][1];

};
//------------------------------------------------------------------------------

gmED.findBrickVertexPars = function() {

  const vPos_10000 = demobbed.event().vertex()[0].pos();

  const vPosGlob = demobbed.event().vertex()[0].posGlob();

  let brVis = [[], []];

  if (vPosGlob[2] < 0) brVis = gmED.bricksSM1VisXY();
  else brVis = gmED.bricksSM2VisXY();

  let brZmin = 10000;

  const brXYmax = [-10000, -10000];

  const Dmax = [0, 0];

  let nbOfBricks = 0;

  for (let ip = 1; ip >= 0; ip--) { //!!!

    vPos_10000[ip] /= 10000;

    Dmax[ip] = DetCfg.brickDims(ip) - 1;

    nbOfBricks = brVis[ip].length;

    for (let ib = 0; ib < nbOfBricks; ib++) {

      const Dxy = vPosGlob[ip] - brVis[ip][ib].xyMax(ip);

      if (Dxy < 0) continue; //!!!

      if ( (Dxy < 1) && (vPos_10000[ip] > Dmax[ip]) )
      {
        brXYmax[ip] = brVis[ip][ib].xyMax(ip);

        break; //!!!

      }

      if ( (Dxy > Dmax[ip]) && (vPos_10000[ip] < 1) )
      {

        brXYmax[ip] = brVis[ip][ib].xyMax(ip) + 2*DetCfg.brickDims(ip);

        break; //!!!

      }

      brXYmax[ip] = brVis[ip][ib].xyMax(ip) + DetCfg.brickDims(ip);

      break; //!!!

    }

    if (brXYmax[ip] < -1000) brXYmax[ip] = brVis[ip][nbOfBricks - 1].xyMax(ip);

  }

  for (let ib = 0; ib < nbOfBricks; ib += DetCfg.nbOfBrickColumns()) { //!!!

    if (brVis[0][ib].zMin() - vPosGlob[2] > 2.7) { // cm

      brZmin = brVis[0][ib].zMin() - DetCfg.brickWallToWallDistZ();

      break; //!!!

    }

  }

  if (brZmin > 1000) brZmin = brVis[0][nbOfBricks - 1].zMin();

  //gmED.brickVertex([new BrickVertex(0, brXYmax[0], brXYmax[1], brZmin, DetCfg.brickDims(0), DetCfg.brickDims(1), DetCfg.brickDims(2))]);

  // Make the vertex brick dims a bit higher to overcome possible disalignment!

  const mm3 = 0.3;   // 3mm
  const mm6 = 2*mm3; 

  gmED.brickVertex([new BrickVertex(0, brXYmax[0] + mm3, brXYmax[1] + mm3, brZmin - mm3,
                   DetCfg.brickDims(0) + mm6, DetCfg.brickDims(1) + mm6, DetCfg.brickDims(2) + mm6)]);

};
//------------------------------------------------------------------------------
