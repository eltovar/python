frutas = {'Plátano':1700, 'Manzana':1000, 'Pera':1000, 'Naranja':1500, 'Uvas':1000, 'Cerezas':950, 'Piña':6000, 'Limon':1900}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")