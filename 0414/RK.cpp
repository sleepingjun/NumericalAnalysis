#include<stdio.h>
#include<stdlib.h>
float func(float t, float w)
{return (1-t+4*w);
 } 
/*wt=write the txt; rt=read the txt*/
 main(){int i,n; 
 float t,w,h,a,b,k1,k2,k3,k4;
 FILE*f1;
 f1=fopen("RK.txt","wt");
 
 a=0.0;b=2.0;n=20;
 h=0.1;
 t=0.0;w=1.0;
 for(i=0;i<n;i++)
 { t=a+i*h;
 k1=h*func(t,w);
 k2=h*func(t+0.5*h,w+0.5*h*k1);
 k3=h*func(t+0.5*h,w+0.5*k2);
 k4=h*func(t+h,w+k3);
 w=w+(1.0/6.0)*(k1+2*k2+2*k3+k4);
 fprintf(f1,"%f %f\n",t+h,w);} /*"%f %f means print float"; \n means new line*/
 fclose(f1);
 }
