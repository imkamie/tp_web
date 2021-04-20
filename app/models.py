from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
  avatar = models.ImageField(default='askmeKamila/static/img/img.png')

  class Meta:
    verbose_name = 'Доп. инфа о пользователе'
    verbose_name_plural = 'Доп. инфа о пользователях'


class User(models.Model):
  identificator = models.IntegerField(verbose_name='id пользователя', default=0)
  name = models.CharField(max_length=50, default='', verbose_name='Имя')
  password = models.CharField(max_length=32, default='', verbose_name='Пароль')
  email = models.EmailField(max_length=50, default='', verbose_name='E-mail')
  author = models.OneToOneField(Author, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'


class Tag(models.Model):
  title = models.TextField(null=True, verbose_name='Тег')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'


class QuestionManager(models.Manager):
  def hot_questions(self):
    return self.order_by('-rating')

  def new_questions(self):
    return self.order_by('-date_create')

  def questions_by_tag(self, tag):
    return self.filter(tags__title=tag)

  class Meta:
    verbose_name = 'User'


class Question(models.Model):
  identificator = models.IntegerField(verbose_name='id вопроса', default=0)
  rating = models.IntegerField(default=0, verbose_name='рейтинг вопроса')
  answers_count = models.IntegerField(default=0, verbose_name='количество ответов')
  title = models.CharField(max_length=1024, verbose_name='Заголовок')
  text = models.TextField(verbose_name='Текст')
  date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag)
  objects = QuestionManager()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Вопрос'
    verbose_name_plural = 'Вопросы'


class Answer(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
  question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
  rating = models.IntegerField(default=0)
  created_date = models.DateTimeField(default=timezone.now)
  is_right = models.BooleanField(default=False, verbose_name='Правильность')
  text = models.TextField(null=True, verbose_name='Текст')

  def __str__(self):
    return self.text

  class Meta:
    verbose_name = 'Ответ'
    verbose_name_plural = 'Ответы'


class QuestionLikes(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
  question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, verbose_name='Вопрос')
  like = models.IntegerField(default=0)
  dislike = models.IntegerField(default=0)

  def __str__(self):
    return self.author

  class Meta:
    verbose_name = 'Лайк на вопрос'
    verbose_name_plural = 'Лайки на вопросы'


class AnswerLikes(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
  answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Ответ')
  like = models.IntegerField(default=0)
  dislike = models.IntegerField(default=0)

  def __str__(self):
    return self.author

  class Meta:
    verbose_name = 'Лайк на ответ'
    verbose_name_plural = 'Лайки на ответы'


class Article(models.Model):
  title = models.CharField(max_length=1024, verbose_name='Заголовок')
  text = models.TextField(verbose_name='Текст')
  date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
  author = models.ForeignKey('Author', on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'


# class ProfileManager(models.Manager):
#   def best_members(self):
#     return self.all()[:5]
#
#
# class TagManager(models.Manager):
#   def popular_tags(self):
#     return self.all().order_by('-rating')[:9]
#
#
# class AnswerManager(models.Manager):
#   def answers_by_que(self, index):
#     return self.all().filter(question__pk=index).all()
#
#
# class QuestionManager(models.Manager):
#   def all_questions(self):
#     return self.all().order_by('-date_create')
#
#   def hot_questions(self):
#     return self.annotate(sum_likes=Count('likes')).order_by('-sum_likes').reverse()
#
#   def questions_by_tag(self, tag):
#     return self.filter(tags__tag_title=tag)
#
#   def one_question(self, number):
#     return self.filter(pk=number)
#
#
# class UserProfile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   user_name = models.CharField(max_length=255, verbose_name='Имя', default='null')
#   avatar = models.ImageField(upload_to='avatars', default='avatars/img.png', verbose_name="avatar")
#   objects = ProfileManager()
#
#   def __str__(self):
#     return self.user_name
#
#   class Meta:
#     verbose_name = 'Пользователь'
#     verbose_name_plural = 'Пользователи'
#
#
# class Tag(models.Model):
#   tag_title = models.CharField(max_length=255, verbose_name='Теги')
#   rating = models.IntegerField(default=0)
#
#   objects = TagManager()
#
#   def __str__(self):
#     return self.tag_title
#
#
# class Question(models.Model):
#   author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#   title = models.CharField(max_length=512, verbose_name='Заголовок вопроса')
#   text = models.TextField(verbose_name='Текст')
#   date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#   tags = models.ManyToManyField(Tag, blank=True)
#   answers = models.IntegerField(default=0)
#   likes = models.IntegerField(default=0)
#   dislikes = models.IntegerField(default=0)
#
#   objects = QuestionManager()
#
#   class Meta:
#     verbose_name = 'Вопрос'
#     verbose_name_plural = 'Вопросы'
#
#   def __str__(self):
#     return self.title
#
#
# class Answer(models.Model):
#   author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#   title = models.CharField(max_length=512, verbose_name='Заголовок ответа')
#   text = models.TextField(verbose_name='Текст')
#   correct = models.BooleanField(default=False, verbose_name='Полезно')
#   date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#   question = models.ForeignKey(Question, on_delete=models.CASCADE)
#   likes = models.IntegerField(default=0)
#   dislikes = models.IntegerField(default=0)
#
#   objects = AnswerManager()
#
#   class Meta:
#     verbose_name = 'Ответ'
#     verbose_name_plural = 'Ответы'
#
#   def __str__(self):
#     return self.title
#
#
# class QuestionsLikes(models.Model):
#   user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#   question = models.ForeignKey(Question, on_delete=models.CASCADE)
#   is_like = models.BooleanField(default=True, verbose_name="Лайк")
#
#   def __str__(self):
#     return self.user.nickname + ' поставил лайк "' + self.question.title + '"'
#
#   class Meta:
#     unique_together = ('question', 'user')
#     verbose_name = 'Лайк вопроса'
#     verbose_name_plural = 'Лайки вопроса'
#
#
# class QuestionsDislikesManager(models.Manager):
#   pass
#
#
# class QuestionsDislikes(models.Model):
#   user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#   question = models.ForeignKey(Question, on_delete=models.CASCADE)
#   is_dislike = models.BooleanField(default=True, verbose_name="Лайк")
#   objects = QuestionsDislikesManager()
#
#   def __str__(self):
#     return self.user.nickname + ' поставил лайк "' + self.question.title + '"'
#
#   class Meta:
#     unique_together = ('question', 'user')
#     verbose_name = 'Лайк вопроса'
#     verbose_name_plural = 'Лайки вопроса'
#
#
# class AnswersLikes(models.Model):
#   user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#   answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#   is_like = models.BooleanField(default=True, verbose_name='Лайк')
#
#   def __str__(self):
#     return self.user.nickname + ' поставил лайк "' + self.answer.question.title + '"'
#
#   class Meta:
#     unique_together = ('answer', 'user')
#     verbose_name = 'Лайк ответа'
#     verbose_name_plural = 'Лайки ответа'
#
#
# class AnswersDislikes(models.Model):
#   user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#   answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#   is_like = models.BooleanField(default=True, verbose_name='Лайк')
#
#   def __str__(self):
#     return self.user.nickname + ' поставил лайк "' + self.answer.question.title + '"'
#
#   class Meta:
#     unique_together = ('answer', 'user')
#     verbose_name = 'Лайк ответа'
#     verbose_name_plural = 'Лайки ответа'
