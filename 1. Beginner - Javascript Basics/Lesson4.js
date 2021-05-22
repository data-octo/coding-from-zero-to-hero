var winston = {
  age: 19,
  eyes: "black",
  likes: ["programming", "being programmed"],
  isCool: true,
  birthplace: {
    city: "Mountain View",
    state: "California",
  },
};

fill(255, 255, 0);

textSize(16);
text("All about Winston:", 10, 30);
text("Winston is " + winston.age + " years old", 10, 50);
text("Winston has " + winston.eyes + " eyes", 10, 70);
text("Winston likes " + winston.likes[0] + " and " + winston.likes[1], 10, 90);
text(
  "Winston was born in " +
    winston.birthplace.city +
    ", " +
    winston.birthplace.state,
  10,
  110
);
