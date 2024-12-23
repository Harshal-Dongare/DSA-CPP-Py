#include<iostream>
using namespace std;

int main(){
  int number;
  cout << "Enter the number: ";
  cin >> number;

  for(int row = 0; row < number; row++){
    for(int col = 0; col < row + 1; col++){
      cout << "* ";
    }
    cout << endl;
  }
}