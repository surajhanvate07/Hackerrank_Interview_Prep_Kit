#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int countingValleys(int steps, string path) {
    int level = 0;
    int valley = 0;
    for(int i=0;i<steps;i++)
    {
        // char c = 'U';
        if(path[i] == 'U'){
            level += 1;
        }
        else{
            level -= 1;
        }

        if(path[i] == 'U' && level == 0) {
            valley++;
        }
    }
    return valley;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string steps_temp;
    getline(cin, steps_temp);

    int steps = stoi(ltrim(rtrim(steps_temp)));

    string path;
    getline(cin, path);

    int result = countingValleys(steps, path);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
