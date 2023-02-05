#include <bits/stdc++.h>
#include <vector>

float pole(int aX,int aY,int bX, int bY, int cX, int cY){
	return 0.5 * abs((bX-aX)*(cY-aY)-(bY-aY)*(cX-aX));	
}

int main(){
	int ax,ay,bx,by,cx,cy,px,py;
	while(
		std::cin >> ax >> ay >> bx >> by >> cx >> cy >> px >> py){

		if (ax == 0 && ay == 0 && bx == 0 && by == 0 && cx == 0 && cy == 0 && px == 0 && py == 0) { break; }
		
		float pAll = pole(ax,ay,bx,by,cx,cy);
		float p1 = pole(ax,ay,bx,by,px,py);
		float p2 = pole(ax,ay,px,py,cx,cy);
		float p3 = pole(px,py,bx,by,cx,cy);

		if (p1 == 0 || p2 == 0 || p3 == 0){
			std::cout << "E";
		}
		else if (p1+p2+p3 == pAll){
			std::cout << "I";
		}
		else {
			std::cout << "O";
		}
	}
}
