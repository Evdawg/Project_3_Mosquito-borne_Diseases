
// Initialization information for base maps

let myMap = L.map("map", {
  center: [39.8, -98.5],
  zoom: 4
});

let myMap2 = L.map("map2", {
  center: [39.8, -98.5],
  zoom: 4
});

let myMap3 = L.map("map3", {
  center: [39.8, -98.5],
  zoom: 4
});


// Adding the tile layer
let first = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
first.addTo(myMap);

let second = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap2);

let third = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap3);


// create drop down for disease selection
function diseaseDropDown() {
  let disease = d3.select("#disease");
  let disArray = [["Lyme"], ["West Nile"]];
   
  //console.log(disArray);
  // add options to dropdown
  disArray.forEach(
      function(addID) {
          disease
          .append("option")
          .attr("value", addID)
          .text(addID);
      })
    };

// creates dropdown for year selection
function YearDropdown() {
  let Year = d3.select("#Year");
    
  for(i= startYear; i < endYear+1; i++) {
    Year
    .append("option")
          .attr("value", i)
          .text(i.toString()); 
  }
}

// reads disease drop down selection 
// and passes to year selection function
function getDisease() {
  let selectDis = d3.select("#disease");  
  selectDis
      .on("change", function() {
          let dis = d3.event.target.value;
          if (dis == "Lyme") {
            disData = LData
          } else {
            disData = WData
          };
          //console.log(dis, disData)

          // if(countyLayer) {
          //   myMap.removeLayer(countyLayer);
          // }
          // if(countyTempLayer) {
          //   myMap2.removeLayer(countyTempLayer);
          // }
          // if(countyPrecLayer) {
          //   myMap3.removeLayer(countyPrecLayer);
          // }
          // console.log(year);
          // CreateDisLayer(disData, year);
          // CreateTempLayer(TData, year);
          // CreatePrecLayer(PData, year);
          getYear(disData);
      }
    )    
}

// reads year selection 
// removes current top layers if needed
// and activates top layer creation
function getYear (data) {
  let selectYr = d3.select("#Year");  
  selectYr
      .on("change", function() {
          let year = d3.event.target.value;
          //remove(heat);
          if(countyLayer) {
            myMap.removeLayer(countyLayer);
          }
          if(countyTempLayer) {
            myMap2.removeLayer(countyTempLayer);
          }
          if(countyPrecLayer) {
            myMap3.removeLayer(countyPrecLayer);
          }
          console.log(year);
          CreateDisLayer(data, year);
          CreateTempLayer(TData, year);
          CreatePrecLayer(PData, year);
      }   
    )
};

// creates disease layer
function CreateDisLayer(Data, year) {
  console.log(Data)
  let len = Data.length
  let countyMarkers = [];

    for (var i = 0; i < len; i++) {
      
      let county = Data[i];
      let mag = county[year]
      
      if (mag >= 1) {
          let param = Color(mag);
          circle = new L.circle([county.lat, county.lon], {
          fillOpacity: .3,
          color: param[0],
          fillColor: param[0],
          //weight:3,
          radius: param[1],
          stroke: false
          })
          countyMarkers.push(circle)
          //.bindPopup(dlist[i][0])
      }
    }
    countyLayer = L.layerGroup(countyMarkers);
    countyLayer.addTo(myMap);
};

// selects color, graduations, and radii for disease layer
function Color(mag) {
  if (mag >= 50) {
      color = "#7B241C";
      radius = 45000;
  } else if (mag >= 40 && mag < 50) {
      color = "#A93226 ";
      radius = 40000;
  } else if (mag >= 30 && mag < 40) {
      color = "#D98880";
      radius = 35000;
  } else if (mag >= 20 && mag <30) {
      color = "#C0392B";
      radius = 30000;
  } else if (mag >= 10 && mag <20) {
      color = "#EB984E";
      radius = 25000;
  } else {
      color = "#85929E"
      radius = 20000;
  };
  return [color, radius];
};

// creates temp layer
function CreateTempLayer(Data, year) {
  let len = Data.length
  let countyTempMarkers = [];

    for (var i = 0; i < len; i++) {
      
      let county = Data[i];
      let mag = county[year]

      if (mag > -20) {
          let param = TempColor(mag);
          circle = new L.circle([county.lat, county.lon], {
          fillOpacity: .2,
          color: param,
          fillColor: param,
          //weight:3,
          radius: 30000,
          stroke: false
          })
          countyTempMarkers.push(circle)
          //.bindPopup(dlist[i][0])
      }
    }
    countyTempLayer = L.layerGroup(countyTempMarkers);
    countyTempLayer.addTo(myMap2);
};

// selects color and graduations for temp layer
function TempColor(mag) {
  if (mag >= 82) {
    color = "#641E16";
  } else if (mag >= 79 && mag < 82) {
    color = "#7B241C";
  } else if (mag >= 76 && mag <79) {
    color = "#C0392B";
  } else if (mag >= 73 && mag <76) {
    color = "#D98880";
  } else if (mag >= 70 && mag <73){
    color = "#EB984E"; //"#D6EAF8"
  } else if (mag >= 67 && mag <70){
    color = "#85C1E9";
  } else {
    color = "#3498DB";
  };
  
  return color;
};

// creates precipitation layer
function CreatePrecLayer(Data, year) {
  let len = Data.length
  let countyPrecMarkers = [];

    for (var i = 0; i < len; i++) {
      
      let county = Data[i];
      let mag = county[year]

      if (mag > -20) {
          let param = precColor(mag);
          circle = new L.circle([county.lat, county.lon], {
          fillOpacity: .2,
          color: param,
          fillColor: param,
          //weight:3,
          radius: 30000,
          stroke: false
          })
          countyPrecMarkers.push(circle)
          //.bindPopup(dlist[i][0])
      }
    }
    countyPrecLayer = L.layerGroup(countyPrecMarkers);
    countyPrecLayer.addTo(myMap3);
  };


// selects color and graduations for prec layer
function precColor(mag) {
  if (mag >= 30) {
    color = "#641E16";
  } else if (mag >=25 && mag < 30) {
    color = "#7B241C";
  } else if (mag >= 20 && mag < 25) {
    color = "#A93226";
  } else if (mag >= 15 && mag <20) {
    color = "#C0392B";
  } else if (mag >= 10 && mag <15) {
    color = "#D98880";
  } else if (mag >= 5 && mag <10){
    color = "#EB984E"; //"#D6EAF8"
  } else if (mag >= 0 && mag <5){
    color = "#85C1E9";
  } else {
    color = "#3498DB";
  };
  
  return color;
};


  // Create a legend to display information about disease map
function diseaseLegend() {
  var info = L.control({
  position: "bottomright"
});
// When the layer control is added, insert a div with the class of "legend"
  info.onAdd = function() {
      var div = L.DomUtil.create("div", "legend");
      div.innerHTML=[
          "<h7>Cases:</h7></br>",
          "<span class='d1'>>=50</span>",
          "</br>",
          "<span class='d2'>40-49</span></br>",
          "<span class='d3'>30-39</span></br>",
          "<span class='d4'>20-29</span></br>",
          "<span class='d5'>10-19</span></br>",
          "<span class='d6'>0-9</span>"
      ].join("");

    return div;
};
// Add the info legend to the map
info.addTo(myMap);
};

 // Create a legend to display information about temp map
 function tempLegend() {
  var info = L.control({
  position: "bottomright"
});
// When the layer control is added, insert a div with the class of "legend"
  info.onAdd = function() {
      var div = L.DomUtil.create("div", "legend2");
      div.innerHTML=[
          "<h8>Temp(F):</h8></br>",
          "<span class='t1'>>82</span>",
          "</br>",
          "<span class='t2'>79-82</span></br>",
          "<span class='t3'>76-79</span></br>",
          "<span class='t4'>73-76</span></br>",
          "<span class='t5'>70-73</span></br>",
          "<span class='t6'>67-70</span></br>",
          "<span class='t7'><67</span>"
      ].join("");

    return div;
};
// Add the info legend to the map
info.addTo(myMap2);
};

// Create a legend to display information about prec map
function precLegend() {
  var info = L.control({
  position: "bottomright"
});
// When the layer control is added, insert a div with the class of "legend"
  info.onAdd = function() {
      var div = L.DomUtil.create("div", "legend3");
      div.innerHTML=[
          "<h8>Prec(in):</h8></br>",
          "<span class='p1'>>30</span>",
          "</br>",
          "<span class='p2'>25-30</span></br>",
          "<span class='p3'>20-25</span></br>",
          "<span class='p4'>15-20</span></br>",
          "<span class='p5'>10-15</span></br>",
          "<span class='p6'>5-10</span></br>",
          "<span class='p7'>0-5</span>"
      ].join("");

    return div;
};
// Add the info legend to the map
info.addTo(myMap3);
};


  
// Main Body
let year = "2002";
let startYear = 2002;
let endYear = 2020;
let LData = lymeData;
let TData = tempData;
let PData = precData;
let WData = wnData;

var countyLayer;
var countyTempLayer;
var countyPrecLayer;
// var heat;
let disData; // = lymeData;
let dis = "Lyme"

diseaseDropDown();
YearDropdown();
tempLegend();
diseaseLegend();
precLegend();
CreateDisLayer(LData, startYear);
CreateTempLayer(TData, startYear);
CreatePrecLayer(PData, startYear);

getDisease();
getYear(LData);

var info = L.control({
  position: "topright"
});
// When the layer control is added, insert a div with the class of "legend"
  info.onAdd = function() {
      var div = L.DomUtil.create("div", "title");
      div.innerHTML=[
          "<h6>Disease Hot-spots and Their Relation to Climate Change</h6>",
      ].join("");

    return div;
};
// Add the info legend to the map
info.addTo(myMap2);




