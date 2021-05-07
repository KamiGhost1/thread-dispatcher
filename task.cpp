#include "task.h"



void TaskManage::init_tasks() {
    task A("A");
    task B("B");
    task C("C");
    task D("D");
    task E("E");
    task F("F");
    task G("G");
    task H("H");
    task K("K");

    A.next_task.push_back("C");
    A.next_task.push_back("D");
    A.next_task.push_back("E");

    B.next_task.push_back("C");
    B.next_task.push_back("D");
    B.next_task.push_back("E");

    C.next_task.push_back("F");
    C.next_task.push_back("G");
    C.next_task.push_back("H");
    C.init_task.push_back("A");
    C.init_task.push_back("B");

    D.next_task.push_back("F");
    D.next_task.push_back("G");
    D.next_task.push_back("H");
    D.init_task.push_back("A");
    D.init_task.push_back("B");

    E.next_task.push_back("F");
    E.next_task.push_back("G");
    E.next_task.push_back("H");
    E.init_task.push_back("A");
    E.init_task.push_back("B");

    G.next_task.push_back("K");
    G.init_task.push_back("C");
    G.init_task.push_back("D");
    G.init_task.push_back("E");

    F.init_task.push_back("C");
    F.init_task.push_back("D");
    F.init_task.push_back("E");

    H.init_task.push_back("C");
    H.init_task.push_back("D");
    H.init_task.push_back("E");

    K.init_task.push_back("G");


    tasks.push_back(A);
    tasks.push_back(B);
    tasks.push_back(C);
    tasks.push_back(D);
    tasks.push_back(E);
    tasks.push_back(F);
    tasks.push_back(G);
    tasks.push_back(H);
    tasks.push_back(K);
}


void TaskManage::clear_tasks() {

}

