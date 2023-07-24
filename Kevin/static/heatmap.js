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
  let startYear = 2002;
  let endYear = 2022;
  let yearArray = []
  for(i= startYear; i < endYear+1; i++) {
    Year
    .append("option")
          .attr("value", i)
          .text(i.toString()); 
  }
  console.log(yearArray);
  
}
   
  
  // add options to dropdown
//   disArray.forEach(
//       function(addID) {
//           disease
//           .append("option")
//           .attr("value", addID)
//           .text(addID);
//       })
// }

diseaseDropDown();
YearDropdown();



//location = "static/LD-Case-Counts-by-County-01-20.csv";


//   d3.csv(location).then(function(response) {

//     console.log(response);
//     //features = response.features;
//  });
  // let heatArray = [];
// let array1 = [[-31.898217252, 115.78228321, 50],
//     [-31.898217252, 115.7822, 50], [-31.898217252, 119.1, 5]];

  // for (let i = 0; i < features.length; i++) {
  //   let location = features[i].geometry;
  //   if (location) {
  //    //console.log(location);
  //     heatArray.push([location.coordinates[1], location.coordinates[0]]);
  //   }

  //  }
  //  console.log(array1[2]);
  //  //console.log(heatArray);
  //  let heat = L.heatLayer(array1, {
  //    radius: 30,
  //    blur: 10,
  //    max: 1, 
  //    minOpacity: .5,
  //   }).addTo(myMap);

// });
