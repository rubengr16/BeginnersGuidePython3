#include <stdio.h>
#include <stdlib.h>

#define NUCLEOTIDOS 90  // debe ser m�ltiplo de tres

struct Tnucleotido{
    char pentosa;
    char baseNitrogenada;
    char fosfato;
};

typedef struct Tnucleotido TacidoNucleico[NUCLEOTIDOS];


char randBaseNitrogenada(char pentosa)
{
    int x;
    x=rand()%4;
    if(x==0)
        return 'A';
    else if(x==1)
        return 'G';
    else if(x==2)
        return 'C';
    else if(x==3)
    {
        if(pentosa=='D')
            return 'T';
        else return 'U';
    }
}

void generarCadenaADN(TacidoNucleico * cadenaADN)
{
    int i;
    for(i=0; i<NUCLEOTIDOS; i++)
        {
            cadenaADN[i]->pentosa='D';
            cadenaADN[i]->baseNitrogenada=randBaseNitrogenada('D');
}

void printAcidoNucleico(TacidoNucleico  acidoNucleico)
{
    for(i=0; i<NUCLEOTIDOS; i++)
    {
        if(i%30==0)
            printf("\n");
        printf("%c", acidoNucleico[i].baseNitrogenada);
    }
}

char baseNitrogenadaComplementaria(char baseNitrogenada)
{
    if(baseNitrogenada=='A')
        baseNitrogenada='T';
    else if(baseNitrogenada=='G')
        baseNitrogenada='C';
    else if(baseNitrogenada=='T')
        baseNitrogenada='A';
    else if(baseNitrogenada=='C')
        baseNitrogenada='G';
}

void generarCadenaComplementariaADN(TacidoNucleico cadenaADN, TacidoNucleico *cadenaComplementariaADN)
{
    int i;
    for(i=0; i<NUCLEOTIDOS; i++)
        {
            cadenaComplementariaADN[i]->pentosa='D';
            cadenaComplementariaADN[i]->baseNitrogenada=baseNitrogenadaComplementaria(cadenaADN);
        }
}

void printDobleCadenaADN(TacidoNucleico cadenaADN, TacidoNucleico cadenaComplementariaADN)
{
    printAcidoNucleico(cadenaADN);
    printAcidoNucleico(cadenaComplementariaADN);
}

char baseNitrogenadaTranscrita(char baseNitrogenada)
{
    if(baseNitrogenada=='T')
        return 'U';
}

void transcribir(TacidoNucleico cadenaADN,TacidoNucleico *cadenaARN)
{
     int i;
    for(i=0; i<NUCLEOTIDOS; i++)
        {
            cadenaARN[i]->pentosa='D';
            cadenaARN[i]->baseNitrogenada=baseNitrogenadaTranscrita(cadenaADN);
        }
}


int main()
{
    TacidoNucleico cadena, cadenaComplementaria, cadenaARN;
    printf("Cadena ADN:");
    printf("\nAcido nucleico = D");
    generarCadenaADN(cadena);
    printAcidoNucleico(cadena);
    printf("\nCadena ADN y complementaria:");
    generarCadenaComplementariaADN(cadena, cadenaComplementaria);
    printDobleCadenaADN(cadena, cadenaComplementaria);
    printf("Cadena ARN transcrita:");
    printf("\nAcido nucleico = R");
    baseNitrogenadaTranscrita('T');
    transcribir(cadena, cadenaARN);
    printAcidoNucleico(cadenaARN);
}
