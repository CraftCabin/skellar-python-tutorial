from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables or a config file
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        DATABASE='path_to_your_database',
    )

    # Register blueprints for API endpoints
    from .api.mission_endpoints import mission_bp
    from .api.validation_endpoints import validation_bp

    app.register_blueprint(mission_bp)
    app.register_blueprint(validation_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)