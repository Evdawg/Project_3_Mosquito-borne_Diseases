let myMap = L.map("map", {
  center: [39.8, -98.5],
  zoom: 3
});

let myMap2 = L.map("map2", {
  center: [39.8, -98.5],
  zoom: 3
});


// Adding the tile layer
let first = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
first.addTo(myMap);

let second = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap2);

function diseaseDropDown() {
  let disease = d3.select("#disease");
  let disArray = [["Lyme"], ["West Nile"]];
   
  console.log(disArray);
  // add options to dropdown
  disArray.forEach(
      function(addID) {
          disease
          .append("option")
          .attr("value", addID)
          .text(addID);
      })
    };
  
function YearDropdown() {
  let Year = d3.select("#Year");
    
  for(i= startYear; i < endYear+1; i++) {
    Year
    .append("option")
          .attr("value", i)
          .text(i.toString()); 
  }
 // HeatMap(startYear);
}

function getDisease() {
  let selectDis = d3.select("#disease");  
  selectDis
      .on("change", function() {
          let dis = d3.event.target.value;
          if (dis == "Lyme") {
            disData = lymeData
          } else {
            disData = wnData
          };
          console.log(dis, disData)
          getYear(disData);
      }
    )    
}

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
          console.log(year);
          CreateDisLayer(data, year);
          CreateTempLayer(tempData, year);
      }   
    )
};
   
  
// Main Body
let startYear = 2002;
let endYear = 2020;

var countyLayer;
var countyTempLayer;
var heat;
let disData; // = lymeData;

diseaseDropDown();
YearDropdown();
CreateDisLayer(lymeData, startYear);
CreateTempLayer(tempData, startYear);
getDisease();
getYear();





function CreateDisLayer(Data, year) {
  let len = Data.length
  let countyMarkers = [];

    for (var i = 0; i < len; i++) {
      
      let county = Data[i];
      let mag = county[year]
      
      if (mag >= 1) {
          let param = Color(mag);
          circle = new L.circle([county.lat, county.lon], {
          fillOpacity: .5,
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

function Color(mag) {
  if (mag >= 50) {
    color = "darkred";
    radius = 50000;
  } else if (mag >= 25 && mag < 50) {
    color = "red";
    radius = 40000;
  } else if (mag >= 10 && mag <25) {
    color = "orange";
    radius = 30000;
  } else {
    color = "gray"
    radius = 20000;
  };
  return [color, radius];
};


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


