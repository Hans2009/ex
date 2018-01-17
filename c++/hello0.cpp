#include <iostream>
using namespace std;
int main()
{
    #if 0
        cout << "Hello, world!" << endl;
        return 0;
    #endif

    #if 1
        cout << "Hello, world! There is comment here!" << endl;
        return 0;
    #endif
}
