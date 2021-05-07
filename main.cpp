#include "task.h"

int main(int C, char **V){
    TaskManage a;
    a.init_tasks();
    cout<<a.tasks.size()<<endl;
    return 0;
}