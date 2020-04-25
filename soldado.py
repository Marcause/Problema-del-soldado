#El bojetivo es realizar una función que devuelva la posición del último soldado vivo
#https://www.youtube.com/watch?v=uCsD3ZGzMgE&feature=youtu.be

def multiplo2(num): #devuelve la mayor potencia de 2 contenida en el número 
    if num == 1:
        return 0
    elif num%2 != 0:
        return (multiplo2(num-1))
    elif num%2 == 0:
        return (1 + multiplo2(num/2))

def soldado_ganador(a):
    x = multiplo2(a)
    soldado = (a-2**x)*2+1
    mensaje = "Para {} soldados, el último soldado en pie es {}".format(a, soldado)
    print(mensaje)