#include <iostream>
#include <cstdlib>
#include <math.h> 

double sumofi(const double A[10][10] , int i )
{
    double  returner = 0  ; 
    for ( int j = 0 ; j < i ; j++){
            returner += A[i][j] ; 
    }

    return returner ; 
}

double sumofj(const double A[10][10] , int i )
{
    double  returner = 0  ; 
    for ( int j = 0 ; j < i ; j++){
            returner += A[j][i] ; 
    }

    return returner ; 
}


double multiply(double A[10][10] , double B[10][10])
{
    double C[10][10];
    for(int i = 0 ; i < std::sqrt(sizeof(A))/sizeof(A[0][0]) ; i++ )
    {
        for (int j = 0 ; j < std::sqrt(sizeof(B))/sizeof(B[0][0]) ; j++ )
        {
            C[i][j] = sumofi(A , i) + sumofj(B , j) ;
        }
    }
}

void printer(double A[10][10])
{
    for (int i = 10 ; i < 10 ; i++)
    {
        for ( int j = 0 ; j < 10 ; j ++)
        {
            std::cout << A[i][j] ; 
        }
        std :: cout << std :: endl ;
    }
}

double generator(int size)
{
    double C[10][10] ;
    for (int i = 0 ; i < size ; i++)
    {
        for (int j = 0 ; j < size ; j ++)
        {
            C[i][j] = std::rand()%10000 + 1 ; 
        }
    }
    return C;
}


int main() {

    double A[10][10] = generator(10)
    double B[10][10] = generator(10) 
    return 0;
}