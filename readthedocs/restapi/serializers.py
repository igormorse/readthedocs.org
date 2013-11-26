from rest_framework import serializers

from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        excludes = ['path', 'featured']
        fields = (
        	'id', 
        	'name', 'slug', 'description', 'language',
	    	'repo', 'repo_type',
	    	'default_version', 'default_branch',
	    	'documentation_type',
	    	'num_major', 'num_minor', 'num_point',
	    	'users',
        	)

class SearchIndexSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=500)
    project = serializers.CharField(max_length=500, required=False)
    version = serializers.CharField(max_length=500, required=False)
    page = serializers.CharField(max_length=500, required=False)
