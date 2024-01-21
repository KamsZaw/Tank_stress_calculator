import time

start_time =time.time()

def calculate_stresses(pressure, thickness, diameter_cylinder):
    # Stałe materiałowe
    modulus_of_elasticity = 210e3  # MPa, dla przykładu
    poisson_ratio = 0.3  # dla przykładu

    # Promień ścianki cylindra
    radius_cylinder = diameter_cylinder / 2

    # Promień wewnętrzny cylindra
    radius_inner_cylinder = radius_cylinder - thickness

    # Naprężenia w cylindrze
    hoop_stress_cylinder = pressure * radius_cylinder / thickness
    longitudinal_stress_cylinder = pressure * radius_inner_cylinder / thickness

    # Naprężenia w dnie sferycznym wypukłym
    hoop_stress_dome = pressure * radius_inner_cylinder / (2 * thickness)
    longitudinal_stress_dome = pressure * radius_inner_cylinder / (2 * thickness)

    # Naprężenia w dnie sferycznym wklęsłym
    hoop_stress_dome_wkl = - pressure * radius_inner_cylinder / (2 * thickness)
    longitudinal_stress_dome_wkl = - pressure * radius_inner_cylinder / (2 * thickness)

    # Całkowite naprężenie von Mises
    von_mises_stress_cylinder = ((hoop_stress_cylinder - longitudinal_stress_cylinder)**2 +
                                 longitudinal_stress_cylinder**2 + hoop_stress_cylinder**2)**0.5
    von_mises_stress_dome = ((hoop_stress_dome - longitudinal_stress_dome)**2 +
                             longitudinal_stress_dome**2 + hoop_stress_dome**2)**0.5
    von_mises_stress_dome_wkl = ((hoop_stress_dome_wkl - longitudinal_stress_dome_wkl) ** 2 +
                             longitudinal_stress_dome_wkl ** 2 + hoop_stress_dome_wkl ** 2) ** 0.5

    return von_mises_stress_cylinder, von_mises_stress_dome, von_mises_stress_dome_wkl

result_file = f'results.txt'
with open('results.txt', 'w') as file:
    file.write(f'pressure [bar]; thickness [mm]; diameter [mm]; von Mises cylinder [MPa]; von Mises Dome [MPa]; von Mises Dome indent [MPa]\n')

# Zakresy parametrów
pressure_range = list(range(1, 16, 1))  # od 1bar do 15bar z rozdzielczością 1bar
thickness_range = list(range(1,6,1))  # od 1mm do 5mm z rozdzielczością 1mm
diameter_cylinder_range = list(range(15,101,1))# od 15mm do 100mm, z rozdzielczością 1mm

results = []

# Wyświetlenie wyników
for pressure in pressure_range:
    for thickness in thickness_range:
        for diameter_cylinder in diameter_cylinder_range:
            von_mises_stress_cylinder, von_mises_stress_dome, von_mises_stress_dome_wkl = calculate_stresses(pressure, thickness, diameter_cylinder)
            print(f"Pressure: {pressure} bar, Thickness: {thickness} mm, Diameter: {diameter_cylinder} mm")
            print(f"Von Mises Stress in Cylinder: {von_mises_stress_cylinder:.2f} MPa")
            print(f"Von Mises Stress in Dome: {von_mises_stress_dome:.2f} MPa")
            print(f"Von Mises Stress in Dome wkl: {von_mises_stress_dome_wkl:.2f} MPa")
            print("=" * 40)
            results = [pressure, thickness, diameter_cylinder, von_mises_stress_cylinder, von_mises_stress_dome, von_mises_stress_dome_wkl]
            with open('results.txt', 'a') as file:
                file.write(f"{pressure}, {thickness}, {diameter_cylinder}, {von_mises_stress_cylinder}, {von_mises_stress_dome}, {von_mises_stress_dome_wkl}\n")



end_time=time.time()
execution_time = end_time - start_time
print(f"Run time: {execution_time:.4f} sec")

with open('results.txt', 'a') as file:
    file.write(f"Calculation time was {execution_time}\n")


