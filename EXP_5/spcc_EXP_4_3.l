%{
#include<stdio.h>
int operator = 0 , operand = 0;
%}
%%
[-+/*^%] {operator++;}
[a-zA-z0-9] {operand++;}
%%
int yywrap() {
return 1;
}
int main() {
	printf("Enter String ");
	yylex();
	printf("Total operators %d \n  " , operator  );
	printf("Total operand %d \n", operand);
}

