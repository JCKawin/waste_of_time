#include <iostream>

class rps
{
private:
    int com , user;
public:

rps()
{
    std::cout<<"---------|Rock - Paper - Scissor|-----------\n";
    rps::runner();
}

// runner funtion

void runner()
{
    while (com!=5 && user!=5)
    {
        char cpu , hum ;
        hum = rps::user_getchoice();
        cpu = rps::comp_getchoice();
        switch (hum)
        {
        case 'r':
            if (cpu=='s') 
            {user++;}
            else if (cpu=='p')
            {com++;}
            break;
        case 's':
            if (cpu=='p') 
            {user++;}
            else if (cpu=='r')
            {com++;}
            break;
        case 'p':
            if (cpu=='r') 
            {user++;}
            else if (cpu=='s')
            {com++;}
            break;        
        default:
            break;
        }
    }
    
}

~rps()
{
    if(com == 5)
    std::cout<<"computer wins";
    else if(user == 5)
    std::cout<<"******* you win the game **********";
}


protected:
 

 // user choosing function

char user_getchoice()
{
    char choice;
    do
    {
    std::cout<<"\n Enter your choice ( r s p ):";
    std::cin>> choice;
    }while (choice != 'r' && choice != 's' && choice != 'p');
    return choice;
}

// computer choosing function

char comp_getchoice()
{
    char choice;
    int chint;
    chint = std::rand() % 3;
    switch (chint)
    {
    case 0:
        choice = 'r';
        break;
    case 1:
        choice = 's';
        break;
    case 2:
         choice = 'p';
         break;
    default:
        break;
    }
    std::cout<<"Computer's choice:"<<choice;
    return choice;
}

};

int main()
{
    rps Play;
    return 0;
}
