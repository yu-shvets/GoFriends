var smartgrid = require('smart-grid');

var settings = {
  filename: "_smartgrid",
  outputStyle: "scss",
  columns: 12,
  offset: "30px",
  container: {
    maxWidth: '1410px', /* max-width оn very large screen */
    fields: '30px' /* side fields */
  },
  oldSizeStyle: false,
  properties: [
    'justify-content',
    'align-items'
  ] 
}

smartgrid('app/sass', settings);