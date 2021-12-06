# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Claire")
define a = Character("Kara first")
define u = Character("[name]")

#screen room:
    #imagemap:
        #hover 'images/smthng/room1_hover.png'#при наведении
        #idle 'images/smthng/room1_idle.png'#standart
        #hotspot (1522, 522, 500, 320) action Jump('labtop')
        #hotspot (0, 457, 820, 820) action Jump('bed')
        #hotspot (1628, 860, 250, 200) action Jump('hall')

init:

    image bahnhof = "gg/bahnhof.png"

    image oh_yeah = "gg/oh_yeah.jpg"

    image oh_pity = "gg/game_over.jpg"

    image dorf = "gg/clare_dorf.jpg"
    $ dt = "Morgen"


    #image smile = Movie(play="images/video/smile.webm") - Video Inizialisierung

# Das Gefühl der Zeit des Tages
#screen daytime:
    #if dt == "Morgen":
        #add "#8404"
    #if dt == "Tag":
        #add "#0484"
    #if dt == "Abend":
        #add "#000b"
#CLAIRE ZACHANASSIAN
#Ich kann sie mir leisten. Eine Milliarde für Güllen, wenn jemand Alfred Ill tötet.“

label start:

    "Musik is playing"
    "just an example"

    #show screen daytime
    #scene nature
    #show girl
    #"Jetzt ist - [dt]."
    #$ dt = "Morgen"
    #"Jetzt ist - [dt]."
    #$ dt = "Tag"
    #"Jetzt ist - [dt]."
    #$ dt = "Abend"
    #"Jetzt ist - [dt]."
    #return

    scene bahnhof with dissolve #fade (anstatt dissolve kann man "fade" benuzten)

    e "Hi!"

    python:
        name = renpy.input(_("Wie heißt du?"))

        name = name.strip() or _("Gamer")


    scene dorf

    e "Hallo, liebe(-r) [name]!"

    e "[name], was möchtest du machen?"

    menu:
        "Game starten":
            jump choice1_ja
        "End the game":
            jump choice1_nein
    label choice1_ja:
        $ menu_flag = True
        scene oh_yeah
        e "Cool!"
        #$ renpy.movie_cutscene("images/video/smile.webm") - um Video zu starten
        jump starten
        jump choice1_done
    label choice1_nein:
        $ menu_flag = False
        scene game_over
        e "Oh..."
        jump enden
        jump choice1_done

label starten:
    e "Super! Let's start!"

label enden:

    e "Okay. Have a nice day!"

    # This ends the game.
    return
