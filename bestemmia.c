/*
Copyright (C) 2017  deerf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
#include <stdio.h>
char *bestemmia[18]={"dio porco","cristo la madonna","madunassa","gesù inchiodato sulla croce","madonna puttanaccia","dio culo infiammato","dio can","Ave Maria piena di Merda","Dio, Madonna e tutti gli angeli in colonna","Gesù scalzo in una valle di chiodi","Gesù cieco in una valle di spigoli","Porco Dio e Padre Pio","Bastardo il clero","Madonna cagna","Dio cantante, Madonna musicante, Giuseppe batterista e Cristo in autopista","Maria putrefatta","Dio bastardo","Madonna inculata da cristo, quel bastardo"};
void mth_initrandom()
{
    srand((unsigned)time(NULL));
}


int mth_random(int n)
{
    return rand() % (n);
}
int main()
{
	mth_initrandom();

    printf("mannaggia a %s", bestemmia[mth_random(18)]);
}
