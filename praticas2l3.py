saluto= input("ciao, come ti chiami?:")

città=input(saluto + ("da dove vieni?:"))

animale=input(saluto+("come si chiama il tuo animale domestico?:"))
 
nome_band=(città+animale)

if (nome_band):
    print(saluto + f"il nome della tua band potrebbe essere: {nome_band}")