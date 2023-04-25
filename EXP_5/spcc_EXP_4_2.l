%{
#include<stdio.h>
int positive = 0,negative = 0,decimalpositive = 0 , decimalnegative = 0; 
%}
%%
[-][0-9]+ {negative++ ;}
[-][0-9]+\.[0-9]+ {decimalnegative++;}
[+]?[0-9] {positive++ ;}
[+]?[0-9]\.[0-9]+ {decimalpositive++;}
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

