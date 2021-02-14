
import random

list_weapons = [
    {'name' : 'Carikiam Shots', 'range' : 150,'Level':'One of a Kind'},
    {'name' : 'BFC', 'range' : 750, 'Level': 'Very Common'},
    {'name' : 'Flame Pistol', 'range' : 200,'Level': 'Uncommon'},
    {'name' : 'Blade of Shadows', 'range' : 300 ,'Level': 'Legendaryily Rare'},
    {'name': 'Overseer', 'range': 500, 'Level': 'Common'},
    {'name' : 'Bergut M4', 'range': 325, 'Level':'Rare' },
    {'name' : 'Arch Venz', 'range': 120, 'Level': 'Common'}
]


list_characters=['Kikando', 'Chester','Jack', 'Uruiguma', 'Hugiami', 'Asahi', 'Haru', 'Reo', 'Hinata']


list_characterpower=['Shape Shifting' ,'Cloning' ,'Invisibilty' ,'Dark Sourcery' ,'Ligthing Bolts ' ,'Sword Figthing Expert' ,'Preditcs The Future Before it happens' ,'Son Of The Devil']
list_charactername=['Clarke', 'Charm', 'Trishmay','Fangs', 'Wilkinson', 'Aoki', 'Aikiyama', 'Hirai', 'Hoga', 'Fujino']



def anime_get_content():
    s_content = ''

    s_content += '<!DOCTYPE html>'
    s_content += '<html>'
    s_content += '   <head>'
    s_content += '      <meta charset="utf-8">'
    s_content += '      <meta name="viewport" content="width=device-width">'
    s_content += '      <title>repl.it</title>'
    s_content += '      <link href="style.css" rel="stylesheet" type="text/css" />'
    s_content += '   </head>'
    s_content += '<body>'
    s_content += '<p style = "font-family:georgia,garamond,serif;font-size:20px;font-style:bold;">'


    s_content += '-----------------------------------<br>\n'
    s_content += '---ANIMEBATTLEGENERATOR.CO.UK.COM--<br>\n'
    s_content += '-----------------------------------<br>\n'


    for _ in range(2):
        weapon = random.choice(list_weapons)

        s_content +='<p>WEAPON : ' + weapon['name'] + '</p><br>'
        s_content +='LEVEL : ' + weapon['Level'] + '<br>'
        s_content +='WEAPON RANGE: ' + str(weapon['range']) + '<br>'
        s_content +='FIRST NAME :'  + random.choice(list_characters) + '<br>'
        s_content +='LAST NAME:' + random.choice(list_charactername) + '<br>'
        s_content +='STRENGTHS:' +random.choice(list_characterpower) + '<br>'
        s_content += '<br>\n'
        s_content += '<br>\n'

    s_content += '</body>'
    s_content += '</html>'

    return s_content
