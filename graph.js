function setup() {
  createCanvas(600, 300);
}

function draw() {
  background(220);
  line(0,height/2,width,height/2);
  line(width/2,0,width/2,height);
  for (var i=-300;i<300;i++){
    x = i/100;
    y = fun(x);
    set(i+width/2, y*100 + height/2, 1);
  }
  updatePixels();
}

function fun(x){
  return (abs(x)*2-3)*(abs(x)*2-2)*(abs(x)*2-4)*abs(x)*2*sqrt(abs(x))/12;
}
