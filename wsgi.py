

from app import init_app


def create_app():
    return init_app()

dash_app = create_app()
application = dash_app.server
 
if __name__ == '__main__':
    dash_app.run(debug=True, host='0.0.0.0', port=8050)
