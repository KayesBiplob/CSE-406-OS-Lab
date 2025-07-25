#include <stdio.h>

void WT(int n, int at[], int bt[], int wt[]) {
    int completed = 0, current_time = 0, min_bt, idx;
    int is_completed[n];
    for (int i = 0; i < n; i++) is_completed[i] = 0;

    while (completed < n) {
        min_bt = 10000;
        idx = -1;
        for (int i = 0; i < n; i++) {
            if (at[i] <= current_time && !is_completed[i]) {
                if (bt[i] < min_bt) {
                    min_bt = bt[i];
                    idx = i;
                }
            }
        }
        if (idx != -1) {
            wt[idx] = current_time - at[idx];
            if (wt[idx] < 0) wt[idx] = 0;
            current_time += bt[idx];
            is_completed[idx] = 1;
            completed++;
        } else {
            current_time++;
        }
    }
}

void TAT(int n, int bt[], int wt[], int tat[]) {
    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
    }
}

void CT(int n, int at[], int tat[], int ct[]) {
    for (int i = 0; i < n; i++) {
        ct[i] = at[i] + tat[i];
    }
}

void printTable(int processes[], int n, int at[], int bt[], int wt[], int tat[], int ct[]) {
    int total_wt = 0;
    printf("Process\tArrival\tBurst\tWaiting\tTurnaround\tCompletion\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%d\t%d\t%d\t%d\t\t%d\n", processes[i], at[i], bt[i], wt[i], tat[i], ct[i]);
        total_wt += wt[i];
    }
    printf("Average Waiting Time: %.2f\n", (float)total_wt / n);
}

int main() {
    int processes[] = {1, 2, 3, 4};
    int arrival_time[] = {0, 1, 2, 3};
    int burst_time[] = {3, 2, 1, 4};
    int n = sizeof(processes) / sizeof(processes[0]);

    int wt[n], tat[n], ct[n];
    WT(n, arrival_time, burst_time, wt);
    TAT(n, burst_time, wt, tat);
    CT(n, arrival_time, tat, ct);

    printTable(processes, n, arrival_time, burst_time, wt, tat, ct);
    return 0;
}