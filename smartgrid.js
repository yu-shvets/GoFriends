var smartgrid = require('smart-grid');

var settings = {
  filename: "_smartgrid",
  outputStyle: "scss",
  columns: 12,
  offset: "30px",
  oldSizeStyle: false,
  properties: [
    'justify-content',
    'align-items'
  ] 
}

smartgrid('app/sass', settings);