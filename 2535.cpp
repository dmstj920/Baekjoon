#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Student{
    int country;
    int num;
    int score;
};

bool cmp(const Student& a, const Student& b){
    return a.score > b.score;

}

int main()
{
    int cnt, countryNum, third;
    vector<Student> v;
    Student student;

    cin >> cnt;
    for(int i=0; i<cnt; i++){
        cin >> student.country >> student.num >> student.score;

        v.push_back(student);
    }

    sort(v.begin(), v.end(), cmp);

    if(v[0].country == v[1].country)
        countryNum = v[0].country;

    for(third=2;;third++){
        if(v[third].country == countryNum)
            continue;
        else break;
    }
    cout << v[0].country << " " << v[0].num << "\n";
    cout << v[1].country << " " << v[1].num << "\n";
    cout << v[third].country << " " << v[third].num;

    return 0;
}
