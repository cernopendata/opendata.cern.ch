import d3 from "d3";
import jQuery from "jquery/dist/jquery";
import "flot/jquery.flot";
import "flot/jquery.flot.selection";

jQuery(function ($) {
  var input_data;

  var input_files = [
    {
      id: "dimuon0",
      name: "dimuon events with invariant mass between 2-110 GeV",
      file: "/record/700/files/MuRun2010B_0.csv",
      type: "two_lepton"
    },
    {
      id: "Jpismumu",
      name: "dimuon events with invariant mass between 2-5 GeV",
      file: "/record/301/files/dimuon-Jpsi.csv",
      type: "two_lepton"
    },
    {
      id: "Jpsiee",
      name: "dielectron events with invariant mass between 2-5 GeV",
      file: "/record/302/files/dielectron-Jpsi.csv",
      type: "two_lepton"
    },
    {
      id: "Yee",
      name: "dielectron events with invariant mass between 8-12 GeV",
      file: "/record/305/files/dielectron-Upsilon.csv",
      type: "two_lepton"
    },
    {
      id: "Zee",
      name: "dielectron events around the Z boson mass",
      file: "/record/306/files/Zee.csv",
      type: "two_lepton"
    },
    {
      id: "Zmumu",
      name: "dimuon events around the Z boson mass",
      file: "/record/307/files/Zmumu.csv",
      type: "two_lepton"
    },
    {
      id: "Wenu",
      name: "W bosons decaying to an electron and a neutrino",
      file: "/record/308/files/Wenu.csv",
      type: "lepton_neutrino"
    },
    {
      id: "Wmuu",
      name: "W bosons decaying to a muon and a neutrino",
      file: "/record/309/files/Wmunu.csv",
      type: "lepton_neutrino"
    }
  ];

  // We know the names of the parameters that we have produced in the csv files.
  // We also have only two event types in the csv: lepton_neutrino and two_lepton.
  // We therefore provide some information on the parameters.
  var event_types = {
    "two_lepton":
      [{name: "E1", unit: "GeV", description: "The total energy of the first lepton"},
        {name: "pt1", unit: "GeV", description: "The transverse momentum of the first lepton"},
        {name: "eta1", unit: null, description: "The pseudorapidity of the first muon"},
        {name: "phi1", unit: "radians", description: "The phi angle of the first lepton direction"},
        {name: "Q1", unit: null, description: "The charge of the first lepton"},
        {name: "E2", unit: "GeV", description: "The total energy of the second lepton"},
        {name: "pt2", unit: "GeV", description: "The transverse momentum of the second lepton"},
        {name: "eta2", unit: null, description: "The pseudorapidity of the second lepton"},
        {name: "phi2", unit: "radians", description: "The phi angle of the second muon lepton"},
        {name: "Q2", unit: null, description: "The charge of the second lepton"},
        {name: "M", unit: "GeV", description: "The invariant mass of the two leptons"}
      ],
    "lepton_neutrino":
      [{name: "E", unit: "GeV", description: "The total energy of the lepton"},
        {name: "MET", unit: "GeV", description: "The missing transverse energy due to the neutrino"},
        {name: "Q", unit: null, description: "The charge of the lepton"},
        {name: "phiMET", unit: "radians", description: "The phi angle of the missing transverse energy"},
        {name: "eta", unit: null, description: "The pseudorapidity of the lepton"},
        {name: "phi", unit: "radians", description: "The phi angle of the lepton direction"},
        {name: "pt", unit: "GeV", description: "The transverse momentum of the lepton"}
      ]
  };


  $('#howto').hide();
  $('#backtohisto').hide();


  $('#backtohisto').on('click', function () {
    $('#histograms').show();
    $('#needhelp').show();
    $('#backtohisto').hide();
    $('#howto').hide();
  });

  $('#needhelp').on('click', function () {
    $('#histograms').hide();
    $('#howto').show();
    $('#needhelp').hide();
    $('#backtohisto').show();
  });

  function loadInitialHistogram() {
    $('#parameter-button-row div button')[0].click();
  }

  function loadFile(input) {
    //$('#filename').html(input.file.split('/').pop());
    // $('#filedropdown').button('loading');

    d3.csv(input.file,
      function (d) { // leading and trailing spaces in csv aren't ignored so we strip them out (if there) in the accessor
        var newd = {};
        var key = null;
        for (key in d) {
          if (!is_excluded(key.trim())) {
            newd[key.trim()] = +d[key];
          }
        }
        return newd;
      },
      function (data) {
        populateValues(data[0], input.type);
        input_data = data;
        // $('#filedropdown').button('reset');
        $('#filedropdown').html(input.name + ' ');
        $('#filedropdown').append('<span class="caret"></span>');
        loadInitialHistogram();
      }
    );
  }

  // Load a file automatically...
  //...and activate the first histogram
  loadFile(input_files[0]);

  $.each(input_files, function (f) {
    $('#filelist').append(
      "<div class='item' data-value='" +
        input_files[f].id +
        "' id='" +
        input_files[f].id +
        "'>" +
        input_files[f].name +
        "</div>"
    );
  });

  // Some fields aren't numbers, or it doesn't make sense to plot them, or they are redundant.
  // Therefore exclude them.
  var excluded = ["Run", "Event", "Type", "Type1", "Type2", "px1", "py1", "pz1", "px2", "py2", "pz2", "px", "py", "pz"];

  function is_excluded(key) {
    if (excluded.indexOf(key) === -1) {
      return false;
    }
    return true;
  }

  function get_parameter_info(name, type) {
    for (var i = 0; i < type.length; i++) {
      if (name === type[i].name) {
        if (type[i].unit !== null) {
          return type[i].description + ' [' + type[i].unit + ']';
        } else {
          return type[i].description;
        }
      }
    }
  }

  function populateValues(data, type) {
    for (var key in data) {
      var parameter_info = get_parameter_info(key, event_types[type]);
      $("#parameter-button-row").append(
        `<div class='item'><button title='${parameter_info}' class='ui toggle button parameter'>${key}</button></div>`
      );
    }
  }

  function buildHistogram(data, bw) {
    var minx = d3.min(data),
      maxx = d3.max(data),
      nbins = Math.floor((maxx - minx) / bw);

    var histogram = d3.layout.histogram();
    histogram.bins(nbins);
    data = histogram(data);

    var output = [];
    for (var i = 0; i < data.length; i++) {
      output.push([data[i].x, data[i].y]);
      output.push([data[i].x + data[i].dx, data[i].y]);
    }
    return output;
  }

  var makeLog = function (v) {
    return v > 0 ? Math.log(v) : 0;
  };
  var makeExp = function (v) {
    return Math.log(v);
  }

  $(document).on('click', '#filelist div', function () {
    var id = $(this).attr("id");
    var input_file = $.grep(input_files, function (i) {
      return i.id == id;
    });
    $('#parameter-button-row').empty();
    $('#flot-plots').empty();
    loadFile(input_file[0]);
  });

  $(document).on('click', '.parameter', function () {
    $(this).toggleClass("active");
    var parameter = $(this).html();
    var title = $(this).attr('title');

    var parId = '#' + parameter;

    if ($(this).hasClass('active')) {
      $('#flot-plots').append(
        "<div id='" + parameter + "' class='eight wide column'></div>"
      );
      $(parId).css({ border: "1px dotted" });

      $(parId).append(
        "<div class='ui form'><div class='inline fields plot-control'></div></div>"
      );
      $(parId).append("<div class='plot-container'></div>");
      $(parId).append("<div class='xlabel'></div>");

      $(parId + ' div.plot-control').css({});
      $(parId + ' div.plot-container').css({ height: "300px" });

      // This screams "template!"
      var logbtns = "<div class='ui buttons'>";
      logbtns +=
        "<button class='ui toggle button logx " +
        parameter +
        "'> Log X</button > ";
      logbtns +=
        "<button class='ui toggle button logy " +
        parameter +
        "'>Log Y</button>";
      logbtns += "</div>";

      $(parId + ' div.plot-control').append(logbtns);

      var bininput = "<div class='ui action input'>";
      bininput +=
        "<input type='number' min='1' name='binwidth' placeholder='Set bin width'>";
      bininput +=
        "<button class='ui button binw " + parameter + "'>Set</button>";
      bininput += "</div>";

      $(parId + " div.plot-control").append(bininput);

      var selectbtn = "<div class='ui buttons'>";
      selectbtn +=
        "<button class='ui button undoselect " +
        parameter +
        "'>Undo selection(s)</button>";
      selectbtn += "</div>";

      $(parId + ' div.plot-control').append(selectbtn);

      var options = {
        label: parameter,
        lines: {show: true, fill: false, lineWidth: 1.2},
        grid: {hoverable: true, autoHighlight: false},
        xaxis: {tickDecimals: 0},
        yaxis: {autoscaleMargin: 0.1},
        crosshair: {mode: "xy"},
        selection: {mode: "x", color: "yellow"}
      };

      var histogram = buildHistogram(input_data.map(function (d) {
        return d[parameter];
      }), 0.1);

      var data = [{data: histogram, label: parameter}];
      var plot = $.plot($(parId + ' .plot-container'), data, options);

      $(parId+ ' .xlabel').html(title);

      plot.setupGrid();
      plot.draw();

      var xmin = plot.getAxes().xaxis.min;
      var xmax = plot.getAxes().xaxis.max;

      $('button.logx.' + parameter).on('click', function () {
        if (!$(this).hasClass('active')) {
          $.extend(true, options, {xaxis: {transform: makeLog, inverseTransform: makeExp}});
        } else {
          $.extend(true, options, {xaxis: {transform: null, inverseTransform: null}});
        }
        $(this).toggleClass("active");
        $.plot($(parId + ' .plot-container'), data, options);
      });

      $("button.logy." + parameter).on("click", function () {
        if (!$(this).hasClass("active")) {
          $.extend(true, options, {
            yaxis: { transform: makeLog, inverseTransform: makeExp },
          });
        } else {
          $.extend(true, options, {
            yaxis: { transform: null, inverseTransform: null },
          });
        }
        $(this).toggleClass("active");
        $.plot($(parId + " .plot-container"), data, options);
      });

      $('button.binw.' + parameter).on(
        'click',
        function () {
          var value = $('input[name=binwidth]').val();
          if (value > 0) {
            histogram = buildHistogram(
              input_data.map(function (d) {
                return d[parameter];
              }),
              value
            );
            data = [{data: histogram, label: parameter}];
            $.plot($(parId + ' .plot-container'), data, options);
          }
        }
      );

      $('button.undoselect.' + parameter).on('click', function () {
        $.extend(true, options, {xaxis: {min: xmin, max: xmax}});
        $.plot($(parId + ' .plot-container'), data, options);
      });

      $(parId + ' .plot-container').bind("plotselected", function (event, ranges) {
        //console.log("You selected " + ranges.xaxis.from.toFixed(1) + " to " + ranges.xaxis.to.toFixed(1));
        $.extend(true, options, {xaxis: {min: ranges.xaxis.from, max: ranges.xaxis.to}});
        $.plot($(parId + ' .plot-container'), data, options);
      });

    } else {
      $('#' + parameter).remove();
    }
  });
});
