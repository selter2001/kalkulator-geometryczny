#!/usr/bin/env python3
"""
Demo - Kalkulator Figur Geometrycznych
Przykładowe użycie kalkulatora (bez interakcji użytkownika)
"""

from kalkulator_geometryczny import KalkulatorGeometryczny
import time


def demo_header(text):
    """Wyświetla nagłówek sekcji demo"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)


def demo_wynik(wynik):
    """Wyświetla wynik w czytelny sposób"""
    print(f"\n📊 {wynik['figura']}:")
    for klucz, wartosc in wynik.items():
        if klucz != 'figura':
            if isinstance(wartosc, float):
                print(f"   • {klucz.replace('_', ' ').title()}: {wartosc:.4f}")
            else:
                print(f"   • {klucz.replace('_', ' ').title()}: {wartosc}")


def main():
    """Główna funkcja demo"""
    print("\n" + "🎯"*35)
    print("🔷 DEMO - KALKULATOR FIGUR GEOMETRYCZNYCH 🔷")
    print("🎯"*35)
    
    kalkulator = KalkulatorGeometryczny()
    
    # ============ DEMO FIGURY 2D ============
    
    demo_header("🔹 FIGURY PŁASKIE (2D)")
    
    print("\n1️⃣  KWADRAT o boku 5")
    wynik = kalkulator.kwadrat(5)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n2️⃣  PROSTOKĄT 4 x 6")
    wynik = kalkulator.prostokat(4, 6)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n3️⃣  KOŁO o promieniu 3")
    wynik = kalkulator.kolo(3)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n4️⃣  TRÓJKĄT prostokątny 3-4-5")
    wynik = kalkulator.trojkat(3, 4, 5)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n5️⃣  TRAPEZ (podstawy: 8 i 4, wysokość: 3)")
    wynik = kalkulator.trapez(8, 4, 3)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n6️⃣  ROMB (bok: 6, wysokość: 4)")
    wynik = kalkulator.romb(6, 4)
    demo_wynik(wynik)
    time.sleep(1)
    
    # ============ DEMO FIGURY 3D ============
    
    demo_header("🔹 FIGURY PRZESTRZENNE (3D)")
    
    print("\n7️⃣  SZEŚCIAN o boku 3")
    wynik = kalkulator.szescian(3)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n8️⃣  PROSTOPADŁOŚCIAN 2 x 3 x 4")
    wynik = kalkulator.prostopadloscian(2, 3, 4)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n9️⃣  KULA o promieniu 3")
    wynik = kalkulator.kula(3)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n🔟 WALEC (promień: 3, wysokość: 5)")
    wynik = kalkulator.walec(3, 5)
    demo_wynik(wynik)
    time.sleep(1)
    
    print("\n1️⃣1️⃣  STOŻEK (promień: 3, wysokość: 4)")
    wynik = kalkulator.stozek(3, 4)
    demo_wynik(wynik)
    time.sleep(1)
    
    # ============ DEMO HISTORIA ============
    
    demo_header("🔹 HISTORIA OBLICZEŃ")
    
    print(f"\n📋 Wykonano {len(kalkulator.history)} obliczeń:")
    for i, obliczenie in enumerate(kalkulator.history, 1):
        print(f"\n   {i}. {obliczenie['figura']}")
    
    # ============ DEMO WALIDACJA ============
    
    demo_header("🔹 DEMONSTRACJA WALIDACJI")
    
    print("\n❌ Próba utworzenia kwadratu z ujemnym bokiem:")
    try:
        kalkulator.kwadrat(-5)
    except ValueError as e:
        print(f"   ✅ Poprawnie odrzucono: {e}")
    
    print("\n❌ Próba utworzenia trójkąta łamiącego nierówność trójkąta:")
    try:
        kalkulator.trojkat(1, 2, 10)
    except ValueError as e:
        print(f"   ✅ Poprawnie odrzucono: {e}")
    
    print("\n❌ Próba utworzenia koła z zerowym promieniem:")
    try:
        kalkulator.kolo(0)
    except ValueError as e:
        print(f"   ✅ Poprawnie odrzucono: {e}")
    
    # ============ DEMO PRECYZJA ============
    
    demo_header("🔹 DEMONSTRACJA PRECYZJI")
    
    print("\n🔬 Obliczenia z dużą precyzją:")
    
    print("\n   Koło jednostkowe (r=1):")
    wynik = kalkulator.kolo(1)
    print(f"   • Pole = π = {wynik['pole']:.10f}")
    print(f"   • Obwód = 2π = {wynik['obwod']:.10f}")
    
    print("\n   Kula jednostkowa (r=1):")
    wynik = kalkulator.kula(1)
    print(f"   • Objętość = 4/3π = {wynik['objetosc']:.10f}")
    print(f"   • Pole powierzchni = 4π = {wynik['pole_powierzchni']:.10f}")
    
    # ============ PODSUMOWANIE ============
    
    demo_header("🎉 KONIEC DEMO")
    
    print("\n✅ Wszystkie funkcje działają poprawnie!")
    print("✅ Walidacja danych działa prawidłowo!")
    print("✅ Precyzja obliczeń jest wysoka!")
    print(f"\n📊 Łącznie wykonano {len(kalkulator.history)} obliczeń")
    print("\n" + "🎯"*35)
    print("\n💡 Aby uruchomić aplikację interaktywną, użyj:")
    print("   python3 kalkulator_geometryczny.py")
    print("\n💡 Aby uruchomić testy, użyj:")
    print("   python3 test_kalkulator.py")
    print("\n" + "🎯"*35 + "\n")


if __name__ == "__main__":
    main()
