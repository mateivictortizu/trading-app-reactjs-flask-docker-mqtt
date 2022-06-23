import json

from flask import jsonify

from app.RabbitMQClients.RecommendationRabbitMQ import RecommendationClient


def recommendation_processor(recommendation_client, json_body):
    if recommendation_client is None:
        recommendation_client = RecommendationClient()
    try:
        response = json.loads(recommendation_client.call(json_body))
        return response, response['code']
    except Exception:
        try:
            recommendation_client = RecommendationClient()
            response = json.loads(recommendation_client.call(json_body))
            return response, response['code']
        except Exception:
            return jsonify({'error': 'Recommendation server error', 'code': 500}), 500
