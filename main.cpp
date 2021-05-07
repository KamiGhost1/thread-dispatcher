#include "task.h"

int main(int C, char **V){
    TaskManage a;
    a.init_tasks();
    for(int i = 0; i<a.tasks.size();i++){
        cout<<a.tasks[i].name<<" "<<a.tasks[i].init_task.size()<<endl;
    }
    a.clear_tasks();
    cout<<a.tasks.size()<<endl;
    return 0;
}