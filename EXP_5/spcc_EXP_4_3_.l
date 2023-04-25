%{
#include<stdio.h>
int operator = 0 , operand = 0;
%}
%%
[\+\-\*\\\^] {operator++;}
[a-z A-z] {operand++;}
[0-9] {operand++;} 
%%
int yywrap() {
return 1;
}
int main() {
	printf("Enter String ");
	yylex();
	printf("Total Positive %d \n  " , positive  );
	printf("Total Negative %d \n",negative);
	printf(" Total floating Positive %d \n ",decimalpositive);
	printf("Total floating negative %d \n",decimalnegative);
}

