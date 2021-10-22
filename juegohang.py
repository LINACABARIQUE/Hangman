def run():
    #LISTA DE PALABRAS
    palabras=[]
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        for line in f:
            palabras.append(line)

    from random import randint
    palabra=palabras[randint(0,len(palabras))].strip()
    import unidecode
    palabra = unidecode.unidecode(palabra)

    
    longitud=len(palabra)
    diccionario=dict(enumerate(palabra))
    import os
    
    #INICIALIZA LA PALABRA A MOSTRAR
    palabra_mostrar=""
    for _ in range(longitud):
        palabra_mostrar=palabra_mostrar+"-"
    print(palabra_mostrar)

    #BUSCA LA LETRA DE INPUT EN EL STRING
    while palabra_mostrar!=palabra:
        letra=input("Por favor escriba una letra: ")
        assert letra.isalpha(),"No son válidos números ni caracteres especiales"

        #SI LA ENCUENTRA, REEMPLAZA EN LA PALABRA
        campos=[]
        for key,value in diccionario.items():
            if value==letra:
                campos.append(key)
        
        for i in campos:
            palabra_mostrar=palabra_mostrar[:i]+letra+palabra_mostrar[i+1:]
        print(palabra_mostrar)


       

if __name__=="__main__":
    run()