from django.db import models
from django.contrib.auth.models import User
# Create your models here.

NOT_STARTED = 0
STARTED     = 1
CANCELLED   = 2
FINISHED    = 3

GAME_STATUSES = (
    (NOT_STARTED, 'Not started'),
    (STARTED, 'Started'),
    (CANCELLED, 'Cancelled'),
    (FINISHED, 'Finished'),
)

class Game(models.Model):
    white = models.ForeignKey(User, related_name='white_games')
    black = models.ForeignKey(User, related_name='black_games')
    status = models.IntegerField(choices=GAME_STATUSES)
    winner = models.ForeignKey(User, blank=True)
    creation_date = models.DateTimeField()

    @classmethod
    def cancel(cls, game_id):
        """
        Cancel game

        :param game_id: game id
        """
        game = cls.objects.get(game_id)
        game.status = CANCELLED
        game.save()

    @staticmethod
    def new(white, black):
        """
        Create new game
        :param white: user playing whites
        :param black: user playing blacks
        """
        #create and return new game
        pass

    def move(user, move_from, move_to):
        """
        Store move for given user
        :param user: instance of :py:class:`User`
        :param move_from: str, ie. B4
        :param move_to: str, ie. C6
        
        """
        #check if it is turn of given user
        #make sure its valid move
        #store new GameMove
        pass

    def is_finished():
        """
        Check if this game was won
        """
        pass

class GameMove(models.Model):
    game = models.ForeignKey(Game)
    move_from = models.CharField(max_length=2)
    move_to = models.CharField(max_length=2)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now_add=True)


