#include <iostream>
#include <string>
using namespace std;

int N;
string Answer = "";

int main(){
    cin >> N;
    while(N>=1){
        if(N%2==0) Answer = "0" + Answer;
        if(N%2==1) Answer = "1" + Answer;
        N = N/2;
    }

    cout << Answer << endl;
    return 0;
}