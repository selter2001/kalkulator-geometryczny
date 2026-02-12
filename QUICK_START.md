# ⚡ QUICK START - MacBook Terminal

Szybki przewodnik uruchomienia kalkulatora na MacBooku

## 🚀 3 kroki do uruchomienia

### Krok 1: Otwórz Terminal
```
Launchpad → Terminal
lub
Cmd + Space → wpisz "Terminal"
```

### Krok 2: Zainstaluj biblioteki
```bash
python3 -m pip install matplotlib numpy
```

### Krok 3: Uruchom kalkulator
```bash
cd ~/Downloads  # lub folder gdzie masz pliki
python3 kalkulator_geometryczny.py
```

## ✅ Gotowe!

---

## 🧪 Opcjonalnie: Uruchom testy

```bash
python3 test_kalkulator.py
```

## 📺 Opcjonalnie: Zobacz demo

```bash
python3 demo.py
```

---

## ❓ Problemy?

### "command not found: python3"
Zainstaluj Pythona:
```bash
brew install python@3.12
```

### "No module named 'matplotlib'"
Zainstaluj biblioteki:
```bash
python3 -m pip install matplotlib numpy
```

### Okna graficzne się nie otwierają
Zainstaluj backend:
```bash
python3 -m pip install PyQt5
```

---

## 📁 Pliki w pakiecie

- `kalkulator_geometryczny.py` - główna aplikacja ⭐
- `test_kalkulator.py` - testy (41 testów)
- `demo.py` - demonstracja funkcji
- `requirements.txt` - lista bibliotek
- `README.md` - pełna dokumentacja
- `RAPORT_TESTOW.md` - raport z testów
- `QUICK_START.md` - ten plik

---

## 💡 Komendy w skrócie

```bash
# Instalacja
python3 -m pip install -r requirements.txt

# Uruchomienie
python3 kalkulator_geometryczny.py

# Testy
python3 test_kalkulator.py

# Demo
python3 demo.py

# Sprawdź wersję Pythona
python3 --version

# Lista zainstalowanych pakietów
python3 -m pip list
```

---

**Python**: 3.12 LTS  
**System**: macOS (działa też na Linux/Windows)  
**Status**: ✅ Przetestowane i zatwierdzone

🎉 **Powodzenia!**
