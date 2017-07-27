function loadEvent(obj, event, value) { // A separate function is used because it is associated
                                                 // with the onkeypress event in the index.html

  if (event.which != 13 && event.keyCode != 13) return;

  let evID = +value;

  let evIndex = demobbed.evList().indexOf(evID);

  if (evIndex == -1) {
    alert("loadEvent.js::Error: Event " + evID + " is not present in the event list!");
    return; //!!!
  }

  demobbed.evIndex(evIndex);

  changeScrLoadEvent(evID);

};
//------------------------------------------------------------------------------

function changeScrLoadEvent(evID) { // It is assumed here that the evID has been already checked!

  let scrLoadEvent = document.createElement("script");

  scrLoadEvent.src = "/demobbed-viewer/js/nuEventsData/loadEvent" + evID + ".js";
  scrLoadEvent.innerHTML = null;
  scrLoadEvent.id = "scrLoadEvent";

  let divScrLoadEvent = document.getElementById("divScrLoadEvent");

  divScrLoadEvent.innerHTML = "";
  divScrLoadEvent.appendChild(scrLoadEvent);

};
//------------------------------------------------------------------------------
