#Desafío40: Búsqueda de múltiples colores. Modificar el programa anterior para que el usuario pueda buscar múltiples colores. Tip: El usuario puede ingresar cuantos colores desee


import sys
search = sys.argv[1]
colors = {
"aliceblue": "#f0f8ff",
"antiquewhite": "#faebd7",
"aqua": "#00ffff",
"aquamarine": "#7fffd4",
"azure": "#f0ffff",
"darkorchid": "#9932cc",
"darkred": "#8b0000",
"darksalmon": "#e9967a",
"navajowhite": "#ffdead",
"navy": "#000080",
"orchid": "#da70d6",
"palegoldenrod": "#eee8aa",
"peachpuff": "#ffdab9",
"peru": "#cd853f",
"pink": "#ffc0cb",
"purple": "#800080",
"rebeccapurple": "#663399",
"red": "#ff0000",
"saddlebrown": "#8b4513",
"seashell": "#fff5ee",
"sienna": "#a0522d",
"silver": "#c0c0c0",
"skyblue": "#87ceeb",
"slateblue": "#6a5acd",
"teal": "#008080",
"thistle": "#d8bfd8",
"tomato": "#ff6347",
"turquoise": "#40e0d0",
"violet": "#ee82ee",
"wheat": "#f5deb3",
"white": "#ffffff",
"whitesmoke": "#f5f5f5",
"yellow": "#ffff00",
"yellowgreen": "#9acd32",
}

searched_hexas = sys.argv[1:]
colors_inv = {v:k for k,v in colors.items()}
for search in searched_hexas:
    if search in colors_inv:
        print(colors_inv[search])
    else:
        print("no-no")
