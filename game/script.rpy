# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Claire")
define a = Character("Kara first")
#define s = Character("[name]")
define m = Character("Menge")


#Kram für später
#image smile = Movie(play="images/video/smile.webm") - Video Inizialisierung
# Das Gefühl der Zeit des Tages
#screen daytime:
    #if dt == "Morgen":
        #add "#8404"
    #if dt == "Tag":
        #add "#0484"
    #if dt == "Abend":
        #add "#000b"
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
#screen room:
    #imagemap:
        #hover 'images/smthng/room1_hover.png'#при наведении
        #idle 'images/smthng/room1_idle.png'#standart
        #hotspot (1522, 522, 500, 320) action Jump('labtop')
        #hotspot (0, 457, 820, 820) action Jump('bed')
        #hotspot (1628, 860, 250, 200) action Jump('hall')

init:

    image bahnhof = "gg/bahnhof.png"

    image zug = "gg/zug.png"

    image oh_pity = "gg/game_over.jpg"

    image dorf = "gg/BGP.png"

    image jungClaire = "gg/clare_dorf.jpg"
    #$ dt = "Morgen"

    image clair_akt1_boese = "gg/clair_akt1_boese.png"

    image menge = "gg/menge.png"

    image clair_akt1_froh = "gg/clair_akt1_froh.png"

    image clair_akt1_boese = "gg/clair_akt1_boese.png"

    image beautiful_life = "gg/beautiful_life.png"

    image danke = "gg/danke.png"

label start:

    play music "<loop 0.001>audio/WB1.mp3"

    scene jungClaire with dissolve

    e "Hi!"

    #python:
        #name = renpy.input(_("Wie heißt du?"))

        #name = name.strip() or _("Alfred")


    scene jungClaire

    e "Hallo, lieber Alfred!"

    scene dorf with dissolve

    play sound "audio/horn_big.wav"
    queue music "<loop 0.001>audio/WB1.mp3"

    s "Oh, es ist schon so spät, ich sollte mich besser beeilen...Aber der Tag ist so schön.."


    menu:
        "Beeilen":
            jump choice1_ja
        "Den Tag genießen":
            jump choice1_nein
    label choice1_ja:
        $ menu_flag = True
        scene zug
        "Zug kommt pfeifend zum Stehen"
        #$ renpy.movie_cutscene("images/video/smile.webm") - um Video zu starten
        jump starten
        #jump choice1_done
    label choice1_nein:
        $ menu_flag = False
        scene game_over
        e "Oh..."
        #jump choice1_done

label starten:

    scene clair_akt1_boese
    e "Puh, endlich aus dem Zug raus. Ich fahre ja gerne Zug, aber dieser? Eine Zumutung!"

    e "Abgerissene Polster, dreckige Fenster und undicht waren sie auch noch! Der Speisewagen
    hatte nicht einmal Foie Gras für mich. So eine Schande!"

    scene menge

    m "Eine wahre Schande!"
    m "Früher haben hier die edelsten Schnellzüge gehalten!"
    m "Das waren noch Zeiten..."

    m "Sieh mal Mama, die Ohrringe!"
    m "Ist das ein Sarg den Sie da mitgebracht hat?"
    m "Ach, sicher nur so ein modischer Koffer."

    scene clair_akt1_froh

    e "Oh seht mal, die alte Bedürfnisanstalt hat mein Vater errichtet."
    e "Gute Arbeit, exakt ausgeführt."
    e "Ich saß als Kind stundenlang auf dem Dach und spuckte hinunter."
    e "Aber nur auf die Männer."

    scene clair_akt1_boese

    e "Also, meine liebe Güllener.."
    e "Ich sehe, unsere schöne Heimat hat ein bisschen gelitten,
    seit ich das letzte Mal zu Besuch war."

    scene menge

    "zustimmendes Gemurmel"

    scene clair_akt1_froh

    e "Dann wird es euch allen eine Freude sein, zu hören, dass ich nicht ausschließlich
    wegen der guten Landluft nach Hause gekommen bin."

    scene menge

    m "Was meint sie denn damit?"
    m "Vielleicht will sie eine neue Fabrik bauen?"
    m "Das würde uns allen Arbeit bringen!"
    m "Kann sie so was denn machen?"
    m "Hast du es nicht gehört?"
    m "Die kleine Claire ist jetzt steinreich!"
    m "Seid leise Leute, so verpassen wir ja alles...psssssssssst"

    scene clair_akt1_froh

    e "Ach ihr Lieben, zumindest das Getuschel hat sich nicht verändert. Ich habe tatsächlich
    eine Proposition für euch, meine liebsten Mitbürger."
    e "Ich möchte euch helfen, ich möchte in meine alte Heimat investieren, damit sie wieder
    ganz im alten Glanz erstrahlen kann."
    e "Um genau zu sein, möchte ich eine ganze Milliarde in euch, liebe Güllener, und unsere
    Stadt investieren."

    scene menge
    m "Eine Milliarde?"
    m "Wow, ich wusste ja, dass sie reich ist, aber..."
    m "Oh was für ein Segen, dafür haben wir alle gebetet!"
    m "Wussten wir es doch, Güllener halten fest zusammen, auch nach so langer Zeit!"
    m "Was ist eine Milliarde, Mama?"
    m "Ich weiß gar nicht, wie viele Nullen das sind."

    scene clair_akt1_froh
    e "Ähem. Natürlich habe ich meine stattlichen Mittel nicht komplett durch reine Menschenliebe erhalten,
    so schön das auch wäre."
    e "Auch wenn mein Angebot schon sehr daran grenzt, wenn ich es recht überdenke."
    e "Liebe Güllener..."
    e "Meine Großzügigkeit ist an eine minimale, winzig kleine
    Bedingung gebunden." #winzig? wiederholt?
    e "Kaum der Rede wert, wenn wir alle uns ausmalen, was diese Mittel unserer schönen Stadt bringen könnten."
    e "Mehr ein Zeichen der Wertschätzung als ein Handel, wenn ihr mich fragt."

    scene clair_akt1_boese
    e "Also, einen ganz kleinen Gefallen, den ihr mir tun müsst, bevor ich den
    Scheck aushändige, den ich schon in meinen Unterlagen vorbereitet habe." #ganz? wiederholt?

    scene clair_akt1_froh
    e "Ihr müsst nichts anderes tun, als meinen alten Liebhaber, den guten
    Alfred, töten."

    stop music
    play audio "<silence 3.0>"
    queue music "<loop 0.001>audio/WB2.mp3" fadein 5.0

    scene menge
    m "Was?"
    m "Das kann sie doch nicht ernst meinen!"
    m "Sicherlich nur ein Scherz unter alten Freunden."
    m "Ich wusste ja, dass die Trennung nicht schön war, aber so was?"
    m "Das ist doch ein Witz!"
    m "Wir sind doch keine Mörder."

    scene clair_akt1_boese
    e "Kein Scherz, nur Gerechtigkeit."
    e "Ich kann sie mir leisten."
    e "Eine Milliarde für Güllen, wenn jemand Alfred tötet."

    scene menge
    m "Niemals!"
    m "Wir würden uns nie so verkaufen!"
    m "Niemand von uns ist ein Mörder!"
    m "Ich wusste es ja immer, sie ist verrückt!"
    m "Wahre Güllener halten zusammen!"
    m "Was denkt sie, wen sie hier vor sich hat?"

    scene clair_akt1_froh
    e "Lasst euch Zeit. Ich warte."

    scene zug
    "Zug kommt pfeifend zum Stehen"

    menu:
        "Vor den Zug werfen":
            jump choice2_ja
        "Das Leben genießen":
            jump choice2_nein

    label choice2_ja:
        $ menu_flag = True
        scene game_over
        "Oh...du Arme.."
        jump choice2_done

    label choice2_nein:
        $ menu_flag = False
        scene beautiful_life
        "Oh ja!"
        jump choice2_done

    label choice2_done:
        scene danke with dissolve


label end:
        scene danke with dissolve

        return
