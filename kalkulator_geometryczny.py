#!/usr/bin/env python3
"""
Kalkulator Figur Geometrycznych
Profesjonalny kalkulator z wizualizacją figur 2D i 3D
Python 3.12 LTS
"""

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, Wedge
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


class KalkulatorGeometryczny:
    """Główna klasa kalkulatora figur geometrycznych"""
    
    def __init__(self):
        self.history = []
    
    # ============ FIGURY 2D ============
    
    def kwadrat(self, bok):
        """Oblicza pole i obwód kwadratu"""
        if bok <= 0:
            raise ValueError("Bok musi być większy od 0")
        
        pole = bok ** 2
        obwod = 4 * bok
        
        wynik = {
            'figura': 'Kwadrat',
            'bok': bok,
            'pole': pole,
            'obwod': obwod
        }
        self.history.append(wynik)
        return wynik
    
    def prostokat(self, a, b):
        """Oblicza pole i obwód prostokąta"""
        if a <= 0 or b <= 0:
            raise ValueError("Boki muszą być większe od 0")
        
        pole = a * b
        obwod = 2 * (a + b)
        przekatna = math.sqrt(a**2 + b**2)
        
        wynik = {
            'figura': 'Prostokąt',
            'bok_a': a,
            'bok_b': b,
            'pole': pole,
            'obwod': obwod,
            'przekatna': przekatna
        }
        self.history.append(wynik)
        return wynik
    
    def kolo(self, promien):
        """Oblicza pole i obwód koła"""
        if promien <= 0:
            raise ValueError("Promień musi być większy od 0")
        
        pole = math.pi * promien ** 2
        obwod = 2 * math.pi * promien
        
        wynik = {
            'figura': 'Koło',
            'promien': promien,
            'pole': pole,
            'obwod': obwod
        }
        self.history.append(wynik)
        return wynik
    
    def trojkat(self, a, b, c):
        """Oblicza pole i obwód trójkąta (wzór Herona)"""
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Boki muszą być większe od 0")
        
        # Sprawdzenie nierówności trójkąta
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Podane boki nie tworzą trójkąta")
        
        obwod = a + b + c
        s = obwod / 2  # Półobwód
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        wynik = {
            'figura': 'Trójkąt',
            'bok_a': a,
            'bok_b': b,
            'bok_c': c,
            'pole': pole,
            'obwod': obwod
        }
        self.history.append(wynik)
        return wynik
    
    def trapez(self, a, b, h):
        """Oblicza pole trapezu"""
        if a <= 0 or b <= 0 or h <= 0:
            raise ValueError("Wymiary muszą być większe od 0")
        
        pole = ((a + b) * h) / 2
        
        wynik = {
            'figura': 'Trapez',
            'podstawa_a': a,
            'podstawa_b': b,
            'wysokosc': h,
            'pole': pole
        }
        self.history.append(wynik)
        return wynik
    
    def romb(self, bok, wysokosc):
        """Oblicza pole i obwód rombu"""
        if bok <= 0 or wysokosc <= 0:
            raise ValueError("Wymiary muszą być większe od 0")
        
        pole = bok * wysokosc
        obwod = 4 * bok
        
        wynik = {
            'figura': 'Romb',
            'bok': bok,
            'wysokosc': wysokosc,
            'pole': pole,
            'obwod': obwod
        }
        self.history.append(wynik)
        return wynik
    
    # ============ FIGURY 3D ============
    
    def szescian(self, bok):
        """Oblicza objętość i pole powierzchni sześcianu"""
        if bok <= 0:
            raise ValueError("Bok musi być większy od 0")
        
        objetosc = bok ** 3
        pole_powierzchni = 6 * bok ** 2
        
        wynik = {
            'figura': 'Sześcian',
            'bok': bok,
            'objetosc': objetosc,
            'pole_powierzchni': pole_powierzchni
        }
        self.history.append(wynik)
        return wynik
    
    def prostopadloscian(self, a, b, c):
        """Oblicza objętość i pole powierzchni prostopadłościanu"""
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Wymiary muszą być większe od 0")
        
        objetosc = a * b * c
        pole_powierzchni = 2 * (a*b + a*c + b*c)
        przekatna = math.sqrt(a**2 + b**2 + c**2)
        
        wynik = {
            'figura': 'Prostopadłościan',
            'bok_a': a,
            'bok_b': b,
            'bok_c': c,
            'objetosc': objetosc,
            'pole_powierzchni': pole_powierzchni,
            'przekatna': przekatna
        }
        self.history.append(wynik)
        return wynik
    
    def kula(self, promien):
        """Oblicza objętość i pole powierzchni kuli"""
        if promien <= 0:
            raise ValueError("Promień musi być większy od 0")
        
        objetosc = (4/3) * math.pi * promien ** 3
        pole_powierzchni = 4 * math.pi * promien ** 2
        
        wynik = {
            'figura': 'Kula',
            'promien': promien,
            'objetosc': objetosc,
            'pole_powierzchni': pole_powierzchni
        }
        self.history.append(wynik)
        return wynik
    
    def walec(self, promien, wysokosc):
        """Oblicza objętość i pole powierzchni walca"""
        if promien <= 0 or wysokosc <= 0:
            raise ValueError("Wymiary muszą być większe od 0")
        
        objetosc = math.pi * promien ** 2 * wysokosc
        pole_podstawy = math.pi * promien ** 2
        pole_boczne = 2 * math.pi * promien * wysokosc
        pole_powierzchni = 2 * pole_podstawy + pole_boczne
        
        wynik = {
            'figura': 'Walec',
            'promien': promien,
            'wysokosc': wysokosc,
            'objetosc': objetosc,
            'pole_powierzchni': pole_powierzchni
        }
        self.history.append(wynik)
        return wynik
    
    def stozek(self, promien, wysokosc):
        """Oblicza objętość i pole powierzchni stożka"""
        if promien <= 0 or wysokosc <= 0:
            raise ValueError("Wymiary muszą być większe od 0")
        
        objetosc = (1/3) * math.pi * promien ** 2 * wysokosc
        tworzaca = math.sqrt(promien**2 + wysokosc**2)
        pole_podstawy = math.pi * promien ** 2
        pole_boczne = math.pi * promien * tworzaca
        pole_powierzchni = pole_podstawy + pole_boczne
        
        wynik = {
            'figura': 'Stożek',
            'promien': promien,
            'wysokosc': wysokosc,
            'objetosc': objetosc,
            'pole_powierzchni': pole_powierzchni,
            'tworzaca': tworzaca
        }
        self.history.append(wynik)
        return wynik
    
    # ============ WIZUALIZACJA ============
    
    def rysuj_kwadrat(self, bok):
        """Wizualizuje kwadrat"""
        fig, ax = plt.subplots(figsize=(6, 6))
        square = Rectangle((0, 0), bok, bok, fill=False, edgecolor='blue', linewidth=2)
        ax.add_patch(square)
        ax.set_xlim(-1, bok + 1)
        ax.set_ylim(-1, bok + 1)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'Kwadrat - bok: {bok}', fontsize=14, fontweight='bold')
        plt.show()
    
    def rysuj_prostokat(self, a, b):
        """Wizualizuje prostokąt"""
        fig, ax = plt.subplots(figsize=(8, 6))
        rect = Rectangle((0, 0), a, b, fill=False, edgecolor='green', linewidth=2)
        ax.add_patch(rect)
        ax.set_xlim(-1, a + 1)
        ax.set_ylim(-1, b + 1)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'Prostokąt - boki: {a} x {b}', fontsize=14, fontweight='bold')
        plt.show()
    
    def rysuj_kolo(self, promien):
        """Wizualizuje koło"""
        fig, ax = plt.subplots(figsize=(6, 6))
        circle = Circle((0, 0), promien, fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim(-promien - 1, promien + 1)
        ax.set_ylim(-promien - 1, promien + 1)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'Koło - promień: {promien}', fontsize=14, fontweight='bold')
        plt.show()
    
    def rysuj_trojkat(self, a, b, c):
        """Wizualizuje trójkąt"""
        # Obliczanie współrzędnych wierzchołków
        A = (0, 0)
        B = (c, 0)
        # Punkt C obliczany z wzorów
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        sin_A = math.sqrt(1 - cos_A**2)
        C = (b * cos_A, b * sin_A)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        triangle = Polygon([A, B, C], fill=False, edgecolor='purple', linewidth=2)
        ax.add_patch(triangle)
        
        # Dodanie opisów boków
        ax.text(c/2, -0.3, f'c={c}', ha='center', fontsize=10)
        ax.text(C[0]/2 - 0.3, C[1]/2, f'b={b}', ha='center', fontsize=10)
        ax.text((B[0] + C[0])/2 + 0.3, C[1]/2, f'a={a}', ha='center', fontsize=10)
        
        ax.set_xlim(-1, max(c, C[0]) + 1)
        ax.set_ylim(-1, C[1] + 1)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.set_title(f'Trójkąt - boki: {a}, {b}, {c}', fontsize=14, fontweight='bold')
        plt.show()
    
    def rysuj_szescian(self, bok):
        """Wizualizuje sześcian 3D"""
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Wierzchołki sześcianu
        vertices = np.array([
            [0, 0, 0], [bok, 0, 0], [bok, bok, 0], [0, bok, 0],
            [0, 0, bok], [bok, 0, bok], [bok, bok, bok], [0, bok, bok]
        ])
        
        # Ściany sześcianu
        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[0], vertices[3], vertices[7], vertices[4]],
            [vertices[1], vertices[2], vertices[6], vertices[5]]
        ]
        
        poly = Poly3DCollection(faces, alpha=0.3, facecolor='cyan', edgecolor='black', linewidth=2)
        ax.add_collection3d(poly)
        
        ax.set_xlim([0, bok])
        ax.set_ylim([0, bok])
        ax.set_zlim([0, bok])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Sześcian - bok: {bok}', fontsize=14, fontweight='bold')
        plt.show()
    
    def rysuj_kule(self, promien):
        """Wizualizuje kulę 3D"""
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Generowanie punktów sfery
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x = promien * np.outer(np.cos(u), np.sin(v))
        y = promien * np.outer(np.sin(u), np.sin(v))
        z = promien * np.outer(np.ones(np.size(u)), np.cos(v))
        
        ax.plot_surface(x, y, z, alpha=0.7, cmap='viridis')
        
        ax.set_xlim([-promien, promien])
        ax.set_ylim([-promien, promien])
        ax.set_zlim([-promien, promien])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Kula - promień: {promien}', fontsize=14, fontweight='bold')
        plt.show()
    
    def rysuj_walec(self, promien, wysokosc):
        """Wizualizuje walec 3D"""
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Parametry walca
        theta = np.linspace(0, 2 * np.pi, 50)
        z = np.linspace(0, wysokosc, 50)
        theta_grid, z_grid = np.meshgrid(theta, z)
        x_grid = promien * np.cos(theta_grid)
        y_grid = promien * np.sin(theta_grid)
        
        ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.7, cmap='coolwarm')
        
        # Podstawy
        theta_circle = np.linspace(0, 2 * np.pi, 50)
        x_circle = promien * np.cos(theta_circle)
        y_circle = promien * np.sin(theta_circle)
        ax.plot(x_circle, y_circle, 0, 'b-', linewidth=2)
        ax.plot(x_circle, y_circle, wysokosc, 'b-', linewidth=2)
        
        ax.set_xlim([-promien, promien])
        ax.set_ylim([-promien, promien])
        ax.set_zlim([0, wysokosc])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Walec - r: {promien}, h: {wysokosc}', fontsize=14, fontweight='bold')
        plt.show()


def wyswietl_menu():
    """Wyświetla menu główne"""
    print("\n" + "="*60)
    print("🔷 KALKULATOR FIGUR GEOMETRYCZNYCH 🔷")
    print("="*60)
    print("\nFIGURY 2D:")
    print("1. Kwadrat")
    print("2. Prostokąt")
    print("3. Koło")
    print("4. Trójkąt")
    print("5. Trapez")
    print("6. Romb")
    print("\nFIGURY 3D:")
    print("7. Sześcian")
    print("8. Prostopadłościan")
    print("9. Kula")
    print("10. Walec")
    print("11. Stożek")
    print("\nINNE:")
    print("12. Historia obliczeń")
    print("0. Wyjście")
    print("="*60)


def wyswietl_wynik(wynik):
    """Wyświetla wynik obliczeń w czytelny sposób"""
    print("\n" + "-"*60)
    print(f"📊 WYNIK DLA: {wynik['figura']}")
    print("-"*60)
    for klucz, wartosc in wynik.items():
        if klucz != 'figura':
            if isinstance(wartosc, float):
                print(f"{klucz.replace('_', ' ').title()}: {wartosc:.4f}")
            else:
                print(f"{klucz.replace('_', ' ').title()}: {wartosc}")
    print("-"*60)


def main():
    """Główna funkcja programu"""
    kalkulator = KalkulatorGeometryczny()
    
    print("\n🎯 Witaj w Kalkulatorze Figur Geometrycznych!")
    print("Wersja: 1.0 | Python 3.12 LTS")
    
    while True:
        wyswietl_menu()
        
        try:
            wybor = input("\nWybierz opcję (0-12): ").strip()
            
            if wybor == '0':
                print("\n👋 Dziękuję za skorzystanie z kalkulatora! Do zobaczenia!")
                break
            
            elif wybor == '1':  # Kwadrat
                bok = float(input("Podaj długość boku: "))
                wynik = kalkulator.kwadrat(bok)
                wyswietl_wynik(wynik)
                if input("\nCzy pokazać wizualizację? (t/n): ").lower() == 't':
                    kalkulator.rysuj_kwadrat(bok)
            
            elif wybor == '2':  # Prostokąt
                a = float(input("Podaj długość boku a: "))
                b = float(input("Podaj długość boku b: "))
                wynik = kalkulator.prostokat(a, b)
                wyswietl_wynik(wynik)
                if input("\nCzy pokazać wizualizację? (t/n): ").lower() == 't':
                    kalkulator.rysuj_prostokat(a, b)
            
            elif wybor == '3':  # Koło
                promien = float(input("Podaj promień: "))
                wynik = kalkulator.kolo(promien)
                wyswietl_wynik(wynik)
                if input("\nCzy pokazać wizualizację? (t/n): ").lower() == 't':
                    kalkulator.rysuj_kolo(promien)
            
            elif wybor == '4':  # Trójkąt
                a = float(input("Podaj długość boku a: "))
                b = float(input("Podaj długość boku b: "))
                c = float(input("Podaj długość boku c: "))
                wynik = kalkulator.trojkat(a, b, c)
                wyswietl_wynik(wynik)
                if input("\nCzy pokazać wizualizację? (t/n): ").lower() == 't':
                    kalkulator.rysuj_trojkat(a, b, c)
            
            elif wybor == '5':  # Trapez
                a = float(input("Podaj długość podstawy a: "))
                b = float(input("Podaj długość podstawy b: "))
                h = float(input("Podaj wysokość: "))
                wynik = kalkulator.trapez(a, b, h)
                wyswietl_wynik(wynik)
            
            elif wybor == '6':  # Romb
                bok = float(input("Podaj długość boku: "))
                wysokosc = float(input("Podaj wysokość: "))
                wynik = kalkulator.romb(bok, wysokosc)
                wyswietl_wynik(wynik)
            
            elif wybor == '7':  # Sześcian
                bok = float(input("Podaj długość boku: "))
                wynik = kalkulator.szescian(bok)
                wyswietl_wynik(wynik)
                if input("\nCzy pokazać wizualizację 3D? (t/n): ").lower() == 't':
                    kalkulator.rysuj_szescian(bok)
            
            elif wybor == '8':  # Prostopadłościan
                a = float(input("Podaj długość boku a: "))
                b = float(input("Podaj długość boku b: "))
                c = float(input("Podaj długość boku c: "))
                wynik = kalkulator.prostopadloscian(a, b, c)
                wyswietl_wynik(wynik)
            
            elif wybor == '9':  # Kula
                promien = float(input("Podaj promień: "))
                wynik = kalkulator.kula(promien)
                wyswietl_wynik(wynik)
                if input("\nCzy pokazać wizualizację 3D? (t/n): ").lower() == 't':
                    kalkulator.rysuj_kule(promien)
            
            elif wybor == '10':  # Walec
                promien = float(input("Podaj promień: "))
                wysokosc = float(input("Podaj wysokość: "))
                wynik = kalkulator.walec(promien, wysokosc)
                wyswietl_wynik(wynik)
                if input("\nCzy pokazać wizualizację 3D? (t/n): ").lower() == 't':
                    kalkulator.rysuj_walec(promien, wysokosc)
            
            elif wybor == '11':  # Stożek
                promien = float(input("Podaj promień: "))
                wysokosc = float(input("Podaj wysokość: "))
                wynik = kalkulator.stozek(promien, wysokosc)
                wyswietl_wynik(wynik)
            
            elif wybor == '12':  # Historia
                if not kalkulator.history:
                    print("\n📋 Historia jest pusta!")
                else:
                    print("\n📋 HISTORIA OBLICZEŃ:")
                    print("="*60)
                    for i, wynik in enumerate(kalkulator.history, 1):
                        print(f"\n{i}. {wynik['figura']}")
                        for klucz, wartosc in wynik.items():
                            if klucz != 'figura' and isinstance(wartosc, float):
                                print(f"   {klucz}: {wartosc:.4f}")
            
            else:
                print("\n❌ Nieprawidłowy wybór! Wybierz opcję 0-12.")
        
        except ValueError as e:
            print(f"\n❌ Błąd: {e}")
        except Exception as e:
            print(f"\n❌ Wystąpił nieoczekiwany błąd: {e}")
        
        input("\nNaciśnij ENTER, aby kontynuować...")


if __name__ == "__main__":
    main()
