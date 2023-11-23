from rest_framework.views import APIView, Response
from django.forms.models import model_to_dict
from teams.models import Team
from .exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from .utils import data_processing


class TeamsView(APIView):
    def post(self, request):
        data_processing(request.data)
        try:
            team = Team.objects.create(**request.data)
            return Response(model_to_dict(team), 201)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({"error": e.message}, status=400)

    def get(self, request, team_id=None):
        if team_id:
            try: 
                team = Team.objects.get(pk=team_id)
            except Team.DoesNotExist: 
                return Response({"error": "team not found"}, 404)
            team_dict = model_to_dict(team)  
            return Response(team_dict)
        else:
            teams = Team.objects.all()
            team_list = [model_to_dict(team) for team in teams]
            return Response(team_list, 200)

    def patch(self, request, team_id):
        data_processing(request.data)
        try:
            team = Team.objects.get(pk=team_id)
            for key, value in request.data.items():
                setattr(team, key, value)
            team.save()
            return Response(model_to_dict(team), 200)
        except Team.DoesNotExist:
            return Response({"error": "team not found"}, 404)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({"error": e.message}, 400)
    
    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
            team.delete()
            return Response({}, 204)    
        except Team.DoesNotExist:
            return Response({"error": "team not found"}, 404)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as e:
            return Response({"error": e.message}, 400)