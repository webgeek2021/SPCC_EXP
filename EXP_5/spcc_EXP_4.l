%{
#include<stdio.h>
int vowel = 0 , consonent = 0;
%}
%%
[aeiou] {vowel++;}
[a-zA-z] {consonent++;}
%%
int yywrap() {
return 1;
}
int main() {
	printf("Enter String ");
	yylex();
	printf("Final Answer \n");
	printf("Vowel are %d \n" ,vowel);
	printf("Consonent are %d" , consonent);
}
