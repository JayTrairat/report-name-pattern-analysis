#include <iostream>
#include <fstream>

using namespace std;

int main(){
        ifstream fileTarget;
        fileTarget.open("assets/type_1.txt");
        if(fileTarget.is_open()){
            string line;
            while (!fileTarget.eof()) {
                getline(fileTarget, line);
                cout << line << '\n';
            }
            fileTarget.close();
        }
        return 0;
}
