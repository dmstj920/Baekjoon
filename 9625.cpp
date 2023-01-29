#include <iostream>

using namespace std;

int main()
{
    int cnt, aCnt1=1, aCnt2=0, bCnt1=0, bCnt2=1, aCnt, bCnt;
    cin >> cnt;

    for(int i=1; i<cnt; i++){
        aCnt = aCnt1 + aCnt2;
        bCnt = bCnt1 + bCnt2;
        aCnt1 = aCnt2;
        bCnt1 = bCnt2;
        aCnt2 = aCnt;
        bCnt2 = bCnt;
    }

    if(cnt == 1){
        aCnt = 0;
        bCnt = 1;
    }

    cout << aCnt << " " << bCnt;

    return 0;
}
