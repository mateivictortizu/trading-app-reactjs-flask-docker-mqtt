from flask import Blueprint, request, session

from app import before_request_function
from app.RabbitMQProcessor.RecommendationRabbitMQProcessor import recommendation_processor
from app.blueprints import recommendation_client, users_connections

recommendations = Blueprint('recommentation', __name__)


@recommendations.route('/recommendation', methods=['GET'])
def recommendation_system():
    before_checking_result = before_request_function(request)
    if before_checking_result[1] == 403:
        return before_checking_result
    return recommendation_processor(recommendation_client, {'user': 'matteovkt@gmail.com'})
