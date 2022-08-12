#include<stdio.h>
#include<stdlib.h>
float func(float t, float w)
{return (1-t+4*w);
 } 
/*wt=write the txt; rt=read the txt*/
 main(){int i,n; 
 float t,w,h,a,b,k1,k2;
 FILE*f1;
 f1=fopen("ImEuler.txt","wt");
 
 a=0.0;b=2.0;n=10;
 h=0.2;
 t=0.0;w=1.0;
 for(i=0;i<10;i++)
 { t=a+i*h;
 k1=func(t,w);
 k2=func(t+h,w+h*k1);
 w=w+h/2*(k1+k2);
 fprintf(f1,"%f %f\n",t+h,w);} /*"%f %f means print float"; \n means new line*/
 fclose(f1);
 }
