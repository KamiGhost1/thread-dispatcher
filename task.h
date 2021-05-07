#include "threadLab.h"
using namespace std;

class task {
public:
    task(string name){
        this->name = name;
    };
    int init_time, P, L, finish_time;
    int **M;
    bool *R;
    string name;
    vector<string> next_task,init_task;
};

class TaskManage{
public:
    void init_tasks();
    void clear_tasks();
    vector <task> tasks;
};