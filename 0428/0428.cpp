#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float func(int m,float t, double w[])
{float A;
if(m==1){A=w[2];}
if(m==2){A=-2*sin(w[1]);}
return (A);}

 int main(){
 	FILE*output;
 	output=fopen("ex3.txt","wt");
 	double a=0.0;double b=1.0;
 	int N=200,m=2;
 	double t,h=0.1;
 	double w[5],v1[5],v2[5],v3[5],v4[5];
 	double k1[5],k2[5],k3[5],k4[5];
 	int i,j;
 	w[1]=3.0;w[2]=-1.0;
 	for(i=1;i<=N;i++){
	 	for(j=1;j<=m;j++) {
	 		k1[j]=h*func(j,t,w);
	 		v1[j]=w[j]+0.5*k1[j]; 
		 }
	 	for(j=1;j<=m;j++){
		 	k2[j]=h*func(j,t+0.5*h,v1);
 			v2[j]=w[j]+0.5*k2[j]; 
		}
 		for(j=1;j<=m;j++){
		 	k3[j]=h*func(j,t+0.5*h,v2);
 			v3[j]=w[j]+k3[j]; 
		}
 		for(j=1;j<=m;j++){
		 	k4[j]=h*func(j,t+h,v3);
		}
 		for(j=1;j<=m;j++){
 			w[j]=w[j]+(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6.0;
		}
 	t=t+h;
 	fprintf(output,"%f %f %f\n",t,w[1],w[2]);} /*"%f %f means print float"; \n means new line*/
 	fclose(output);
 }
