from config import app
from controllers.auth_controller import auth_bp
from controllers.episode_controller import episodes_bp
from controllers.guest_controller import guests_bp
from controllers.appearance_controller import appearances_bp
from controllers.main_controller import main_bp 

app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(episodes_bp, url_prefix='/episodes')
app.register_blueprint(guests_bp, url_prefix='/guests')
app.register_blueprint(appearances_bp, url_prefix='/appearances')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
