

from app import init_app


def create_app():
    return init_app()

application = create_app()

 
if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=8050)
