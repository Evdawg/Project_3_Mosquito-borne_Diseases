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
  HeatMap(startYear);

}

function getYear () {
  let selectYr = d3.select("#Year");  
  selectYr
      .on("change", function() {
          let id = d3.event.target.value;
          //remove(heat);
          if(heat) {
            myMap.removeLayer(heat);
          }
          HeatMap(id);
      }   
    )
};
   
  
// Main Body
let startYear = 2002;
let endYear = 2022;
var heat;

diseaseDropDown();
YearDropdown();
getYear();




function HeatMap (year) {
    
    console.log(year);
    let heatArray = [];
    let len = lymeData.length

      for (let i = 0; i < len; i++) {
        let county = lymeData[i];
        heatArray.push([county.Lat, county.Lon, county[year]]);
        }
    console.log(heatArray);
    
    heat = L.heatLayer(heatArray, {
      radius: 10,
      blur: 7,
      max: 50, 
      minOpacity: .5,
    });

    heat.addTo(myMap);
  }

function remove () {
map.eachLayer(function (layer) {
    map.removeLayer(layer);
    })
};