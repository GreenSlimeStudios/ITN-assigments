#include <bits/stdc++.h>
#include <vector>

using namespace std;

vector<int> sito(int n)
{
	vector<int> nums;
	for (int i = 2; i < n + 1; ++i)
	{
		nums.push_back(i);
	}

	for (int i = 0; i < floor(sqrt(nums.size())); ++i)
	{
		if (i >= nums.size() - 1)
		{
			break;
		}
		// cout << "\n i = " << nums[i] << "\n";
		for (int j = 0; j < nums.size(); j++)
		{
			int offset = 0;
			// cout << nums[j - offset] << ":" << nums[i] << " ";
			if (j - offset >= nums.size())
			{
				break;
			}
			cout << nums[j - offset] << ":" << nums[i] << " ";

			if (nums[j - offset] % nums[i] == 0 && nums[j - offset] != nums[i])
			{
				nums.erase(nums.begin() + j - offset);
				offset += 1;
			}
		}
	}
	return nums;
}

int main()
{
	int x;
	cin >> x;
	vector<int> soto = sito(x);
	cout << "\n";
	for (int i = 0; i < soto.size(); ++i)
	{
		cout << soto[i] << " ";
	}
	cout << "\n";
}
