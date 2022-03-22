// Code related to colcade grid system

var colc = new Colcade('.grid', {
  columns: '.grid-col',
  items: '.grid-item'
});

/**Overlay added to pages with colcade to 
 * allow time for it to load */

window.onload = function () {
  document.getElementById('overlay').style.display = "none";
};