contra="UCA2025"
entrada=""
intentos=0




while intentos < 3:
    entrada=input("Ingrese contrasena: ")

    if entrada!=contra:
        print("Contrasena incorrecta")
        intentos+=1 
    if entrada==contra:
        print("Contrasena correcta")



