# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random

description = """EcoHelper: tu bot de cambio climático."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)


@bot.event
async def on_ready():
    assert bot.user is not None
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')


# ---------------------------
#       COMANDO #hola
# ---------------------------
@bot.command()
async def hola(ctx):

    # El bot saluda al usuario
    await ctx.send(
        '¡Hola! Mucho gusto, yo soy tu EcoHelper personal. Puedo ayudarte con *consejos (#tip)*, *retos (#reto)*, *datos (#dato)*, *frases (#frase)*, adivinanzas (#adivinanza) o incluso puedo hacerte un *quiz* para var que tanto sabes sobre el calentamiento global *(#quiz)*!!'
    )


# ---------------------------
#       COMANDO #tip
# ---------------------------
@bot.command()
async def tip(ctx):

    # Lista de tips
    tips = [
        "Usá botella reutilizable en lugar de botellas plásticas.",
        "Apagá luces cuando salís de un cuarto.",
        "Desconectá cargadores y aparatos que no estás usando.",
        "Cerrá el grifo mientras te cepillás los dientes.",
        "Reutilizá bolsas en lugar de pedir nuevas.",
        "Separá tu basura: orgánico, reciclaje y no reciclable.",
        "Llevá tus propios cubiertos reutilizables cuando salís.",
        "Elegí caminar o usar bicicleta para viajes cortos.",
        "Llevá una camiseta de tela para hacer las compras.",
        "Evitá comprar comida muy empacada en plástico.",
        "Reutilizá frascos de vidrio como contenedores.",
        "Reducí tus duchas a menos de 10 minutos.",
        "Apagá la compu o tablet cuando no estás usando.",
        "Cerrá ventanas cuando está encendido el A/C.",
        "Usá ropa de segunda o intercambiá con amigos.",
        "Plantá aunque sea una planta pequeña en tu casa.",
        "Reutilizá papel escribiendo por ambos lados.",
        "Doná ropa que ya no usás en vez de tirarla.",
        "Recolectá agua de lluvia para regar plantas.",
        "Usá un termo para tus bebidas calientes/frías."
    ]

    await ctx.send(random.choice(tips))


# ---------------------------
#       COMANDO #frase
# ---------------------------
@bot.command()
async def frase(ctx):

    # Lista de frases
    frases = [
    "Sé cambio, no excusa.",
    "Pequeño paso, gran impacto.",
    "Cuidá el planeta… es el único con café.",
    "Dejá el mundo mejor de como lo encontraste.",
    "Menos ruido, más conciencia.",
    "Tu rutina también cambia el clima.",
    "Hacelo por vos. Hacelo por todos.",
    "Lo que hacés suma. Siempre.",
    "Elegí intención, no costumbre.",
    "Salvar al planeta es la nueva moda.",
    "El planeta te escucha. Responde bien.",
    "Hoy cuenta. Mañana también.",
    "La Tierra no es un recurso, es un hogar.",
    "Sostenible se ve mejor en vos.",
    "No esperés a mañana. El planeta tampoco.",
    "Cambiar un hábito cambia un mundo.",
    "Cuidar el planeta nunca pasa de moda.",
    "Tu mejor versión también cuida la Tierra.",
    "Ser consciente es ser poderoso.",
    "La diferencia empieza en tu elección.",
    "Pequeños actos, grandes cambios.",
    "Tu huella cuenta. Hacela ligera.",
    "Elegí verde, viví mejor.",
    "El planeta también siente.",
    "Cuidar la Tierra nunca fue tan urgente.",
    "Respirá profundo. El planeta también quiere.",
    "Construí futuro, no basura.",
    "Elegí consciente, viví consciente.",
    "Un día a la vez, un impacto a la vez.",
    "Sé parte del cambio, no del daño.",
    "El mundo te observa. Sorprendelo.",
    "Ser eco no es difícil. No serlo sí.",
    "Una acción tuya es un respiro del planeta.",
    "La Tierra habla. Escuchala.",
    "Menos consumo, más conexión.",
    "Green is the new cool.",
    "Tu poder está en tus hábitos.",
    "Elegí lo que suma, no lo que sobra.",
    "Ser sostenible se ve bien en vos.",
    "Tomá decisiones con impacto, no con prisa."
]


    await ctx.send(random.choice(frases))


# ---------------------------
#       COMANDO #quiz
# ---------------------------
@bot.command()
async def quiz(ctx):

    #lista de preguntas para el quiz
    preguntas = [
    ["¿Quién es el principal causante del calentamiento global? (Respondé con a, b, c o d)", 
     "a) Oxígeno \n b) Dióxido de carbono (CO₂) \n c) Nitrógeno \n d) Helio", 
     "b"],

    ["¿Cuál es una de las principales actividades humanas que aumenta las emisiones de CO₂? (Respondé con a, b, c o d)", 
     "a) Plantar árboles \n b) Quemar combustibles fósiles \n c) Reciclar papel \n d) Usar energía solar", 
     "b"],

    ["¿Cuál gas de efecto invernadero es liberado principalmente por la ganadería? (Respondé con a, b, c o d)", 
     "a) Metano (CH₄) \n b) Ozono \n c) Vapor de agua \n d) Argón", 
     "a"],

    ["¿Qué consecuencia directa está relacionada con el derretimiento de los polos? (Respondé con a, b, c o d)", 
     "a) Más sequías \n b) Ascenso del nivel del mar \n c) Menos tormentas \n d) Disminución de CO₂", 
     "b"],

    ["¿Cuál de estas acciones ayuda a reducir el calentamiento global? (Respondé con a, b, c o d)", 
     "a) Usar más plástico \n b) Dejar luces encendidas \n c) Andar en bicicleta \n d) Comprar ropa cada semana", 
     "c"],

    ["¿Qué sector produce la mayor cantidad de emisiones de gases de efecto invernadero a nivel mundial? (Respondé con a, b, c o d)", 
     "a) Transporte \n b) Agricultura \n c) Generación de energía \n d) Moda", 
     "c"],

    ["¿Cuál de los siguientes NO es un gas de efecto invernadero? (Respondé con a, b, c o d)", 
     "a) Dióxido de carbono \n b) Metano \n c) Ozono \n d) Neón", 
     "d"],

    ["¿Qué fenómeno climático extremo es más frecuente debido al calentamiento global? (Respondé con a, b, c o d)", 
     "a) Lluvias moderadas \n b) Huracanes intensos \n c) Vientos suaves \n d) Cielos despejados", 
     "b"],

    ["¿Qué tipo de energía es más sostenible y no emite CO₂? (Respondé con a, b, c o d)", 
     "a) Carbón \n b) Petróleo \n c) Energía eólica \n d) Gas natural", 
     "c"],

    ["¿Qué práctica contribuye a aumentar el calentamiento global? (Respondé con a, b, c o d)", 
     "a) Reforestación \n b) Deforestación \n c) Energía solar \n d) Transporte público", 
     "b"],

    ["¿Cuál es la fuente principal de basura en los océanos? (Respondé con a, b, c o d)", 
     "a) Vidrio \n b) Metal \n c) Plástico \n d) Cartón", 
     "c"],

    ["¿Cuál de estas acciones ahorra MÁS agua? (Respondé con a, b, c o d)", 
     "a) Cerrar el grifo al lavarse los dientes \n b) Usar pajillas de metal \n c) Apagar luces \n d) Usar bicicleta", 
     "a"],

    ["¿Qué energía es renovable? (Respondé con a, b, c o d)", 
     "a) Carbón \n b) Petróleo \n c) Energía solar \n d) Gas natural", 
     "c"],

    ["¿Qué material tarda MÁS en descomponerse? (Respondé con a, b, c o d)", 
     "a) Papel \n b) Cáscara de banana \n c) Algodón \n d) Botella plástica", 
     "d"],

    ["¿Qué porcentaje del agua del planeta es dulce? (Respondé con a, b, c o d)", 
     "a) 50% \n b) 20% \n c) 2.5% \n d) 10%", 
     "c"],

    ["¿Cuál es una práctica sostenible? (Respondé con a, b, c o d)", 
     "a) Usar ropa fast fashion \n b) Separar los residuos \n c) Comprar más plástico \n d) Tener luces prendidas todo el día", 
     "b"],

    ["¿Qué produce más emisiones? (Respondé con a, b, c o d)", 
     "a) El transporte aéreo \n b) La ganadería \n c) Los trenes eléctricos \n d) Los libros", 
     "b"],

    ["¿Cuál es un ejemplo de energía limpia? (Respondé con a, b, c o d)", 
     "a) Energía eólica \n b) Energía del carbón \n c) Energía del petróleo \n d) Energía del gas", 
     "a"],

    ["¿Cuál acción ayuda a reducir emisiones? (Respondé con a, b, c o d)", 
     "a) Comprar autos grandes \n b) Caminar o usar bicicleta \n c) Comprar más ropa \n d) Dejar aparatos encendidos", 
     "b"],

    ["¿Qué causa la lluvia ácida? (Respondé con a, b, c o d)", 
     "a) Exceso de vapor de agua \n b) Emisiones industriales de azufre y nitrógeno \n c) Rayos solares \n d) Aire frío", 
     "b"],

    ["¿Qué ecosistema es más vulnerable al aumento de temperatura global? (Respondé con a, b, c o d)", 
     "a) Desierto \n b) Bosque seco \n c) Arrecife coralino \n d) Sabana", 
     "c"],

    ["¿Qué acción humana contribuye al deshielo polar? (Respondé con a, b, c o d)", 
     "a) Reciclar \n b) Usar paneles solares \n c) Quemar combustibles fósiles \n d) Reutilizar agua", 
     "c"],

    ["¿Qué país emite más CO₂ actualmente? (Respondé con a, b, c o d)", 
     "a) Canadá \n b) China \n c) Brasil \n d) España", 
     "b"],

    ["¿Qué dispositivo consume más energía si se deja conectado todo el día? (Respondé con a, b, c o d)", 
     "a) Un cargador sin uso \n b) Un televisor \n c) Un reloj digital \n d) Una lámpara LED", 
     "b"],

    ["¿Cuál de estas acciones genera MÁS residuos? (Respondé con a, b, c o d)", 
     "a) Reutilizar botellas \n b) Comprar comida empacada \n c) Usar bolsas de tela \n d) Compostar restos orgánicos", 
     "b"],

    ["¿Qué sector consume más agua dulce mundialmente? (Respondé con a, b, c o d)", 
     "a) Agricultura \n b) Industria \n c) Hogares \n d) Transporte", 
     "a"],

    ["¿Qué tipo de transporte contamina menos? (Respondé con a, b, c o d)", 
     "a) Motocicleta \n b) Avión \n c) Bicicleta \n d) Automóvil", 
     "c"],

    ["¿Qué gas se libera cuando se quema petróleo? (Respondé con a, b, c o d)", 
     "a) Oxígeno \n b) Dióxido de carbono \n c) Helio \n d) Neón", 
     "b"],

    ["¿Cuál es una consecuencia directa de la deforestación? (Respondé con a, b, c o d)", 
     "a) Aumento de oxígeno \n b) Pérdida de biodiversidad \n c) Más sombra \n d) Suelo más fértil", 
     "b"],

    ["¿Qué efecto tiene el plástico en los animales marinos? (Respondé con a, b, c o d)", 
     "a) Mejora su crecimiento \n b) Los confunde y pueden ingerirlo \n c) Les da alimento \n d) Los protege del sol", 
     "b"],

    ["¿Qué objeto contamina más por su producción? (Respondé con a, b, c o d)", 
     "a) Botella de vidrio \n b) Botella plástica \n c) Libro \n d) Cepillo de dientes de bambú", 
     "b"],

    ["¿Qué tipo de energía NO es renovable? (Respondé con a, b, c o d)", 
     "a) Geotérmica \n b) Solar \n c) Hidroeléctrica \n d) Petróleo", 
     "d"],

    ["¿Cuál de estas acciones ayuda a conservar bosques? (Respondé con a, b, c o d)", 
     "a) Comprar papel reciclado \n b) Comprar muebles nuevos siempre \n c) Usar más plástico \n d) Imprimir todo", 
     "a"],

    ["¿Qué fenómeno climático aumenta por el calentamiento global? (Respondé con a, b, c o d)", 
     "a) Huracanes más intensos \n b) Nubes más pequeñas \n c) Días más cortos \n d) Menos evaporación", 
     "a"]
]


    # Escoge una pregunta aleatoria de la lista 'preguntas' y envía la pregunta con las opciones
    pregunta = random.choice(preguntas)
    await ctx.send(pregunta[0]) #pregunta
    await ctx.send(pregunta[1]) #opciones


    # Espera la respuesta durante 20 segundos
    try:
        answer = await bot.wait_for("message", timeout = 20)

    # Avisa que se acabó el tiempo
    except:
        await ctx.send("¡Se acabó el tiempo! La respuesta correcta era: " + pregunta[2])
        return

    # Si la respuesta es correcta
    if answer.content.lower() == pregunta[2]:
        await ctx.send("¡Respuesta correcta!")

    # Si la respuesta es incorrecta
    else:
        await ctx.send("Respuesta incorrecta. La respuesta correcta era: " + pregunta[2])



# ---------------------------
#       COMANDO #adivinanza
# ---------------------------
@bot.command()
async def adivinanza(ctx):

    # Lista de adivinanzas

    # Lista de adivinanzas
    adivinanzas = [
        ("No tengo manos ni pies, pero puedo destruir montañas. ¿Qué soy?", "agua"),
        ("Puedo ser tormenta, brisa o huracán. Todos me sienten pero nadie me ve. ¿Qué soy?", "viento"),
        ("Cuando llego, todos corren a esconderse del sol. ¿Qué soy?", "nube"),
        ("Vivo en el suelo, pero sin mí nada crecería. ¿Qué soy?", "tierra"),
        ("Soy frío, soy blanco, y si desaparezco el mar sube. ¿Qué soy?", "hielo"),
        ("Soy grande, azul, y guardo más secretos que libros. ¿Qué soy?", "océano"),
        ("Me movés con tus decisiones aunque nunca me toqués. ¿Qué soy?", "huella de carbono"),
        ("Tengo anillos pero no soy de casamiento. ¿Qué soy?", "árbol"),
        ("No tengo boca pero grito; no tengo cuerpo pero destruyo. ¿Qué soy?", "terremoto"),
        ("Subo y bajo sin escaleras, y muevo barcos sin tocarlos. ¿Qué soy?", "marea"),
        ("Llevo luz sin quemarte y energía sin contaminarte. ¿Qué soy?", "sol"),
        ("Traigo vida, pero también puedo llevarla. ¿Qué soy?", "lluvia"),
        ("Si me cuidás, vivo miles de años. Si me cortás, muero en segundos. ¿Qué soy?", "árbol"),
        ("Soy invisible, pero sin mí morirías en minutos. ¿Qué soy?", "aire"),
        ("Soy pequeño, pero puedo destruir ecosistemas enteros. ¿Qué soy?", "microplástico"),
        ("Mi hogar se derrite y no es mi culpa. ¿Qué soy?", "oso polar"),
        ("Puedo ser cristalina o mortal, pura o contaminada. ¿Qué soy?", "agua"),
        ("No hablo, pero te digo cómo está el planeta. ¿Qué soy?", "clima"),
        ("Soy silencioso, pero mi ausencia hace ruido. ¿Qué soy?", "bosque")
    ]

    # Escoge una adivinanza aleatoria
    pregunta, respuesta_correcta = random.choice(adivinanzas)

    # Enviar la adivinanza
    await ctx.send(pregunta)

    # Espera cualquier respuesta 
    try:
        respuesta_usuario = await bot.wait_for("message", timeout=20)
    except:
        await ctx.send("Se acabó el tiempo. La respuesta correcta era: " + respuesta_correcta)
        return

    # Revisa respuesta
    if respuesta_usuario.content.lower().strip() == respuesta_correcta:
        await ctx.send("¡Respuesta correcta!")
    else:
        await ctx.send("Respuesta incorrecta. Era: " + respuesta_correcta)



# ---------------------------
#       COMANDO #reto
# ---------------------------
@bot.command()
async def reto(ctx):

    # Lista de retos
    retos = [
        "Hoy, tomá una ducha de menos de 8 minutos.",
        "Usá tu botella reutilizable todo el día.",
        "Desconectá tres aparatos que no estés usando.",
        "Salí a caminar al menos 10 minutos sin usar transporte.",
        "Reutilizá un frasco o contenedor para algo nuevo.",
        "Separá correctamente tu basura durante todo el día.",
        "Día sin plásticos de un solo uso.",
        "Ducha en 3 minutos o menos.",
        "Usar solo botella reutilizable por una semana.",
        "Apagar y desconectar todo lo que no se usa (energía fantasma).",
        "Reto de separar toda la basura durante 7 días.",
        "Crear un objeto útil con materiales reciclados.",
        "Recolectar basura en un parque o zona verde por 20 minutos.",
        "Traer un snack sin empaques.",
        "Un día sin carne o alimentos de alto impacto.",
        "Reutilizar un outfit (sin comprar nada nuevo).",
        "Plantar una semilla o planta nativa y documentar su crecimiento.",
        "No pedir bolsas en ninguna tienda durante una semana.",
        "Usar transporte sostenible (caminar, bici, carpool).",
        "Reutilizar agua (por ejemplo, del lavado de frutas) para regar plantas.",
        "Usar un solo cuaderno ecológico hecho con papel reciclado.",
        "Reto de “cero basura” por un día.",
        "Llevar siempre un cubierto reutilizable para evitar los desechables.",
        "Hacer un cartel o mini campaña para concientizar sobre el reciclaje.",
        "Intercambiar algo que ya no usás en vez de botarlo.",
        "Guardar toda la basura producida en un día para analizarla y reducirla.",
    ]

    await ctx.send(random.choice(retos))


# ---------------------------
#       COMANDO #dato
# ---------------------------
@bot.command()
async def dato(ctx):

    #Lista de datos
    datos = [
        "La Tierra ya está 1.1°C más caliente que hace 150 años.",
        "Más del 90% del calor extra queda atrapado en los océanos.",
        "Cada minuto se tiran 1 millón de botellas plásticas en el mundo.",
        "Cambiar una bombilla normal por LED reduce un 80% de energía.",
        "Las vacas producen más gases contaminantes que todos los aviones juntos.",
        "Los polos se están calentando cuatro veces más rápido que el resto del planeta.",
        "Un árbol grande puede absorber el CO₂ de un carro manejando 40 km.",
        "La moda rápida produce más contaminación que el transporte marítimo y aéreo combinados.",
        "La temperatura más alta registrada en la Tierra fue 56.7°C.",
        "El 70% del oxígeno del planeta viene del mar.",
        "1 kilo de carne necesita hasta 15.000 litros de agua para producirse.",
        "Si todo el hielo de la Antártida se derritiera, el mar subiría 58 metros.",
        "Los huracanes son más fuertes porque los océanos están más calientes.",
        "El plástico tarda más de 400 años en degradarse.",
        "Más del 40% de las especies animales están en riesgo por el clima.",
        "Una persona promedio genera 4.5 kilos de basura diaria.",
        "El Ártico podría quedar sin hielo en verano para el año 2050.",
        "Usar una botella reutilizable por un año evita 150 botellas plásticas.",
        "Los incendios forestales liberan tanto CO₂ que pueden cambiar el clima local.",
        "Las olas de calor son ahora 5 veces más frecuentes que en los 80s.",
    ]

    await ctx.send(random.choice(datos))



# ---------------------------
#   RESPUESTA SI EL COMANDO NO EXISTE
# ---------------------------
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando desconocido ❌. Probá con #hola, #tip, #reto o #dato.")
    else:
        raise error


# ---------------------------
#        EJECUTAR BOT
# ---------------------------
bot.run("MTMzMzU4MDYxNTIwNjgzNDI3MQ.GiAT5V.hjENiD3AqNO-fAzigcfBcSm8mG29fHDtmKq0cc")