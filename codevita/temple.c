#include<stdio.h>
int main(){
	int n,arr[100000],i,q,cnt=0,ne,cn,j;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
		cnt+=arr[i];
	}
	scanf("%d",&q);
	for(i=0;i<q;i++){
		cn=0;
		scanf("%d",&ne);
		if(cnt<ne){
			printf("-1\n");
		}
		else{
			for(j=0;j<n;j++){
				cn+=arr[j];
				if(cn>=ne){
					printf("%d\n",j+1);
					break;
				}
			}
		}
		
	}
}
