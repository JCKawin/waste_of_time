#include <iostream>

void print(const bool message)
{
    std::cout << message << std::endl; 
}

int isprime(int no)
{
    int i = 2;
    if ( no == i)
    {return 1 ;}
    else{
    for ( i = 2 ; i < no ; i++ )
    {
        if (no%i == 0)
        return 0;
    }
    if ( i == no )
    {return 1;}

}

int main() 
{
    std::cout << "Enter a Number :";
    int no;
    std::cin >> no ; 
    std::cout << isprime(no) ; 
    return 0;
}