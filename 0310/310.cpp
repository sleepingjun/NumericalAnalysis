#include<stdio.h>
#include<stdlib.h>
float func(float t, float w)
{return (1-t+4*w);
 } 
/*wt=write the txt; rt=read the txt*/
 main(){int i,n; 
 float t,w,h,a,b;
 FILE*f1;
 f1=fopen("Euler33.txt","wt");
 
 a=0.0;b=2.0;n=10;
 h=0.01;
 t=0.0;w=1.0;
 for(i=0;i<10;i++)
 { t=a+i*h;
 w=w+h*func(t,w);
 fprintf(f1,"%f %f\n",t+h,w);}
 fclose(f1);
 }
