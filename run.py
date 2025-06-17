from app import create_app

app = create_app()
# nambah komentar
if __name__ == '__main__':
    app.run(debug=True, port=5030)