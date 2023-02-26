#include <bits/stdc++.h>
#include <vector>

int main(){
	float x;
	std::cin >> x;
	std::vector<int> binary;
	while (x >= 1){
		float y = x / 2;
		x = floor(y);
		if (y==x){
			binary.push_back(0);
		}
		else{
			binary.push_back(1);
		}
	}
	for (int i=binary.size()-1;i>=0;--i){
		std::cout << binary[i];
	}
	/* std::cout << std::endl; */
	return 0;
}
