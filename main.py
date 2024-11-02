import ollama
MODELO_IA = "gemma2"
MENSAJES_COMPROBACION = [{'role':'assistant',
                           'content':"""Te comportarás como un croupier profesional en una mesa de ruleta de casino. El usuario va a mandar una apuesta y tienes que comprobar que la apuesta es correcta con las siguientes reglas:
                           La apuesta es un número entre el 1 y 36 (incluidos), o una de las siguientes cadenas de texto: 'rojo', 'negro', 'par', 'impar'.
                           En caso de que la apuesta sea correcta sólo debes contestar 'La apuesta es válida'
                           En caso de que la apuesta no sea correcta muy educadamente que se ha equivocado y las posibilidades"""}]
MENSAJES_GIRA_RULETA = [{'role':'assistant',
                            'content':"""Te comportarás como un croupier profesional en una mesa de ruleta de casino. Cada vez que te lo pida, dirás un número al azar entre 0 y 36, especificando las siguientes características en un formato claro y preciso:
                            Si el número es 0, simplemente dirás: 0, la banca gana.
                            Si el número es del 1 al 36, deberás indicar:
                            Color: Especificar si es rojo o negro según el color tradicional de la ruleta.
                            Paridad: Indicar si es par o impar.
                            Pasa o No Pasa:
                            No pasa para números entre 1 y 18.
                            Pasa para números entre 19 y 36.
                            Ejemplo de salida:

                            15 rojo impar y no pasa
                            36 negro par y pasa
                            Emite solo el resultado en este formato cada vez que se te solicite."""},
                            {'role':'user',
                             'content': 'dime un numero'}]
MENSAJES_FINALES = [{'role':'assistant',
                           'content':"""El usuario te va a enviar una apuesta y un resultado y tienes que decirle el premio que ha conseguido con las siguientes reglas:
                           Si la apuesta es un numero y coincide con el numero del resultado ha conseguido un premio de 3600 euros
                           Si la apuesta es un color y coincide con el color del resultado ha conseguido 200 euros
                           Si la apuesta es 'par' o 'impar' y coincide con el resultado ha conseguido un premio de 200 euros
                           Si no se cumple ninguna regla le agradeces su jugada y le deseas suerte para la próxima"""}]

def ChumbarLaLlama(mensajes):
    respuesta = ollama.chat(model=MODELO_IA, messages=mensajes)
    #print(mensajes)
    print (respuesta['message']['content'])
    return respuesta['message']['content']

def ComprobarApuesta(apuesta):
    mensajeTemporal = MENSAJES_COMPROBACION.copy()
    mensajeTemporal.append({
        'role': 'user',
        'content': f'mi apuesta es {apuesta}'
    })
    
    return (ChumbarLaLlama(mensajeTemporal))
    
def GirarRuleta():
    print('La ruleta esta girando')
    return (ChumbarLaLlama(MENSAJES_GIRA_RULETA))

def ComprobarPremio(apuesta, resultado):
    mensajeTemporal = MENSAJES_FINALES.copy()

    mensajeTemporal.append({
        'role': 'user',
        'content': f'mi apuesta es {apuesta} y el resultado es {resultado}'
    })
    return (ChumbarLaLlama(mensajeTemporal))

def main():
    apuestaValida = False
    print("Bienvenido al casino")
    while True:
    
        while not apuestaValida:

            apuesta = input("Introduce tu apuesta( rojo, negro, par, impar o un numero del 1 al 36) (fin para terminar). Las apuestas son de 100 € ")
            if apuesta == 'fin': exit()
            apuestaValida = 'La apuesta es válida' in ComprobarApuesta(apuesta)
        resultado = GirarRuleta()
        ComprobarPremio(apuesta,resultado)
        apuestaValida = False


if __name__ == "__main__":
    main()