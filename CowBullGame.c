/*
This is a simple Bulls and Cows game. Two players take turns guessing a randomly selected 4-digit number (digits not repeated).
The game provides feedback on each guess by counting the number of "Bulls" (correct digits in the correct position) and "Cows" (correct digits in the wrong position). 
The players continue guessing until they correctly identify the number or choose to quit, and their scores are displayed at the end to determine the winner.
*/


#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void main()
{
    int ans,a[100] = {1234,2345,6754,8790,4567,2345,1987,5678,6543,5670,2345,6789,7654,4793,1479,2759,4183,7890,3267,8901};
    int cow=0,bull=0;
    srand(time(NULL));
    int num = a[rand()%21];
    char b[100],c[100];
    printf("Welcome to COW BULL Game!\n");
    printf("Enter first player name: ");
    scanf("%s",b);
    printf("Enter second player name: ");
    scanf("%s",c);
    int end,b1 = 0, c1 = 0;   //players intial scores
    printf("Game starts!\n");
  
    while(1)
    {   cow = 0, bull = 0;
        int n =10;
        while(n>0)
        {
        
            cow=0,bull=0;
            printf("player1 %s turn\n",b);
            printf("%s Guess the 4 digit number(digits are not repeated)? = ",b);
            scanf("%d",&ans);
            if(ans == num)
            {
                cow = 0;
                bull = 4;
                b1++;
                printf("\nBull = %d and Cow = %d\n",bull,cow);
                printf("\ncorrect guess, %s scored one point",b);
                printf("\nNow socre of player1 %s = %d",b,b1);
                break;
            }
            int A=ans,N=num, arr[4], arrN[4],i=3,j,exit;
            printf("\nYour number=%d\n",ans); //
        
            while(A>0)
            { 
                arr[i] = A%10;
                A = A/10;
                i--;
            }
            i=3;
            while(N>0)
            {
                arrN[i] = N%10;
                N = N/10;
                i--;
            }

            
            for(i=0; i<4; i++)
            {
                if(arr[i] == arrN[i])
                {
                    bull++;
                }
            }
            for(i=0; i<4; i++)
            {
                for(j=0; j<4; j++)
                {
                    if(arr[i] == arrN[j] && j != i)
                    {
                        cow++;
                    }
                }
            }
            printf("\nYou have more %d chances\n",n);
            printf("\nBull = %d and Cow = %d\n",bull,cow);
            n--;
        
            printf("Press 1 to continue or press 0 to quit: ");
            scanf("%d",&exit);
            if(exit == 0)
                break;
        }
        srand(time(NULL));
        num = a[rand()%21];

        printf("\nPress 1 to continue(FOR NEXT PLAYER) or press 0 to leave the game(EXIT): ");
        scanf("%d",&end);
        if(end == 0)
        {   printf("Player1 %s score = %d\n",b,b1);
            printf("Player2 %s socre = %d\n",c,c1);
            if(b1>c1)
                printf("Player1 %s won the game! \n",b);
            else if(b1 == c1)
                printf("Tie\n");
            else
                printf("Player2 %s won the game! \n",c);
            printf("Thank You! for playing ");
            break;
        }
        cow = 0,bull = 0;
        n = 10;
        srand(time(NULL));
        num = a[rand()%21];
        while(n>0)
        {
            cow=0,bull=0;
            printf("player2 %s turn\n",c);
            printf("%s Guess the 4 digit number(digits are not repeated)? = ",c);
            scanf("%d",&ans);
            if(ans == num)
            {
                cow = 0;
                bull = 4;
                c1++;
                printf("\nBull = %d and Cow = %d\n",bull,cow);
                printf("\ncorrect guess, %s scored one point",c);
                printf("\nNow socre of player2 %s = %d",c,c1);
                break;
            }
            int A=ans,N=num, arr[4], arrN[4],i=3,j,exit;
        
            while(A>0)
            { 
                arr[i] = A%10;
                A = A/10;
                i--;
            }
            i=3;
            while(N>0)
            {
                arrN[i] = N%10;
                N = N/10;
                i--;
            }

           
            for(i=0; i<4; i++)
            {
                if(arr[i] == arrN[i])
                {
                    bull++;
                }
            }
            for(i=0; i<4; i++)
            {
                for(j=0; j<4; j++)
                {
                    if(arr[i] == arrN[j] && j != i)
                    {
                        cow++;
                    }
                }
            }
            n--;
            printf("You have more %d chances",n);
            printf("\nBull = %d and Cow = %d\n",bull,cow);
            
            printf("Press 1 to continue or press 0 to quit: ");
            scanf("%d",&exit);

            if(exit == 0)
                break;
        }
        
        srand(time(NULL));
        num = a[rand()%21];
    
        printf("\nPress 1 to continue(FOR NEXT PLAYER) or press 0 to leave the game(EXIT): ");
        scanf("%d",&end);
        if(end == 0)
        {   printf("Player1 %s score = %d\n",b,b1);
            printf("Player2 %s socre = %d\n",c,c1);
            if(b1>c1)
                printf("PLAYER1 %s WON the GAME!\n",b);
            else if(b1 == c1)
                printf("TIE\n");
            else
                printf("PLAYER2 %s WON the GAME! \n",c);
            printf("THANK You! for playing ");
            break;
        }
    }
    
}