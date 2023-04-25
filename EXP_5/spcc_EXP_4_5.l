%{
#include<stdio.h>
int space = 0 ,character = 0, newline = 0 , keyword = 0 , identifiers = 0;
%}
%%
[a-zA-Z]{1} {character++;}
(int|float|double|return) {keyword++;}
[_a-zA-Z][a-zA-Z]* {identifiers++;}
[\n] {newline++;}
[ ] {space++;}
%%
int yywrap() {
return 1;
}
int main() {
	printf("Enter String ");
	yylex();
	printf("Total keywords %d \n  " , keyword );
	printf("Total Character %d \n", character);
	printf("Total newline %d \n  " , newline );
	printf("Total Space %d \n", space);
	printf("Total Identifiers %d \n", identifiers);
}

