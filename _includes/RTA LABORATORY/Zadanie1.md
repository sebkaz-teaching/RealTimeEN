Zadanie: 


Write a program on Apache Spark RDD object in spark1.py file: 

1. Read README.md 
2. count how many "spark" words is in file 

Result should contain
```python
print(f"You have {result} elements with ,,spark'' word)
```
Go to console and run 
```bash
spark-submit spark1.py
```



















Napisz program wykorzystujący Apache Spark RDD 
wczytaj plik README.md i policz ile razy wystąpił wyraz "spark" 

w ostatnim wierszu dodaj kod: 
```python
print(f"Masz {result} wierszy z wyrazem spark")
```


uwaga - program powinine zliczać zarówno wyrazy "Spark" jak i "spark"

Kod zapisz do pliku spark1.py a następnie otwórz uruchom polecenie 
```bash
spark-submit spark1.py
```