from flask import request, jsonify
from flask.views import MethodView
from src.repositories.user_repository import UserRepository
from src.models.user_model import User

class UserController(MethodView):
    def __init__(self):
        self.repository = UserRepository()
        self.model = User

    def get(self, id=None, login=None):
        
        if login:
            response = self.repository.get_by_Login(login)
            if not response:
                return jsonify({"error": "Registro não encontrado"}), 404
            return jsonify(response.to_dict()), 200    
        
        if id :
            response = self.repository.get_by_id(id)
            if not response:
               return jsonify({"error": "Registro não encontrado"}), 404
            return jsonify(response.to_dict()), 200    
            
        responseData = self.repository.get_all()
        return jsonify([e.to_dict() for e in responseData]), 200
        
        

    def post(self):
        
        data = request.get_json()        
        if not data or 'login' not in data or 'password' not in data:
            return jsonify({"error": "Dados inválidos"}), 400

        new_record = self.model.from_dict(data)
        novo_id = self.repository.create(new_record)
        new_record.id = novo_id
        return jsonify(new_record.to_dict()), 201

    def put(self, id):
        data = request.get_json()
        dataRecord = self.model.from_dict(data)
        updated = self.repository.update(id, dataRecord)
        if not updated:
            return jsonify({"error": "Registro não encontrado"}), 404
        return jsonify({"message": "Registro atualizado com sucesso"}), 200

    def delete(self, id):
        deleted = self.repository.delete(id)
        if not deleted:
            return jsonify({"error": "Registro não encontrado"}), 404
        return jsonify({"message": "Registro removido com sucesso"}), 200