from django.shortcuts import render

class TeamsView(APIView):
    def post(self, request):
        team = Team.objects.create(**request.data)
        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()
        team_list = [model_to_dict(team) for team in teams]
        return Response(team_list, 200)

    def put(self, request):
        team_id = request.data.get('id')
        team = Team.objects.get(id=team_id)
        team.name = request.data.get('name')
        team.save()
        return Response({'msg': 'Team updated successfully!'})

    def delete(self, request):
        team_id = request.data.get('id')
        team = Team.objects.get(id=team_id)
        team.delete()
        return Response({'msg': 'Team deleted successfully!'})