#include <iostream>


class calc
{
private:
    double buffer;
public:
    calc();
    void runner();
    double get_input();
    void calculator();
    ~calc();
};

calc::calc()
{
    buffer = get_input();
    calc::runner();
}


double calc::get_input()
{
    double a;
    std::cout<<"Enter the number:";
    std::cin>>a;
    return a;
}

void calc::calculator()
{
    double b = get_input();
    char oper ;
    std::cout<<"Enter the operation: ";
    std::cin>> oper ; 
    switch (oper)
    {
    case '+':
        buffer += b;
        break;
    case '-':
        buffer -= b;
        break;
    case '*':
        buffer *= b;
        break;
    case '/':
        buffer /= b;
        break;
    
    default:
        break;
    }
    std::cout<<buffer<<std::endl;


}

void calc::runner()
{
    while (buffer!= 0 )
    {
        calculator();
    }
   
}
calc::~calc()
{
    std::cout<<"Thank you for using us!!";
}

int main()
{
    calc Player;
}