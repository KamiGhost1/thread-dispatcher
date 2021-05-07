class task {
public:
    int init_time, P, L, finish_time;
    int **M;
    bool *R;
    string name, init_task;
    vector <string> next_task;
    void (* func) ();
};