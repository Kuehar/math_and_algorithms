// P.173

#include <iostream>

using namespace std;

int N,A[109];
int Answer = 0;


int main(){
    // 入力
    cin >> N;
    for(int i=1;i<=N;i++) cin >> A[i];

    // 5つのカードを全探索
    for(int i=1;i<=N;i++){
        for(int j=i+1;j<=N;j++){
            for(int k=j+1;k<=N;k++){
                for(int l=k+1;l<=N;l++){
                    for(int m=l+1;m<=N;m++){
                        if(A[i]+A[j]+A[k]+A[l]+A[m] == 1000) Answer+=1;
                        }
                    }
                }
            }
        }
    }