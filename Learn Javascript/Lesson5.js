// Object oriented programming

/* 
 Winston
 - nickname
 - age
 - x 
 - y
*/
var Winston = function (nickname, age, x, y) {
  this.nickname = nickname;
  this.age = age + "yrs old";
  this.x = x;
  this.y = y;


};

fill(255, 255, 0);

var winstonTeen = new Winston("Winsteen", 15, 20, 50);
// winstonTeen.drawImg(20, 50);
var winstonAdult = new Winston("Mr. Winst-a-lot", 30, 229, 50);


var drawWinston = function (winston) {
//   fill(255, 0, 0);
//   var img = getImage("creatures/Winston");
//   image(img, winston.x, winston.y);
  var txt = winston.nickname + ", " + winston.age;
  text(txt, winston.x + 20, winston.y - 10);
};

drawWinston(winstonTeen);
drawWinston(winstonAdult);

function drawImg(x, y) {
    ellipse(200, 200, 250, 300);
    ellipse(200, 250, 100, 60);
    ellipse(150, 150, 30, 30);
    ellipse(250, 150, 30, 30);
  }

drawImg(20, 50);



