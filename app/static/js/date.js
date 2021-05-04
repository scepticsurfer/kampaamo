function showToday() {
 var monthNames = new Array("tammikuuta","helmikuuta","maaliskuuta","huhtikuuta","toukokuuta","kesäkuuta","heinäkuuta","elokuuta","syyskuuta","lokakuuta","marraskuuta","joulukuuta");
 var dt = new Date();
 var y = dt.getYear();
 if (y < 1000) y +=1900;
 document.write(dt.getDate() + ". " + monthNames[dt.getMonth()] + " " + y);
}
//showToday();