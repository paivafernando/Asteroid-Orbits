    from asteroid_orbits import Asteroid

    def main():
        asteroid = Asteroid()
        result = asteroid.find_designations(
            year=2010,
            orbit_class="Aten")
        
        print("\n".join(result))

    if __name__ == "__main__": 
        main()