from app import create_app
app = create_app('development')
app.run(port=5060)