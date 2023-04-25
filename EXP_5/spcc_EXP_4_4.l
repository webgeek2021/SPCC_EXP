%{
#include<stdio.h>
int space = 0 ,character = 0, newline = 0 , words = 0;
%}
%%
[a-zA-Z]{1} {character++;}
[a-zA-Z]{2,} {words++;}
[ ] {space++;}
[\n] {newline++;}
%%
int yywrap() {
return 1;
}
int main() {
	printf("Enter String ");
	yylex();
	printf("Total words %d \n  " , words );
	printf("Total Character %d \n", character);
	printf("Total newline %d \n  " , newline );
	printf("Total Space %d \n", space);
}

