from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from config import config
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
login_manager = LoginManager()                  # 创建登陆管理
login_manager.session_protection = "strong"     # 设定保护等级
login_manager.login_view = "main.login_menu"    # 添加登陆界面，放在view层
db = MongoEngine()

def create_app(config_name):#创建APP
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 获取CONFIG
    config[config_name].init_app(app)            # 初始化APP设置
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)                  # 初始化登陆管理
    db.init_app(app)                             # 初始化数据库
    # attach routes and custom error pages here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)       # 初始化蓝图
    return app
