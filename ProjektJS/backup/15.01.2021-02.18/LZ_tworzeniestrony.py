import webbrowser

l = input("Podaj początek nazwy pliu aż do _wynik.txt: ")
z = l+"_wyniki.txt"
n = l+"_statystyka.txt"
name=l+"_zaprzyjaznione.html"
f = open(name,'w')
table=" "
i=0

#Generowanie tabeli
try:
    plik = open(z)
    for line in plik:
        if(i%2==0):
            table += """<tr>"""
        table+="""<td>"""+line
        i+=1
except IOError:
    print("Błąd otwarcia pliku!")
    exit()

#Wczytywanie statystyk
try:
    stat = open(n)
    statystyka="""<h4>"""
    for line in stat:
        statystyka+=line+"""<br>"""
    statystyka+="""</h4>"""
except IOError:
    print("Błąd otwarcia pliku!")
    exit()

#Budowa strony
ttop="""
<table>
   <thead>
      <tr> <th> Czy liczby są zaprzyjaźnione? <th> Skąd? 
   <tbody>
"""

top = """
<html>
<center>
<style>
body {background-color: CC99FF;}
h1 {padding: 30px;padding-bottom: 40px;}
th, td, table {border: 1px solid black}
th{width: 33%;}
table{background-color:#CC66FF; margin-bottom:15px;}
thead tr, thead th{border: 3px solid black; font-size: 20px;background-color:#9900CC; witdh: 33%;}
td {border-left: 3px solid black;}
table {width: 70%; border-collapse: collapse; text-align: center; border: 3px solid black}
h3 {text-align:center; margin-top: 50px; font-size: 25px}
h4 {text-align:center; font-weight: normal; font-size: 25px}
</style>
<head><h1>PROGRAM LICZB ZAPRZYJAŹNIONYCH - WYNIKI </h1></head>
<body>
"""

tend = """
</table>
"""

bottom = """
<h3>This website was brought to you by Natalia Szalas.</h3.	
</body>
</center>
</html>
"""

#Generowanie całości
f.write(top+ttop+table+tend+statystyka+bottom)
f.close()
