# Generated by Django 2.2.20 on 2023-01-23 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correctness', models.FloatField(default=0)),
                ('visible', models.IntegerField(default=1)),
                ('fixedValue', models.IntegerField(default=0)),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph', models.TextField()),
                ('isCalculatedPos', models.IntegerField(default=0)),
                ('isCalculatingPos', models.IntegerField(default=0)),
                ('multipleChoiceProblem', models.IntegerField(default=1)),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodeIdList', models.TextField(default='')),
                ('edgeIdList', models.TextField(default='')),
                ('studentId', models.TextField()),
                ('correctness', models.FloatField(default=0)),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('nodePositionX', models.IntegerField(default=-1)),
                ('nodePositionY', models.IntegerField(default=-1)),
                ('correctness', models.FloatField(default=0)),
                ('fixedValue', models.IntegerField(default=0)),
                ('visible', models.IntegerField(default=1)),
                ('alreadyCalculatedPos', models.IntegerField(default=0)),
                ('customPos', models.IntegerField(default=0)),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('edge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='knowledgeComponentEdge', to='studentGraph.Edge')),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='knowledgeComponentNode', to='studentGraph.Node')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('visible', models.IntegerField(default=1)),
                ('priority', models.IntegerField(default=0)),
                ('usefulness', models.IntegerField(default=0)),
                ('edge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hintsEdge', to='studentGraph.Edge')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('visible', models.IntegerField(default=1)),
                ('priority', models.IntegerField(default=0)),
                ('usefulness', models.IntegerField(default=0)),
                ('edge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='explanationsEdge', to='studentGraph.Edge')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='ErrorSpecificFeedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('visible', models.IntegerField(default=1)),
                ('priority', models.IntegerField(default=0)),
                ('usefulness', models.IntegerField(default=0)),
                ('edge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='errorSpecificFeedbackEdge', to='studentGraph.Edge')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
        migrations.AddField(
            model_name='edge',
            name='destNode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destNode', to='studentGraph.Node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem'),
        ),
        migrations.AddField(
            model_name='edge',
            name='sourceNode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sourceNode', to='studentGraph.Node'),
        ),
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('edge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubtEdge', to='studentGraph.Edge')),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doubtNode', to='studentGraph.Node')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField()),
                ('dateModified', models.DateTimeField(blank=True, default=None, null=True)),
                ('usefulness', models.IntegerField(default=0)),
                ('doubt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AnswerDoubt', to='studentGraph.Doubt')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentGraph.Problem')),
            ],
        ),
    ]
