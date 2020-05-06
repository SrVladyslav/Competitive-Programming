#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

int main(){
    int casos, actual, previo,i;
    string salida;
    bool s;

    do{
        s = true;
        previo = -1;
        cin >> casos;
        for(i = 0; i < casos; i ++){
            cin >> actual;
            if(actual <= previo){
                s = false;
            }else{
                previo = actual;
            }
        }
        if(!s){
            salida = "NO";
        }else{
            salida = "SI";
        }
        if(previo != -1){
            cout <<salida <<endl;
        }
    }while(casos > 0);

    return 0;
}