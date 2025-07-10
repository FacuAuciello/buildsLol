#MENU PRINCIPAL

#\n para los saltos de linea
print("BIENVENIDO A LA GUIA DE BUILDS DE LEAGUE OF LEGENDS\n------MENU PRINCIPAL------\n1.Ver Builds por campeon (por el momento solo ADC...)\n2.Agregar una Build nueva\n3.Eliminar una Build\n4.Simular un duelo entre dos Builds\n5.Salir")

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
        "KogMaw":[["Hoja del Rey Arruinado", "Hoja de furia de Guinsoo", "Huracan de Runaan", "Final del Ingenio", "Verdugo de Krakens"]],
        "Lucian":[["Segador de Esencia", "Filofugaz de Navori", "Filo Infinito", "Recuerdos de Lord Dominik", "Canion de Fuego Rapido"]],
        "MissFortune":[["Filo fantasmal de Yomuu", "Recaudadora", "Filo Infinito", "Rencor de Serylda", "Filo de la Noche"]],
        "Nilah":[["Recaudadora", "Filo Infinito", "Recuerdos de Lord Dominik", "Arcoescudo Inmortal", "Baile de la Muerte"]],
        "Samira":[["Recaudadora", "Filo Infinito", "Recuerdos de Lord Dominik", "Arcoescudo Inmortal", "Angel de la Guarda"]],
        "Senna":[[ "Cuchilla Negra", "Canion de Fuego Rapido", "Filo Infinito", "Angel de la Guarda"]],
        "Sivir":[["Flechas de los Yun Tal", "Filofugaz de Navori", "Filo Infinito", "Recordatorio Letal", "Sanguinaria"]],
        "Smolder":[["Segador de Esencia", "Lanza de Shojin", "Canion de Fuego Rapido", "Filo Infinito", "Recuerdos de Lord Dominik"]],
        "Tristana":[["Flechas de los Yun Tal", "Filo Infinito", "Filofugaz de Navori", "Canion de Fuego Rapido", "Sanguinaria"]],
        "Twitch":[[ "Recaudadora", "Huracan de Runaan", "Filo Infinito", "Recuerdos de Lord Dominik"]],
        "Varus":[["Hoja del Rey Arruinado", "Filo fantasmal de Yomuu", "Muramana", "Rencor de Serylda", "Filo de la Noche"]],
        "Vayne":[["Hoja del Rey Arruinado", "Hoja de furia de Guinsoo", "Verdugo de Krakens", "Recuerdos de Lord Dominik", "Filo Infitio"]],
        "Kayah":[["Segador de Esencia", "Filofugaz de Navori", "Filo Infinito", "Bailarin Espectral", "Sanguinaria"]],
        "Zeri":[["Punial de Statikk", "Flechas de los Yun Tal", "Filo Infinito", "Recuerdos de Lord Dominik", "Bailarin Espectral"]],
        "Ziggs":[["Acompaniante de Luden", "Tormento de Liandry", "Abrazo del Serafin", "Llamasombria", "Sombrero mortal de Rabadon"]],
    }

numero = int(input("Ingresa el numero de la opcion que deseas ver: "))

if numero == 1:
    print("------BUILDS POR CAMPEON------\n1:Aphelios\n2:Ashe\n3:Caitlyn\n4:Corki\n5:Draven\n6:Ezreal\n7:Jhin\n8:Jinx\n9:Kaisa\n10:Kalista\n11:KogMaw\n12:Lucian\n13:MissFortune\n14:Nilah\n15:Samira\n16:Senna\n17:Sivir\n18:Smolder\n19:Tristana\n20:Twitch\n21:Varus\n22:Vayne\n23:Xayah\n24:Zeri\n25:Ziggs")
    
    nombre = int(input("Selecciona el numero del campeon que quieras: "))
    campeon = diccionario[nombre]
    print(f"Seleccionaste: {campeon}")
    print("Build para", campeon, ":", " - ".join(builds[campeon])) #join toma una lista de strings y los une en una sola cadena, toma cada item de la build. Lo que va adelante de join es lo que se usa como separador.

elif numero == 2:
    print("------AGREGAR BUILD NUEVA------\n1:Aphelios\n2:Ashe\n3:Caitlyn\n4:Corki\n5:Draven\n6:Ezreal\n7:Jhin\n8:Jinx\n9:Kaisa\n10:Kalista\n11:KogMaw\n12:Lucian\n13:MissFortune\n14:Nilah\n15:Samira\n16:Senna\n17:Sivir\n18:Smolder\n19:Tristana\n20:Twitch\n21:Varus\n22:Vayne\n23:Xayah\n24:Zeri\n25:Ziggs")
    
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

elif numero == 3:
    print("------ELIMINAR UNA BUILD------\n1:Aphelios\n2:Ashe\n3:Caitlyn\n4:Corki\n5:Draven\n6:Ezreal\n7:Jhin\n8:Jinx\n9:Kaisa\n10:Kalista\n11:KogMaw\n12:Lucian\n13:MissFortune\n14:Nilah\n15:Samira\n16:Senna\n17:Sivir\n18:Smolder\n19:Tristana\n20:Twitch\n21:Varus\n22:Vayne\n23:Xayah\n24:Zeri\n25:Ziggs")
    eliminarBuild = int(input("Selecciona el campeon que queres eliminarle una Build: "))
    campeon = diccionario[eliminarBuild]
    print(f"Seleccionaste:{campeon}")
    
    
    for j, build in enumerate(builds[campeon]): #J es la variable que representa el indice numero y build representa el valor de la lista en esa posicion. 
        print(f"Build {j + 1}: {' - '.join(build)}") #Enumerate nos da los dos valores en cada iteracion. La coma permite desempaquetar esos dos valores en dos variables distintas
        indiceBuild = int(input("Selecciona la Build que queres eliminar: ")) - 1
        del builds[campeon][indiceBuild]
    print("Build eliminada correctamente")
    

elif numero == 4:
    print("------SIMULAR BATALLA DE BUILDS------")
    batalla1 = str(input("Selecciona el primer campeon para la batalla: "))
    batalla2 = str(input("Selecciona el segundo campeon para la batalla: "))

elif numero == 5:
    print("Hasta luego INVOCADOR")

else:
    print("ERROR. Ingresa un numero correcto")