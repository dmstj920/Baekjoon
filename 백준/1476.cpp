#include <iostream>

using namespace std;

int main()
{
    int earth, sun, moon, year;

    cin >> earth >> sun >> moon;

    if(earth == 15) earth = 0;
    if(sun == 28) sun = 0;
    if(moon == 19) moon =0;

    for(int i=1;;i++){
        if(i%15 == earth && i%28 == sun && i%19 == moon){
            year = i;
            break;
        }
    }
    cout << year;

    return 0;
}
