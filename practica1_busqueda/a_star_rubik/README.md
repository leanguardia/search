## Adapters

¿Quieres ganarte unos puntos extra?

Necesitamos transformar este formato de cubos en diferentes formatos.

```
{ 
  'U': ['RBY', 'YWB', 'OGW'],
  'L': ['YRW', 'WOB', 'RWO'],
  'F': ['BRG', 'OGG', 'YOY'],
  'R': ['RYG', 'ORY', 'RBG'],
  'B': ['OWG', 'GBO', 'OWB'],
  'D': ['BYB', 'GYR', 'WRW']
}
```

Elije uno de los siguientes adaptadores, impleméntalo y abre un Pull Request (PR). 

Solo el autor(a) del primer PR aceptado por adaptador ganará los puntos.

Encontrarás ejemplos de los resultados deseados en `cubes/formats/*`

#### Criterios de aceptación
- Pruebas Unitarias
- Correctitud
- Completitud
- Código Limpio
- Seguir el mismo estilo que el resto del código (Opcional pero muy recomendable)
- Transformar e incluir las 30 configuraciones de cubos dentro de la carpeta `cubes` en un folder específico. Por ejemplo `cubes/snake/snake-12.txt,cubes/snake/snake-13.txt, ....` como prueba de su funcionamiento.


### `ToSquare` (3.5 puntos)
```
WWWWWWWWW
OOOOOOOOO
GGGGGGGGG
RRRRRRRRR
BBBBBBBBB
YYYYYYYYY
```
**Opciones:**

`--value_map=["W":"white","O":'orange'..]`
Por defecto es `None`


`--face_order=["U","L","F","R","B","D"]`
Por defecto es U,L,F,R,B,D


`--prepend_face` Si está presente, añade la letra que representa la cara al inicio
```
UWWBWWBWWB
FGGWGGWGGW
RRRRRRRRRR
DYYGYYGYYG
BYBBYBBYBB
LOOOOOOOOO
```

`--fill_with=' '` Si está presente, rellena los valores con el texto de entrada
```
W W B W W B W W B
G G W G G W G G W
R R R R R R R R R
Y Y G Y Y G Y Y G
Y B B Y B B Y B B
O O O O O O O O O
```


`--wrap_with="[]"` Si está presente, envuelve cada fila con el primer y el segundo caracter
```
[azul,amarillo,verde,amarillo,blanco,rojo,naranja,verde,azul]
[azul,blanco,amarillo,verde,rojo,rojo,naranja,verde,azul]
[amarillo,azul,amarillo,blanco,verde,rojo,amarillo,blanco,rojo]
[naranja,azul,blanco,amarillo,rojo,amarillo,naranja,azul,blanco]
[rojo,rojo,verde,azul,amarillo,rojo,blanco,azul,blanco]
[verde,blanco,naranja,amarillo,blanco,azul,naranja,amarillo,verde]
```


### `ToSnake` (4 puntos)
```
www
www
wwo
ooo
ooo
ooo
yyy
yyy
yyy
rrr
rrr
rrr
bbb
bbb
bbb
ggg
ggg
ggg
```
`--face_order=[]` IDEM

`--prepend_face` IDEM

`--sort_by={ face, level }` Son dos posibles valores; face y level.
`Face` obedece al valor de `face_order` y ordena la salida por cada cara.
`Level` ordena por nivel, primero la capa de arriba, luego la primera fila de las caras laterales, luego la segunda, la tercera y por último la cara inferior

```
W W W
W W W
W W W
O O O 
R R R 
G G G 
B B B
O O O 
R R R 
G G G 
B B B
O O O 
R R W 
G G W 
B B B
Y Y Y
Y Y Y
Y Y Y
```


`--add_breakline`
```
555
555
555

333
333
333

111
111
111

666
666
666

444
444
444

222
222
222
```

### Face Dictionary `ToDictionary` (1 punto)
```
{
    "F": [["G", "G", "G"], ["G", "W", "G"], ["G", "G", "G"]],
    "U": [["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]],
    "D": [["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]],
    "B": [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]],
    "L": [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
    "R": [["R", "R", "R"], ["R", "R", "R"], ["R", "R", "R"]]
}
```

### YAML `ToYaml` (1 Punto)
```
up:
    white white white
    white white white
    white white white
front:
    green green green
    green green green
    green green green
left:
    orange orange orange
    orange orange orange
    orange orange yellow
right:
    red red red
    red red red
    red red red
down:
    yellow yellow yellow
    yellow yellow yellow
    yellow yellow yellow
back:
    blue blue blue
    blue blue blue
    blue blue blue
```

### CSV `ToCsv` (1 punto)
```
Up,Front,Left,Right,Down,Back
Y,W,O,G,B,R
Y,W,O,G,B,R
Y,W,O,G,B,R
Y,W,O,G,B,R
Y,W,W,G,B,R
Y,W,O,G,B,R
Y,W,O,G,B,R
Y,W,O,G,B,R
Y,W,O,G,B,R
```

### JSON Start End `ToJsonStartEnd` (1 punto)
```
{
  "start": {
    "w": [
      [
        "b2",
        "b1",
        "b0"
      ],
      [
        "r5",
        "w4",
        "r3"
      ],
      [
        "r8",
        "w1",
        "r6"
      ]
    ],
    "r": [
      [
        "y8",
        "y5",
        "y2"
      ],
      [
        "r7",
        "r4",
        "r1"
      ],
      [
        "y6",
        "y3",
        "y0"
      ]
    ],
    "g": [
      [
        "g8",
        "g5",
        "r2"
      ],
      [
        "g7",
        "g4",
        "w7"
      ],
      [
        "g6",
        "g3",
        "r0"
      ]
    ],
    "o": [
      [
        "w6",
        "o7",
        "w8"
      ],
      [
        "w3",
        "o4",
        "w5"
      ],
      [
        "w0",
        "o1",
        "w2"
      ]
    ],
    "y": [
      [
        "g2",
        "g1",
        "g0"
      ],
      [
        "o5",
        "y4",
        "o3"
      ],
      [
        "o8",
        "y1",
        "o6"
      ]
    ],
    "b": [
      [
        "o0",
        "b3",
        "b6"
      ],
      [
        "y7",
        "b4",
        "b7"
      ],
      [
        "o2",
        "b5",
        "b8"
      ]
    ]
  },
  "end": {
    "w": [
      [
        "w6",
        "w7",
        "w8"
      ],
      [
        "w3",
        "w4",
        "w5"
      ],
      [
        "w0",
        "w1",
        "w2"
      ]
    ],
    "r": [
      [
        "r6",
        "r7",
        "r8"
      ],
      [
        "r3",
        "r4",
        "r5"
      ],
      [
        "r0",
        "r1",
        "r2"
      ]
    ],
    "g": [
      [
        "g6",
        "g7",
        "g8"
      ],
      [
        "g3",
        "g4",
        "g5"
      ],
      [
        "g0",
        "g1",
        "g2"
      ]
    ],
    "o": [
      [
        "o6",
        "o7",
        "o8"
      ],
      [
        "o3",
        "o4",
        "o5"
      ],
      [
        "o0",
        "o1",
        "o2"
      ]
    ],
    "y": [
      [
        "y6",
        "y7",
        "y8"
      ],
      [
        "y3",
        "y4",
        "y5"
      ],
      [
        "y0",
        "y1",
        "y2"
      ]
    ],
    "b": [
      [
        "b6",
        "b7",
        "b8"
      ],
      [
        "b3",
        "b4",
        "b5"
      ],
      [
        "b0",
        "b1",
        "b2"
      ]
    ]
  }
}
```
