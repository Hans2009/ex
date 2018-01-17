#include <iostream>
//using namespace std;
using std::cout;

// 第一个命名空间
namespace first_space{
   void func(){
      //cout << "Inside first_space" << endl;
      cout << "Inside first_space" << std::endl;
   }
}
// 第二个命名空间
namespace second_space{
   void func(){
      //cout << "Inside second_space" << endl;
      cout << "Inside second_space" << std::endl;
   }
}
using namespace second_space;
int main ()
{

   // 调用第一个命名空间中的函数
   func();

   return 0;
}
