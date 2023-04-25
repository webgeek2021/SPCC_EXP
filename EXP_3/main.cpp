#include<bits/stdc++.h>
using namespace std;
int i = 0;
bool flag  = true;
void production_EDash(string);
void production_T(string);

void production_E(string str)
{
    production_T(str);
    production_EDash(str);
}
void production_F(string str)
{
    if(str[i] == '(')
    {
        i++;
        production_E(str);
        if(str[i] == ')')
            i++;
        else {
            flag = false;
            cout<<"ERROR"<<endl;
        }
    }
    else if(str[i] == 'i')
        i++;
    else    {
        cout<<"ERROR"<<endl;
        flag = false;
    }
}
void production_TDash(string str){
    if(str[i] == '*')
    {
        i++;
        production_F(str);
        production_TDash(str);
    }
}

void production_T(string str)
{
    production_F(str);
    production_TDash(str);
}
void production_EDash(string str)
{
    if(str[i] =='+')
    {
        i++;
        production_T(str);
        production_EDash(str);
    }
}

int main(){
    
    cout<<"Enter input"<<endl;
    string str;
    cin>>str;
    int n = str.size();
    production_E(str);
    if(flag){
        cout<<"Input Accepted"<<endl;
    }
    else{
        cout<<"Input Rejected"<<endl;
    }
    return 0;
}