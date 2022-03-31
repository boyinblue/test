#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#define MAX_STRING 20

using namespace std;

int main()
{
	char map[10][10];

	ifstream inFile;
	ofstream outFile;
	inFile.open("input.txt");
	outFile.open("output.txt");

	string a[10][10];

	int i = 0;
	int j = 0;

	while( !inFile.eof())
	{
		inFile >> a[i][j];
		printf("[%d][%d] %d\n", i, j, a[i][j]);
		j++;
		if (j == 10 )
		{
			j = 0;
			i++;
			outFile << endl;
		}
		outFile << a[i][j] << " ";
	}
}
