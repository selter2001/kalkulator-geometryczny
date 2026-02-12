#!/usr/bin/env python3
"""
Test Suite - Kalkulator Figur Geometrycznych
Testy jednostkowe i integracyjne
"""

import unittest
import math
import sys
from kalkulator_geometryczny import KalkulatorGeometryczny


class TestFigury2D(unittest.TestCase):
    """Testy dla figur płaskich (2D)"""
    
    def setUp(self):
        """Przygotowanie przed każdym testem"""
        self.kalkulator = KalkulatorGeometryczny()
    
    def test_kwadrat_podstawowy(self):
        """Test podstawowych obliczeń dla kwadratu"""
        wynik = self.kalkulator.kwadrat(5)
        self.assertEqual(wynik['pole'], 25)
        self.assertEqual(wynik['obwod'], 20)
        self.assertEqual(wynik['figura'], 'Kwadrat')
    
    def test_kwadrat_dziesietny(self):
        """Test kwadratu z liczbami dziesiętnymi"""
        wynik = self.kalkulator.kwadrat(3.5)
        self.assertAlmostEqual(wynik['pole'], 12.25, places=2)
        self.assertAlmostEqual(wynik['obwod'], 14.0, places=2)
    
    def test_kwadrat_walidacja(self):
        """Test walidacji danych wejściowych dla kwadratu"""
        with self.assertRaises(ValueError):
            self.kalkulator.kwadrat(0)
        with self.assertRaises(ValueError):
            self.kalkulator.kwadrat(-5)
    
    def test_prostokat_podstawowy(self):
        """Test podstawowych obliczeń dla prostokąta"""
        wynik = self.kalkulator.prostokat(4, 6)
        self.assertEqual(wynik['pole'], 24)
        self.assertEqual(wynik['obwod'], 20)
        self.assertAlmostEqual(wynik['przekatna'], 7.211, places=3)
    
    def test_prostokat_kwadrat(self):
        """Test prostokąta ze wszystkimi bokami równymi (kwadrat)"""
        wynik = self.kalkulator.prostokat(5, 5)
        self.assertEqual(wynik['pole'], 25)
        self.assertEqual(wynik['obwod'], 20)
    
    def test_prostokat_walidacja(self):
        """Test walidacji dla prostokąta"""
        with self.assertRaises(ValueError):
            self.kalkulator.prostokat(0, 5)
        with self.assertRaises(ValueError):
            self.kalkulator.prostokat(5, -3)
    
    def test_kolo_podstawowe(self):
        """Test podstawowych obliczeń dla koła"""
        wynik = self.kalkulator.kolo(3)
        self.assertAlmostEqual(wynik['pole'], 28.274, places=3)
        self.assertAlmostEqual(wynik['obwod'], 18.850, places=3)
    
    def test_kolo_jednostkowe(self):
        """Test koła o promieniu 1"""
        wynik = self.kalkulator.kolo(1)
        self.assertAlmostEqual(wynik['pole'], math.pi, places=5)
        self.assertAlmostEqual(wynik['obwod'], 2 * math.pi, places=5)
    
    def test_kolo_walidacja(self):
        """Test walidacji dla koła"""
        with self.assertRaises(ValueError):
            self.kalkulator.kolo(0)
        with self.assertRaises(ValueError):
            self.kalkulator.kolo(-2)
    
    def test_trojkat_rownoboczny(self):
        """Test trójkąta równobocznego"""
        wynik = self.kalkulator.trojkat(5, 5, 5)
        self.assertEqual(wynik['obwod'], 15)
        self.assertAlmostEqual(wynik['pole'], 10.825, places=3)
    
    def test_trojkat_prostokatny(self):
        """Test trójkąta prostokątnego (3-4-5)"""
        wynik = self.kalkulator.trojkat(3, 4, 5)
        self.assertEqual(wynik['obwod'], 12)
        self.assertAlmostEqual(wynik['pole'], 6.0, places=1)
    
    def test_trojkat_walidacja_nierownosc(self):
        """Test nierówności trójkąta"""
        with self.assertRaises(ValueError):
            self.kalkulator.trojkat(1, 2, 10)  # Nie tworzy trójkąta
        with self.assertRaises(ValueError):
            self.kalkulator.trojkat(0, 5, 5)
    
    def test_trapez_podstawowy(self):
        """Test podstawowych obliczeń dla trapezu"""
        wynik = self.kalkulator.trapez(5, 3, 4)
        self.assertEqual(wynik['pole'], 16.0)
    
    def test_trapez_rownoramennyy(self):
        """Test trapezu równoramiennego"""
        wynik = self.kalkulator.trapez(8, 4, 3)
        self.assertEqual(wynik['pole'], 18.0)
    
    def test_trapez_walidacja(self):
        """Test walidacji dla trapezu"""
        with self.assertRaises(ValueError):
            self.kalkulator.trapez(0, 5, 3)
        with self.assertRaises(ValueError):
            self.kalkulator.trapez(5, -2, 3)
    
    def test_romb_podstawowy(self):
        """Test podstawowych obliczeń dla rombu"""
        wynik = self.kalkulator.romb(6, 4)
        self.assertEqual(wynik['pole'], 24)
        self.assertEqual(wynik['obwod'], 24)
    
    def test_romb_walidacja(self):
        """Test walidacji dla rombu"""
        with self.assertRaises(ValueError):
            self.kalkulator.romb(0, 5)
        with self.assertRaises(ValueError):
            self.kalkulator.romb(5, -3)


class TestFigury3D(unittest.TestCase):
    """Testy dla figur przestrzennych (3D)"""
    
    def setUp(self):
        """Przygotowanie przed każdym testem"""
        self.kalkulator = KalkulatorGeometryczny()
    
    def test_szescian_podstawowy(self):
        """Test podstawowych obliczeń dla sześcianu"""
        wynik = self.kalkulator.szescian(3)
        self.assertEqual(wynik['objetosc'], 27)
        self.assertEqual(wynik['pole_powierzchni'], 54)
    
    def test_szescian_jednostkowy(self):
        """Test sześcianu jednostkowego"""
        wynik = self.kalkulator.szescian(1)
        self.assertEqual(wynik['objetosc'], 1)
        self.assertEqual(wynik['pole_powierzchni'], 6)
    
    def test_szescian_walidacja(self):
        """Test walidacji dla sześcianu"""
        with self.assertRaises(ValueError):
            self.kalkulator.szescian(0)
        with self.assertRaises(ValueError):
            self.kalkulator.szescian(-4)
    
    def test_prostopadloscian_podstawowy(self):
        """Test podstawowych obliczeń dla prostopadłościanu"""
        wynik = self.kalkulator.prostopadloscian(2, 3, 4)
        self.assertEqual(wynik['objetosc'], 24)
        self.assertEqual(wynik['pole_powierzchni'], 52)
        self.assertAlmostEqual(wynik['przekatna'], 5.385, places=3)
    
    def test_prostopadloscian_szescian(self):
        """Test prostopadłościanu o wszystkich równych bokach (sześcian)"""
        wynik = self.kalkulator.prostopadloscian(5, 5, 5)
        self.assertEqual(wynik['objetosc'], 125)
        self.assertEqual(wynik['pole_powierzchni'], 150)
    
    def test_prostopadloscian_walidacja(self):
        """Test walidacji dla prostopadłościanu"""
        with self.assertRaises(ValueError):
            self.kalkulator.prostopadloscian(0, 3, 4)
        with self.assertRaises(ValueError):
            self.kalkulator.prostopadloscian(2, -3, 4)
    
    def test_kula_podstawowa(self):
        """Test podstawowych obliczeń dla kuli"""
        wynik = self.kalkulator.kula(3)
        self.assertAlmostEqual(wynik['objetosc'], 113.097, places=3)
        self.assertAlmostEqual(wynik['pole_powierzchni'], 113.097, places=3)
    
    def test_kula_jednostkowa(self):
        """Test kuli o promieniu 1"""
        wynik = self.kalkulator.kula(1)
        self.assertAlmostEqual(wynik['objetosc'], (4/3) * math.pi, places=5)
        self.assertAlmostEqual(wynik['pole_powierzchni'], 4 * math.pi, places=5)
    
    def test_kula_walidacja(self):
        """Test walidacji dla kuli"""
        with self.assertRaises(ValueError):
            self.kalkulator.kula(0)
        with self.assertRaises(ValueError):
            self.kalkulator.kula(-3)
    
    def test_walec_podstawowy(self):
        """Test podstawowych obliczeń dla walca"""
        wynik = self.kalkulator.walec(3, 5)
        self.assertAlmostEqual(wynik['objetosc'], 141.372, places=3)
        self.assertAlmostEqual(wynik['pole_powierzchni'], 150.796, places=3)
    
    def test_walec_niski(self):
        """Test walca o małej wysokości"""
        wynik = self.kalkulator.walec(5, 1)
        self.assertAlmostEqual(wynik['objetosc'], 78.540, places=3)
    
    def test_walec_walidacja(self):
        """Test walidacji dla walca"""
        with self.assertRaises(ValueError):
            self.kalkulator.walec(0, 5)
        with self.assertRaises(ValueError):
            self.kalkulator.walec(3, -2)
    
    def test_stozek_podstawowy(self):
        """Test podstawowych obliczeń dla stożka"""
        wynik = self.kalkulator.stozek(3, 4)
        self.assertAlmostEqual(wynik['objetosc'], 37.699, places=3)
        self.assertAlmostEqual(wynik['tworzaca'], 5.0, places=1)
    
    def test_stozek_wysoki(self):
        """Test stożka o dużej wysokości"""
        wynik = self.kalkulator.stozek(2, 10)
        self.assertAlmostEqual(wynik['objetosc'], 41.888, places=3)
    
    def test_stozek_walidacja(self):
        """Test walidacji dla stożka"""
        with self.assertRaises(ValueError):
            self.kalkulator.stozek(0, 5)
        with self.assertRaises(ValueError):
            self.kalkulator.stozek(3, -4)


class TestHistoria(unittest.TestCase):
    """Testy funkcji historii obliczeń"""
    
    def setUp(self):
        """Przygotowanie przed każdym testem"""
        self.kalkulator = KalkulatorGeometryczny()
    
    def test_historia_pusta(self):
        """Test pustej historii"""
        self.assertEqual(len(self.kalkulator.history), 0)
    
    def test_historia_dodawanie(self):
        """Test dodawania do historii"""
        self.kalkulator.kwadrat(5)
        self.kalkulator.kolo(3)
        self.assertEqual(len(self.kalkulator.history), 2)
    
    def test_historia_zawartosc(self):
        """Test zawartości historii"""
        self.kalkulator.kwadrat(5)
        self.assertEqual(self.kalkulator.history[0]['figura'], 'Kwadrat')
        self.assertEqual(self.kalkulator.history[0]['bok'], 5)


class TestPrecyzja(unittest.TestCase):
    """Testy precyzji obliczeń"""
    
    def setUp(self):
        """Przygotowanie przed każdym testem"""
        self.kalkulator = KalkulatorGeometryczny()
    
    def test_duze_liczby(self):
        """Test obliczeń z dużymi liczbami"""
        wynik = self.kalkulator.kwadrat(1000)
        self.assertEqual(wynik['pole'], 1000000)
    
    def test_male_liczby(self):
        """Test obliczeń z małymi liczbami"""
        wynik = self.kalkulator.kwadrat(0.01)
        self.assertAlmostEqual(wynik['pole'], 0.0001, places=6)
    
    def test_liczby_irracjonalne(self):
        """Test z liczbami irracjonalnymi"""
        wynik = self.kalkulator.kolo(1)
        self.assertAlmostEqual(wynik['obwod'], 2 * math.pi, places=10)


class TestEdgeCases(unittest.TestCase):
    """Testy przypadków brzegowych"""
    
    def setUp(self):
        """Przygotowanie przed każdym testem"""
        self.kalkulator = KalkulatorGeometryczny()
    
    def test_bardzo_mala_liczba(self):
        """Test z bardzo małą liczbą"""
        wynik = self.kalkulator.kwadrat(0.000001)
        self.assertGreater(wynik['pole'], 0)
    
    def test_bardzo_duza_liczba(self):
        """Test z bardzo dużą liczbą"""
        wynik = self.kalkulator.szescian(1000000)
        self.assertEqual(wynik['objetosc'], 1000000**3)
    
    def test_trojkat_prawie_zdegenerowany(self):
        """Test trójkąta prawie zdegenerowanego"""
        wynik = self.kalkulator.trojkat(5, 5, 9.9)
        self.assertGreater(wynik['pole'], 0)


def uruchom_testy():
    """Funkcja uruchamiająca wszystkie testy"""
    print("\n" + "="*70)
    print("🧪 ROZPOCZYNAM TESTY KALKULATORA GEOMETRYCZNEGO")
    print("="*70 + "\n")
    
    # Utworzenie zestawu testów
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Dodanie wszystkich testów
    suite.addTests(loader.loadTestsFromTestCase(TestFigury2D))
    suite.addTests(loader.loadTestsFromTestCase(TestFigury3D))
    suite.addTests(loader.loadTestsFromTestCase(TestHistoria))
    suite.addTests(loader.loadTestsFromTestCase(TestPrecyzja))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Uruchomienie testów
    runner = unittest.TextTestRunner(verbosity=2)
    wynik = runner.run(suite)
    
    # Podsumowanie
    print("\n" + "="*70)
    print("📊 PODSUMOWANIE TESTÓW")
    print("="*70)
    print(f"✅ Testy zaliczone: {wynik.testsRun - len(wynik.failures) - len(wynik.errors)}")
    print(f"❌ Testy niezaliczone: {len(wynik.failures)}")
    print(f"⚠️  Błędy: {len(wynik.errors)}")
    print(f"📈 Wszystkich testów: {wynik.testsRun}")
    
    if wynik.wasSuccessful():
        print("\n🎉 WSZYSTKIE TESTY PRZESZŁY POMYŚLNIE!")
        print("✅ Aplikacja jest gotowa do użycia!")
    else:
        print("\n⚠️  NIEKTÓRE TESTY NIE PRZESZŁY!")
        print("❌ Aplikacja wymaga poprawek przed wydaniem!")
    
    print("="*70 + "\n")
    
    return wynik.wasSuccessful()


if __name__ == "__main__":
    sukces = uruchom_testy()
    sys.exit(0 if sukces else 1)
