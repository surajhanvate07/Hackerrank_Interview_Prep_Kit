#include <bits/stdc++.h>
using namespace std;

void countSwaps(vector<int> a) {
    int total_swaps = 0;
    for(int i=0;i<a.size()-1;i++)
    {
        int swap = 0;
        for(int j=0;j<a.size()-1-i;j++)
        {
            if(a[j] > a[j+1]) {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                
                swap += 1;
            }
        }
        total_swaps += swap;
        if(swap == 0){
            break;
        }
    }
    cout << "Array is sorted in " << total_swaps << " swaps." << endl;
    cout << "First Element: "<< a[0] << endl;
    cout << "Last Element: "<< a[a.size()-1] << endl;
}

int main()
{
    int n;
    cin >> n;
    int temp;
    vector<int> a;

    for (int i = 0; i < n; i++) {
        cin >> temp;
        a.push_back(temp);
    }

    countSwaps(a);

    return 0;
}