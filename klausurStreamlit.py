import streamlit as st

st.title("Klausur")

st.subheader("Aufgabe 1")

st.code(
    """
# Nehme zwei Werte als Input, die zu einem float gecasted werden.
zahl1 = float(input("Geben Sie eine Zahl ein: "))
zahl2 = float(input("Geben Sie eine zweite Zahl ein: "))

# Mache eine Liste aus den Werte, die sortiert wieder ausgegeben wird.
print(
    "Zahlen von klein nach groß:",
    *sorted([zahl1, zahl2])
)
    """, language="python"
)

zahl1 = st.number_input("Zahl1", value=2)
zahl2 = st.number_input("Zahl2", value=1)

a1Btn = st.button("Aufgabe 1")

if a1Btn:
    st.write(
        "Zahlen von klein nach groß:",
        *sorted([zahl1, zahl2])
    )

st.subheader("Aufgabe 2")

kreditSumme = st.number_input("Kreditsumme in Euro", value=500, min_value=0)
zinsSatz = st.number_input("Zinssatz in Prozent", value=3, min_value=0)
jahre = st.slider("Anzahl der Jahre", value=1, max_value=20)
a2Btn = st.button("Aufgabe 2")

if a2Btn:
    st.text(
    f"""
Kreditsumme nach einem Jahr: {
    round(kreditSumme * ((1 + zinsSatz / 100) ** jahre), 2)
    }€
"""
    )

st.subheader("Aufgabe 3")

st.code(
    """
# Nehme zwei Werte, die jeweils zu ints gecasted werden.
basis = int(input("Basis: "))
exponent = int(input("Exponent: "))

# option a) for-Schleife
# Multipliziere die Basis exponent-mal mit sich selbst. 
myBasisForLoop = 1
for i in range(exponent):
    myBasisForLoop = myBasisForLoop * basis

# option b) while-Schleife
# Hier wird zusätzlich ein counter verwendet, um die Anzahl der Multiplikationen zu ermitteln.
myBasisWhileLoop = 1
counter = exponent
while counter:
    myBasisWhileLoop = myBasisWhileLoop * basis
    counter -= 1
    """
)

basis = st.number_input("Basis", value=2)
exponent = st.number_input("Exponent", value=4)

a3Btn = st.button("Aufgabe 3")

if a3Btn:
    # option a) for-Schleife
    myBasisForLoop = 1
    for i in range(exponent):
        myBasisForLoop = myBasisForLoop * basis

    # option b) while-Schleife
    myBasisWhileLoop = 1
    counter = exponent
    while counter:
        myBasisWhileLoop = myBasisWhileLoop * basis
        counter -= 1

    st.text(f"""
    Basis: {basis}
    Exponent: {exponent}
    Ergebnis for-Schleife: {myBasisForLoop}
    Ergebnis while-Schleife: {myBasisWhileLoop}
    Kontrolle: {basis ** exponent}
        """)


st.subheader("Aufgabe 4")

st.code(
    """
def fibonacci(l):
    k, j = 0, 1 # Definiere die Startwerte k & j

    # Gebe die Startwerte aus
    print(k)
    print(j)

    for i in range(l):
        # Gebe die Summe der Beiden vergangen zahlen aus.
        n = k+j
        print(n)
        # Gleiche anschließend die Startwerte mit den nun vergangen Zahlen an.
        k, j = j, k
        j = n
    """
)

def fibonacci(l):
    k, j = 0, 1
    st.success(k)
    st.success(j)
    for i in range(l):
        n = k+j
        k, j = j, k
        j = n
        st.success(n)

fibonacciLaenge = st.slider("Fibonacci Länge", value=11)
a4Btn = st.button("Aufgabe 4")

if a4Btn:
    fibonacci(fibonacciLaenge)

st.subheader("Aufgabe 5")

st.code(
    """
name = "CSAIPRALKAINACZEYLVOST"

# Gebe jedes 2. Element des strings aus. Fange beim Index 1 an.
print(name[1::2])
    """
)

name = st.text_input(label="Text", value="CSAIPRALKAINACZEYLVOST")

a5Btn = st.button("Aufgabe 5")

if a5Btn:
    st.text(name[1::2])

st.subheader("Aufgabe 6")

st.code(
    """
nameList = ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

# Erstelle eine neue Liste, die alle Namen aus der alten Liste beeinhaltet, die mit A oder mit M anfangen.
print(
    *[name for name in nameList if name[0] in ['A', 'M']]
)
    """
)

nameList = ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria']

customNameList = st.text_area("List der Namen", value=" ".join(nameList))


a6Btn = st.button("Aufgabe 6")

if a6Btn:
    st.write(
        *[name for name in customNameList.split(" ") if name[0] in ['A', 'M']]
    )

st.subheader("Aufabe 7")

st.code(
    """
for i in range(1, 100+1):
    # Überprüfe die Teilbarkeit über Modulo
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")
    
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
    """
)

a7Btn = st.button("Aufgabe 7")

if a7Btn:
    for i in range(1, 100+1):
        if i % 3 == 0 and i % 5 == 0:
            st.success("FizzBuzz")

        elif i % 3 == 0:
            st.success("Fizz")
        
        elif i % 5 == 0:
            st.success("Buzz")

        else:
            st.text(i)

st.subheader("Aufgabe 8 - Weihnachtsbaum")

def weihnachtsBaum(l = 6):
    w = 1 + 2 * (l - 1)

    for i in range(1, l + 1):
        st.text(
            ("*" * (1 + (i - 1) * 2)).center(w, "_") + "\n"
        )

    st.text("frohe Weihnachten")
    st.warning("Im Browser funktioniert der Weihnachtsbaum nur mit einem Füller statt den Leerzeichen. Siehe hierfür jupyter-Notebook")

st.code("""
def weihnachtsBaum(l = 6):
    w = 1 + 2 * (l - 1) # Ermittle die Breite des Baums
    for i in range(1, l + 1): # Schleife über die Länge des Baums
        # Printe eine 'Zeile' des Baums | backslash{n} für Leerzeile + center zum zentrieren. 
        print(
            ("*" * (1 + (i - 1) * 2)).center(w) + "backslash{n}"
        )

# Backslash{} wird hier statt \ verwendet. 
""", language="python")

a8Btn = st.button("Aufgabe 8")

if a8Btn:
    weihnachtsBaum(l=7)
