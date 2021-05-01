var Winston = function (nickname, age, x, y) {
  this.nickname = nickname;
  this.age = age + "yrs old";
  this.x = x;
  this.y = y;
};

// the draw method
Winston.prototype.draw = function () {
  fill(255, 255, 0);
//   var img = getImage("creatures/Winston");
//   image(img, this.x, this.y);
  this.x = this.x + 100;
  this.y = this.y + 150;

  ellipse(this.x, this.y, 150, 200);
  ellipse(this.x, this.y + 50, 100, 60);
  ellipse(this.x - 50, this.y - 50, 30, 30);
  ellipse(this.x + 50, this.y - 50, 30, 30);
  var txt = this.nickname + ", " + this.age;
  text(txt, this.x - 50, this.y - 120);
};

Winston.prototype.talk = function () {
  text("I'm Winston!", this.x - 30, this.y + 150);
};

var winstonTeen = new Winston("Winsteen", 15, 20, 50);
var winstonAdult = new Winston("Mr. Winst-a-lot", 30, 229, 50);

winstonTeen.draw();
winstonTeen.talk();
winstonAdult.draw();
winstonAdult.talk();
