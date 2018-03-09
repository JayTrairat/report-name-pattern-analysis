#include <iostream>
#include <fstream>

using namespace std;

int main(){
        ifstream fileTargetStreamIn;
        ofstream fileTargetStreamOut;

        string fileTargetURLIn = "assets/type_1_original.txt";
        string fileTargetURLOut = "assets/type_1_output.txt";

        fileTargetStreamIn.open(fileTargetURLIn);
        if(fileTargetStreamIn.is_open()){
            fileTargetStreamOut.open(fileTargetURLOut);
            string line;
            while (!fileTargetStreamIn.eof()) {
                getline(fileTargetStreamIn, line);
                fileTargetStreamOut << line << '\n';
            }
            fileTargetStreamOut.close();
            fileTargetStreamIn.close();
        }
        return 0;
}
