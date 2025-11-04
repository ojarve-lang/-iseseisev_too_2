import turtle

# Seadistused
turtle.speed(0)
turtle.pensize(2)

def joonista_maja_joontega(x, y, katus_varv, uks_varv, ukse_suurus=15):
    maja_suurus = 40
    katuse_korgus = 40

    # Katuse kolmnurk
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(katus_varv)
    turtle.goto(x + maja_suurus / 2, y + katuse_korgus)
    turtle.goto(x + maja_suurus, y)
    turtle.goto(x, y)

    # Maja ruut
    turtle.pencolor("black")
    for _ in range(4):
        turtle.forward(maja_suurus)
        turtle.right(90)

    # Uks keskel all
    ukse_x = x + (maja_suurus - ukse_suurus) / 2
    ukse_y = y - maja_suurus + ukse_suurus
    turtle.penup()
    turtle.goto(ukse_x, ukse_y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pencolor(uks_varv)
    for _ in range(4):
        turtle.forward(ukse_suurus)
        turtle.right(90)

def joonista_kass(x, y, suurus=10):
    """Joonistab kassi näo. Asendab naerunäo."""
    turtle.penup()
    turtle.goto(x, y) # Liigub kassi näo asukohta
    turtle.pendown()

    # Kassi pea (lihtsustatud ring)
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.circle(suurus)
    turtle.end_fill()

    # Kassi kõrvad (lihtsustatud kolmnurgad)
    pool_suurus = suurus / 2
    korva_suurus = suurus / 3

    # Vasak kõrv
    turtle.penup()
    turtle.goto(x - pool_suurus, y + suurus * 1.5)
    turtle.pendown()
    turtle.setheading(60) # Määrab suuna
    turtle.forward(korva_suurus)
    turtle.left(120)
    turtle.forward(korva_suurus)
    turtle.left(120)
    turtle.forward(korva_suurus)

    # Parem kõrv
    turtle.penup()
    turtle.goto(x + pool_suurus, y + suurus * 1.5)
    turtle.pendown()
    turtle.setheading(120)
    turtle.forward(korva_suurus)
    turtle.right(120)
    turtle.forward(korva_suurus)
    turtle.right(120)
    turtle.forward(korva_suurus)
