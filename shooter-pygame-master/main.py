# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Student:
   def __init__(self, name, rollno):
       self.name=name
       self.rollno=rollno
   def __str__(self):
       return 'This is Student object with name {} and roll no {}'.format(self.name, self.rollno)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    preguntas = { "¿Cual es el animal mas grande del mundo": "la ballena azul",
              "¿Cual es el planeta mas cercano al sol?": "Mercurio",
              "¿Que animal tiene la piel da rayas negras y blancas":"La cebra"}

    puntos=0



    for pregunta , respuesta in preguntas.items():
        print(pregunta)
        respuesta_usuario = input("Tu respuesta:")

        if respuesta_usuario.lower()==respuesta.lower():
            print("¡Correcto")
            puntos+=1
        else:
            print("Incorrecto , la repsuesta correcta es : " + respuesta)

    print(f"Finalizo el juego , obtuviste {puntos} puntos ")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    main()
    print("este es un primer cambioooo")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
