#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Group{
    string name;
    int num;
    string member[20];
};

struct Quiz{
    string name;
    int num;
};


int main()
{
    int groupCnt, quizCnt;
    vector<Group> groupVector;
    vector<Quiz> quizVector;
    Group group;
    Quiz quiz;

    cin >> groupCnt >> quizCnt;
    for(int i=0; i<groupCnt; i++){
        cin >> group.name >> group.nuam;
        for(int j=0; j<group.num; j++){
            cin >> group.member[j];
        }

        sort(group.member, group.member+group.num);
        groupVector.push_back(group);
    }

    for(int i=0; i<quizCnt; i++){
        cin >> quiz.name >> quiz.num;

        quizVector.push_back(quiz);
    }

    for(int i=0; i<quizCnt; i++){
        if(quizVector[i].num == 0){
            for(int j=0; j<groupCnt; j++){
                if(quizVector[i].name == groupVector[j].name){
                    for(int k=0; k<groupVector[j].num; k++){
                        cout << groupVector[j].member[k] << "\n";
                    }
                    break;
                }
            }
        }

        else{
            for(int j=0; j<groupCnt; j++){
                for(int k=0; k<groupVector[j].num; k++){
                    if(quizVector[i].name == groupVector[j].member[k]){
                        cout << groupVector[j].name << "\n";
                        break;
                    }
                }
            }
        }

    }






    return 0;
}
