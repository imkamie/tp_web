# Generated by Django 3.2 on 2021-04-20 09:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210420_0534'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Лайк на ответ',
                'verbose_name_plural': 'Лайки на ответы',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='askmeKamila/static/img/img.png', upload_to='')),
            ],
            options={
                'verbose_name': 'Доп. инфа о пользователе',
                'verbose_name_plural': 'Доп. инфа о пользователях',
            },
        ),
        migrations.CreateModel(
            name='QuestionLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Лайк на вопрос',
                'verbose_name_plural': 'Лайки на вопросы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificator', models.IntegerField(default=0, verbose_name='id пользователя')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('password', models.CharField(default='', max_length=32, verbose_name='Пароль')),
                ('email', models.EmailField(default='', max_length=50, verbose_name='E-mail')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterUniqueTogether(
            name='answerslikes',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='answerslikes',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answerslikes',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='questionsdislikes',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='questionsdislikes',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionsdislikes',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='questionslikes',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='questionslikes',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionslikes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='dislikes',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='correct',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='date_create',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_title',
        ),
        migrations.AddField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(default=False, verbose_name='Правильность'),
        ),
        migrations.AddField(
            model_name='question',
            name='answers_count',
            field=models.IntegerField(default=0, verbose_name='количество ответов'),
        ),
        migrations.AddField(
            model_name='question',
            name='identificator',
            field=models.IntegerField(default=0, verbose_name='id вопроса'),
        ),
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='рейтинг вопроса'),
        ),
        migrations.AddField(
            model_name='tag',
            name='title',
            field=models.TextField(null=True, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_create',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='Заголовок'),
        ),
        migrations.DeleteModel(
            name='AnswersDislikes',
        ),
        migrations.DeleteModel(
            name='AnswersLikes',
        ),
        migrations.DeleteModel(
            name='QuestionsDislikes',
        ),
        migrations.DeleteModel(
            name='QuestionsLikes',
        ),
        migrations.AddField(
            model_name='questionlikes',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='questionlikes',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.question', verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
        migrations.AddField(
            model_name='answerlikes',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.answer', verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='answerlikes',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='Автор'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]