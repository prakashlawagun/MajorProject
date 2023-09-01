from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recommendation
from .serializers import RecommendationSerializer
from rest_framework.exceptions import PermissionDenied
import os
import pickle


file_path = os.path.join(os.path.dirname(__file__), '/home/linux/FinalProject/TripManager/recommend/static/recommendation_datas.pkl')
with open(file_path, 'rb') as file:
    recommendation_data = pickle.load(file)

svm_model = recommendation_data['svm_model']
data = recommendation_data['data']
vectorizer = recommendation_data['vectorizer']

def recommend_places_svm(review_text, num_recommendations=7):
    review_vector = vectorizer.transform([review_text])
    probabilities = svm_model.predict_proba(review_vector)[0]
    top_indices = probabilities.argsort()[-num_recommendations:][::-1]
    recommended_names = svm_model.classes_[top_indices]

    # Original data ma corresponding indices of the recommended places lai get gareko
    indices = [data[data['name'] == name].index[0] for name in recommended_names]

    # Extract the relevant information (description, Longitude, Latitude, Address, Link) for the recommended places
    recommended_info = data.loc[indices, ['name', 'description', 'Longitude', 'Latitude', 'Address', 'Link']]

    return recommended_info




class RecommendationAPIView(APIView):
    def post(self, request, format=None):
        user = request.user  # Assuming you're using Token or Session Authentication
        query = request.data.get('query', '')
        num_recommendations = 7
        
        # Call your recommend_places_svm function to get recommendations
        recommended_info = recommend_places_svm(query, num_recommendations)
        
        # Convert the DataFrame to a list of dictionaries
        recommended_list = recommended_info.to_dict(orient='records')
        
        # Create a recommendation entry
        recommendation = Recommendation.objects.create(user=user, query=query, response=recommended_list)

        serializer = RecommendationSerializer(recommendation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, user_id, format=None):
        if request.user.id != user_id:
            raise PermissionDenied("You are not allowed to access this recommendation history.")
        # Get the user's recommendation history
        recommendations = Recommendation.objects.filter(user_id=user_id)
        
        serializer = RecommendationSerializer(recommendations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)