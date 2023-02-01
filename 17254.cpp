#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct KeyInput{
    int num;
    int time;
    char alphabet;
};

bool cmp(const KeyInput& a, const KeyInput& b){
    if(a.time == b.time) return a.num < b.num;
    else return a.time < b.time;
}

int main()
{
    int keyboard, cnt;
    vector<KeyInput> v;
    KeyInput keyinput;


    cin >> keyboard >> cnt;

    for(int i=0; i<cnt; i++){
        cin >> keyinput.num >> keyinput.time >> keyinput.alphabet;
        v.push_back(keyinput);
    }

    sort(v.begin(), v.end(), cmp);

    for(int i=0; i<cnt; i++){
        cout << v[i].alphabet;
    }


    return 0;
}
