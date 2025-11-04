import turtle

# Seadistused
turtle.speed(0) # Kiireim kiirus joonistamiseks
turtle.pensize(2)

def joonista_maja_joontega(x, y, katus_varv, uks_varv, ukse_laius, ukse_korgus):
    # Maja standardmõõtmed
    maja_suurus = 40
    katuse_korgus = 40
    house_bottom_y = y - maja_suurus # Maja alumine serv (põrand)

    # Katuse kolmnurk
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(katus_varv)
    turtle.goto(x + maja_suurus / 2, y + katuse_korgus)
    turtle.goto(x + maja_suurus, y)
    turtle.goto(x, y) # Sulgeb katuse

    # Maja ruut (seinad)
    turtle.pencolor("black")
    turtle.goto(x + maja_suurus, y)
    turtle.setheading(270) # Alla
    turtle.forward(maja_suurus)
    turtle.setheading(180) # Vasakule
    turtle.forward(maja_suurus)
    turtle.setheading(90) # Üles
    turtle.forward(maja_suurus)
    turtle.setheading(0) # Taastab suuna 0 (paremale)

    # Uks keskel all
    
    # Arvutab ukse alguspunkti maja alumisel serval (keskele)
    ukse_x_algus = x + (maja_suurus - ukse_laius) / 2
    ukse_y_algus = house_bottom_y 
    
    turtle.penup()
    turtle.goto(ukse_x_algus, ukse_y_algus)
    turtle.setheading(0) # Näoga paremale
    turtle.pendown()
    turtle.pencolor(uks_varv)
    
    # Joonistab ukse (ristküliku) alustades alumisest vasakust nurgast
    turtle.forward(ukse_laius) # Paremale (alumine serv)
    turtle.left(90)
    turtle.forward(ukse_korgus) # Üles (parem serv)
    turtle.left(90)
    turtle.forward(ukse_laius) # Vasakule (ülemine serv)
    turtle.left(90)
    turtle.forward(ukse_korgus) # Alla (vasak serv)
    
    turtle.setheading(0) # Taastab horisontaalse suuna
    turtle.penup()

# --- Paigutus ja Majade Joonistamine ---
start_x = -150
start_y_ylem = 100
start_y_alumine = start_y_ylem - 80 # Piisav vahe ridade vahel
maja_vahe = 60 # Majade vaheline kaugus

## 🏡 Ülemine rida – Roheline katus ja PUNANE uks (RUUT)

# Ukse mõõtmed ruudu jaoks: laius = kõrgus
ruut_uks_suurus = 15 
for i in range(5):
    x = start_x + i * maja_vahe
    # Ruudukujuline uks (15x15)
    joonista_maja_joontega(x, start_y_ylem, "green", "red", 
                           ukse_laius=ruut_uks_suurus, ukse_korgus=ruut_uks_suurus)


## 🏠 Alumine rida – Roheline katus ja SININE uks (RISTKÜLIK)

# Ukse mõõtmed ristküliku jaoks: kõrgus > laius
ristkulik_laius = 15
ristkulik_korgus = 20
for i in range(5):
    x = start_x + i * maja_vahe
    # Ristkülikukujuline uks (15 lai, 20 kõrge)
    joonista_maja_joontega(x, start_y_alumine, "green", "blue", 
                           ukse_laius=ristkulik_laius, ukse_korgus=ristkulik_korgus)


# Peidame kilpkonna ja hoiame akna lahti
turtle.hideturtle()
turtle.done()

