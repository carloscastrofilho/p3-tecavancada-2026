from flask import Blueprint
from src.controllers.user_controller import UserController

class UserRoutes:
    @staticmethod
    def get_blueprint() -> Blueprint:
        # Cria o blueprint exclusivo do módulo
        bp = Blueprint('users', __name__, url_prefix='/users')
        
        # Mapeia as views
        router_view = UserController.as_view('user_api')
        
        # Rotas da coleção
        bp.add_url_rule(
            '', 
            view_func=router_view, 
            methods=['GET', 'POST']
        )
        
        # Rotas do item por ID
        bp.add_url_rule(
            '/<int:id>', 
            view_func=router_view, 
            methods=['GET', 'PUT', 'DELETE']
        )
        
        # Rotas do item por ID
        bp.add_url_rule(
                    '/login/<string:login>', 
                    view_func=router_view, 
                    methods=['GET']
                )
        
        return bp