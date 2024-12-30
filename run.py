from app import create_app

# Kreiraj aplikaciju koristeći create_app funkciju
app = create_app()

if __name__ == '__main__':
    # Pokreni aplikaciju
    app.run(debug=True)
