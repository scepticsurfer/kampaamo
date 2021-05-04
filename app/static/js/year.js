function showYear() {
    var dt = new Date();
    var y = dt.getYear();
    if (y < 1000) y +=1900;
    document.write(y);
   }
   //showYear();