from flask import Blueprint, jsonify, make_response, request

from app.models.departamento import Departamento
from app.database import db_session


class DepartamentoController:

    departamento = Blueprint('departamento', __name__, url_prefix='/departamentos')

    @departamento.route('/', methods=["GET"])
    def obter_todos_departamentos():
        """Rota para obter todos os departamentos"""

        lista_departamentos = []

        departamentos = Departamento.query.all()

        for d in departamentos:
            lista_departamentos.append({
                "id": d.id_departamento,
                "nome": d.nome_departamento,
                "descricao": d.descricao
            })

        resposta = make_response(jsonify(lista_departamentos))
        resposta.headers['Content-Type'] = 'application/json'

        return resposta

    @departamento.route('/<int:id_departamento>', methods=["GET"])
    def obter_departamento_por_id(id_departamento):
        """Rota para obter um departamento por ID"""

        departamento = Departamento.query.get(id_departamento)

        if departamento:
            resposta = make_response(jsonify({
                "id": departamento.id_departamento,
                "nome": departamento.nome_departamento,
                "descricao": departamento.descricao
            }))

            resposta.headers['Content-Type'] = 'application/json'

            return resposta
        else:
            return make_response(jsonify({
                'message': 'Departamento não encontrado'
            }), 404)

    @departamento.route('/', methods=["POST"])
    def adicionar_departamento():
        """Rota para adicionar um novo departamento"""
        dados = request.get_json()

        novo_departamento = Departamento(
            nome=dados.get('nome_departamento'),
            descricao=dados.get('descricao')
        )

        db_session.add(novo_departamento)
        db_session.commit()

        resposta = make_response(jsonify({'message': 'Departamento criado com sucesso', 'id_departamento': novo_departamento.id_departamento}))
        resposta.headers['Content-Type'] = 'application/json'

        return resposta

    @departamento.route('<int:id_departamento>', methods=["PUT"])
    def atualizar_departamento(id_departamento):
        """Rota para atualizar um departamento existente"""
        dados = request.get_json()
        departamento = Departamento.query.get(id_departamento)

        if departamento:

            if dados.get('nome_departamento'):
                departamento.nome_departamento = dados.get('nome_departamento')

            if dados.get('descricao'):
                departamento.descricao = dados.get('descricao')

            db_session.commit()

            return make_response(jsonify({'message': 'Departamento atualizado com sucesso'}))
        else:
            return make_response(jsonify({'message': 'Departamento não encontrado'}), 404)

    @departamento.route('<int:id_departamento>', methods=["DELETE"])
    def excluir_departamento(id_departamento):
        """Rota para excluir um departamento"""
        departamento = Departamento.query.get(id_departamento)

        if departamento:
            db_session.delete(departamento)
            db_session.commit()
            return make_response(jsonify({'message': 'Departamento excluído com sucesso'}))
        else:
            return make_response(jsonify({'message': 'Departamento não encontrado'}), 404)
