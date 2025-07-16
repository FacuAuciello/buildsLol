def mostrarMenu():
    print("BIENVENIDO A LA GUIA DE BUILDS DE LEAGUE OF LEGENDS\n------MENU PRINCIPAL------\n1.Ver Builds por campeon (por el momento solo ADC...)\n2.Agregar una Build nueva\n3.Eliminar una Build\n4.Simular un duelo entre dos Builds\n5.Salir") #\n para los saltos de linea

def mostrarCampeones():
    print("n1:Aphelios\n2:Ashe\n3:Caitlyn\n4:Corki\n5:Draven\n6:Ezreal\n7:Jhin\n8:Jinx\n9:Kaisa\n10:Kalista\n11:KogMaw\n12:Lucian\n13:MissFortune\n14:Nilah\n15:Samira\n16:Senna\n17:Sivir\n18:Smolder\n19:Tristana\n20:Twitch\n21:Varus\n22:Vayne\n23:Xayah\n24:Zeri\n25:Ziggs")

def verBuilds():
    print("------BUILDS POR CAMPEON------")
    mostrarCampeones()

def agregarBuilds():
    print("------AGREGAR BUILD NUEVA------")
    mostrarCampeones()

def eliminarBuilds():
    print("------ELIMINAR UNA BUILD------")
    mostrarCampeones()

def calculoDanio(build):
    sumaDanio = 0
    for k in build:
        sumaDanio += damageObjetos[k]
    return sumaDanio

def volver():
    while True:
        usuario = str.upper(input("Presiona 'V' para volver al Menu: "))
        if usuario == "V":
            print("Volviendo al Menu...")
            break
        else:
            print("ERROR. Presiona 'V' para volver al Menu: ")
        





#movi los diccionarios porque los habia puesto dentro del if y claramente viven ahi adentro, no me reconocia que estaban inicializados
diccionario = {
        1:"Aphelios",
        2:"Ashe",
        3:"Caitlyn",
        4:"Corki",
        5:"Draven",
        6:"Ezreal",
        7:"Jhin",
        8:"Jinx",
        9:"Kaisa",
        10:"Kalista",
        11:"KogMaw",
        12:"Lucian",
        13:"MissFortune",
        14:"Nilah",
        15:"Samira",
        16:"Senna",
        17:"Sivir",
        18:"Smolder",
        19:"Tristana",
        20:"Twitch",
        21:"Varus",
        22:"Vayne",
        23:"Xayah",
        24:"Zeri",
        25:"Ziggs",
    }

builds = { 
        "Aphelios":[["Recaudadora", "Filo Infinito", "Recuerdos de Lord Dominik", "Sanguinaria", "Arcoescudo Inmortal"]],
        "Ashe":[["Flechas de los Yun Tal", "Huracan de Runaan", "Filo Infinito", "Recuerdos de Lord Dominik","Sanguinaria"]],
        "Caitlyn":[["Recaudadora","Canion de Fuego Rapido", "Flechas de los Yun Tal", "Filo Infinito", "Recordatorio Letal"]],
        "Corki":[["Fuerza de Trinidad", "Muramana", "Canion de Fuego Rapido", "Lanza de Shojin","Filo Infinito"]],
        "Draven":[["Sanguinaria", "Recaudadora", "Recuerdos de Lord Dominik", "Filo Infinito", "Angel de la Guarda"]],
        "Ezreal":[["Fuerza de Trinidad", "Muramana", "Lanza de Shojin", "Rencor de Serylda", "Corazon de Hielo"]],
        "Jhin":[["Recaudadora", "Filo fantasmal de Yomuu", "Filo Infinito", "Recuerdos de Lord Dominik", "Sanguinaria"]],
        "Jinx":[["Flechas de los Yun Tal", "Huracan de Runaan", "Filo Infinito", "Recuerdos de Lord Dominik", "Verdugo de Krakens"]],
        "Kaisa":[["Punial de Statikk", "Hoja de furia de Guinsoo", "Diente de Nashor", "Recuerdos de Lord Dominik", "Filo Infinito"]],
        "Kalista":[["Hoja del Rey Arruinado", "Hoja de furia de Guinsoo", "El final", "JakSho el Proteico", "Filo Infinito"]],
        "KogMaw":[["Hoja del Rey Arruinado", "Hoja de furia de Guinsoo", "Huracan de Runaan", "Filo de la Cordura", "Verdugo de Krakens"]],
        "Lucian":[["Segador de Esencia", "Filofugaz de Navori", "Filo Infinito", "Recuerdos de Lord Dominik", "Canion de Fuego Rapido"]],
        "MissFortune":[["Filo fantasmal de Yomuu", "Recaudadora", "Filo Infinito", "Rencor de Serylda", "Filo de la Noche"]],
        "Nilah":[["Recaudadora", "Filo Infinito", "Recuerdos de Lord Dominik", "Arcoescudo Inmortal", "Baile de la Muerte"]],
        "Samira":[["Recaudadora", "Filo Infinito", "Recuerdos de Lord Dominik", "Arcoescudo Inmortal", "Angel de la Guarda"]],
        "Senna":[[ "Cuchilla Negra", "Canion de Fuego Rapido", "Filo Infinito", "Angel de la Guarda", "Filo de la Noche"]],
        "Sivir":[["Flechas de los Yun Tal", "Filofugaz de Navori", "Filo Infinito", "Recordatorio Letal", "Sanguinaria"]],
        "Smolder":[["Segador de Esencia", "Lanza de Shojin", "Canion de Fuego Rapido", "Filo Infinito", "Recuerdos de Lord Dominik"]],
        "Tristana":[["Flechas de los Yun Tal", "Filo Infinito", "Filofugaz de Navori", "Canion de Fuego Rapido", "Sanguinaria"]],
        "Twitch":[[ "Recaudadora", "Hoja de furia de Guinsoo","Huracan de Runaan", "Filo Infinito", "Recuerdos de Lord Dominik"]],
        "Varus":[["Hoja del Rey Arruinado", "Filo fantasmal de Yomuu", "Muramana", "Rencor de Serylda", "Filo de la Noche"]],
        "Vayne":[["Hoja del Rey Arruinado", "Hoja de furia de Guinsoo", "Verdugo de Krakens", "Recuerdos de Lord Dominik", "Filo Infitio"]],
        "Xayah":[["Segador de Esencia", "Filofugaz de Navori", "Filo Infinito", "Bailarin Espectral", "Sanguinaria"]],
        "Zeri":[["Punial de Statikk", "Flechas de los Yun Tal", "Filo Infinito", "Recuerdos de Lord Dominik", "Bailarin Espectral"]],
        "Ziggs":[["Acompaniante de Luden", "Tormento de Liandry", "Abrazo del Serafin", "Llamasombria", "Sombrero mortal de Rabadon"]],
    }

damageObjetos = {
    "Recaudadora":50,
    "Filo Infinito": 65,
    "Recuerdos de Lord Dominik": 35,
    "Sanguinaria": 80,
    "Arcoescudo Inmortal": 55,
    "Flechas de los Yun Tal": 55,
    "Huracan de Runaan": 40,
    "Canion de Fuego Rapido": 35,
    "Recordatorio Letal": 35,
    "Fuerza de Trinidad": 36,
    "Muramana": 35,
    "Lanza de Shojin": 45,
    "Angel de la Guarda": 55,
    "Rencor de Serylda": 45,
    "Corazon de Hielo": 60,
    "Filo fantasmal de Yomuu": 55,
    "Verdugo de Krakens":45,
    "Punial de Statikk": 45,
    "Hoja de furia de Guinsoo": 30,
    "Diente de Nashor": 80,
    "El final": 30,
    "JakSho el Proteico": 30,
    "Hoja del Rey Arruinado": 40,
    "Filo de la Cordura": 50,
    "Segador de Esencia": 60,
    "Filofugaz de Navori": 35,
    "Filo de la Noche": 50,
    "Baile de la Muerte": 60,
    "Cuchilla Negra": 40,
    "Bailarin Espectral": 50,
    "Acompaniante de Luden": 100,
    "Tormento de Liandry": 60,
    "Abrazo del Serafin": 70,
    "Llamasombria": 80,
    "Sombrero mortal de Rabadon": 130,
}

while True: #se va a ejecutar siempre, hasta que el usuario quiera salir

    mostrarMenu()
    numero = int(input("Ingresa el numero de la opcion que deseas ver: "))

    if numero == 1:
        verBuilds()
        
        nombre = int(input("Selecciona el numero del campeon que quieras: "))
        campeon = diccionario[nombre]
        print(f"Seleccionaste: {campeon}")
    
        for i, build in enumerate(builds[campeon]):
            print(f"Build {i + 1}: {' - '.join(build)}") #join toma una lista de strings y los une en una sola cadena, toma cada item de la build. Lo que va adelante de join es lo que se usa como separador.

        volver()

    elif numero == 2:
        agregarBuilds()

        buildNueva = int(input("Selecciona el numero del campeon que quieras agregarle una Build nueva: "))
        campeon = diccionario[buildNueva]
        print(f"Seleccionaste: {campeon}")
    
        listaItems = []
        for j in range(5):
            items = str(input("Ingresa el item: "))
            listaItems.append(items)
            print("Build nueva para", campeon, ":", " - ".join(listaItems))

            if campeon in builds:
                builds[campeon].append(listaItems)
            else: 
                builds[campeon] = [listaItems]
        
        volver()

    elif numero == 3:
        eliminarBuilds()

        eliminarBuild = int(input("Selecciona el campeon que queres eliminarle una Build: "))
        campeon = diccionario[eliminarBuild]
        print(f"Seleccionaste:{campeon}")
    
    
        for j, build in enumerate(builds[campeon]): #J es la variable que representa el indice numero y build representa el valor de la lista en esa posicion. 
            print(f"Build {j + 1}: {' - '.join(build)}") #Enumerate nos da los dos valores en cada iteracion. La coma (en linea 98) permite desempaquetar esos dos valores en dos variables distintas
            indiceBuild = int(input("Selecciona la Build que queres eliminar: ")) - 1 #si pone 1 se rompe, arranca desde el 0 pa
            del builds[campeon][indiceBuild]
            print("Build eliminada correctamente")
    
        volver()

    elif numero == 4:
        print("------SIMULAR BATALLA DE BUILDS------")
        mostrarCampeones()
    
        opcion1 = int(input("Selecciona el primer campeon para la batalla: "))
        opcion2 = int(input("Selecciona el segundo campeon para la batalla: "))

        campeon1 = diccionario[opcion1]
        print(f"Seleccionaste:{campeon1}")

        for i, build in enumerate(builds[campeon1]):
            print(f"Build {i + 1}: {' - '.join(build)}")
        indiceBuild = int(input("Selecciona la Build: ")) - 1
        build1 = builds[campeon1][indiceBuild]
    
        campeon2 = diccionario[opcion2]
        print(f"Seleccionaste:{campeon2}")
    
        for i, build in enumerate(builds[campeon2]):
            print(f"Build {i + 1}: {' - '.join(build)}")
        indiceBuild = int(input("Selecciona la Build: ")) - 1
        build2 = builds[campeon2][indiceBuild]
    
        import time
        print("La batalla comienza en...")
        for i in range(3, 0, -1):
            print(i)
        time.sleep(1)

        danio1 = calculoDanio(build1)
        danio2 = calculoDanio(build2)

        if danio1 > danio2:
            print(f"El ganador es {campeon1} con un danio total de: {danio1}")
        else:
            print(f"El ganador es {campeon2} con un danio total de: {danio2}")

        print(f"\nDaño de cada objeto de {campeon1}:")
        for item in build1:
            print(f"{item}: {damageObjetos[item]}")

        print(f"\nDaño de cada objeto de {campeon2}:")
        for item in build2:
            print(f"{item}: {damageObjetos[item]}")

        volver()

    elif numero == 5:
        print("Hasta luego INVOCADOR")
        break
    else:
        print("ERROR. Ingresa un numero correcto")