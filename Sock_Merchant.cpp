#include <bits/stdc++.h>
#include <set>
using namespace std;

int sockMerchant(int n, vector<int> ar) {
    set<int> s1{begin(ar), end(ar)};
    int cnt = 0;
    for(auto const v:s1)
    {
        cnt += int(count(ar.begin(), ar.end(), v)/2);
    }
    return cnt;
}

int main()
{
    int n;
    cin >> n;
    int temp;
    vector<int> ar;

    for (int i = 0; i < n; i++) {
        cin >> temp;
        ar.push_back(temp);
    }

    int result = sockMerchant(n, ar);
    cout << result << endl;
    return 0;
}
